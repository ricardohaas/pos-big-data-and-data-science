import socket
import time
from _thread import start_new_thread

#HOST = "10.199.35.238"  # The server's hostname or IP address
HOST = "127.0.0.1"
PORT = 20001  # The port used by the server
name = input("Enter a name: \n")
running = True

def receiveMessagesThread():
    lastMessage = 0
    while(running):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOST, PORT))
            data = bytes("getMessages():"+str(lastMessage), 'utf-8')
            s.sendall(data)
            data = s.recv(1024)
            receivedString = data.decode('utf-8')
            if(receivedString != "empty"):
                print(receivedString)
                lastMessage += 1
            s.close()
            time.sleep(1)


start_new_thread(receiveMessagesThread, ())

while(running):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        msg = input("Enter a message (type 'exit' to finish):\n")
        s.connect((HOST, PORT))
        if(msg == "exit"):
            print("\nChat finished\n")
            running = False
            msg = name+": left the chat"
        dataSend = "\n"+name+":\n"+ msg
        data = bytes(dataSend , 'utf-8')
        s.sendall(data)
        data = s.recv(1024)
        s.close()
    receivedString = data.decode('utf-8')
    if(receivedString != "empty"):
        print("\n"+receivedString)
    time.sleep(1)

