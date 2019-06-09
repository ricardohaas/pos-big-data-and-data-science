import random
import time
from threading import BoundedSemaphore, Thread

max_itens = 3
container = BoundedSemaphore(max_itens)

def producer(nloops):
    for i in range(nloops):
        time.sleep(random.randrange(2,5))
        print(time.ctime(),end=": ")
        try:
            container.release()
            print("Produced an item")
        except ValueError:
            print("Full, skipping")

def consumer(nloops):
    for i in range(nloops):
        time.sleep(random.randrange(2,5))
        print(time.ctime(), end=":")
        if(container.acquire(False)):
            print('Consumed an item.')
        else:
            print('Empty, skipping')

threads = []
nloops = random.randrange(3,6)
print("Startin with % items." % max_itens)
threads.append(Thread(target=producer, args=(nloops,)))
threads.append(Thread(target=consumer, args=(random.randrange(nloops,nloops+max_itens+2),)))

for thread in threads:
    thread.start()

for thread in threads:
    thread.join()
print("All done")