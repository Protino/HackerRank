n = int(input())
h = list(map(int,input().strip().split(' ')))
m = int(input())
x = list(map(int,input().strip().split(' ')))
x.sort()

oldlaserpoint = 0
for x_laser in x:
    temp = x_laser
    new_h = 1
    while(x_laser>oldlaserpoint):
        if h[x_laser-2]>new_h:
            h[x_laser-2] = new_h
        new_h+=1
        x_laser-=1

    oldlaserpoint = temp

print (sum(h))
        

