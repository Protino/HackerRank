import sys
n = int(input())
child_parent = dict()
parent_child = dict()

isLongTree = True
isBroadTree = True
parent_tree_sum = n*(n-1)/2
temp = 0
root = 1
parents = [int(x) for x in input().split()]
for child,parent in enumerate(parents):
    if parent!=1:
        isBroadTree = False 
    if parent in parent_child:
        parent_child[parent].append(child+2)
    else:
        temp+=parent
        parent_child[parent]=[child+2]
    child_parent[child+2]=parent

if (temp!=parent_tree_sum):
    isLongTree = False

if not isBroadTree:
    # generate distance to root table
    distance_to_root = dict()
    distance_to_root[1] = 0
    tree_stack = [1]
    while tree_stack:
        cur_node = tree_stack.pop()
        if cur_node in parent_child:
            children_of_cur_node = parent_child[cur_node]
            cur_dist = distance_to_root[cur_node]
            for child in children_of_cur_node:
                distance_to_root[child] = cur_dist+1
            tree_stack+=children_of_cur_node
    
    #generate gravity force of each node's children on itself
    gravity = dict()
    for i in range(1,n+1):
        gravity[i] = 0
    
    for i in range(2,n+1):
        child = i
        sq_num = 1
        while child in child_parent:
            parent = child_parent[child]
            gravity[parent]+=sq_num**2
            child=parent
            sq_num+=1
            

cache = dict()
results = []

q = []
for __ in range(int(input())):
    q+=map(int,input().split())

for (u,v) in zip(q[::2],q[1::2]):
    cache_key = (u,v)
    if cache_key in cache:
        results.append(cache[cache_key])
        continue

    if isBroadTree:
        if (u!=1 and v!=1):
            cache[cache_key]=0
        elif (v==u):
            cache[cache_key] = n-1
        elif (v==1):
            cache[cache_key]=(n-1)*2 +1
        else:
            cache[cache_key]=1
        continue
    
    v_r = distance_to_root[v]
    u_r = distance_to_root[u]

    if isLongTree:
        g_v = gravity[v]
        g_u = gravity[u]
        if (g_v<g_u):
            # u is above v
            dist_u_v = u_r + v_r  - 2*distance_to_root[u] - 1
            result= int(g_u-((dist_u_v*(dist_u_v+1)*(2*dist_u_v+1))/6))
            results.append(result)
            cache[cache_key] = result
            
        else:
            dist_u_v = u_r + v_r  - 2*distance_to_root[v]
            result= int(g_u+((dist_u_v*(dist_u_v+1)*(2*dist_u_v+1))/6))
            results.append(result)
            cache[cache_key] = result
        continue


    if u==v:
        result = gravity[u]
        results.append(result)
        cache[cache_key] = result
        continue
    elif u==1 or v==1:
        lca = 1
        if u==1:
            dist_u_v = v_r
        else:
            dist_u_v = u_r
    else:
        # finding LCA O(n)
        u_route = set()
        u_route.add(u)
        cur_node = u
        while cur_node!=1:
            cur_node = child_parent[cur_node]
            u_route.add(cur_node)
        cur_node = v
        while True:
            if (cur_node in u_route):
                break
            cur_node = child_parent[cur_node]
        
        lca = cur_node
        dist_u_v = u_r + v_r  - 2*distance_to_root[cur_node]
        
    lcar_r = distance_to_root[lca]

    distance_to_u = dict()
    distance_to_u[u] = 0
    distance_to_u[v] = dist_u_v
    

    if (lca == v):
        # find all the distance between direct parents of u and u
        cur_node = u
        i=1
        while cur_node!=v:
            cur_node = child_parent[cur_node]
            distance_to_u[cur_node]=i
            i+=1
    temp_parent = []
    parent = v
    while True:
        if parent in parent_child:
            children = parent_child[parent]
            for child in children:
                if(child not in distance_to_u):
                    distance_to_u[child] = distance_to_u[parent]+1
            temp_parent+=children
            parent = temp_parent.pop()
        elif not temp_parent:
            break
        else:
            parent = temp_parent.pop()
    result = 0
    for key,value in distance_to_u.items():
        result+=value**2
    results.append(result)
    cache[cache_key] = result

res = ("{}".format(i) for i in results)
print('\n'.join(res))
    
'''
    1 1 1 1 1 3 3 5 6 6 8 8 5 10 11 12 12 12 14
    2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

28
1 1 3 3 1 6 2 2 8 10 11 11 8 14 14 15 17 17 18 8 21 21 22 24 25 13 23
30
10 2
10 8
10 9
2 3
2 6
6 2
5 3
1 6
2 1
1 2
11 8
11 8
17 11
3 14
11 8
8 11
2 8
8 2


    broad tree
    10
    1 1 1 1 1 1 1 1 1 1

    long tree
16
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15
20
13 14
14 13
12 13
13 12
1 5
1 7
7 1
1 1
16 16
16 15

    def calc(i,j):
        sq = 0
        for n in range(i,j+1):
            sq+=n**2
        print (sq)

        
def s(l):
    m = 0
    for n in l:
        m+=n**2
    print (m)

    temp_parent = []
    depths = dict()
    parent = v
    depths[parent] = 0
    depth = 0
    old_depth = 0
    debug = False
    if (v==8 and u==2):
        print ("LCA",lca,"DIST_U_V",dist_u_v)
        debug =True
        print ("Parent  ","depth")
    while True:
        if parent in parent_child:
            depth = depths[parent]
            children = parent_child[parent]
            if debug:
                print (parent,"    ",depth)
            temp_parent+=children
            depth+=1
            for child in children:
                depths[parent]
                result+=(depth+dist_u_v)**2
            parent = temp_parent.pop()
        elif not temp_parent:
            break
        else:
         parent = temp_parent.pop()

    print (result)
    '''
        
        
    
    
