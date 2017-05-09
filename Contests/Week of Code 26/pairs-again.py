import math
from fractions import gcd
import time
import itertools
import gc


def primes(n): #SO say its a fake sieve, meh, it's fast
    np1 = n + 1
    s = list(range(np1))
    s[1] = 0
    sqrtn = int(round(math.sqrt(n)))
    for i in range(2, sqrtn + 1):
        if s[i]:
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)


def factorize(n, primes):
    factors = []
    for p in primes:
        if p*p > n: break
        i = 0
        while n % p == 0:
            n //= p
            i+=1
        if i > 0:
            factors.append((p, i));
    if n > 1: factors.append((n, 1))

    return factors

def divisors(factors):
    div = [1]
    for (p, r) in factors:
        div = [d * p**e for d in div for e in range(r + 1)]
    return div


def solve(n):
    res=[]
    for i in range(1,n):
        ax = divs[i]
        bx = divs[n-i]
        for a in ax:
            for b in bx:
                if (a<b):
                    res.append((a,b))
                
    return (len(set(res)))

n=int(input())
start=time.time()
primes=list(primes(n+1))
divs=[]
for x in range(n+1):
    sp=itertools.islice(primes,int(math.sqrt(x))+1)
    divs.append(divisors(factorize(x,sp)))
primes=[]
gc.collect()
print (solve(n))
