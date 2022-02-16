import sys
import threading
import time

nr_threads = 3

class cpaThread(threading.Thread):
    
    mutex_lock = threading.Lock()

    def __init__(self, thread_id, data):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.data = data

    def run(self):
        global g_num

        for i in range(8):
            cpaThread.mutex_lock.acquire()
            g_num += 1
            print("Thread id = {} , data = {} - executing....".format(self.thread_id, self.data))
            cpaThread.mutex_lock.release()
            time.sleep(1)

        """
        print("Child thread is running..")
        i = 0
        while i < 10:
            print("Thread id = {} , data = {} - executing....".format(self.thread_id, self.data))
            time.sleep(1)
            i = i + 1
            
        print('Child thread exiting..')
        """


def main():
    thread_handle_list = []
    for i in range(nr_threads):
        thread_handle = cpaThread(i+1, ["hello", i*100])
        thread_handle.start()
        thread_handle_list.append[thread_handle]

    for thread_h in thread_handle_list:
        thread_h.join() 

    """
    print("Main thread start")
    th1 = cpaThread(1, [100, 200])
    th1.start()
    print("main thread block until child thread teminates")
    th1.join()
    
    """
    print("main thread exit")
    sys.exit(0)
    

main()
