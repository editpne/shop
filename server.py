#!/usr/bin/python
#coding=utf-8

import socket
import os
#import subprocess
import multiprocessing
import threading
import os


HOST = ''
PORT = 8000

#S = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#S.bind((HOST, PORT))


class Checker(threading.Thread):
    def __init__(self, socket):
        threading.Thread.__init__(self)
        self.socket = socket

    def run(self):
        self.socket.listen(1)
        conn, addr = self.socket.accept()

        while True:
            request = conn.recv(1024)
            if request == 'exit':
                break
            else:
                conn.send('This is thread num %s Hello %s' % (os.getpid(), request))
                print request
        conn.close()
        self.socket.close()


class authServer(object):
    def __init__(self):
        self.socket = None

    def run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((HOST, PORT))
        self.socket.listen(2)

        socket_list = []
        while True:
            client, address = self.socket.accept()
            p = Checker(client, address)
            p.start()
            socket_list.append(p)
        self.socket.close()


class ThreadServer(multiprocessing.Process):
    def __init__(self, client, address):
        multiprocessing.Process.__init__(self)
        self.client = client
        self.address = address

    def run(self):
        while True:
            request = self.client.recv(1024)
            if not request:
                break
            self.client.send("Hello %s" % request)
        self.client.close()


class ListenServer(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.socket = None

    def run(self):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((HOST, PORT))
        self.socket.listen(2)
        while True:
            cs, address = self.socket.accept()
            p = ThreadServer(cs, address)
            p.start()
        self.socket.close()



if __name__ == '__main__':
    s = ListenServer()
    s.start()
    s.join()
