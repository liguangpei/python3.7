# -*- coding: UTF-8 -*-

import random
import threading
import time


class myThread(threading.Thread):
    def __init__(self, name, urls):
        threading.Thread.__init__(self, name=name)
        self.urls = urls

    def run(self):
        print "current %s is running......" % threading.currentThread().name
        for url in self.urls:
            print "%s----->> %s" % (threading.current_thread().name, url)
            time.sleep(random.random())
        print "current thread %s is end....." % threading.currentThread().name

if __name__=="__main__":
    print "thread %s is running....." % threading.currentThread().name
    t1 = myThread(name="t1", urls=["url_1", "url_2", "url_3"])
    t2 = myThread(name="t2", urls=["url_4", "url_5", "url_6"])

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print "thread %s is end......" % threading.currentThread().name