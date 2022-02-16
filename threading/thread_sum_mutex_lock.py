import random
import sys
import threading

g_lst = [random.randint(1, 10000) for _ in range(1000)]
g_sum = 0

class CPA_Thread(threading.Thread):
    mu_lock = threading.Lock()
    def __init__(self, thread_id, from_index, to_index):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.from_index = from_index
        self.to_index = to_index
    
    def run(self):
        global g_lst
        global g_sum
        local_sum = 0
        for i in range(self.from_index, self.to_index):
            local_sum += g_lst[i]
        
        print("Thread id = {} doing sum from :{} to: {} -> sum is: {}".format(self.thread_id, self.from_index, self.to_index, local_sum))
        
        CPA_Thread.mu_lock.acquire()
        g_sum += local_sum
        CPA_Thread.mu_lock.release()

def main():    
    nr_threads = 4
    start_index = 0
    chnk_size = 250
    thread_list = []

    for i in range(nr_threads):
        thread_handle = CPA_Thread(i + 1, start_index, start_index + chnk_size)
        thread_handle.start()
        thread_list.append(thread_handle)
        start_index += chnk_size
    for thread_handle in thread_list:
        thread_handle.join()

    global g_sum, g_lst
    print("Global Summation:", g_sum)

    from functools import reduce    
    print("verification:", reduce(lambda x, y: x + y, g_lst))

    sys.exit(0)

main()