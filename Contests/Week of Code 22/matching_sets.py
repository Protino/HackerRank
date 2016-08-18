import time
n = int(input())
X = [x*1000 for x in range(n)]
Y = [x*(-1000) for x in range(n)]

start_time = time.time()
i = 0
temp = n
while(i<temp):
    if(X[i]== Y[i]):
        del X[i]
        del Y[i]
        temp-=1
    i+=1
        
Y.sort()
X.sort()

i = 0
temp = len(Y)
while(i<temp):
    if(X[i]==Y[i]):
        del X[i]
        del Y[i]
        temp-=1 
    i+=1

diff = []

if (sum(X) != sum(Y)):
    print (-2)
else:
    for i in range(len(Y)):
        diff.append(X[i]-Y[i])
    plus = 0
    minus = 0
    for e in diff:
        if e>0:
            plus+=e
        else:
            minus+=e
        
    if plus!=(minus*-1):
        print (-1)
    else:
        print (plus)
        
print("--- %s seconds ---" % (time.time() - start_time))
