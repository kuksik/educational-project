import os

path='/Users/K/Documents/pr.directory'


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
    print(path)
    
    s=0
    for i in l:
         if os.path.splitext(i)[1][1:]==os.path.split(path)[1]:
              s=s+1
    print(len(l), s)

    if len(l)!=s:
         for i in l:
              k=os.path.splitext(i)
              g=k[1][1:]
              if g!='':
                   print(i)
                   if g in l:
                        os.rename( os.path.join(path,i), os.path.join(path,g,i) )
                   else:
                        os.mkdir(  os.path.join(path,g)  ) 
                        os.rename(  os.path.join(path, i) , os.path.join(path, g,i) ) 
                        

              else:
                   f(os.path.join(path,i))

                        

     
               
                 




f(path)

