def exponentiate(a,b,k,m):
    if (k < 2):
        print (a,b)
        return
        
    while (k%2 == 0):
        tempa= a
        a = ((a*a) - (b*b))%m
        b = (2*tempa*b)%m
        k//=2
    c = a
    d = b
    k//=2
    while k>0:
        tempa = a
        a = ((a*a) - (b*b))%m
        b = (2*tempa*b)%m
        if (k%2!=0):
            tempc = c
            c = (c*a - b*d)%m
            d = (tempc*b + a*d)%m

        k//=2

    print (c,d)
            

        
for __ in range(int(input())):
    a,b,k,m = map(int,input().split())
    exponentiate(a,b,k,m)
       
