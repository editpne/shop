#!/usr/bin/python
#coding=utf-8

import socket
import os
#import subprocess
import multiprocessing
import threading


HOST = ''
PORT = 8000

S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
S.bind((HOST, PORT))


def run_server(s):
    s.listen(1)
    conn, addr = s.accept()
    if conn:
        while True:
            request = conn.recv(1024)
            _message = request.split(' ')
            if request == 'exit':
                break
            else:
                conn.send('This is thread num %s Hello %s' % (os.getuid(), request))
                print request
        conn.close()
    return False
message = ''

process_list = []
for i in xrange(3):
        #p = threading.Thread(target=run_server, args=(S, ))
        p = multiprocessing.Process(target=run_server, args=(S, ))
        p.start()
        process_list.append(p)

for process in process_list:
    process.join()