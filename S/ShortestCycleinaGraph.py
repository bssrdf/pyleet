'''
-Hard-
*BFS*
*DFS*
There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1. The edges in the graph are represented by a given 2D integer array edges, where edges[i] = [ui, vi] denotes an edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

Return the length of the shortest cycle in the graph. If no cycle exists, return -1.

A cycle is a path that starts and ends at the same node, and each edge in the path is used only once.

 

Example 1:


Input: n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]
Output: 3
Explanation: The cycle with the smallest length is : 0 -> 1 -> 2 -> 0 
Example 2:


Input: n = 4, edges = [[0,1],[0,2]]
Output: -1
Explanation: There are no cycles in this graph.
 

Constraints:

2 <= n <= 1000
1 <= edges.length <= 1000
edges[i].length == 2
0 <= ui, vi < n
ui != vi
There are no repeated edges.

'''
from typing import List
from collections import defaultdict, deque

class Solution:
    '''
    This problem shows techniques to find cycles in undirected graphs
    using BFS or DFS

    Key point: both DFS and BFS need to keep track of the parent of the
    current node; when traversing to a neighbor node v, if v is not the
    parent but already visited, a cycle is found.  
    '''
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        # DFS 
        G = defaultdict(set)
        for u,v in edges:
            G[u].add(v)
            G[v].add(u)
    
        ans = 1001
        def dfs(u, par, l, depth, visited):
            nonlocal ans
            visited.add(u)
            depth[u] = l
            for v in G[u]:
                # Detect cycles
                if v not in visited:
                    dfs(v, u, l+1, depth, visited)
                elif depth[v] != -1 and l >= depth[v] and par != v:
                    ans = min(ans, l - depth[v] + 1) 
                    # print(ans, depth, l, v)
            return

        for u in G:
            depth = [-1]*n
            dfs(u, -1, 1, depth, set())
        # print(depth)
        return ans if ans != 1001 else -1

    def findShortestCycle3(self, n: int, edges: List[List[int]]) -> int:
        # DFS 
        # Wrong for one test case
        G = defaultdict(set)
        for u,v in edges:
            G[u].add(v)
            G[v].add(u)
        ans = 1001
        # for u in range(n):
        for u in [7]:
            depth = [-1]*n
            def dfs(u, par, d):
                nonlocal ans
                depth[u] = d
                for v in G[u]:
                    # Detect cycles
                    if depth[v] == -1:
                        dfs(v, u, d+1)
                    elif d >= depth[v] and par != v:
                        print(d, depth[v], u, v, par)
                        ans = min(ans, d - depth[v] + 1) 
                return
            dfs(u, -1, 0)
            # print(u, ans)
            print(depth)
        return ans if ans != 1001 else -1
    
    def findShortestCycle4(self, n: int, edges: List[List[int]]) -> int:
        # DFS 
        G = defaultdict(set)
        for u,v in edges:
            G[u].add(v)
            G[v].add(u)
        ans = 1001
        depth = [1001]*n
        for u in range(n):
            def dfs(u, par, d):
                nonlocal ans
                depth[u] = d
                for v in G[u]:
                    # Detect cycles
                    if par != v:
                        if depth[v] > d + 1:
                            dfs(v, u, d+1)
                        elif d > depth[v]:
                            ans = min(ans, d - depth[v] + 1) 
            if depth[u] == 1001: dfs(u, -1, 0)
        return ans if ans != 1001 else -1
    
    
    def findShortestCycle2(self, n: int, edges: List[List[int]]) -> int:
        # BFS 
        G = defaultdict(set)
        inf = 1001
        ans = inf
        for u,v in edges:
            G[u].add(v)
            G[v].add(u)
        
        def bfs(i):
            dis = [inf] * n
            dis[i] = 0
            que = deque([[i, -1]])
            while que:
                i, fa = que.popleft()
                for j in G[i]:
                    if dis[j] == inf:
                        dis[j] = 1 + dis[i]
                        que.append([j, i])
                    elif fa != j:
                        return dis[i] + dis[j] + 1
            return inf
        for u in range(n):
            ans = min(ans, bfs(u))
            # print(u, ans)
        return -1 if ans == inf else ans




if __name__ == '__main__':
    # print(Solution().findShortestCycle(n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]))
    # print(Solution().findShortestCycle2(n = 7, edges = [[0,1],[1,2],[2,0],[3,4],[4,5],[5,6],[6,3]]))
    # print(Solution().findShortestCycle2(n = 4, edges = [[0,1],[0,2]]))
    # n = 13
    # edges = [[0,1],[1,2],[2,0],[0,3],[3,4],[4,5],[6,7],[7,8],[8,9],[9,10],[10,11],[11,12],[12,0],[2,7],[2,4],[1,8],[1,11]]
    # print(Solution().findShortestCycle2(n = n, edges = edges))
    # n = 10
    # edges = [[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7],[1,8],[1,9],[2,3],[2,4],[2,5],[2,6],[2,7],[2,8],[2,9],[3,4],[3,5],[3,6],[3,7],[3,8],[3,9],[4,5],[4,6],[4,7],[4,8],[4,9],[5,6],[5,7],[5,8],[5,9],[6,7],[6,8],[6,9],[7,8],[7,9],[8,9]]
    # print(Solution().findShortestCycle2(n = n, edges = edges))
    n = 20
    edges = [[8, 19], [1, 19], [0, 19], [7, 15], [13, 17], [4, 19], [2, 6], [17, 18], [7, 14], [7, 18], [5, 6], [16, 17], [1, 12], [9, 16], [6, 15], [2, 14], [4, 17], [2, 10], [0, 18], [7, 11], [5, 14], [8, 14], [4, 9], [7, 9], [9, 18], [0, 14]]
    # print(Solution().findShortestCycle2(n = n, edges = edges))
    # print(Solution().findShortestCycle4(n = n, edges = edges))
    print(Solution().findShortestCycle3(n = n, edges = edges))