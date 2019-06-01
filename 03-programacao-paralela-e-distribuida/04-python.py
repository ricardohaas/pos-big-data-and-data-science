from threading import *
import time

def hello():
    print("hello, world")
    print(time.time())

t = Timer(10.0, hello)

print(time.time())
t.start()
