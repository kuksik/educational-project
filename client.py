import socket

import os

import sorttree

import os

import sys

host = '127.0.0.1'
port = 9091

sock = socket.socket()
sock.connect((host, port))

file_size = sock.recv(10)
sock.send(b'the file size has received\n')


file_name = sock.recv(20)
print(file_name.decode("utf-8"))
sock.send(b'the file name has received\n')

path = os.path.join('/Users/K/Documents/project', file_name.decode("utf-8"))
file_data = sock.recv(int(file_size))
file = open(path, 'w')
file.write(file_data.decode("utf-8"))

#sock.sendfile('/Users/K/Documents/zada4ky.py')

#data = sock.recv(10)

#file = open(/Users/K/Documents/zada4ky.py)

#udata = data.decode("utf-8")
#print(udata)

file.close()

sock.close()


