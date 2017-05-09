from functools import reduce
def factors(n):
    return set(reduce(list.__add__,
            ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

dummy=input()
A=[int(x) for x in input().split()]
B=[int(x) for x in input().split()]

factor_set_B=factors(B[0])
for num in B[1:]:
    factor_set_B=set.intersection(factor_set_B,factors(num))
    
print (len({x for x in factor_set_B if all(x%n==0 for n in A)}))

