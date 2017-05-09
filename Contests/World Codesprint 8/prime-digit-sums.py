import math
import time

def primes(n): #SO say its a fake sieve, meh, it's fast
    np1 = n + 1
    s = list(range(np1))
    s[1] = 0
    sqrtn = int(round(math.sqrt(n)))
    for i in range(2, sqrtn + 1):
        if s[i]:
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)
primes = list(primes(10**5))
count=0
for i in range(10000,99999):
    x=sum(map(int,str(i)))
    
    y1=sum(map(int,str(i)[1:]))
    y2=sum(map(int,str(i)[:4]))

    z1=sum(map(int,str(i)[2:]))
    z2=sum(map(int,str(i)[:3]))
    z3=sum(map(int,str(i)[1:4:1]))

    if all(x in primes for x in [x,y1,y2,z1,z2,z3]):
        print (i);count+=1

print (count)
    
        
'''
Total 5-30339
6 - 95




for 6 digits
    x1=sum(map(int,str(i)[1:]))
    x2=sum(map(int,str(i)[:5]))
    
    y1=sum(map(int,str(i)[2:5:1]))
    y2=sum(map(int,str(i)[3:]))
    y3=sum(map(int,str(i)[:3]))
    y4=sum(map(int,str(i)[1:4:1]))

    z1=sum(map(int,str(i)[2:]))
    z2=sum(map(int,str(i)[:4]))
    z3=sum(map(int,str(i)[1:5:1]))
'''
