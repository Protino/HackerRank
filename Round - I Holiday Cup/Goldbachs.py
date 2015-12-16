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

def primeSum(n):
    p=2
    for p in primes:
        q=n-p
        if(p>q):
            break
        if(q in primes):
            out.extend([p,q])

pset = set(sieve(32000))
primes = sorted(pset)

for i in range(int(input())):
    out = []
    n = int(input());
    primeSum(n)
    print (n,"has",round(len(out)/2),"representation(s)")
    results = ("{}+{}".format(i, j) for i, j in zip(out[0::2], out[1::2]))
    print ('\n'.join(results))
    print ("")

