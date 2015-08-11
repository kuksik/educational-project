import os
import shutil as sh



_path='/Users/K/Documents/pr.directory'


_list=os.listdir(path=_path)

_list.remove('.DS_Store') 



for i in _list:
    if '.' in i:
        name = i[0:i.index('.')]
        if i[len(name)+1:len(i)] in _list:
            sh.move(_path + '/' + i , _path + '/' +i[len(name)+1:len(i)] )

        else:
            sh.move(_path + '/' + i , _path + '/' +i[len(name)+1:len(i)] )
 
            



