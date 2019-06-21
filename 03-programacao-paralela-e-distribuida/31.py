from concurrent import futures
import os
import time

def task(n):
    time.sleep(3)
    return (n, os.getpid())


ex = futures.ProcessPoolExecutor(max_workers=5)
results = ex.map(task, range(5, 0, -1))
for n, pid in results:
    print('ran task {} in process {}'.format(n, pid))