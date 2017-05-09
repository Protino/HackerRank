from collections import defaultdict
from collections import deque
from math import gcd

class Graph:
    def __init__(self):
        self.nodes = defaultdict(set)
        self.shortest = dict()
        self.data = defaultdict(int)

    def addEdge(self, u, v):
        self.nodes[u].add(v)
        self.nodes[v].add(u)

    def shortestPathNodes(self,u,v):
        ansp = self.shortest[u]
        cur_node = v
        res = set()
        while cur_node!=u:
            res.add(self.data[cur_node])
            cur_node = ansp[cur_node]
        res.add(self.data[u])
        return res

    def APSP(self):
        for node in self.nodes:
            self.shortest[node] = self.bfs(node)
    '''
    Returns a list of nodes in bfs order
    '''

    def bfs(self, node):
        que, visited, parent = deque(), [False] * (len(self.nodes)), {}
        visited[node-1] = True
        que.append(node)
        while que:
            u = que.pop()
            # get all connections to the current node
            for i in self.nodes[u]:
                if not visited[i-1]:
                    que.append(i)
                    parent[i] = u
                    visited[i-1] = True
        return parent

def main():
    n,q = map(int,input().split())
    g = Graph()
    values = list(map(int,input().split()))
    for i,value in enumerate(values):
        g.data[i+1] =value


    m=n-1  #number of edges
    for __ in range(m):
        u,v=map(int,input().split())
        g.addEdge(u,v)
    g.APSP()
    
    for __ in range(q):
        u,v = map(int,input().split())
        values = g.shortestPathNodes(u,v)
        # counting the number of pairs that have gcd(x,y)==1
        print (sum([(1,0)[gcd(values[i],values[j])==1] for i in range(len(values))] for j in range(len(values))))

if __name__=="__main__":
    main()