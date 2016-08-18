n, m = map(int,input().strip().split(' '))
cache = []
for __ in range(m):
    q = [x for x in input().strip().split(' ')]
    if q[0]=='1' or q[0]=='2':
        x = int(q[1])
        mask = int(q[2],2)
        if q[0] == '1':
            if (mask == ((2**n)-1)):
                cache[:] = []
            cache.append(['1',x,mask])
        if q[0] == '2':
            cache.append(['2',x,mask])
    elif q[0]=='3':
        x = int(q[0])
        mask = int(q[1],2)
        value = 0
        for i_caches in reversed(cache):
            type_q = i_caches[0]
            x = i_caches[1]
            cache_mask = i_caches[2]
            if (mask & cache_mask == mask):
                value^=x
                if(type_q == '1'):
                    break
                
        print (value)
