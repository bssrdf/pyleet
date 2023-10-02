'''

-Hard-
*DFS*
*BFS*
*Topological Sort*
There is a directed graph consisting of n nodes numbered from 0 to n - 1 and n directed edges.

You are given a 0-indexed array edges where edges[i] indicates that there is an edge from node i to node edges[i].

Consider the following process on the graph:

You start from a node x and keep visiting other nodes through edges until you reach a node that you have already visited before on this same process.
Return an array answer where answer[i] is the number of different nodes that you will visit if you perform the process starting from node i.

 

Example 1:


Input: edges = [1,2,0,0]
Output: [3,3,3,4]
Explanation: We perform the process starting from each node in the following way:
- Starting from node 0, we visit the nodes 0 -> 1 -> 2 -> 0. The number of different nodes we visit is 3.
- Starting from node 1, we visit the nodes 1 -> 2 -> 0 -> 1. The number of different nodes we visit is 3.
- Starting from node 2, we visit the nodes 2 -> 0 -> 1 -> 2. The number of different nodes we visit is 3.
- Starting from node 3, we visit the nodes 3 -> 0 -> 1 -> 2 -> 0. The number of different nodes we visit is 4.
Example 2:


Input: edges = [1,2,3,4,0]
Output: [5,5,5,5,5]
Explanation: Starting from any node we can visit every node in the graph in the process.
 

Constraints:

n == edges.length
2 <= n <= 105
0 <= edges[i] <= n - 1
edges[i] != i



'''


from typing import List
from collections import deque
class Solution:
    def countVisitedNodes(self, edges: List[int]) -> List[int]:
        n = len(edges)
        indegs = [0]*n
        G = [[] for _ in range(n)]
        for i,v in enumerate(edges):
            G[i].append(v)
            indegs[v] += 1
        que = deque()
        for i in range(n):
            if indegs[i] == 0:
               que.append(i)
        notCycle = set()
        while que:
            u = que.popleft()
            notCycle.add(u)
            for v in G[u]:
                indegs[v] -= 1
                if indegs[v] == 0:
                    que.append(v)
        visited = set()
        depth = [-1]*n
        def dfs(u, d):
            if u in visited:               
               return d 
            visited.add(u)  
            v = G[u][0]
            ret = dfs(v, d+1)
            depth[u] = ret
            return ret

        for i in range(n):
            if i not in notCycle and i not in visited:
                dfs(i, 0)
                
        def dfs1(u):
            if u not in notCycle:
                return depth[u]             
            ret = 1 + dfs1(G[u][0])            
            depth[u] = ret 
            notCycle.remove(u)
            return ret
        for i in range(n):
            if i in notCycle:
               dfs1(i)   

        return depth



if __name__ == "__main__":
    print(Solution().countVisitedNodes(edges = [1,2,0,0]))
    print(Solution().countVisitedNodes(edges = [1,2,3,4,0]))
        