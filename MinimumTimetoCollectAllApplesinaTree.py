'''
-Medium-
*DFS*


Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples 
in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum 
time in seconds you have to spend to collect all apples in the tree, starting at vertex 0 and 
coming back to this vertex.

The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means 
that exists an edge connecting the vertices ai and bi. Additionally, there is a boolean array 
hasApple, where hasApple[i] = true means that vertex i has an apple; otherwise, it does not 
have any apple.

 

Example 1:



Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], 
hasApple = [false,false,true,false,true,true,false]
Output: 8 
Explanation: The figure above represents the given tree where red vertices have an apple. One 
optimal path to collect all apples is shown by the green arrows.  
Example 2:



Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], 
hasApple = [false,false,true,false,false,true,false]
Output: 6
Explanation: The figure above represents the given tree where red vertices have an apple. 
One optimal path to collect all apples is shown by the green arrows.  
Example 3:

Input: n = 7, edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]], 
hasApple = [false,false,false,false,false,false,false]
Output: 0
 

Constraints:

1 <= n <= 10^5
edges.length == n - 1
edges[i].length == 2
0 <= ai < bi <= n - 1
fromi < toi
hasApple.length == n

'''

from collections import defaultdict

class Solution(object):
    def minTime(self, n, edges, hasApple):
        """
        :type n: int
        :type edges: List[List[int]]
        :type hasApple: List[bool]
        :rtype: int
        """
        graph = defaultdict(list)
        for e in edges:
            graph[e[0]].append(e[1])
            graph[e[1]].append(e[0])
        visited = [False]*n
        visited[0] = True
        def dfs(node):
            cost = 0            
            for nxt in graph[node]:
                if not visited[nxt]:
                    visited[nxt] = True
                    cost += dfs(nxt)
            if node != 0:
               if cost > 0: cost += 2
               elif hasApple[node]: cost += 2
            return cost
        return dfs(0)            
        
if __name__ == "__main__":
    edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]] 
    hasApple = [False, False, True, False, True, True, False]
    print(Solution().minTime(7, edges, hasApple))
    edges = [[0,1],[1,2],[0,3]] 
    hasApple = [True, True, True, True]
    print(Solution().minTime(4, edges, hasApple))