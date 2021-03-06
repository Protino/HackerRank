import math
import time

def p(n): #SO say its a fake sieve, meh, it's fast
    np1 = n + 1
    s = list(range(np1))
    s[1] = 0
    sqrtn = int(round(math.sqrt(n)))
    for i in range(2, sqrtn + 1):
        if s[i]:
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return list(filter(None, s))
'''
Returns all the primes between a and b inclusive.
'''

def segmented_sieve(a,b):
    limit = int(round(math.sqrt(b)))
    base_primes = p(limit)
    s = [True]*(b-a+1)

    for prime in base_primes:
        i = (a//prime)*prime
        if i<a: i+=prime
        i-=a
        for i in range(i,b-a+1,prime):
            s[i]=False

    primes=[]

    for i,value in enumerate(s):
        if value and i<=b: primes.append(a+i)
        
    if a<= base_primes[-1]:
        for prime in reversed(base_primes):
            if prime>=a:
                primes.insert(0,prime)
            else:
                return primes
    return primes

    
def test(a,b,n):
    for i in a:
        if i>=n:
            i=a.index(i)
            return True if (a[i:]==b) else False    
    else:
        return False

def main(n,m):
    a=list(p(m))
    b=segmented_sieve(n,m)
    print (test(a,b,n))

main(10,10000)

