
import os

path_ = '/Users/K/Documents/pr.directory'



def sort_list(inputStr):
# Sorting the list: 1)files, 2)directories.

    if '.' in inputStr:
        return 'a'
    else:
        return('b')
        

def sort_tree(path):

    l = os.listdir(path_)
    l.sort(key=sortlist)
    
    if '.DS_Store' in l: l.remove('.DS_Store')
    
    # To check whether need to sort directory.
    s = 0
    for i in l:
        if os.path.splitext(i)[1][1:] != os.path.split(path)[1]:
            s = 1
            break
 

    if s==1:
        for i in l:
            g=os.path.splitext(i)[1][1:]

            if g != '':
                if g in l:
                    os.rename(os.path.join(path,i), os.path.join(path,g,i))
            else:
                os.renames(os.path.join(path, i) , os.path.join(path,g,i))                        
    else:
        f(os.path.join(path,i))

                        

sort_tree(path)

