import threading
import time

def thread_function(name):
    time.sleep(2)

if __name__ == "__main__":
    threads = list()
    for index in range(3):
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()

    for index, thread in enumerate(threads):
        thread.join()
