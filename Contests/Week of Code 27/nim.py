def grundy(n,zero_move_played,cache):
    if n==0:
        return 0
    if zero_move_played:
        return n
    else:
        if cache[n-1]!=-1:
            return cache[n]
        mex_set = set()
        mex_set.add(grundy(n,True,cache))
        for i in range(n):
            mex_set.add(grundy(i,False,cache))
        #calulate mex set
        mex=0
        while mex in mex_set:
            mex+=1
        cache[n-1]=mex
        return mex

for i in range(100):
    cache = [-1]*(i)
    res = grundy(i,False,cache)
    print (i,res,res-i)
