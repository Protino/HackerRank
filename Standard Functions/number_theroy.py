import math
import time

def fake_sieve(n): #SO say its a fake sieve, meh, it's fast
    np1 = n + 1
    s = list(range(np1))
    s[1] = 0
    sqrtn = int(round(math.sqrt(n)))
    for i in range(2, sqrtn + 1):
        if s[i]:
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)

'''
Returns gcd(b,n),x,y where gcd(b,n)=xb+yn
'''
def eea(b, n):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while n != 0:
        q, b, n = b // n, n, b % n
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1
    return  b, x0, y0

'''
Returns all the primes between a and b inclusive.
'''

def segmented_sieve(a,b):
    limit = int(round(math.sqrt(b)))
    base_primes = list(fake_sieve(limit))
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
def number_of_divisors(factors):
    count=1
    for i in factors:
        count*=(i[1]+1)
    return count
def sum_of_divisors(factors):
    _sum=1
    for prime in factors:
        count=0
        for i in range(prime[1]+1):
            count+=(prime[0]**(i))
        _sum*=count
    return _sum
