'''
-Medium-
*BFS*


You are given an integer n, the number of nodes in a directed graph where the nodes are labeled from 0 to n - 1. Each edge is red or blue in this graph, and there could be self-edges and parallel edges.

You are given two arrays redEdges and blueEdges where:

redEdges[i] = [ai, bi] indicates that there is a directed red edge from node ai to node bi in the graph, and
blueEdges[j] = [uj, vj] indicates that there is a directed blue edge from node uj to node vj in the graph.
Return an array answer of length n, where each answer[x] is the length of the shortest path from node 0 to node x such that the edge colors alternate along the path, or -1 if such a path does not exist.

 

Example 1:

Input: n = 3, redEdges = [[0,1],[1,2]], blueEdges = []
Output: [0,1,-1]
Example 2:

Input: n = 3, redEdges = [[0,1]], blueEdges = [[2,1]]
Output: [0,1,-1]
 

Constraints:

1 <= n <= 100
0 <= redEdges.length, blueEdges.length <= 400
redEdges[i].length == blueEdges[j].length == 2
0 <= ai, bi, uj, vj < n


'''

from typing import List
from collections import defaultdict, deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u,v in redEdges:
            graph[u].append((v, 1))
        for u,v in blueEdges:
            graph[u].append((v, -1))
        res = [-1]*n
        que = deque([(0, 0, 0)])
        visited = {(0,-1), (0, 1)}
        while que:
            u, col, d = que.popleft()
            if res[u] == -1:
                res[u] = d
            for v,c in graph[u]:
                if col == 1:
                    if c == -1 and (v, -1) not in visited:
                        visited.add((v, -1))
                        que.append((v, -1, d+1))
                elif col == -1:        
                    if c == 1 and (v, 1) not in visited:
                        visited.add((v, 1))
                        que.append((v, 1, d+1))
                else:
                    if c == -1 and (v, -1) not in visited:
                        visited.add((v, -1))
                        que.append((v, -1, d+1))
                    if c == 1 and (v, 1) not in visited:
                        visited.add((v, 1))
                        que.append((v, 1, d+1))
        return res

if __name__ == "__main__":
    n = 5
    red = [[0,1],[1,2],[2,3],[3,4]]
    blue = [[1,2],[2,3],[3,1]]
    print(Solution().shortestAlternatingPaths(n, red, blue))