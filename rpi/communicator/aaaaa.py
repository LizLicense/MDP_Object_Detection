from bluetooth import *
#from config import ANDROID_SOCKET_BUFFER_SIZE, LOCALE, RFCOMM_CHANNEL, UUID

class AndroidComm:
    def __init__(self):
        self.server_sock = None
        self.client_sock = None
       
        self.server_sock = BluetoothSocket(RFCOMM)
        #print("server_sock_teacher",server_sock)
        self.server_sock.bind(("",4))
        self.server_sock.listen(1)
        self.port = self.server_sock.getsockname()[1]
        print("server_sock_teacher",self.port)
        self.uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
        
        #self.server_sock = BluetoothSocket(RFCOMM)
        print('li testing: ',self.server_sock)
        #self.port = self.server_sock.getsockname()[1]
        #self.ip = '192.168.1.1'
        #print("server_sock_lil ",self.port)
        #self.server_sock = bt.BluetoothSocket(bt.RFCOMM)
        #self.server_sock.bind(("", 4))
        #self.server_sock.listen(1)
        #self.port = self.server_sock.getsockname()[1]
        #self.server_sock.listen(RFCOMM_CHANNEL)
        
        advertise_service(
            self.server_sock, 
            'MDP-Server',
            service_id=self.uuid,
            service_classes=[self.uuid, SERIAL_PORT_CLASS],
            profiles=[SERIAL_PORT_PROFILE],
            protocols = [ OBEX_UUID ]
        )
        print('server socket:', str(self.server_sock))
        #print("11Waiting for connection on RFCOMM channel %d" % self.port)
    def connect(self):
        while True:
            retry = False

            try:
                #print('Establishing connection with Android N7 Tablet...')
                print("Waiting for connection on RFCOMM channel %d" % self.port)
                #client_sock, client_info = self.server_sock.accept()
                #print("Accepted connection from ", client_info)
                if self.client_sock is None:
                    #self.client_sock, address = self.server_sock.accept()
                    #print("Successfully connected to Android at address: " + str(address))
                    self.client_sock, self.client_info = self.server_sock.accept()
               	    print("Accepted connection from ", self.client_info)
                    retry = False

            except Exception as error:	
                print("Connection with Android failed: " + str(error))

                if self.client_sock is not None:
                    self.client_sock.close()
                    self.client_sock = None
                
                retry = True

            if not retry:
                break

            print('Retrying Bluetooth Connection to Android...')
            
    def disconnect(self):
        try:
            if self.client_sock is not None:
                self.client_sock.close()
                self.client_sock = None

            print("Android disconnected Successfully")

        except Exception as error:	
            print("Android disconnect failed: " + str(error))
            
    def disconnect_all(self):
        try:
            if self.client_sock is not None:
                self.client_sock.close()
                self.client_sock = None

            if self.server_sock is not None:
                self.server_sock.close()
                self.server_sock = None

            print("Android disconnected Successfully")

        except Exception as error:	
            print("Android disconnect failed: " + str(error))
        
    def read(self):
        try:
            #message = self.client_sock.recv(ANDROID_SOCKET_BUFFER_SIZE).strip()
            message = self.client_sock.recv(1024)
            print("xxxxx ",message)
            print('From android:')
            print(message)
            
            if message is None:
                return None

            if len(message) > 0:
                return message
            
            return None
            
        except Exception as error:
            print('Android read failed: ' + str(error))
            raise error
        #try:
            #message = self.client_sock.recv(ANDROID_SOCKET_BUFFER_SIZE).strip()
            #data = self.client_sock.recv(1024)
            #if len(data) == 0: break
           # print("Received [%s]" % data)
            #print(data)
            #print(type(data))
            #print(data.decode())
            #print(type(data.decode()))
            #client_sock.send(data.decode('UTF-8') + " i am pi!")
            #coord = data.decode('UTF-8')
            #mylist = ast.literal_eval(coord)
            #new_list = [list(map(int, lst)) for lst in mylist]
            #client_sock.send(int(13))
        #return new_list
            #print('From android:')
            #print(message)
            
            #if data is None:
            #    return None

            #if len(data) > 0:
            #    return new_list
            
            #return None
            
        #except Exception as error:
            #print('Android read failed: ' + str(error))
            #raise error
      
    def write(self, message):
        try:
            print('To Android:')
            print(message)
            self.client_sock.send(message)

        except Exception as error:	
            print('Android write failed: ' + str(error))
            raise error
