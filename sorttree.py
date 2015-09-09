
import os

import socket




def sort_tree(path_):

    list_dir = os.listdir(path_)

    # Sort the list: [files, directories].
    for el in list_dir:
        if '.' in  el: 
            list_dir.insert(0, list_dir.pop(list_dir.index(el)))
    
    if '.DS_Store' in list_dir:
        list_dir.remove('.DS_Store')
    if '.localized' in list_dir:
        list_dir.remove('.localized')
    

    # To check whether need to sort directory.
    s = 0
    for el in list_dir:
        if  os.path.splitext(el)[1][1:] != os.path.split(path_)[1]:
            s = 1
            break
 
    # sort the directory
    if s == 1:
        for el in list_dir:   

            if len(el.split('.')) == 2:
                file_ext = el.split('.')[1]
                
                if file_ext in list_dir:
                    os.rename(os.path.join(path_, el), os.path.join(path_, \
                                                               file_ext, el))
                else:
                    os.renames(os.path.join(path_, el), os.path.join(path_, \
                                                                file_ext, el))                        

            else:
                sort_tree(os.path.join(path_, el))
                        



def client_send(path_, sock):

    list_dir = os.listdir(path_)

    if '.DS_Store' in list_dir:
        list_dir.remove('.DS_Store')
    if '.localized' in list_dir:
        list_dir.remove('.localized')
    

    sock.send(str(len(list_dir)).encode('utf-8'))
    sock.recv(51)


    for el in list_dir:

        path_el = os.path.join(path_, el)
        
        if len(el.split('.')) == 2:

            sock.send(b'file')
            sock.recv(51)

            file_name = os.path.basename(path_el)
            sock.send(str(file_name).encode('utf-8'))
            sock.recv(51)
            
            file_size = os.path.getsize(path_el) 
            sock.send(str(file_size).encode('utf-8'))
            sock.recv(51)

            file = open(path_el)
            file_data = file.read()
            file.close
        
            sock.send(file_data.encode('utf-8'))
            sock.recv(51)
    
        else:
            sock.send(b'drct')
            sock.recv(51)
    
            sock.send(str(el).encode('utf-8'))
            sock.recv(51)

            client_send(os.path.join(path_, el), sock)



def server_recv(path_, conn):

    list_dir_len = conn.recv(10)
    list_dir_len = int(list_dir_len.decode('utf-8'))
    conn.send(b"ok")


    for el in range(list_dir_len):

        file_or_drctr = conn.recv(53)
        file_or_drctr.decode('utf-8')
        conn.send(b'ok')
    
    
        if file_or_drctr == "file":
    
            file_name = conn.recv(30)
            file_name = str(file_name.decode('utf-8'))
            conn.send(b'ok') 
    
            file_size = conn.recv(10)
            file_size = int(file_size.decode('utf-8'))
            conn.send(b'ok')
                           
            path_save = os.path.join(path_, file_name)
            file_data = conn.recv(file_size)
            conn.send(b'ok')
             
            file = open(path_save, 'w')
            file.write(file_data.decode('utf-8'))
            file.close()
        
        else:
            drctr_name = conn.recv(20)
            drctr_name = str(drctr_name.decode("utf-8"))
            conn.send(b'ok')
        
            path_save = os.path.join(path_, drctr_name)
            os.mkdir(path_save)
            server_recv(path_save, conn)
    
