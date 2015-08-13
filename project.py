import os


a='/Users/K/Documents/pr.directory'

def sort(path):
    
    m=os.walk(path)


    k=[d for d in m]
    del k[1:]
    k=k[0]
    k[2].remove('.DS_Store')


    for el in k[2]:

        f = os.path.splitext(el)[1][1:] 
        if f in k[1]:
            os.rename(  os.path.join(k[0],el), os.path.join(k[0],f,el)  )  

        else:
            os.mkdir(  os.path.join( k[0], f)  )
            os.rename(  os.path.join(k[0],el),  os.path.join(k[0],f,el)  )

sort(a)
