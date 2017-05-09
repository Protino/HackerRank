import math
for __ in range(int(input())):
    a,b,c = map(int,input().split())
    _max=c-(a+b)
    if c==0:
        print (0)
        continue
    if c%b==0: 
        print (c//b)
        continue
    if c%a==0: 
        print (c//a) 
        continue
    if b>c:
        if a>c:
            print (2)
        elif a==c:
            print (1)
        else:
            print (a//c+2)
        continue
    if _max==0:
        print (2)
    else:
        giant_step=math.floor(_max/b)
        rem=c - giant_step*b
        if (rem <= a+b or rem<=b+b or rem<=a+a):
            print (giant_step+2)
            continue
        giant_step+=1
        rem=c - giant_step*b
        if (rem <= a+b or rem<=b+b or rem<=a+a):
            print (giant_step+2)
            continue

