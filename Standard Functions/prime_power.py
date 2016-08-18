import math
def isPrimePower(n):
    for i in range(math.log(n)):
        root = iroot(i,n)


def iroot(k, n):
    u, s = n, n+1
    while u < s:
        s = u
        t = (k-1) * s + n // pow(s, k-1)
        u = t // k
    return s       
    
print (iroot(3,125))
