from concurrent import futures
import time
import math
import os


def task(n):
    print('{} running in process {}'. format(n,os.getpid()))
    # print('{}: start'.format(n))
    isPrime = is_prime(n)
    # print('{}: done'.format(i))
    return isPrime

def is_prime(n):
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            print( '{} not is Prime'.format(n))
            return False
    print( '{} is Prime'.format(n))
    return True

def done(fn):
    if fn.cancelled():
        print('{}: canceled'.format(fn.arg))
    elif fn.done():
        print('{}: not canceled'.format(fn.arg))


if __name__ == '__main__':
    ex = futures.ThreadPoolExecutor(max_workers=1)
    # print('main: starting')
    tasks = []

    #big prime numbers
    primos = [
        170141183460469231731687303715884105727,
        170141183460469231731687303715884105727,
        170141183460469231731687303715884105727,
        170141183460469231731687303715884105727,
        170141183460469231731687303715884105727]

    for i in primos:
        # print('main: submitting {}'.format(i))
        f = ex.submit(task, i)
        f.arg = i
        #f.add_done_callback(done)
        tasks.append((i, f))

    for i, t in (tasks):
        if not t.cancel():
            print('main: did not cancel {}'.format(i))
        a = 1
    ex.shutdown()