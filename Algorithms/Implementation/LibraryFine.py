import datetime
a = list(map(int,input().split()))
d = list(map(int,input().split()))
deadline = datetime.date(d[2],d[1],d[0])
actual = datetime.date(a[2],a[1],a[0])
if (deadline>=actual):
    print (0)
else:
    if(a[2]>d[2]):
        print (10000)
    elif (a[1]==d[1]):
        print (15 * (a[0]-d[0]))
    else:
        print (500 * (a[1]-d[1]))
        