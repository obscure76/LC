'''
 Nov 2019 04:02:31,437 [WARN] a72db6c7-2785-4394-8d06-913cd233fb16 (Coral Endpoint : 11) com.amazon.dee.util.DeeMetricsRecorder: ThreadLocal already contains a DeeMetrics object. Removing already existing DeeMetrics object from ThreadLocal. Old operation name is [GetProviderContentItems], New operation name is [GetProviderContentItems]

'''
import threading
import time
import Queue
import random
import sys

exit_flag = 0


class MyThread(threading.Thread):

    def __init__(self, threadID, name, delay):
        threading.Thread.__init__(self, daemon=True)
        self.threadID = threadID
        self.name = name
        self.delay = delay

    def run(self):
        print "Starting " + self.name
        threadLock.acquire()
        print_time(self.name, 5, self.delay)
        print "Exiting " + self.name
        threadLock.release()


def print_time(threadName, counter, delay):
    while counter:
        time.sleep(delay)
        print "%s: %s" % (threadName, time.ctime(time.time()))
        counter -= 1

# Create new threads


threadLock = threading.Lock()
# threads = []

# Create new threads
# thread1 = MyThread(1, "Thread-1", 1)
# thread2 = MyThread(2, "Thread-2", 2)
#
# # Add threads to thread list
# threads.append(thread1)
# threads.append(thread2)
# Start new Threads
# for t in threads:
#     t.start()
#     t.join()


queueLock = threading.Lock()
workQueue = Queue.Queue(1000000)


class ConsumerThread(threading.Thread):

    def __init__(self, thread_id, name, queue):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.queue = queue

    def run(self):
        print "Starting " + self.name
        self.process_data()
        print "Exiting " + self.name

    def process_data(self):
        while True:
            # if not producer_pool[0].is_alive():
            #     print "Exiting Main Thread", time.time() - start
            #     sys.exit()
            try:
                queueLock.acquire()
                if not self.queue.empty():
                    data = self.queue.get()
                    print "%s processing %s" % (self.name, data)
            except Exception:
                print "No available items, exiting"
                break
            finally:
                queueLock.release()
            time.sleep(random.random())


class ProducerThread(threading.Thread):
    def __init__(self, thread_id, name, queue):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.queue = queue

    def run(self):
        print "Starting Producer" + self.name
        self.produce_data()
        print "Exiting Producer" + self.name

    def produce_data(self):
        for x in xrange(10):
            try:
                queueLock.acquire()
                print "%s producing %s" % (self.name, x)
                workQueue.put(str(x))
            finally:
                queueLock.release()
            time.sleep(random.random()/2)


consumer_pool = []
producer_pool = []
start = time.time()
for i in xrange(1):
    pt = ProducerThread("Producer"+str(0), "id"+str(0), workQueue)
    pt.start()
    producer_pool.append(pt)

for i in xrange(2):
    t = ConsumerThread("Consumer"+str(i), "id"+str(i), workQueue)
    t.start()
    consumer_pool.append(t)

# for t in producer_pool:
#     t.join()
#
# for t in consumer_pool:
#     t.join()

if not producer_pool[0].is_alive():
    print "Exiting Main Thread", time.time() - start
    sys.exit()

# total = producer_pool + consumer_pool
# for t in total:
#     t.join()

