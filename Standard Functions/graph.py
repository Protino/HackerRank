from collections import defaultdict

class Graph:

    def __init__(self):
        self.nodes = defaultdict(list)

    def addEdge(self,u,v):
    	self.nodes[u].append(v)

    '''
    Returns a list of nodes in bfs order
    '''
    def bfs(self,node):
        res,que,visited = [],[],[False]*(len(self.nodes))

        que.append(node)
        visited[node]=True
        while que:
            u = que.pop(0)
            res.append(u)

    	    #get all connections to the current node
            for i in self.nodes[u]:
                if not visited[i]:
                    que.append(i)
                    visited[i]=True
        return res


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

print (g.bfs(2))




    
    
    
    
