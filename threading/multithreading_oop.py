import threading
import time

class cpaThread(threading.Thread):

    def __init__(self, thread_id, data):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.data = data

    def run(self):
        print("Child thread is running..")
        i = 0
        while i < 10:
            print("Thread id = {} , data = {} - executing....".format(self.thread_id, self.data))
            time.sleep(1)
            i = i + 1
            
        print('Child thread exiting..')


def main():
    print("Main thread start")
    th1 = cpaThread(1, [100, 200])
    th1.start()
    print("main thread block until child thread teminates")
    th1.join()

    print("main thread exit")

main()
