#!/bin/python3
import math

def gcd(a, b):
    while b:
        a, b=b, a%b
    return a

n = int(input().strip())

def factors(n):
	facs= []
	for i in range(2,math.ceil(math.sqrt(n))):
		if(n%i)==0:
			facs.append((i,n/i))
	return facs

def coprimes(n):
    facs = factors(n)
    cp=0
    for fac in facs:
        if(gcd(fac[0],fac[1])==1):
            cp+=1
    return cp

count = 0
for i in range(n):
    count+=coprimes(i)

print (count+1)

