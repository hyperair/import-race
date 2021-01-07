import random
import threading
import time

def foo(): ...
time.sleep(random.random())
def bar(): ...
def baz(): ...
def asdf(): ...

print(f'{threading.current_thread().name}: before loop', list(globals().keys()))
try:
    for x in globals():
        print(f'{threading.current_thread().name}: before sleep', list(globals().keys()))
        time.sleep(1)
        print(f'{threading.current_thread().name}: during loop', list(globals().keys()))
except Exception:
    print(f'{threading.current_thread().name}: caught exception', list(globals().keys()))
