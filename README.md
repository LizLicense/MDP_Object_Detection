# MDP_Object_Detection

#This object detection is performed on Raspberry Pi and PiCam

#In detect.py file, I refine nick's script and customize it with my own .tflit file. The program will take pictures when detecting successfully. Image id will be returned.

#This project follows https://github.com/nicknochnack/TFODRPi 

Here's the step you will need to set up:

Step 1. Walk through TFOD tutorial up to step 12 to generate TFLite files: https://github.com/nicknochnack/TFODCourse

Step 2. Clone the current repository onto your Raspberry Pi or copy it from a machine using RDP.
 git clone https://github.com/nicknochnack/TFODRPi


Step 3.Install the required dependencies onto your Raspberry Pi
pip3 install opencv-python 
sudo apt-get install libcblas-dev
sudo apt-get install libhdf5-dev
sudo apt-get install libhdf5-serial-dev
sudo apt-get install libatlas-base-dev
sudo apt-get install libjasper-dev 
sudo apt-get install libqtgui4 
sudo apt-get install libqt4-testv
echo "deb https://packages.cloud.google.com/apt coral-edgetpu-stable main" | sudo tee /etc/apt/sources.list.d/coral-edgetpu.list
curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | sudo apt-key add -
sudo apt-get update
sudo apt-get install python3-tflite-runtime


Step 4. Copy your detect.tflite model into the same repository and update the labels.txt file to represent your labels.

Step 5. Run real time detections using the detect.py script
python3 detect.py


#'detect.tflite' and 'label.txt' can be replaced your custom data

