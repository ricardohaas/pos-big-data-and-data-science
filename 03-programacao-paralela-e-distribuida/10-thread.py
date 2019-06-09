import time
import threading 
import logging
import math
import random
import os


class MyThread(threading.Thread):
    def __init__(self, thread_number):
        self.stop = threading.Event()
        self.tnumber = thread_number
        super(MyThread, self).__init__()

    def run(self):
        for i in range(random.randint(1,10)):
            if(os.path.exists('divisor.txt')):
                print('Divisor ja encontrado, thread '+format(self.tnumber))
                break
            
            ###Aqui seria parte processamento para verificar se o numero e divisivel
            print('processando na thread '+format(self.tnumber))
            time.sleep(1)

            if( random.randint(1,10) == 10 ):
                f = open("divisor.txt","w+")
                f.write('O divisor eh xxx')
                print('Divisor encontrado pela thread: '+format(self.tnumber))
                break
            #####
            

def checkSomeThreadIsAlive(threadList):
    for i in range(len(thread_list)):
        if(thread_list[i].isAlive()):
            return True
    return False

def checkResult():
    if(os.path.exists('divisor.txt')):
        return True
    return False


thread_number = 5
thread_list = []
if(os.path.exists('divisor.txt')):
    os.remove('divisor.txt') 

for i in range (thread_number):
    time.sleep(1)
    thread = MyThread(i)
    thread_list.append(thread)
    thread.start()

for thread in thread_list:
    thread.join()

# isChecking = True
# while( isChecking ):
#     if(checkResult() == True):
#         break
#         #encontrou um divisor

#     if(checkSomeThreadIsAlive(thread_list)==False):
#         break

if(os.path.exists('divisor.txt')):
    print('Encontrou um divisor')
    f = open("divisor.txt","r")
    contents =f.read()
    print("O divisor eh "+ contents)
else:
    print('Não encontrou um divisor')



