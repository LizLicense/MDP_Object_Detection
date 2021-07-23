"""
Communication protocols.
They are defined so that all subsystems know how to communicate with each other.
"""

MESSAGE_SEPARATOR = '|'.encode()
NEWLINE = '\n'.encode()


class Status:
    IDLE = 'idle'.encode()
    EXPLORING = 'exploring'.encode()
    FASTEST_PATH = 'fastest path'.encode()


class AndroidToRPi:
    CALIBRATE_SENSOR = 'SS|'.encode()

class RPiToAndroid:
    STATUS_EXPLORING = '{"status":"exploring"}'.encode()
    STATUS_FASTEST_PATH = '{"status":"fastest path"}'.encode()
    STATUS_TURNING_LEFT = '{"status":"turning left"}'.encode()
    STATUS_TURNING_RIGHT = '{"status":"turning right"}'.encode()
    STATUS_IDLE = '{"status":"idle"}'.encode()
    STATUS_TAKING_PICTURE = '{"status":"taking picture"}'.encode()
    STATUS_CALIBRATING_CORNER = '{"status":"calibrating corner"}'.encode()
    STATUS_SENSE_ALL = '{"status":"sense all"}'.encode()
    STATUS_MOVING_FORWARD = '{"status":"moving forward"}'.encode()
    STATUS_ALIGN_RIGHT = '{"status":"align right"}'.encode()
    STATUS_ALIGN_FRONT = '{"status":"align front"}'.encode()
    
    MOVE_UP = '{"move":[{"direction":"forward"}]}'.encode()
    TURN_LEFT = '{"move":[{"direction":"left"}]}'.encode()
    TURN_RIGHT = '{"move":[{"direction":"right"}]}'.encode()
