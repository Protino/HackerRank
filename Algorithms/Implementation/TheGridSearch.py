def searchPattern():
    count=0
    inner=0
    outer=0
    index=0
    validIndex=0
    restart=True
    scanning=False
	firstTIme=True
    while restart :
        for i in range(outer,r):
            for j in range(inner,R):
                index=G[j].find(P[i])
                print (P[i],G[j])
                if(index<0):
                    count=0
                    if(scanning):
                        outer=0
                        restart=True
                        break
                else:
                    if firstTIme:
                        restart=False
                        validIndex=index
                        scanning=False
                        inner=j
                    if index==validIndex:
                        count+=1
                        inner=j+1
                        if count==r :
                            print("YES")
                            return
                        break
                    else:
                        count=0
                        scanning=True
            if restart:
                break
    print ("NO")
    return

for __ in range(int(input())):  #test cases
    R,C = map(int,input().split())          #rows and cols of matrix G
    G = [input() for i in range(R)]         #scan G matrix as 1D string, cols is of no use
    r,c = map(int,input().split())          #rows and cols of matrix P
    P = [input() for i in range(r)]         #again c is of no use.
    searchPattern()