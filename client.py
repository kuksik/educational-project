import socket

import os

from sorttree import client_send


print('enter server ip')
host = input()
# host = '127.0.0.1'

print('enter port number')
port = int(input())
# port = 9091

print('enter the path to the folder which you want to copy')
drctr_path = input()
# drctr_path = "/Users/K/Documents/client"

    
sock = socket.socket()
sock.connect((host, port))


client_send(drctr_path, sock)


sock.close()


