#!/usr/bin/python
#coding=utf-8


import socket

HOST = '127.0.0.1'
PORT = 8000


client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

while True:
    stdin = raw_input("Please Enter Text:")
    client.send(stdin)
    if stdin == 'exit':
        break
    else:
        response = client.recv(1024)
        print response