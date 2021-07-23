from bluetooth import *
from config import ANDROID_SOCKET_BUFFER_SIZE, LOCALE, RFCOMM_CHANNEL, UUID
import ast

def AndroidToRpi():
    client_Sock = None
    server_Sock = None
    server_sock = bt.BluetoothSocket(bt.RFCOMM)
    server_sock.bind(("", RFCOMM_CHANNEL))

    server_sock.listen(RFCOMM_CHANNEL)
    bt.advertise_service(
        server_sock,
        'MDPGrp1_RPi',
        service_id=UUID,
        service_classes=[UUID, bt.SERIAL_PORT_CLASS],
        profiles=[bt.SERIAL_PORT_PROFILE]
            )
    print("Waiting for connection on RFCOMM channel %d" % port)

    client_sock, client_info = server_sock.accept()
    print("Accepted connection from ", client_info)

    try:
        while True:
            print ("In while loop...")
            data = client_sock.recv(1024)
            if len(data) == 0: break
           # print("Received [%s]" % data)
            print(data)
            print(type(data))
            print(data.decode())
            print(type(data.decode()))
            #client_sock.send(data.decode('UTF-8') + " i am pi!")
            coord = data.decode('UTF-8')
            mylist = ast.literal_eval(coord)
            new_list = [list(map(int, lst)) for lst in mylist]
            #client_sock.send(int(13))
            return new_list
    except IOError:
        pass

    print("disconnected")
    #client_sock.close()
    #server_sock.close()
    print("all done")

#Android()
def writeAndroid():
    #server_sock = BluetoothSocket(RFCOMM)
    #server_sock.bind(("",4))
    #server_sock.listen(1)
    #port = server_sock.getsockname()[1]
    #uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
    advertise_service( server_sock, "MDP-Server",
                       service_id = uuid,
                       service_classes = [ uuid, SERIAL_PORT_CLASS ],
                       profiles = [ SERIAL_PORT_PROFILE ],
                       protocols = [ OBEX_UUID ]
                       )
    print("Waiting for connection on RFCOMM channel %d" % port)


    client_sock, client_info = server_sock.accept()
    print("Accepted connection from ", client_info)

    try:
        while True:
            print ("In while loop...")
            #data = client_sock.recv(1024)
            #if len(data) == 0: break
           # print("Received [%s]" % data)
            #print(data)
            #print(type(data))
            #print(data.decode())
            #print(type(data.decode()))
            #client_sock.send(data.decode('UTF-8') + " i am pi!")
            data = str(13)
            #coord = data.decode('UTF-8')
            #mylist = ast.literal_eval(coord)
            #new_list = [list(map(int, lst)) for lst in mylist]
            client_sock.send(data)
            #return new_list
    except IOError:
        pass
    
#writeAndroid()

