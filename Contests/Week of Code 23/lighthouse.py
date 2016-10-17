import math
n = int(input())
max_possible = n//2-(1)*(n%2==0)
arr = []

def format_input():
    for __ in range(n):
        line = input()
        in_arr = []
        for ch in line:
            if ch=='*':
                in_arr.append(0)
            else:
                in_arr.append(1)
        arr.append(in_arr)

def isCircle(si,sj,radius):
    breakOut = False
    for i in range(si-radius,si+radius+1):
        for j in range(sj-radius,sj+radius+1):
            dist = (i-si)**2 + (j-sj)**2
            if dist<=radius:
                if arr[i][j] == 0:
                    breakOut = True
                    break
            if (breakOut):
                break        
        if (breakOut):
            break
    return (not breakOut)
    

def findCircleRadius(i,j):
    #d(p,q) - sqrt((pi-qi)^2 + (p2-q2)^2))
        
    max_radius = 0
    for radius in range(1,max_possible+1):
        if i-radius < 0 or j-radius < 0:
            break
        if isCircle(i,j,radius):
            if (radius>max_radius):
                max_radius = radius
    return max_radius
                


max_list = []
format_input()
for i in range(1,n-1):
    for j in range(1,n-1):
            max_list.append(findCircleRadius(i,j))

print (max_list)
        
'''
5
**1**
*111*
11111
*111*
**1**
'''






    
