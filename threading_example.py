import threading
from queue import Queue

import time

start_time = time.time()
q = Queue()


def display_job(job_num):
    """
    The function we want to run simultaneously on different threads.
    This one just waits half a second and prints the job is completed
    :param job_num:
    :return: void
    """
    time.sleep(0.5)
    print(threading.current_thread().name, 'complete Job', job_num, 'at', time.time())


def display_job_loop():
    """
    One thread takes jobs off the queue, does the job, marks as done, repeats until queue is empty.
    :return:
    """
    while q:
        display_job(job_num=q.get())
        q.task_done()


# Add 20 jobs to the queue
for job in range(20):
    q.put(job)


# Start 20 threads (each thread will do 1 job)
for x in range(20):
    t = threading.Thread(target=display_job_loop)
    t.daemon = True  # ends process
    t.start()


q.join()  # block printing until all tasks are done
print("Entire job took:", time.time() - start_time)