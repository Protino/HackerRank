#!/bin/python3

import re
from collections import Counter

rx = re.compile(r'(.)\1{1,}')

def isHappy(board):
    unique = set(board)
    if '_' in unique:
        unique.remove('_')
       
    count = set(rx.findall(board.replace('_','')))
    if len(unique) == len(count):
        return True
    return False
        
    
    
Q = int(input().strip())
for a0 in range(Q):
    n = int(input().strip())
    b = input().strip()
    if isHappy(b):
        print ('YES')
        continue
    elif '_' not in b or Counter(b.replace('_','')).most_common()[-1][1] == 1:
        print ('NO')
    else:
        print ('YES')
        


'''
TEST CASES

10
A__
BAB_BA
JRZ_RRRRR____ZXYASDWSASD_JRZ_ZXYASDWSASD
JXR_JXR
___
_l_o_l_o_
_
asa_sasss
asd
dwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdwdswdwdwdwdwdwdwdwdwdwdwddwdwdwdwdwdwdwdwdwdwd
'''
