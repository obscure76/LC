from threading import Thread, Lock
from Queue import Queue
import time
import random

queueLock = Lock()
workQueue = Queue(1000000)


def produce_data():
    for x in xrange(10):
        try:
            queueLock.acquire()
            print "producing %s" % (x)
            workQueue.put(str(x))
        finally:
            queueLock.release()
        time.sleep(random.random() / 2)


def process_data():
    while True:
        # if not producer_pool[0].is_alive():
        #     print "Exiting Main Thread", time.time() - start
        #     sys.exit()
        try:
            queueLock.acquire()
            if not workQueue.empty():
                data = workQueue.get()
                print "processing %s" % (data)
        except Exception:
            print "No available items, exiting"
            break
        finally:
            queueLock.release()
        time.sleep(random.random())


consumer_pool = []
producer_pool = []
start = time.time()
p = Thread(target=produce_data())
p.start()
c = Thread(target=process_data())
c.start()
