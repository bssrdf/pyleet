'''
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = 
[fromi, toi, weighti] represents a bidirectional and weighted edge between cities fromi 
and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path 
and whose distance is at most distanceThreshold, If there are multiple such cities, 
return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the 
edges' weights along that path.

 

Example 1:



Input: n = 4, edges = [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], distanceThreshold = 4
Output: 3
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 4 for each city are:
City 0 -> [City 1, City 2] 
City 1 -> [City 0, City 2, City 3] 
City 2 -> [City 0, City 1, City 3] 
City 3 -> [City 1, City 2] 
Cities 0 and 3 have 2 neighboring cities at a distanceThreshold = 4, but we have to 
return city 3 since it has the greatest number.

Example 2:



Input: n = 5, edges = [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], distanceThreshold 
= 2
Output: 0
Explanation: The figure above describes the graph. 
The neighboring cities at a distanceThreshold = 2 for each city are:
City 0 -> [City 1] 
City 1 -> [City 0, City 4] 
City 2 -> [City 3, City 4] 
City 3 -> [City 2, City 4]
City 4 -> [City 1, City 2, City 3] 
The city 0 has 1 neighboring city at a distanceThreshold = 2.
 

Constraints:

2 <= n <= 100
1 <= edges.length <= n * (n - 1) / 2
edges[i].length == 3
0 <= fromi < toi < n
1 <= weighti, distanceThreshold <= 10^4
All pairs (fromi, toi) are distinct.

'''
from collections import defaultdict
import sys

class Solution(object):
    def findTheCityFloyd(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        inf = sys.maxsize
        graph = [[inf for _ in range(n)] for _ in range(n)]
        for i in range(n): graph[i][i] = 0
        for u,v,w in edges:
            graph[u][v] = w
            graph[v][u] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):                    
                    graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])                   
        
        mx = n
        res = n                     
        for i in range(n-1,-1,-1):
            cnt = 0
            for j in range(n):        
                if j != i and graph[i][j] <= distanceThreshold:
                    cnt += 1
            if cnt < mx:
                mx = cnt
                res = i                   
        
        return res


    def findTheCity(self, n, edges, distanceThreshold):
        """
        :type n: int
        :type edges: List[List[int]]
        :type distanceThreshold: int
        :rtype: int
        """
        graph = defaultdict(dict)
        for u,v,w in edges:
            graph[u][v] = w
            graph[v][u] = w
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if k in graph[i] and j in graph[k]:
                        if j in graph[i]:
                            graph[i][j] = min(graph[i][j], graph[i][k]+graph[k][j])
                        else:
                            graph[i][j] = graph[i][k]+graph[k][j]                        
        
        mx = n
        res = n                     
        for i in range(n-1,-1,-1):
            cnt = 0
            for j in graph[i]:        
                if j != i and graph[i][j] <= distanceThreshold:
                    cnt += 1
            if cnt < mx:
                mx = cnt
                res = i                   
        
        return res

      


if __name__ == "__main__":
    print(Solution().findTheCity(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2))
    print(Solution().findTheCity(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4))
    print(Solution().findTheCityFloyd(5, [[0,1,2],[0,4,8],[1,2,3],[1,4,2],[2,3,1],[3,4,1]], 2))
    print(Solution().findTheCityFloyd(4, [[0,1,3],[1,2,1],[1,3,4],[2,3,1]], 4))