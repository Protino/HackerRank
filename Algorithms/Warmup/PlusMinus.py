def calcFraction(v,n):
    negcount=0
    poscount=0
    zero=0
    for num in v:
        if (num<0):
            negcount+=1
        elif (num>0):
            poscount+=1
        else:
            zero+=1
    print (format((poscount/n),'.4f'))
    print (format((negcount/n),'.4f'))
    print (format((zero/n),'.4f'))

n = int(input())
if(n>0):
    v = map(int,input().split())
    calcFraction(v,n)
else:
    print (0.00)
    print (0.00)
    print (0.00)
