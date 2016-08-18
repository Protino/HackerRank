# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
def sieve(n):
    "Return all primes <= n using sieve of erato."
    np1 = n + 1
    s = list(range(np1))
    x = []
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1):
        if s[i]:
            s[i*i: np1: i] = [0] * int(math.ceil((np1 - i*i) / i))
    return filter(None, s)

"""
n = int(input())
limit = 10**5
pset = list(sieve(n))
primepowers = []
count = 0
for x in range(1,n):
    for p in pset:
        if (p**x)>limit:
            break
        primepowers.append(p**x);
        count+=1
        if count>n:
            break
    if count>n:
        break
        
temp = primepowers
primepowers = []
temp.sort()
for primepower in temp:
    if primepower<=n:
       primepowers.append(primepower)
    else:
        break
prime = 10**9+7
a = [int(x) for x in input().strip().split(' ')]
print (primepowers)
for k in range(2,n+1):
    if k in primepowers:
        if a[k-1]!=-1:
            primepowers.remove(k)
        else:
            next_prime_power=k
            while True:
                next_prime_power*=k
                if next_prime_power>n:
                    break
                elif next_prime_power in primepowers:
                    primepowers.remove(k)
                    break
possible = 1
print (primepowers)
for p in primepowers:
    possible = (p%prime)*(possible%prime)
print (possible%prime)
"""
mod = 10**9 + 7
prime_powers = []
n = int(input())
primes = list(sieve(n))
a = [int(x) for x in input().strip().split(' ')]
primes.sort()
primepowers = []
for prime in primes:
    if prime > n:
        break
    primepower=prime
    primepowers.append(prime)
    while True:
        primepower*=prime
        if primepower>n:
            break
        primepowers.append(primepower)

primepowers.sort()
print (primepowers)
print (primes)
possible = 1
for k in primepowers:
    if a[k-1]==-1:
        i=2
        possible*=(k%mod)
        print (possible)
        if k in primes:
            while True:
                next_mul = k*i
                i+=1
                if next_mul<n:
                    if a[next_mul-1]!=-1:
                        possible/=(k%mod)
                        break
                else:
                    break
             
             
            
        
        
        
print (possible)
