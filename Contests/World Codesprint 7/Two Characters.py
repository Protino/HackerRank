
import sys
import re
from pprint import pprint
from collections import defaultdict
from itertools import combinations


s_len = int(input().strip())
s = input().strip()
clean_s = list(s)

to_be_deleted = re.findall(r"(.)\1", s)
while (to_be_deleted):
    clean_s = [y for y in clean_s if y not in to_be_deleted]
    to_be_deleted = re.findall(r"(.)\1", "".join(clean_s))

occurs = defaultdict(int)
for item in clean_s:
    occurs[item]+=1
    
max_chars = sorted(occurs,key=occurs.get,reverse = True)
combies = list(combinations(max_chars,2))

count=[]
for combi in combies:
    l_count = 0
    x,y = combi
    searching = True
    for ch in clean_s:
        if(searching and (ch==x or ch==y)):
            next_char = y if ch==x else x
            not_next_char = ch
            searching=False
        elif not searching:
            if(ch==not_next_char):
                l_count=0
                break
            elif(ch==next_char):
                l_count+=1
                next_char=not_next_char
                not_next_char=ch
        
    count.append(l_count+1 if l_count>1 else l_count )
    
if (s_len==2 and s[0]!=s[1]):
    print (2)
else:
    print (max(count) if count else 0)
    

    
