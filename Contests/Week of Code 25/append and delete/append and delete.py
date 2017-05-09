import sys
n=int(input())
while (n):
    n-=1
    s = input().strip()
    t = input().strip()
    k = int(input().strip())
    if k >= len(s)+len(t):
        print ('Yes')
    else:
        for i,j in zip(range(len(s)),range(len(t))):
            if s[i]!=t[j]:
                break
        x,y=len(s[i if i!=0 else 1:]),len(t[j if j!=0 else 1:])
        minop=x+y if x>=y else y-x
        print ('Yes' if minop==k or ((k-minop)%2==0 and (k-minop>=0)) else 'No')
            
            
            
                    
                
'''
a a 1 No
ab a 1 Yes
a a 2 Yes
a a 5 Yes
b a 3 Yes
abcd abcdef 4 Yes
abcd abcdef 3 No
abcd abcdef 7 No
abcd abcdef 1 No
abcdsdf abcd 7 Yes
abcdsdf abcd 2 No
abcdsdf abcd 4 No
abcdsdf abcd 10 No
abcdsdf abcdas 3 No
abcdsdf abcdas 5 Yes
abcdsdf abcdas 7 Yes
apple apple 3 No
aba aba 5 No
abcd abcef 4 No
abcd abcef 5 Yes
abc add 7 Yes
abcd abcef 4 No
abcd abcef 5 Yes
alad alafb 4 No
abcd abc 3 Yes
'''
        

'''
a
a
1
ab
a
1
a
a
2
a
a
5
b
a
3
abcd
abcdef
4
abcd
abcdef
3
abcd
abcdef
7
abcd
abcdef
1
abcdsdf
abcd
7
abcdsdf
abcd
2
abcdsdf
abcd
4
abcdsdf
abcd
10
abcdsdf
abcdas
3
abcdsdf
abcdas
5
abcdsdf
abcdas
7

No
Yes
Yes
Yes
Yes
No
No
No
No
Yes
No
No
No
No
Yes
Yes
'''

