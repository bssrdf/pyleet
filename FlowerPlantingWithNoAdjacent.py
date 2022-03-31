'''
-Medium-
*Greedy*
You have n gardens, labeled from 1 to n, and an array paths where paths[i] = [xi, yi] 
describes a bidirectional path between garden xi to garden yi. In each garden, 
you want to plant one of 4 types of flowers.

All gardens have at most 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens 
connected by a path, they have different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type of flower 
planted in the (i+1)th garden. The flower types are denoted 1, 2, 3, or 4. It is 
guaranteed an answer exists.

 

Example 1:

Input: n = 3, paths = [[1,2],[2,3],[3,1]]
Output: [1,2,3]
Explanation:
Gardens 1 and 2 have different types.
Gardens 2 and 3 have different types.
Gardens 3 and 1 have different types.
Hence, [1,2,3] is a valid answer. Other valid answers include [1,2,4], [1,4,2], and [3,2,1].
Example 2:

Input: n = 4, paths = [[1,2],[3,4]]
Output: [1,2,1,2]
Example 3:

Input: n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]
Output: [1,2,3,4]
 

Constraints:

1 <= n <= 104
0 <= paths.length <= 2 * 104
paths[i].length == 2
1 <= xi, yi <= n
xi != yi
Every garden has at most 3 paths coming into or leaving it.


'''

from typing import List
from collections import defaultdict, deque

class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        ans = [0]*(n+1)
        for u,v in paths:
            graph[u].append(v)
            graph[v].append(u)
        visited = [False]*(n+1)
        def dfs(g, t):
            ans[g] = t            
            # print(g, ans[g])
            for v in graph[g]:
                if not visited[v]:
                    visited[v] = True
                    dfs(v, t) 
        k = 0    
        for i in range(1, n+1):
            if not visited[i]:
                visited[i] = True
                dfs(i, k)
                k += 1
        m = defaultdict(list)
        for i in range(1, n+1):
            m[ans[i]].append(i)
        for j in m:
            for i,v in enumerate(m[j]):
                ans[v] = i+1 
        return ans[1:]    

    def gardenNoAdj2(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = defaultdict(list)        
        ans = [0]*(n+1)
        for u,v in paths:
            graph[u].append(v)
            graph[v].append(u)
        
        for i in range(1,n+1):
            ans[i] = ({1,2,3,4} - {ans[j] for j in graph[i]}).pop()
        return ans[1:]



 
if __name__ == "__main__":
    print(Solution().gardenNoAdj2(n = 3, paths = [[1,2],[2,3],[3,1]]))
    print(Solution().gardenNoAdj2(n = 4, paths = [[1,2],[3,4]]))
    print(Solution().gardenNoAdj2(n = 4, paths = [[1,2],[2,3],[3,4],[4,1],[1,3],[2,4]]))
    print(Solution().gardenNoAdj2(n = 5, paths = [[4,1],[4,2],[4,3],[2,5],[1,2],[1,5]]))
    print(Solution().gardenNoAdj2(n = 6, paths = [[6,4],[6,1],[3,1],[4,5],[2,1],[5,6],[5,2]]))
        

