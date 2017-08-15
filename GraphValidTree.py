"""
Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each edge 
is a pair of nodes), write a function to check whether these edges make up a valid tree.

For example:

Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

Hint:

Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], what should your return? Is 
this case a valid tree?

According to the definition of tree on Wikipedia: “a tree is an undirected 
graph in which any two vertices are connected by exactly one path. In other 
words, any connected graph without simple cycles is a tree.”

Premium Question
"""
from collections import defaultdict

__author__ = 'Daniel'


class Solution(object):
    def validTree(self, n, edges):
        """
        A graph is a tree:
          1. no cycle
          2. all connected
        :type n: int
        :type edges: List[List[int]
        :rtype: bool
        """
        if not edges:
            return n in (0, 1)
        graph = defaultdict(list)
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        visited = [False]*n
        if not self.dfs(graph, 0, -1, visited):
            return False
        for v in visited:
            if not v:
                print 'not connected'
                return False
        return True

    def dfs(self, V, v, pre, visited):
        if visited[v]:
            print 'cycle found: ', v, ' has been visited before'
            return False
        visited[v] = True
        for x in V[v]:
            if x != pre:
                if not self.dfs(V, x, v, visited):
                    return False
        return True
        
    # union find
    """
    我们再来看Union Find的方法，这种方法对于解决连通图的问题很有效，思想是我们遍历
    节点，如果两个节点相连，我们将其roots值连上，这样可以帮助我们找到环，我们初始化
    roots数组为-1，然后对于一个pair的两个节点分别调用find函数，得到的值如果相同的话，
    则说明环存在，返回false，不同的话，我们将其roots值union上    
    """
    def validTreeUF(self, n, edges):
        roots = [-1]*n        
        for e in edges:
            x = self.find(roots, e[0])
            y = self.find(roots, e[1])
            if x == y:
                return False
            roots[x] = y
        print roots
            
        return len(edges) == n-1
        
    def find(self, roots, i):
        while roots[i] != -1:
            i = roots[i]
        return i
        
        
if __name__ == "__main__":
    #edges = [[0, 1], [0, 2], [0, 3], [1, 4]]  
    N=1000
    edges = [[0,x] for x in range(1,N)]  
    #edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    #edges = [[0, 1], [1, 2], [2, 3],  [1, 4]]
    print Solution().validTree(N, edges)
    #print Solution().validTreeUF(5, edges)
    #print Solution().validTreeUF(N, edges)