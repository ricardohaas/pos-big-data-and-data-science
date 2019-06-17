import socket 
import threading 
from _thread import start_new_thread
from array import array

print_lock = threading.Lock() 

# thread fuction 
def threaded(c): 
    while True: 
        # data received from client 
        data = c.recv(1024) 
        if not data: 
            print('Bye') 
            print_lock.release() 
            break
        
        string = "empty"
        receivedString = data.decode('utf-8')
        if( receivedString.find("getMessages()") != -1):
            parts = receivedString.split(":")
            lastMessage = int(parts[1])
            string = getMessages(lastMessage)
        else:
            messages.append(receivedString)
        data = bytes(string, 'utf-8')
        # send back reversed string to client 
        c.send(data) 
    # connection closed 
    c.close() 

def Main():
    host = "" 
    #host = "10.199.35.238" 
    # reverse a port on your computer 
    # in our case it is 12345 but it 
    # can be anything 
    port = 20001
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to post", port) 
    # put the socket into listening mode 
    s.listen(5) 
    print("socket is listening") 
    # a forever loop until client wants to exit 
    while True: 
        # establish connection with client 
        c, addr = s.accept() 
        # lock acquired by client 
        print_lock.acquire() 
        print('Connected to :', addr[0], ':', addr[1]) 
        # Start a new thread and return its identifier 
        start_new_thread(threaded, (c,)) 
    s.close() 

messages = []
def getMessages(lastMessage):
    if(len(messages) <= (lastMessage) ):
        return "empty"
    return messages[lastMessage]

if __name__ == '__main__': 
    Main() 