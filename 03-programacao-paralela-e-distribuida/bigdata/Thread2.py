import threading

class MyThread(threading.Thread):
    def __init__(self):
        super(MyThread, self).__init__()

    def run(self):
        print ("Running")

thread_list = []
for i in range(4):
    thread = MyThread()
    thread_list.append(thread)
    thread.start()
