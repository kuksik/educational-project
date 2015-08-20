
import os


def sort_tree(path_):

    list_dir = os.listdir(path_)

    # Sort the list: [files, directories].
    for el in list_dir:
        if '.' in  el: 
            list_dir.insert(0, list_dir.pop(list_dir.index(el)))
    
    if '.DS_Store' in list_dir: list_dir.remove('.DS_Store')
    if '.localized' in list_dir: list_dir.remove('.localized')
    

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
                        




