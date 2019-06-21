import time
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor


def multiprocessing(func, args, workers):
    with ProcessPoolExecutor(workers) as ex:
        res = ex.map(func, args)
    return list(res)

def live_tracker(x):
    print('I am', x)
    reference = time.time()
    l = []
    for i in range(10**6):
        l.append(time.time() - reference)
    return l


result = multiprocessing(live_tracker, range(8), 2)

print(result)