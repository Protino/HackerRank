n,m = map(int, input().split())

#Number of 2x2 bases possible
_2x2_bases = (n//2)*(m//2)

#both are odd
if n%2!=0 and m%2!=0:
    extras = (n//2+1)+(m//2+1)-1
#one of them is even or odd
elif (n%2==0 and m%2!=0)or(m%2==0 and n%2!=0):
    extras = (n//2 if n%2==0 else 0) + (m//2 if m%2==0 else 0)
else:
    extras = 0
print ((_2x2_bases+extras) if n and m!=0 else (0))

'''
# Test cases
2 2
1
3 2
2
0 1
0
0 0
0
1000 1000
'''
