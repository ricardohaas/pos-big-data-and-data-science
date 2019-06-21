import time
import threading 
import logging
import math
import concurrent.futures
from concurrent import futures
import os

global IS_PRIME
global tasks

def get_is_prime(prime_tuple):
    global IS_PRIME
    #forcando um processamento consideravel para observar as cpu's sendo utilizadas em paralelo
    print( 'pid: {}'.format(os.getpid()))
    a = 0
    for i in range(1, 1000000000):
        a = i + a

    number_start, number_end, number_test = prime_tuple

    for i in range(number_start, number_end ):
        if (number_test / i ).is_integer():
            IS_PRIME = False
            print('Divisor encontrado {}'.format(i))
            return True
    return False


#Esse número foi retirado da wikipedia como um numero primo bastante grande
#porem ao tentar processar a divisao ele nao retorna conforme esperado
#numberTest = 170141183460469231731687303715884105727
#Entao foi utilizado um numero primo menor
numberTest = 10000019

#lista de processos que sera aberta, ideal colocar o numero de core's da cpu
proc_number = 4
lists_number = 100
sqrt_number = math.sqrt(numberTest)
number_sqrt = int(sqrt_number) + 1
number_part = int(number_sqrt/lists_number) + 1

def done(result):
    global IS_PRIME

    if(not IS_PRIME):
        # 'finalizou um processo que identificou que o número é primo')
        # print('finalizando as demais tasks')
        for i, t in reversed(tasks):
            print('cancelou {}'.format(i))
            t.cancel()
        exit

if __name__ == '__main__':
    global IS_PRIME
    global tasks

    #inicia considerando que o numero eh primo, isso muda assim que encontrar o primeiro divisor
    IS_PRIME = True

    ex = futures.ProcessPoolExecutor(max_workers=proc_number)
    print('main: starting')
    tasks = []

    for i in range(0,lists_number):
        startNumber = number_part * i if number_part * i > 1 else 3
        endNumber = number_part * (i+1)
        prime_tuple = (startNumber, endNumber, numberTest)

        #print('main: submitting {}: {} / {}'.format(i, startNumber, endNumber))
        f = ex.submit(get_is_prime, prime_tuple)
        f.arg = i
        f.add_done_callback(done)
        tasks.append((i, f))

    ex.shutdown()

    if( IS_PRIME ):
        print('É primo')
    else:
        print('Não é primo')