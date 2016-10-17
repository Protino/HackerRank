#!/bin/python3

import sys


T = int(input().strip())
for a0 in range(T):
    n = int(input().strip())
    q = [int(q_temp) for q_temp in input().strip().split(' ')]
    index = [x for x in range(1,n+1)]
    q = [3 if a-b > 2 else a-b for a,b in zip(q,index)]
    if (3 in q):
        print ("Too chaotic")
    else:
        print (sum([x if x>0 else 0 for x in q]))
    # your code goes here
