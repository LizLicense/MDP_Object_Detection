from test_sim import Simulator
#from simulator import final_id
import argparse
import logging
from map import *
import re

import cv2
from tflite_runtime.interpreter import Interpreter
import numpy as np
import time
import os
from bullseyeTurn import*
from active_move import*
import os

#os.system("sudo hciconfig hci0 piscan")
parser = argparse.ArgumentParser(
    description='MDP Maze Exploration Module'
)
parser.add_argument("-v", "--verbose", help="Increase output verbosity", action="store_true")

args = parser.parse_args()
if args.verbose:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

x=Simulator()
print('final_id',final_id)


