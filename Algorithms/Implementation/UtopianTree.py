t=int(input())
for iter in range(t):
    cycles=int(input())
    height=1
    if (cycles==0):
        print (1)
    else:
        for cycle in range (cycles):
            if(cycle%2==0):
                height=height*2
            else:
                height=height+1
        print (height)
