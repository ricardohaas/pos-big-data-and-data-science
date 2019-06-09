import time
import threading 
import logging
import math

class MyThread(threading.Thread):
    def __init__(self, number_test, number_start, number_end):
        self.number_test = float(number_test)
        self.number_start = number_start
        self.number_end = number_end
        super(MyThread, self).__init__()

    def run(self):
        #print("\r\nRunning", format(self.number_test), format(self.number_start), format(self.number_end))
        for i in range(self.number_start, self.number_end ):
            print("\r\ntesting:",format(i),format(self.number_start))
            if (self.number_test / i ).is_integer():
                #print("True, stop: ", format(self.number_test),format(i))
                return True
        return False

number_test = 10000000
# number_test = 10000019
number_test = 19
# number_test = 10
thread_number = 3
thread_list = []
sqrt_number = math.sqrt(number_test)
number_sqrt = int(sqrt_number) + 1
number_part = int(number_sqrt/thread_number) + 1

# print(number_part)
for i in range (thread_number):
    startNumber = number_part * i if number_part * i > 1 else 2
    endNumber = number_part * (i+1)
    #print("\r\nPartes:",format(startNumber),format(endNumber))
    thread = MyThread(number_test, startNumber, endNumber)
    thread_list.append(thread)
    thread.start()