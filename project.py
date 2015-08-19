import os

path='/Users/K/Documents/pr.directory'

#sorting the list: 1)files, 2)directories
def fsort(inputStr):
     if '.' in inputStr:
        return 'a'
     else:
         return('b')
        

def f(path):

    l = os.listdir(path)
    l.sort(key=fsort)
    
    if '.DS_Store' in l:
        l.remove('.DS_Store')
    
#to check whether need to sort directory

    s=0
    for i in l:
         if os.path.splitext(i)[1][1:]!=os.path.split(path)[1]:
              s=1
              break
 

    if s==1:
         for i in l:

              g=os.path.splitext(i)[1][1:]

              if g!='':
                   if g in l:
                        os.rename( os.path.join(path,i), os.path.join(path,g,i) )
 
                   else:
                        os.renames(  os.path.join(path, i) , os.path.join(path,g,i) )                        
              else:
                   f(os.path.join(path,i))

                        

f(path)

