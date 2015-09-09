import socket

import os

from sorttree import server_recv

from sorttree import sort_tree


print('enter ip server')
host = input()
# host = '127.0.0.1'

print('enter port number')
port = int(input())
# port = 9091

print('enter the path to the folder in which the files will be saved')
path_save = input()
# path_save = "/Users/K/Documents/server"


sock = socket.socket()
sock.bind((host, port))
sock.listen(1)
conn, addr = sock.accept()


server_recv(path_save, conn)

        
sock.close()
conn.close()


sort_tree(path_save)



