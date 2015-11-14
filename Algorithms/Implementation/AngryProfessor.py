for __ in range(int(input())):
    N,K = map(int, input().split())
    timings = list(map(int, input().split()))
    inTimeCount=0
    for t in timings:
        if(t<=0):
            inTimeCount+=1
        if(inTimeCount==K):
            print ("NO")
            break
    if(inTimeCount<K):
        print ("YES")
		