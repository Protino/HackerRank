useless = input()
sticks = list(map(int,input().split()))
while(len(sticks)!=0):
    smallest=min(sticks)
    sticks=[x-smallest for x in sticks]
    print(len(sticks))
    sticks=[x for x in sticks if x!=0]
	