'''

-Medium-

Generate a uniformly distributed random labelled trees with N nodes.



'''

from typing import List
from collections import defaultdict
from random import random, randint
from sortedcontainers import SortedSet

class Solution:
    def generateTree(self, n: int) -> List[List[int]]:
        # O(N^2) from wikipedia
        self.n = n
        # generate a random Prufer sequence of length n-2
        prufer = [randint(1, n) for i in range(n-2)]
        degree = [1]*(n+1)
        edges = []
        for i in prufer:
            degree[i] += 1
        # print(prufer)
        # print(degree)
        for i in prufer:
            for j in range(1, n+1):
                if degree[j] == 1:
                    edges.append([i,j])
                    degree[i] -= 1
                    degree[j] -= 1
                    break
        u, v = 0, 0
        for i in range(1, n+1):
            if degree[i] == 1:
                if u == 0: u = i
                else:
                    v = i
                    break
        edges.append([u,v])
        degree[u] -= 1
        degree[v] -= 1
        return edges
        
        
    def generateTreeFast(self, n: int) -> List[List[int]]:
        # O(NlogN) 
        # https://forthright48.com/prufer-code-linear-representation-of-a-labeled-tree/
        self.n = n
        prufer = [randint(1, n) for i in range(n-2)]
        nodeCount = defaultdict(int)
        leaves = SortedSet()
        edges = []
        for i in range(len(prufer)):
           nodeCount[prufer[i]] += 1
        # Find the absent nodes
        for i in range(1, n+1):
            if i not in nodeCount: leaves.add(i)
        for i in range(len(prufer)):
            a = prufer[i]
            b = leaves.pop()
            edges.append([a,b])
            nodeCount[a] -= 1
            if nodeCount[a] == 0:
                leaves.add(a)
        edges.append([leaves[0], leaves[-1]])
        return edges     
        
    

    def swapRoot(self, edges: List[List[int]]) -> List[int]:
        deg = [0]*(self.n+1)
        outdeg = [0]*(self.n+1)
        for u,v in edges:
            deg[v] += 1
            outdeg[u] += 1
        root = -1
        for i in range(1,self.n+1):
            if deg[i] == 0:
                root = i
        if root != 1:
            for i in range(len(edges)):
                u, v = edges[i]
                if v == 1:
                    edges[i] = [u-1, root-1]
                elif u == root:
                    edges[i] = [0, v-1]
                else:
                    edges[i] = [u-1, v-1]
        graph = defaultdict(int)
        for u,v in edges:
            graph[v] = u
        edges = []
        for i in range(self.n):
            if i == 0:
                edges.append(-1)
            else:
                edges.append(graph[i])
        return edges
        


        



if __name__ == "__main__":
    n = 20
    sol = Solution()
    tree = sol.generateTree(n)
    # tree = sol.generateTreeFast(n)

    tree = sol.swapRoot(tree) 
    print(tree)
    # deg = [0]*(n)
    # for u,v in tree:
    #     deg[v] += 1
    # root = -1
    # for i in range(n):
    #     if deg[i] == 0:
    #         root = i
    # print(root)

        








