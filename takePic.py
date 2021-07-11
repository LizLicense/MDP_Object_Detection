import cv2
import time
import os
import numpy as np


cam = cv2.VideoCapture(0)

cv2.namedWindow("test")

def img_proc(img):

    YCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB) #转换至YCrCb空间
    (y,cr,cb) = cv2.split(YCrCb) #拆分出Y,Cr,Cb值
    cr1 = cv2.GaussianBlur(y, (5,5), 0)
    _, skin = cv2.threshold(cr1, 10, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) #Ostu处理
    res = cv2.bitwise_and(img,img, mask = skin)
    return res

def C(img):
    brightHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    bgr = [25, 117, 55]
    thresh = 60
    hsv = cv2.cvtColor( np.uint8([[bgr]] ), cv2.COLOR_BGR2HSV)[0][0]
    minHSV = np.array([hsv[0] - thresh, hsv[1] - thresh, hsv[2] - thresh])
    maxHSV = np.array([hsv[0] + thresh, hsv[1] + thresh, hsv[2] + thresh])
    maskHSV = cv2.inRange(brightHSV, minHSV, maxHSV)
    cr1 = cv2.GaussianBlur(maskHSV, (5,5), 10)
    _, skin = cv2.threshold(cr1, 10, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) #Ostu处理
    res = cv2.bitwise_and(brightHSV, brightHSV, mask = skin)
    
    return res
count = 0
while True:
    ret, res_img = cam.read()
    # res_img = img_proc(frame)
    if not ret:
        print("failed to grab frame")
        break
    cv2.imshow("test", res_img)

    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k%256 == 32:
        # SPACE pressed
        timestamp = int(time.time() * 1e6) # 为防止文件重名，使用时间戳命名文件名
        filename = "{}.jpeg".format(timestamp)
        filepath = os.path.join("/home/pi/MDP-team3/image_recognition/Images/test", filename)
        cv2.imwrite(filepath, res_img)
        print("Image {} - {} written!".format(count, filename))
        count+=1

cam.release()

cv2.destroyAllWindows()