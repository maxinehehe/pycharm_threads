# -*- coding: UTF-8 -*-
# import time
# import threading
# import Queue
# import urllib2
#
# class Consumer(threading.Thread):
#     def __init__(self,queue):
#         threading.Thread.__init__(self)
#         self._queue = queue
#
#     def run(self):
#         while True:
#             content = self._queue.get()
#             if isinstance(content,str) and content == 'quit':
#                 break
#             response = urllib2.urlopen(content)
#         print 'Bye byes!'
#
#
# def Producer():
#     urls = ['http://www.baidu.com','http://wwww.sougou.com',
#             'http://www.sina.com','http://wwww.ccsu.cn'
#     ]
#     queue = Queue.Queue()
#     worker_threads = build_worker_pool(queue,4)
#     start_time = time.time()
#
#     #Add the urls to process
#     for url in urls:
#         queue.put(url)
#
#     #Add the poison pillv
#     for worker in worker_threads:
#         queue.put('quit')
#     for worker in worker_threads:
#         worker.join()
#
#     print 'Done! Time taken:{}'.format(time.time() - start_time)
#
# def build_worker_pool(queue,size):
#     workers = []
#     for _ in range(size):
#         worker = Consumer(queue)
#         worker.start()
#         workers.append(worker)
#     return workers
#
# if __name__ == '__main__':
#     Producer()
#
#
#
#












import urllib2
from multiprocessing.dummy import Pool as ThreadPool

urls = [
    'http://www.python.org',
    'http://www.python.org/about/',
    'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
    'http://www.python.org/doc/',
    'http://www.python.org/download/',
    'http://www.python.org/getit/',
    'http://www.python.org/community/',
    'https://wiki.python.org/moin/',
    'http://planet.python.org/',
    'https://wiki.python.org/moin/LocalUserGroups',
    'http://www.python.org/psf/',
    'http://docs.python.org/devguide/',
    'http://www.python.org/community/awards/'
    # etc..
]

# Make the Pool of workers
pool = ThreadPool(4)
# Open the urls in their own threads
# and return the results
results = pool.map(urllib2.urlopen, urls)
#close the pool and wait for the work to finish
pool.close()
pool.join()




# results = []
# for url in urls:
#         result = urllib2.urlopen(url)
#         results.append(result)

# # ------- VERSUS ------- #


# # ------- 4 Pool ------- #
# pool = ThreadPool(4)
# results = pool.map(urllib2.urlopen, urls)

# # ------- 8 Pool ------- #

# pool = ThreadPool(8)
# results = pool.map(urllib2.urlopen, urls)

# # ------- 13 Pool ------- #

# pool = ThreadPool(13)
# results = pool.map(urllib2.urlopen, urls)

#                            Single thread:  14.4 Seconds
#                                   4 Pool:   3.1 Seconds
#                                   8 Pool:   1.4 Seconds
#                                  13 Pool:   1.3 Seconds