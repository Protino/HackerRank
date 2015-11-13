import math
def initialize():
    k=0
    for i in range(cols):
        for j in range(rows):
            x[i][j]=pt[k]
            k+=1
            if(k==length):
                return

def printct():
    for i in range(rows):
        for j in range(cols):
            val=x[j][i]
            if(str(val)!='0'):
                print (val,end="")
        print (" ",end="")
        
pt = input()
length = len(pt)
root = math.sqrt(length)
rows = math.ceil(root)
cols = math.floor(root)
if((rows*cols)<length):
        cols+=1
x = [[0 for i in range(rows)] for j in range(cols)]
initialize()
printct ()