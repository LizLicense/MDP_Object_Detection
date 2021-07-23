import time
import collections
from datetime import datetime
from multiprocessing import Process, Value
from multiprocessing.managers import BaseManager

#import cv2
#import imagezmq

#from picamera import PiCamera
#from picamera.array import PiRGBArray

from androidComm import Android
#from Algorithm import Algorithm
from config import STOPPING_IMAGE, IMAGE_WIDTH, IMAGE_HEIGHT, IMAGE_FORMAT
from protocols import *

class MultiProcessComms:
    """
    This class handles multi-processing communications between Arduino, Algorithm and Android.
    """
    def __init__(self):
        """
        Instantiates a MultiProcess Communications session and set up the necessary variables.

        Upon instantiation, RPi begins connecting to
        - Arduino
        - Algorithm
        - Android
        in this exact order.

        Also instantiates the queues required for multiprocessing.
        """
        print('Initializing Multiprocessing Communication')

        self.android = Android()  # handles connection to Android
        
        self.manager = Manager()

        # messages from Arduino, Algorithm and Android are placed in this queue before being read
        self.message_queue = self.manager.Queue()
        self.to_android_message_queue = self.manager.Queue()

        self.read_arduino_process = Process(target=self._read_arduino)
        self.read_android_process = Process(target=self._read_android)
        
        self.write_process = Process(target=self._write_target)
        self.write_android_process = Process(target=self._write_android)

        self.image_process = Process(target=self._process_pic)
        
        
    def start(self):        
        try:
            self.android.connect()

            print('Connected to Arduino, Algorithm and Android')

            self.read_android_process.start()
            self.write_process.start()
            self.write_android_process.start()

            print('Multiprocess communication session started')

        except Exception as error:
            raise error

        self._allow_reconnection()

    def end(self):
        # children processes should be killed once this parent process is killed
        self.algorithm.disconnect_all()
        self.android.disconnect_all()
        print('Multiprocess communication session ended')

    def _allow_reconnection(self):
        print('You can reconnect to RPi after disconnecting now')

        while True:
            try:
                if not self.read_android_process.is_alive():
                    self._reconnect_android()

                if not self.write_process.is_alive():
                    if self.dropped_connection.value == 0:
                        self._reconnect_arduino()
                    elif self.dropped_connection.value == 1:
                        self._reconnect_algorithm()

                if not self.write_android_process.is_alive():
                    self._reconnect_android()

            except Exception as error:
                print("Error during reconnection: ",error)
                raise error

    def _read_android(self):
        while True:
            try:
                raw_message = self.android.read()
                
                if raw_message is None:
                    continue
                  
                message_list = raw_message.splitlines()
                
                for message in message_list:
                    if len(message) <= 0:
                        continue
                        
                    else:  # if message in ['ES|', 'FS|', 'SendArena']:
                        #TODO motion.py
                        active_car(message)
                        # if message == AndroidToAlgorithm.START_EXPLORATION:
                        #     self.status = Status.EXPLORING
                        #     self.message_queue.put_nowait(self._format_for(
                        #         ARDUINO_HEADER,
                        #         RPiToArduino.START_EXPLORATION + NEWLINE
                        #     ))
                        #
                        # elif message == AndroidToAlgorithm.START_FASTEST_PATH:
                        #     self.status = Status.FASTEST_PATH
                        #     self.message_queue.put_nowait(self._format_for(
                        #         ARDUINO_HEADER,
                        #         RPiToArduino.START_FASTEST_PATH + NEWLINE
                        #     ))

                        # self.message_queue.put_nowait(self._format_for(
                        #     ALGORITHM_HEADER,
                        #     message + NEWLINE
                        # ))
                    
            except Exception as error:
                print('Process read_android failed: ' + str(error))
                break
                
    def _write_android(self):
        while True:
            try:
                if not self.to_android_message_queue.empty():
                    message = self.to_android_message_queue.get_nowait()
                    
                    self.android.write(message)
                
            except Exception as error:
                print('Process write_android failed: ' + str(error))
                break

    def _process_pic(self):

        # initialize the ImageSender object with the socket address of the server
        # image_sender = imagezmq.ImageSender(connect_to=self.image_processing_server_url)
        image_id_list = []
        # image_sender = return ID

        while True:
            try:
                #get id from image and send msg to andriod
                msg = return_from_camera()
                # detections = msg.split()
                detection = msg

                # for detection, coordinates in zip(detections, obstacle_coordinate_list):

                if detection == '-1':
                    continue  # if no symbol detected, skip mapping of symbol id
                else:
                    id_string_to_android = '{"image":[' + detection + ']}'
                    print(id_string_to_android)

                    if detection not in image_id_list:
                        self.image_count.value += 1
                        image_id_list.append(detection)

                    self.to_android_message_deque.append(
                        id_string_to_android + '\n'
                    )

            except Exception as error:
                print('Image processing failed: ' + str(error))

    def _format_for(self, target, payload):
        return {
            'target': target,
            'payload': payload,
        }

