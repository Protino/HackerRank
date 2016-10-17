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

primes = list(sieve(100))
primes.sort()

for __ in range(int(input())):
    n = int(input())
    if (n==1):
        print (0)
        continue
    res = primes[0]
    for i in range(1,len(primes)):
        res*=primes[i]
        if(res>n):
            print (i)
            break
        elif(res==n):
            print(i+1)
            break
            
        
