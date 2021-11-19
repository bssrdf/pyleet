'''

-Easy-

There is a bi-directional graph with n vertices, where each vertex is 
labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex start to vertex end.

Given edges and the integers n, start, and end, return true if there is a valid path from start to end, or false otherwise.

 

Example 1:


Input: n = 3, edges = [[0,1],[1,2],[2,0]], start = 0, end = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2
Example 2:


Input: n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], start = 0, end = 5
Output: false
Explanation: There is no path from vertex 0 to vertex 5.
 

Constraints:

1 <= n <= 2 * 10^5
0 <= edges.length <= 2 * 10^5
edges[i].length == 2
0 <= ui, vi <= n - 1
ui != vi
0 <= start, end <= n - 1
There are no duplicate edges.
There are no self edges.

'''
from typing import List
from collections import defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], start: int, end: int) -> bool:
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        visited = [False]*n
        visited[start] = True
        def dfs(u):
            if u == end: return True
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    if dfs(v): return True
            return False

        return dfs(start)    




if __name__ == "__main__":
    print(Solution().validPath(n = 3, edges = [[0,1],[1,2],[2,0]], start = 0, end = 2))
    print(Solution().validPath(n = 6, edges = [[0,1],[0,2],[3,5],[5,4],[4,3]], start = 0, end = 5))
    print(Solution().validPath(10, [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]], 5, 9))
        