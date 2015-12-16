from __future__ import division

def sum_of_multiples_of_n(n,limit):
    """ let limit be 1000 and n be 3 """
    """ now 3+6+9+....+999 = 3(1+2...333)"""
    """ size = len(1+2+...333) which is 999//3 """
    """ sum = 3*(size*(size+1)/2)) """
    size = (limit-1) // n
    return n*(size*(size+1)//2)

def sum(limit):
    return sum_of_multiples_of_n(3,limit)+sum_of_multiples_of_n(5,limit)-sum_of_multiples_of_n(15,limit)
    
print ('\n'.join(str(sum(int(input()))) for __ in range(int(input()))))
