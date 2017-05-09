import math
def fake_sieve(n): #SO say its a fake sieve, meh, it's fast
    np1 = n + 1
    s = list(range(np1))
    s[1] = 0
    sqrtn = int(round(math.sqrt(n)))
    for i in range(2, sqrtn + 1):
        if s[i]:
            s[i*i: np1: i] = [0] * len(range(i*i, np1, i))
    return filter(None, s)

def primes(a,b):
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

n,m=map(int,input().split())
n=n+1 if n==1 else n
data=primes(n,m)
base=data[0]
count=0
for prime in data:
    if base+2==prime:
        count+=1
    base=prime
print (count)
