import os
import shutil as sh

name = 'project'

_path='/Users/K/Documents/pr.directory'

_list=os.listdir(path=_path)



for i in _list:
    if  name == i[0:len(name)]:
       if i[len(name)+1:len(i)] in _list:
           sh.move(_path + '/' + i , _path + '/' +i[len(name)+1:len(i)] )

       else:
           os.mkdir(_path+'/'+i[len(name)+1:len(i)])
           sh.move(_path + '/' + i , _path + '/' +i[len(name)+1:len(i)] )
 
            



