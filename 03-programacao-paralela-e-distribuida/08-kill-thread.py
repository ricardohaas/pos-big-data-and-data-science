import time
import threading 
import logging
import math

class MyThread(threading.Thread):
    def __init__(self, thread_number):
        self.end = False
        self.number_end = thread_number
        super(MyThread, self).__init__()

    def run(self):
       while( self.end == False):
            print('run'+format(self.number_end))
            time.sleep(5)

    def setEnd(self):
        self.end = True

thread_number = 5
thread_list = []

for i in range (thread_number):
    time.sleep(1)
    thread = MyThread(i)
    thread_list.append(thread)
    thread.start()
    thread.setEnd()

while( True ):
    for i in range(len(thread_list)):
        if(thread_list[i].isAlive()):
            print('Alive')
    print('while')
