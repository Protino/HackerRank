import math
import time
import zlib
from operator import itemgetter

from collections import defaultdict


def solve(n):
    
    sins=defaultdict()
    for i in range(n+1):
        sins[i]=math.sin(i)
    
    for key,value in sorted(sins.items(),key=itemgetter(1),reverse=True):
        

start=time.time()
print (solve(10**6)[0],time.time()-start)














'''
s=''
for i in range(10,10**1):
    s+=solve(i)+","

with open('maxies4.txt','w') as the_file:
    the_file.write(s)

x=0
start=time.time()
for i in range(10**4):
    for i in range(10**4):
        x+=1
print (x,time.time()-start)
'''
