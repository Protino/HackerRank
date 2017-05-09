#!/bin/python3

import sys

def findMinimumPair():
    mini=10**6
    x=a[0]
    y=a[1]
    for i in range(len(a)-1):
        if (a[i+1]-a[i]<mini):
            mini=a[i+1]-a[i]
            x=a[i+1]
            y=a[i]
    return x,y

n,k = input().strip().split(' ')
n,k = [int(n),int(k)]
a = [int(a_temp) for a_temp in input().strip().split(' ')]

a.sort()
sumi=0
for i in range(k):
    for j in range(k):
        sumi+=(a[i]-a[j])**2

print (sumi)
'''
if k==1:
    print (0)
elif k==2:
    x,y = findMinimumPair()
    print (((x-y)**2)*2)
else:
'''
            
    
    


