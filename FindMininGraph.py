import collections

class Solution(object):

    def dfs(self, v, vmin):
        
        self.visited.add(v)
       
        res = vmin 

        for w in self.adjList[v]:
            if w not in self.visited:
                res = min(res, self.dfs(w, min(w, res)))
                 
        return res

    def findMinimum(self, edges, r):
        """
        :type edges: List[List[int]], int
        :rtype: int
        """
    
        n = len(edges)
        
        self.adjList = collections.defaultdict(list)   

        
        for e in edges:
            w, v = e[0], e[1]
            self.adjList[w].append(v)
            self.adjList[v].append(w)
        
        self.visited = set()
       

        return self.dfs(r, r)
        


print(Solution().findMinimum([[1,2], [2,3], [3,4], [4,1], [1,5]], 4))
print(Solution().findMinimum([[1,2], [1,3], [2,3]], 3))
print(Solution().findMinimum([[2,1],[3,1],[4,2],[1,4]], 1))






