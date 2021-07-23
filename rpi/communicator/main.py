import os
from androidComm import *
from multiProcessComm import MultiProcessComms

def init():
    #args = parser.parse_args()
    #image_processing_server = args.image_recognition

    os.system("sudo hciconfig hci0 piscan")

    try:
        multiprocess_communications = MultiProcessComms()
     #       IMAGE_PROCESSING_SERVER_URLS.get(image_processing_server)
     #   )
        multiprocess_communications.start()

    except Exception:
        multiprocess_communications.end()


if __name__ == "__main__":
    init()
