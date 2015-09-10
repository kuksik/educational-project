import socket

import os

from sorttree import client_send


# print('enter server ip')
# host = input()
host = '127.0.0.1'

# print('enter port number')
# port = int(input())
port = 9091

# print('enter the path to the folder which you want to copy')
# drctr_path = input()
drctr_path = "/Users/K/Documents/client"

# open socket
sock = socket.socket()
sock.connect((host, port))

# sends to server folder name
sock.send(str(os.path.basename(drctr_path)).encode('utf-8'))
sock.recv(51)

# fucntion which sends diriecty to seever
client_send(drctr_path, sock)


sock.close()


