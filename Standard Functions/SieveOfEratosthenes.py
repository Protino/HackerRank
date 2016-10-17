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

print (list(sieve(int(input()))))
