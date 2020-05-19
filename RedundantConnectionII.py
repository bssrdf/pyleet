

from UF import UF


class Solution(object):

    def detectCycle(self, V):
        self.visited[V] = True
        for i in range(len(self.adjList[V])):
            nextV = self.adjList[V][i]
            if self.visited[nextV]:
                return (V, nextV)
            ret = self.detectCycle(nextV)
            if ret[0]:
                return ret
        return (None, None)

    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        uf = UF(len(edges))
        self.adjList = [[] for i in range(len(edges)+1)]
        hasFather = [False] * (len(edges)+1)     # Whether a vertex has already got a parent
        criticalEdge = None

        res = None
        for e in edges:
            n1, n2 = e[0], e[1]
            self.adjList[n1].append(n2)
            if hasFather[n2]:
                criticalEdge = (e[0], e[1])   
            hasFather[n2] = True       
            if uf.connected(n1, n2):
                
                cycleEdge = (e[0], e[1])
            else:
                uf.union(n1, n2)
        if not criticalEdge:                                    # Case 1
            return cycleEdge
        self.visited = [False] * (len(edges)+1)
        (w, v) = self.detectCycle(criticalEdge[1])
        return (w, v) if w else criticalEdge       
        


print(Solution().findRedundantDirectedConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))
print(Solution().findRedundantDirectedConnection([[1,2], [1,3], [2,3]]))

print(Solution().findRedundantDirectedConnection([[2,1],[3,1],[4,2],[1,4]]))