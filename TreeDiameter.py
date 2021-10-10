'''
-Medium-

Given an undirected tree, return its diameter: the number of edges in a 
longest path in that tree.

The tree is given as an array of edges where edges[i] = [u, v] is a 
bidirectional edge between nodes u and v.  Each node has labels in the 
set {0, 1, ..., edges.length}.

 

Example 1:



Input: edges = [[0,1],[0,2]]
Output: 2
Explanation: 
A longest path of the tree is the path 1 - 0 - 2.
Example 2:



Input: edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
Output: 4
Explanation: 
A longest path of the tree is the path 3 - 2 - 1 - 4 - 5.
 

Constraints:

0 <= edges.length < 10^4
edges[i][0] != edges[i][1]
0 <= edges[i][j] <= edges.length
The given edges form an undirected tree.

'''

from typing import List
from collections import deque, defaultdict


class Solution(object):
    def treeDiameter(self, edges):
        n = len(edges)+1
        degrees = [0]*n
        visited = [False]*n
        graph = defaultdict(set)
        que = deque()
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
            degrees[u] += 1
            degrees[v] += 1
        for i in range(n):
            if degrees[i] == 1:
                que.append(i)
                visited[i] = True
        depth = 0
        #print(que)
        remaining = n
        while que and remaining > 2:
            nxt = deque()
            size = len(que)
            for _ in range(len(que)):
                u = que.popleft()
                degrees[u] -= 1
                for v in graph[u]:
                    degrees[v] -= 1
                    if degrees[v] == 1 and not visited[v]:
                        nxt.append(v)
                        visited[v] = True
            que = nxt
            remaining -= size
            depth += 1

        return depth*2 if remaining == 1 else depth*2+1

    def treeDiameter2(self, edges):
        n = len(edges)+1
        graph = defaultdict(set)
        for u,v in edges:
            graph[u].add(v)
            graph[v].add(u)
        def bfs(src):
            visited = {src}
            q = deque([(src, 0)])  # Pair of (vertex, distance)
            farthestNode, farthestDist = -1, 0
            while len(q) > 0:
                farthestNode, farthestDist = u, d = q.popleft()
                for v in graph[u]:
                    if v not in visited:
                        visited.add(v)
                        q.append((v, d + 1))
            return farthestNode, farthestDist
        farthestNode, _ = bfs(0)
        _, dist = bfs(farthestNode)
        return dist
        
        



if __name__ == "__main__":
    edges = [[0,1],[1,2],[2,3],[1,4],[4,5]]
    print(Solution().treeDiameter(edges))
    print(Solution().treeDiameter2(edges))
