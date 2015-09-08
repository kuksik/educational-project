import socket

import os


host = '127.0.0.1'
port = 9091
drctr_path = "/Users/K/Documents/exp"

    
sock = socket.socket()
sock.connect((host, port))

list_dir = os.listdir(drctr_path)

if '.DS_Store' in list_dir:
    list_dir.remove('.DS_Store')

sock.send(str(len(list_dir)).encode('utf-8'))
sock.recv(51)



for el in list_dir:

    el_path = os.path.join(drctr_path, el)

    if len(el.split('.')) == 2:

        sock.send(b'file')

            
        file_size = os.path.getsize(el_path) 
        sock.send(str(file_size).encode('utf-8'))
        sock.recv(75)

        file_name = os.path.basename(el_path)
        sock.send(str(file_name).encode('utf-8'))
        sock.recv(75)

        file = open(el_path)
        file_data = file.read()
        sock.send(file_data.encode('utf-8'))

        file.close
    

    else:
        sock.send(b'drct')
        sock.send(str(el).encode('utf-8'))
        sock.recv(81)


sock.close()


