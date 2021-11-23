'''
-Hard-
*DFS*
*BFS*

Given an undirected tree consisting of n vertices numbered from 1 to n. A frog 
starts jumping from vertex 1. In one second, the frog jumps from its current 
vertex to another unvisited vertex if they are directly connected. The frog 
can not jump back to a visited vertex. In case the frog can jump to several 
vertices, it jumps randomly to one of them with the same probability. Otherwise, 
when the frog can not jump to any unvisited vertex, it jumps forever on the same vertex.

The edges of the undirected tree are given in the array edges, where 
edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi.

Return the probability that after t seconds the frog is on the vertex target.

 

Example 1:



Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4
Output: 0.16666666666666666 
Explanation: The figure above shows the given graph. The frog starts at vertex 1, jumping with 1/3 probability to the vertex 2 after second 1 and then jumping with 1/2 probability to vertex 4 after second 2. Thus the probability for the frog is on the vertex 4 after 2 seconds is 1/3 * 1/2 = 1/6 = 0.16666666666666666. 
Example 2:



Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7
Output: 0.3333333333333333
Explanation: The figure above shows the given graph. The frog starts at vertex 1, jumping with 1/3 = 0.3333333333333333 probability to the vertex 7 after second 1. 
Example 3:

Input: n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 20, target = 6
Output: 0.16666666666666666
 

Constraints:

1 <= n <= 100
edges.length == n - 1
edges[i].length == 2
1 <= ai, bi <= n
1 <= t <= 50
1 <= target <= n
Answers within 10-5 of the actual value will be accepted as correct.


'''
from typing import List

from collections import defaultdict, deque

class Solution:
    def frogPosition(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        visited = [False]*(n+1)
        self.prob = 0.0
        def dfs(u, cur_t, prob):
            if cur_t > t:                 
                return False            
            if u == target:
                if cur_t == t or len(graph[u]) == (u != 1):
                    self.prob = prob
                return True                 
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    if dfs(v, cur_t+1, prob/(len(graph[u])-(u!=1))):
                        return True 
            return False

        visited[1] = True
        dfs(1, 0, 1.0)
        return self.prob

    def frogPosition2(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        graph, que = defaultdict(set), deque()
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        visited = [False]*(n+1)
        prob = [0.0]*(n+1)
        prob[1] = 1.0
        visited[1] = True
        que.append(1)
        while que and t > 0:
            t -= 1
            for _ in range(len(que)):
                u = que.popleft()
                n = 0
                for v in graph[u]:
                    if not visited[v]: n += 1
                for v in graph[u]:
                    if not visited[v]: 
                        visited[v] = True
                        que.append(v)
                        prob[v] = prob[u] / n 
                if n > 0: prob[u] = 0.0 # frog don't stay vertex u, he keeps going to the next vertex
        return prob[target]         

    def frogPosition3(self, n: int, edges: List[List[int]], t: int, target: int) -> float:
        # when we found target during BFS search, we can immediately return the result
        #There are 3 cases to consider:

        # t == 0, we return p[target]
        # t >0 && target has no children. Frog will be trapped at target, we return p[target]
        # t >0 && target has children. Frog will jump to the children node, we return 0.0
        graph, que = defaultdict(set), deque()
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        visited = [False]*(n+1)
        prob = [0.0]*(n+1)
        prob[1] = 1.0
        visited[1] = True
        que.append(1)
        while que:
            if t < 0: break # time t run out, did not meet target
            for _ in range(len(que)):
                u = que.popleft()
                n = 0
                for v in graph[u]:
                    if not visited[v]: n += 1
                if u == target:
                    if t == 0 or n == 0: return prob[u] # stop at target(t=0) or stuck at target(t>0)
                    else: return 0.0 # move past target
                # did not meet target yet, continue BFS
                for v in graph[u]:
                    if not visited[v]: 
                        visited[v] = True
                        que.append(v)
                        prob[v] = prob[u] / n 
            t -= 1                            
        return 0.0
        

if __name__ == "__main__":
    print(Solution().frogPosition(n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4))
    print(Solution().frogPosition(n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7))
    print(Solution().frogPosition(n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 20, target = 6))
    print(Solution().frogPosition(8, [[2,1],[3,2],[4,1],[5,1],[6,4],[7,1],[8,7]], 7, 7))
    print(Solution().frogPosition2(n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 2, target = 4))
    print(Solution().frogPosition2(n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 1, target = 7))
    print(Solution().frogPosition2(n = 7, edges = [[1,2],[1,3],[1,7],[2,4],[2,6],[3,5]], t = 20, target = 6))
    print(Solution().frogPosition2(8, [[2,1],[3,2],[4,1],[5,1],[6,4],[7,1],[8,7]], 7, 7))