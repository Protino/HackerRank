def eratosthenes(n):
    """ Returns primes in range 2 to n inclusive """
    multiples = set()
    for i in range(2, n+1):
        if i not in multiples:
            yield i
            multiples.update(range(i*i, n+1, i))
