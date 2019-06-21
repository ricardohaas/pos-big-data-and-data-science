import time
import threading 
import logging
import math
import concurrent.futures

def get_is_prime(prime_tuple):

    #forcando um processamento consideravel para observar as cpu's sendo utilizadas em paralelo
    a = 0
    for i in range(1, 1000000000):
        a = i + a

    number_start, number_end, number_test = prime_tuple
    for i in range(number_start, number_end ):
        if (number_test / i ).is_integer():
            print('Divisor encontrado {}'.format(i))
            return True
    return False


#Esse número foi retirado da wikipedia como um numero primo bastante grande
#porem ao tentar processar a divisao ele nao retorna conforme esperado
#numberTest = 170141183460469231731687303715884105727
#Entao foi utilizado um numero primo menor
numberTest = 10000019
numberTest = 10000023

proc_number = 2
lists_number = 100
sqrt_number = math.sqrt(numberTest)
number_sqrt = int(sqrt_number) + 1
number_part = int(number_sqrt/lists_number) + 1

primos = []

#divide o processo em n partes para trabalhar de forma paralela
for i in range(1,lists_number):
    startNumber = number_part * i if number_part * i > 1 else 2
    endNumber = number_part * (i+1)
    prime_tuple = (startNumber, endNumber, numberTest)
    primos.append(prime_tuple)

is_prime = True
with concurrent.futures.ProcessPoolExecutor(max_workers=proc_number) as executor:
    executor.map(get_is_prime, )
    for job, not_is_prime in zip(primos, executor.map(get_is_prime, primos)):
            startNumber, endNumber,numberTest = job
            if( not_is_prime):
                print('%d não é primo' % (numberTest))
                is_prime = False
        
if(is_prime):
    print('{} é primo'.format(numberTest))
