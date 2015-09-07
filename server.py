import socket

import os

import sorttree

import os

import sys

host = '127.0.0.1'
port = 9091

sock = socket.socket()
sock.bind((host, port))
sock.listen(1)
conn, addr = sock.accept()

file_size = os.path.getsize("/Users/K/Documents/Unititied.txt") 
conn.send(str(file_size))
conn.recv(75)

file_name = os.path.basename("/Users/K/Documents/Unititied.txt")
conn.send(file_name)
conn.recv(75)

file = open("/Users/K/Documents/Unititied.txt")
file_data = file.read()
conn.send(file_data)

#data = conn.recv(20000)

#udata = data.decode("utf-8")
#print(udata)

file.close()

conn.close()
sock.close()



