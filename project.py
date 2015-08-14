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

        

    if l!=0:
        
        for i in l:
            k=os.path.splitext(i)

            if k[1]=='':
                f(os.path.join(path,k[0]) )

            else:
                g=k[1][1:]

                if g in l:
                    os.rename(  os.path.join(path,i), os.path.join(path, g,i)  )
                    
                else:
                    os.mkdir(  os.path.join(path,g )  )
                    os.rename(  os.path.join(path, i) , os.path.join(path, g,i) )

    else:
        return()
    




f(path)

