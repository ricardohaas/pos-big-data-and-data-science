import time
import threading 
import logging

class MyThread(threading.Thread):
    def __init__(self):
        super(MyThread, self).__init__()

    def run(self):
        print("\r\nRunning")
    
thread_list = []
for i in range (4):
    thread = MyThread()
    thread_list.append(thread)
    thread.start()