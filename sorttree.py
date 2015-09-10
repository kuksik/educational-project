
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
                        


#this function sends directory to server
def client_send(path_, sock):

    # sends to server folder name
    sock.send(str(os.path.basename(path_)).encode('utf-8'))
    sock.recv(51)
    

    list_dir = os.listdir(path_)

    # deletes system files    
    if '.DS_Store' in list_dir:
        list_dir.remove('.DS_Store')
    if '.localized' in list_dir:
        list_dir.remove('.localized')
        
    # sends to server a number of elements which will send
    sock.send(str(len(list_dir)).encode('utf-8'))
    sock.recv(51)


    for el in list_dir:

        path_el = os.path.join(path_, el)

        # file
        if len(el.split('.')) == 2:

            sock.send(b'file')
            sock.recv(51)

            # sends file name
            fl_name = os.path.basename(path_el)
            sock.send(str(fl_name).encode('utf-8'))
            sock.recv(51)

            # sends file size
            fl_size = os.path.getsize(path_el) 
            sock.send(str(fl_size).encode('utf-8'))
            sock.recv(51)

            # opens and sends file
            fl = open(path_el)
            fl_data = fl.read()
            fl.close
        
            sock.send(fl_data.encode('utf-8'))
            sock.recv(51)

        # folder
        else:

            sock.send(b'drct')
            sock.recv(51)

            # for folder calls this function again  
            client_send(os.path.join(path_, el), sock)




# function receives directory from client
def server_recv(path_, conn):

    # recieves folder name
    drctr_name = conn.recv(20)
    drctr_name = str(drctr_name.decode("utf-8"))
    conn.send(b'ok')

    # creates new folder
    path_save = os.path.join(path_, drctr_name)
    os.mkdir(path_save)

    # number of elements which will send client
    list_dir_len = conn.recv(10)
    list_dir_len = int(list_dir_len.decode('utf-8'))
    conn.send(b"ok")

    
    for el in range(list_dir_len):

        # file or folder
        file_or_drctr = conn.recv(53)
        file_or_drctr.decode('utf-8')
        conn.send(b'ok')

        # file    
        if file_or_drctr == "file":

            # receives file name
            fl_name = conn.recv(30)
            fl_name = str(fl_name.decode('utf-8'))
            conn.send(b'ok') 

            # receives file size
            fl_size = conn.recv(10)
            fl_size = int(fl_size.decode('utf-8'))
            conn.send(b'ok')

            # receives and saves file                
            fl_path_save = os.path.join(path_save, fl_name)
            fl_data = conn.recv(fl_size)
            conn.send(b'ok')
             
            fl = open(fl_path_save, 'w')
            fl.write(fl_data.decode('utf-8'))
            fl.close()

        # folder        
        else:

            # calls this function again
            server_recv(path_save, conn)
    
