n=int(input())
if(n>0):
    space=n-1
    has=1
    for i in range(n):
        for s in range(space):
            print (' ',end = '')
        for h in range(has):
            print ('#',end = '')
        has+=1
        space-=1
        print ()
		