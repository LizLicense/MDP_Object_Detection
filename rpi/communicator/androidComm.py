from bluetooth import *
import ast
from communicator.Android import *

ad = AndroidComm()
ad.connect()
def AndroidToRpi():
    
    while True:
        try:
            print ("In while loop...")
            raw_message = ad.read()

            coord = raw_message.decode('UTF-8')
            mylist = ast.literal_eval(coord)
            new_list = [list(map(int, lst)) for lst in mylist]
            if raw_message is None:
                continue
            else:
                return new_list
                      
        except Exception as error:
            print('Process read_android failed: ' + str(error))
            break

def write_android(msg):
    #while True:
    #try:
    #ad = AndroidComm()
    #ad.connect()
            #if not self.to_android_message_queue.empty():
    #message = ['13,1,8,90,automode','13,3,8,90,automode','13,5,8,90,automode']

   # while True:
    #for msg in message:
        #print(msg)
    ad.write(msg)
    #time.sleep(3)

    #except Exception as error:
    #    print('Process write_android failed: ' + str(error))
    #break

#Android()
#def write_RpiToAndroid():
    #server_sock = BluetoothSocket(RFCOMM)
    #server_sock.bind(("",4))
    #server_sock.listen(1)
    #port = server_sock.getsockname()[1]
    #uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
    #advertise_service( server_sock, "MDP-Server",
    #                   service_id = uuid,
    #                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
    #                   profiles = [ SERIAL_PORT_PROFILE ],
    #                   protocols = [ OBEX_UUID ]
    #                   )
    #print("Waiting for connection on RFCOMM channel %d" % port)


    #client_sock, client_info = server_sock.accept()
    #print("Accepted connection from ", client_info)

    #try:
    #    while True:
    #        print ("In while loop...")
            #data = client_sock.recv(1024)
            #if len(data) == 0: break
           # print("Received [%s]" % data)
            #print(data)
            #print(type(data))
            #print(data.decode())
            #print(type(data.decode()))
            #client_sock.send(data.decode('UTF-8') + " i am pi!")
    #        data = str(13)
            #coord = data.decode('UTF-8')
            #mylist = ast.literal_eval(coord)
            #new_list = [list(map(int, lst)) for lst in mylist]
    #        client_sock.send(data)
            #return new_list
    #except IOError:
    #    pass
    
#writeAndroid()
