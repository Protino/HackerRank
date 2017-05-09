from operator import itemgetter
dist lambda x1,y1,x2,y2: return math.sqrt((x1-x2)**2(y1-y2**2))

def isOnline(Ax,Ay,Bx,By,Cx,Cy):
    return dist(Ax,Ay,Cx,Cy)+dist(Bx,By,Cx,Cy)==dist(Ax,Ay,Bx,By)

for __ in range(int(input())):
    points = []
    for __ in range(int(input())):
        points.append((x,y))

    lx=min(points,key=itemgetter(0))[0]
    ly=min(points,key=itemgetter(1))[1]
    hx=max(points,key=itemgetter(0))[0]
    hy=max(points,key=itemgetter(1))[1]

    x1,y1=lx,hy
    x2,y2=hx,hy
    x3,y3=hx,ly
    x4,y4=lx,ly

    online = True
    for point in points:
        x,y=point[0],point[1]
        if not (isOnline(x1,y1,x2,y2,x,y) or isOnline(x2,y2,x3,y3,x,y) \
                or isOnline(x3,y3,x4,y4,x,y) or isOnline(x4,y4,x1,y1,x,y)):
            online = False
            break

    print ('YES' if online else 'NO')
        
                    
                
                
