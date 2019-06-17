import socket 
import threading 
from _thread import start_new_thread
from array import array

print_lock = threading.Lock() 

# thread que fica responsavel por esperar o dado do cliente
# separado em um thread para nao ser bloqueante na conexao de outros clientes 
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

        #se for uma mensagem especifica para retonar as mensagens
        if( receivedString.find("getMessages()") != -1):
            parts = receivedString.split(":")
            lastMessage = int(parts[1])
            string = getMessages(lastMessage)
        #senao eh uma mensagem comum que deve ser armazenada para ficar disponivel para os demais clientes
        else:
            messages.append(receivedString)
        data = bytes(string, 'utf-8')
        c.send(data) 
    # connection closed 
    c.close() 

def Main():
    host = "127.0.0.1" 
    port = 20001
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    s.bind((host, port)) 
    print("socket binded to post", port) 
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
    #se a ultima mensagem do client eh a ultima mensagem no server entao retorna a string "empty" para client ter esse controle
    if(len(messages) <= (lastMessage) ):
        return "empty"
    return messages[lastMessage]

if __name__ == '__main__': 
    Main() 