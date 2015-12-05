def primes_sieve(limit):
    limitn = limit+1
    not_prime = [False] * limitn
    primes = []

    for i in range(2, limitn):
        if not_prime[i]:
            continue
        for f in range(i*i, limitn, i):
            not_prime[f] = True

        primes.append(i)

    return primes
print (primes_sieve(1000))
