#!/usr/bin/python


import multiprocessing
import os


def run(i):
    print "My Num is %s, and my pid is %s" % (i, os.getpid())
    pass

record = []
if __name__ == '__main__':
    print "My is Main Process , my pid is %s" % os.getpid()
    for i in xrange(8):
        p = multiprocessing.Process(target=run, args=(i, ))
        p.start()
        record.append(p)

    for process in record:
        process.join()
