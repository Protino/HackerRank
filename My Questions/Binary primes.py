import math
def sieve(n):
    "Return all primes <= n using sieve of erato."
    np1 = n + 1
    s = list(range(np1))
    s[1] = 0
    sqrtn = int(round(n**0.5))
    for i in range(2, sqrtn + 1):
        if s[i]:
            s[i*i: np1: i] = [0] * int(math.ceil((np1 - i*i) / i))
    return filter(None, s)

primes = set(sieve(10000))
primes.add(2)
bin_primes_1 = []
bin_primes_0 = []


for i in range(1000):
    bin_r = bin(i)[2:]
    bin_primes_1+=[i] if (bin_r.count('1') in primes) else []

for i in range(1000):
    bin_r = bin(i)[2:]
    bin_primes_0+=[i] if (bin_r.count('0') in primes) else []


for i in range(100):
    if i in bin_primes_1 and i in bin_primes_0 and i in primes: 
        print (bin(i))
