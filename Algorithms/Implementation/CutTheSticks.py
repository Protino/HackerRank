useless = input()
sticks = list(map(int,input().split()))
while len(sticks):
    print (len(sticks))
    smallest=min(sticks)
    sticks=[x-smallest for x in sticks if x-smallest!=0]
