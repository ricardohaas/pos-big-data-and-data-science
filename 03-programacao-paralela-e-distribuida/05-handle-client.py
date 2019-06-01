from threading import *
import time

def handleClient1():
    while(True):
        print("Waitin for client 1...")
        time.sleep(5)
    
def handleClient2():
    while(True):
        print("Waitin for client 2...")
        time.sleep(2.5)
    
t = Timer(5.0, handleClient1)
t2 = Timer(1.0, handleClient2)

t.start()
t2.start()
