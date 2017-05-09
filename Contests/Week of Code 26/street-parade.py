t=1
from collections import defaultdict
'''
'''  
def can_break_barriers(start,end,q):
    if(start-1!=-1):    
        prev=a[start]-a[start-1]    #not first
        if (prev>=m-q>=hmin):
            return a[start]-(m-q)
    elif(end+1!=len(a)):
        _next=a[end+1]-a[end]   #not end
        if(_next>=m-q>=hmin):
            return a[end]-(m-q)
    else:
        #it's either first or end or it cannot fit
        if (m-q>=hmin):
            if (start==0):
                return a[start]-(m-q)
            elif (end==0):
                return a[start]
            else:
                return -1
        else:
            return -1

def try_to_fit(best_hours):
    start,end = v_hours[best_hours]
    if (best_hours>=m):
        #check if start and end are real ends
        if (m == hmin):
            return a[start]
        if (m-hmin>=hmin):
            if(start-1!=-1):
                prev=a[start]-a[start-1]    #not first
                if (hmin<=prev):
                    return a[start]-(m-hmin)
            elif(end+1!=len(a)):
                _next=a[end+1]-a[end]   #not end
                if(hmin<=_next):
                    return a[end]-(m-hmin)
            else:
                #it's either first or end
                return
        return a[start]
    else:
        return can_break_barriers(start,end,best_hours)
        
def best_validhours(v_hours,end):
    old=a[0]
    old_index=0
    for i in range(1,end):
        new = a[i]
        if (hmin<=new-old<=hmax):
            v_hours[old-new]=(i,old_index)
            old=new
            old_index=i

    for hour in sorted(v_hours):
        res = try_to_fit(v_hours[hour])
        if (res!=-1):
            return res
    #none of those pieces are valid so better return a[0]-m or a[end}+m
    return a[0]-m
        
def solve():
    #check for valid start point
    old = a[-1]
    old_index=len(a)-1
    v_hours=defaultdict()
    for i in reversed(range(len(a)-1)):
        new = a[i]
        if not (hmin<=old-new<=hmax):
            # check if better hours exist
            return best_validhours(v_hours,i-1)
        v_hours[old-new]=(i,old_index)
        old=new
        old_index=i
    
    q=a[-1]=a[0]
    if m==q:
        return a[0]
    elif m>q:
        return a[0]-1
    else:
        return a[0]-hmax
        
for __ in range(t):
    n=int(input())
    a=list(map(int,input().split()))
    m,hmin,hmax=map(int,input().split())
    '''
    n=100
    a=[1,4,7,8]
    m,hmin,hmax = 10,1,3
    '''
    print (solve())
