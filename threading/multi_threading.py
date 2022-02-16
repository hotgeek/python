import _thread
from re import S
import time

def thread_1_g(thread_id, data):
    print("in thread_1_g")
    i = 0
    while i < 10:
        print("Thread 1 My Id : {}, data = {}".format(thread_id, data))
        time.sleep(1)
        i = i + 1

 
def thread_1_f(thread_id, data):
    print("in thread 1...")
    time.sleep(1)
    thread_1_g(thread_id, data)

def thread_1_main(thread_id, data_from_parent_thread):
    print("Thread 1 just started...")    
    thread_1_f(thread_id, data_from_parent_thread)
    print("Thread 1 exiting...")


def main_thread_g():
    print("In main thread g")
    i = 0
    while(i < 15):
        print("main thread: in work!")
        time.sleep(1)
        i = i + 1

def main_thread_f():
    print("in main thread_f")
    time.sleep(2)
    main_thread_g()



def main():
    print("I am in main thread...")
    _thread.start_new_thread(thread_1_main, (100, [200, 300]))
    main_thread_f()
    print("main thread end")

main()