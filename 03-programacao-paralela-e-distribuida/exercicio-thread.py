import time
import threading 
import logging
import math
import random
import os

"""
O numero a ser verificado eh dividido em N partes para ser processado por varias threads

Ao encontrar um divisor, a thread escreve em uma varvariaveliável global

Em cada thread, ao identificar que o o divisor já foi encontrado ou terminar os itens a serem processados,
ela eh finalizada

No final da execucao o processo principal verifica a variavel global, indicando que um divisor foi encontrado

"""

class MyThread(threading.Thread):
    def __init__(self, procName, number_test, number_start, number_end):
        self.procName = procName
        self.number_test = float(number_test)
        self.number_start = number_start
        self.number_end = number_end
        super(MyThread, self).__init__()

    def run(self):
        global divisor
        for i in range(self.number_start, self.number_end ):
            if( divisor != ''):
                print('Divisor ja encontrado: ' + divisor)
                break

            #imprime o número que está sendo verificado
            #print("\ntesting:",format(i))

            if (self.number_test / i ).is_integer():
                divisor = ''+format(i)
                print('Pelo menos um divisor encontrado pela thread: '+ self.procName)
                return True
        return False            


#testes


#teste numero nao primo
number_test = 10000000

#teste numero primo
number_test = 10000019


#teste numero primo
number_test = 10000000019

thread_number = 5
thread_list = []
sqrt_number = math.sqrt(number_test)
number_sqrt = int(sqrt_number) + 1
number_part = int(number_sqrt/thread_number) + 1
global divisor
divisor = ''

for i in range (thread_number):
    startNumber = number_part * i if number_part * i > 1 else 2
    endNumber = number_part * (i+1)
    print("\r\nPartes:",format(startNumber),format(endNumber))
    thread = MyThread('Proc_'+format(i) ,number_test, startNumber, endNumber)
    thread_list.append(thread)
    thread.start()

for thread in thread_list:
    thread.join()

if(divisor != ''):
    print('\nEncontrou um divisor: '+ divisor)
else:
    print(format(number_test)+' eh primo')



