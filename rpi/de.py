# Based on https://github.com/tensorflow/examples/blob/master/lite/examples/object_detection/raspberry_pi/README.md
import re
import cv2
from tflite_runtime.interpreter import Interpreter
import numpy as np
import time
import os
from bullseyeTurn import*
from active_move import *


bullseye_id = 16
initiat_id = 21
probability = 0.9
CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480

def load_labels(path='labels.txt'):
  """Loads the labels file. Supports files with or without index numbers."""
  with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()
    labels = {}
    for row_number, content in enumerate(lines):
      pair = re.split(r'[:\s]+', content.strip(), maxsplit=1)
      if len(pair) == 2 and pair[0].strip().isdigit():
        labels[int(pair[0])] = pair[1].strip() 
      else:
        labels[row_number] = pair[0].strip()  
  return labels

def takePic(res_img):
    timestamp = int(time.time() * 1e6)
    filename = "{}.jpeg".format(timestamp)
    filepath = os.path.join("/home/pi/rpi/detectionPic", filename)
    cv2.imwrite(filepath, res_img)
    #print("Image - {} written!".format(filename))
    

def update_id(id):
  if id == 0:
    id = 5
  elif id == 1:
    id = 1
  elif id == 2:
    id = 13
  elif id == 3:
    id = 6
  elif id == 4:
    id = 4
  elif id == 5:
    id = 11
  elif id == 6:
    id = 7
  elif id == 7:
    id = 3
  elif id == 8:
    id = 10
  elif id == 9:
    id = 8
  elif id ==10:
    id = 0 
  elif id == 11:
    id = 12
  elif id == 12:
    id = 9
  elif id ==13:
    id = 2
  elif id == 14:
    id = 14
  elif id ==15:
    id = 15
  else:
    id =id
  return id
  
  
def set_input_tensor(interpreter, image):
  """Sets the input tensor."""
  tensor_index = interpreter.get_input_details()[0]['index']
  input_tensor = interpreter.tensor(tensor_index)()[0]
  input_tensor[:, :] = np.expand_dims((image-255)/255, axis=0)


def get_output_tensor(interpreter, index):
  """Returns the output tensor at the given index."""
  output_details = interpreter.get_output_details()[index]
  tensor = np.squeeze(interpreter.get_tensor(output_details['index']))
  return tensor


def detect_objects(interpreter, image, threshold):
  """Returns a list of detection results, each a dictionary of object info."""
  labels = load_labels()
  set_input_tensor(interpreter, image)
  interpreter.invoke()
  # Get all output details
  boxes = get_output_tensor(interpreter, 0)
  classes = get_output_tensor(interpreter, 1)
  scores = get_output_tensor(interpreter, 2)
  count = int(get_output_tensor(interpreter, 3))

  results = []

  for i in range(count):
    if scores[i] >= threshold:
      result = {
          'bounding_box': boxes[i],
          'class_id': classes[i],
          'score': scores[i]
      }
      results.append(result)
  return results

def bullseye():
    
    print('bullseyes, turn')
    move_forwardLeft(13)
    time.sleep(0.1)
    move_forwardRight(13)
    time.sleep(0.1)
    move_backward(11)
    time.sleep(0.1)
    move_forwardRight(3)
    time.sleep(0.1)
    move_forward(2)

# import from active_move.py
    #active_car('a')
    #time.sleep(1)
    #active_car('w5')
    #time.sleep(1)
    #active_car('d')
    #time.sleep(1)
    #active_car('w4')
    #time.sleep(1)
    #active_car('d')


#detect to get id
def detection():
    labels = load_labels()
    interpreter = Interpreter('detect.tflite')
    interpreter.allocate_tensors()
    _, input_height, input_width, _ = interpreter.get_input_details()[0]['shape']   
    count=1
    proList = [initiat_id,0] ##intial value
    cap = cv2.VideoCapture(0)
          
    while count < 6: 
      # while cap.isOpened():
      cap.isOpened()
      ret, frame = cap.read()
      img = cv2.resize(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), (320,320))
      res = detect_objects(interpreter, img, 0.7)
      #print(res)
      #--res list
              
      for result in res:

#print(type(result) --> dict
          L = [int(result['class_id']),result['score']]
          if L[1]>=proList[1]:
            del proList[:]
            proList = L
          
          
          ymin, xmin, ymax, xmax = result['bounding_box']
          xmin = int(max(1,xmin * CAMERA_WIDTH))
          xmax = int(min(CAMERA_WIDTH, xmax * CAMERA_WIDTH))
          ymin = int(max(1, ymin * CAMERA_HEIGHT))
          ymax = int(min(CAMERA_HEIGHT, ymax * CAMERA_HEIGHT))

          
          cv2.rectangle(frame,(xmin, ymin),(xmax, ymax),(255,0,0),3)
          if proList[1] > probability:
              cv2.putText(frame,labels[int(result['class_id'])]+' P: '+ str(round(proList[1],2)),(xmin, min(ymax, CAMERA_HEIGHT-20)), cv2.FONT_HERSHEY_SIMPLEX, 0.5,(255,255,255),2,cv2.LINE_AA) 
              
      cv2.imshow('Pi Detect', frame)
      count = count + 1
      #print("result:", count, proList)
      if cv2.waitKey(10) & 0xFF ==ord('q'):
          cap.release()
          cv2.destroyAllWindows()
    proList[0] = update_id(proList[0])+1
    takePic(frame)
    #print("detection result final:", proList[0], "Probability: ", proList[1])   
    return proList

#def test():
#    while True:
#        detection()    

def main1():
    #proList=[]
    proList=detection()
    id = proList[0]
    pro = proList[1]
    #if True:
        
    
    if pro > probability:
        if id == bullseye_id:
            print("Deetection result final:", id, "Probability: ", pro)           
            bullseye()
            main1()
        elif id in range(0, bullseye_id):
             print("Detection result final:", id, "Probability: ", pro)
             print("id found, end.")
             #print('debug - ', id)
             #print('testing None ',id)
             return id #return id of the camera #TODO

        elif id not in range(0, bullseye_id + 1):
            print('no id found, continue detecting...')
            main1()     
   
        else:
            print('none of above')
        
    else:
        print('probability too low, continue detecting...')
        main1()


    
if __name__ == "__main__":
    proID=main1()
    if not proID:
        proID=main1()
    print('proID: ', proID)
