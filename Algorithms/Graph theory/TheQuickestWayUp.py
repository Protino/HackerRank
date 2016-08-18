def bfs(graph, start, end):
    # maintain a queue of paths
    queue = []
    # push the first path into the queue
    queue.append([start])
    extended_list = []
    while queue:
        # get the first path from the queue
        path = queue.pop(0)
        # get the last node from the path
        node = path[-1]
        # path found
        if node == end:
            return path
        # enumerate all adjacent nodes, construct a new path and push it into the queue
        if not node in extended_list:
            extended_list.append(node)
            for adjacent in graph.get(node, []):
                new_path = list(path)
                new_path.append(adjacent)
                queue.append(new_path)
    return queue


def set_up_graph(graph):
    """
    update ladder edges
    """
    for __ in range(int(input())):
        begin, end = map(int, input().split())
        graph.pop(begin,None)
        graph.update((k,[end if x==begin else x for x in v]) for k, v in graph.items() if begin in v)

    """
    #update snake edges
    """
    for __ in range(int(input())):
        begin, end = map(int, input().split())
        #graph.pop(begin,None)
        graph[begin] = [end]
        graph.update((k,[end if x==begin else x for x in v]) for k, v in graph.items() if begin in v)

    result = bfs(graph,1,100)
    print (-1 if result == None else len(result) - 1)

# graph is in adjacent list representation
"""
Graph of the snake and ladder board
Each node i.e, a place connected with reachable nodes
Ex: From 1 , {2,3,4,5,6,7} are reachable
"""

for __ in range(int(input())):
    set_up_graph({x:[edges for edges in reversed(range(x+1,x+7))] for x in range(1,100)})
    
