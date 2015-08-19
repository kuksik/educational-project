
import os


def sort_list(inputStr):
# Sorting the list: 1)files, 2)directories.

    if '.' in inputStr:
        return 'a'
    else:
        return('b')
        

def sort_tree(path_):

    l = os.listdir(path_)
    l.sort(key=sort_list)
    
    # if '.DS_Store' in l: l.remove('.DS_Store')
    # if '.localized' in l: l.remove('.localized')
    

    # To check whether need to sort directory.
    s = 0
    for i in l:
        if os.path.splitext(i)[1][1:] != os.path.split(path_)[1]:
            s = 1
            break
 

    if s == 1:
        for i in l:   
            g = os.path.splitext(i)[1][1:]

            if g != '':
                if g in l:
                    os.rename(os.path.join(path_, i), os.path.join(path_, g, i))
                else:
                    os.renames(os.path.join(path_, i), os.path.join(path_, g, i))                        

            else:
                sort_tree(os.path.join(path_, i))
                        


sort_tree('/Users/K/Downloads/')

