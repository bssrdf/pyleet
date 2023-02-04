'''
-Hard-
*DP*
*Topological Sort*


There is a directed graph of n colored nodes and m edges. The nodes are numbered 
from 0 to n - 1.

You are given a string colors where colors[i] is a lowercase English letter 
representing the color of the ith node in this graph (0-indexed). You are also 
given a 2D array edges where edges[j] = [aj, bj] indicates that there is a 
directed edge from node aj to node bj.

A valid path in the graph is a sequence of nodes x1 -> x2 -> x3 -> ... -> xk such 
that there is a directed edge from xi to xi+1 for every 1 <= i < k. The color 
value of the path is the number of nodes that are colored the most frequently 
occurring color along that path.

Return the largest color value of any valid path in the given graph, or -1 if 
the graph contains a cycle.

 

Example 1:



Input: colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]
Output: 3
Explanation: The path 0 -> 2 -> 3 -> 4 contains 3 nodes that are colored "a" (red in the above image).
Example 2:



Input: colors = "a", edges = [[0,0]]
Output: -1
Explanation: There is a cycle from 0 to 0.
 

Constraints:

n == colors.length
m == edges.length
1 <= n <= 105
0 <= m <= 105
colors consists of lowercase English letters.
0 <= aj, bj < n


'''

from typing import List

from collections import defaultdict, deque

class Solution:

    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:
        n = len(colors)
        indeg = [0]*n        
        graph = defaultdict(list)
        memo = [[0]*26 for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            indeg[v] += 1
        que = deque()
        for i in range(n):
            if indeg[i] == 0:
                que.append(i)
        while que:
            u = que.popleft()
            memo[u][ord(colors[u])-ord('a')] += 1
            for v in graph[u]:
                for i in range(26):
                    memo[v][i] = max(memo[v][i], memo[u][i]) 
                indeg[v] -= 1
                if indeg[v] == 0:
                    que.append(v)
        ans = 0
        for i in range(n):
            if indeg[i] > 0:
                return -1
            ans = max(ans, max(memo[i]))
        return ans

            


if __name__ == "__main__":
    print(Solution().largestPathValue(colors = "abaca", edges = [[0,1],[0,2],[2,3],[3,4]]))
    print(Solution().largestPathValue(colors = "a", edges = [[0,0]]))
    colors = "hhqhuqhqff"
    edges = [[0,1],[0,2],[2,3],[3,4],[3,5],[5,6],[2,7],[6,7],[7,8],[3,8],[5,8],[8,9],[3,9],[6,9]]
    print(Solution().largestPathValue(colors, edges))
    colors = "nnllnzznn"
    edges = [[0,1],[1,2],[2,3],[2,4],[3,5],[4,6],[3,6],[5,6],[6,7],[7,8]]
    print(Solution().largestPathValue(colors, edges))
    colors =  "xxbgbgxgbx"
    edges =[[0,1],[1,2],[0,3],[2,4],[4,5],[5,6],[5,7],[4,8],[4,9]]
    print(Solution().largestPathValue(colors, edges))