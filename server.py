import socket

import os

from sorttree import server_recv

from sorttree import sort_tree


# print('enter ip server')
# host = input()
host = '127.0.0.1'

# print('enter port number')
# port = int(input())
port = 9091

# print('enter the path to the folder in which the files will be saved')
# drctr_path_ = input()
drctr_path = "/Users/K/Documents/server"

# open socket
sock = socket.socket()
sock.bind((host, port))
sock.listen(1)
conn, addr = sock.accept()

# recieves folder name
drctr_name = conn.recv(20)
drctr_name = str(drctr_name.decode("utf-8"))
conn.send(b'ok')

path_sort = os.path.join(drctr_path, drctr_name)

# function recieves diriectory form client and saves
server_recv(drctr_path, conn)

sock.close()
conn.close()

# function sorts recived files
sort_tree(path_sort)



