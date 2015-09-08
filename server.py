import socket

import os

import sys

host = '127.0.0.1'
port = 9091
path_save = '/Users/K/Documents/123'

sock = socket.socket()
sock.bind((host, port))
sock.listen(1)
conn, addr = sock.accept()

list_dir_len = conn.recv(10)
list_dir_len = int(list_dir_len.decode('utf-8'))
conn.send(b"ok")
# print(list_dir_len)

for el in range(list_dir_len):

    file_or_drctr = conn.recv(53)
    file_or_drctr.decode('utf-8')
    # print(str(file_or_drctr), type(file_or_drctr))

    if file_or_drctr == "file":
    
        file_size = conn.recv(10)
        file_size = int(file_size.decode('utf-8'))
        # print('file size = ', file_size)
        conn.send(b'the file size has received')

        file_name = conn.recv(30)
        file_name = str(file_name.decode('utf-8'))
        # print('file name is', file_name)
        conn.send(b'the file name has received')            
        
        path_ = os.path.join(path_save, file_name)
        file_data = conn.recv(file_size)
        file = open(path_, 'w')
        file.write(file_data.decode('utf-8'))
        file.close()

    else:
        drctr_name = conn.recv(20)
        conn.send(b'the name  of folder has received')
        drctr_name = str(drctr_name.decode("utf-8"))
        # print('directories name is', drctr_name)
        path_ = os.path.join(path_save, drctr_name)
        os.mkdir(path_)

        
sock.close()
conn.close()




