from collections import defaultdict

n = int(input())
colors = [int(x) for x in input().split()]
 
tree = defaultdict(list)
edges = []
temp = defaultdict(list)
subTreeColors = defaultdict(set)
for __ in range(1,n):
    x,y = map(int,input().split())
    tree[x]+=[y]
    tree[y]+=[x]
    temp[x]+=[y]
    edges.append((x,y))
    
result = 0

for i,color in enumerate(colors):
    subTreeColors[i+1].add(color)

for key in temp:
    directNodes = temp[key]
    subTree=[]
    subTree+=directNodes
    while directNodes:
        node = directNodes.pop()
        subTreeColors[key].add(colors[node-1])
        if (node in temp):
            deeperNodes=temp[node]
            subTree+=deeperNodes
            directNodes+=deeperNodes
    
    
for edge in edges:
    u = edge[0]
    v = edge[1]
   
    
    u_edges = tree[u]
    
    if u in u_edges:
        u_edges.remove(u)
    
    
    u_colors = set()
    
    u_colors.add(colors[u-1])
    
    visited = set()
    visited.add(u)
    visited.add(v)
    
    to_be_visited = set()
    to_be_visited.update(u_edges)
    while to_be_visited:
        node = to_be_visited.pop()
        if node in visited:
            continue
        node_edges = tree[node]
        
        visited.add(node)
        to_be_visited.update(node_edges)
        
        u_colors.add(colors[node-1])
        
        
    v_colors=subTreeColors[v]
        
    result+=(len(v_colors)*len(u_colors))

        
print (result)  
        

    
    
