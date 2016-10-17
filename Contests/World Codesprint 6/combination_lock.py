given = list(map(int,input().split(' ')))
req = list(map(int,input().split(' ')))
rot = 0
for i in range(len(given)):
    diff = abs(given[i]-req[i])
    if diff == 0:
        continue
    elif diff<5:
        rot+=diff
    else:
        rot+=(10-diff)

print (rot)
        
        
        
