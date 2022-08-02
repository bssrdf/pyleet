'''

-Hard-
*DFS*
*Topological Sort*

You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.

The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from node i, then edges[i] == -1.

Return the length of the longest cycle in the graph. If no cycle exists, return -1.

A cycle is a path that starts and ends at the same node.

 

Example 1:


Input: edges = [3,3,4,2,3]
Output: 3
Explanation: The longest cycle in the graph is the cycle: 2 -> 4 -> 3 -> 2.
The length of this cycle is 3, so 3 is returned.
Example 2:


Input: edges = [2,-1,3,1]
Output: -1
Explanation: There are no cycles in this graph.
 

Constraints:

n == edges.length
2 <= n <= 105
-1 <= edges[i] < n
edges[i] != i



'''

from typing import List

class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        n = len(edges)
        dist, visited = [-1]*n, [False]*n
        ans = -1
        def dfs(u, d):
            nonlocal ans
            dist[u] = d
            v = edges[u] 
            if v != -1:
                if dist[v] == -1:
                    dfs(v, d+1)
                elif not visited[v] and dist[v] < d+1:
                    ans = max(ans, d+1-dist[v])
            visited[u] = True    
        for i in range(n):
            if edges[i] != -1 and dist[i] == -1:
                dfs(i, 0)
        return ans

    def longestCycle2(self, edges: List[int]) -> int:
        MAX, n = 10**6, len(edges)
        dist = [-1]*n
        ans = -1
        def dfs(u, d):
            nonlocal ans
            dist[u] = d
            v = edges[u] 
            if v != -1:
                if dist[v] == -1:
                    dfs(v, d+1)
                elif dist[v] < d+1:
                    ans = max(ans, d+1-dist[v])
            dist[u] = MAX  
        for i in range(n):
            if edges[i] != -1 and dist[i] == -1:
                dfs(i, 0)
        return ans


if __name__ == "__main__":
    print(Solution().longestCycle(edges = [3,3,4,2,3]))
    print(Solution().longestCycle(edges = [2,-1,3,1]))
    print(Solution().longestCycle(edges = [-1,4,-1,2,0,4]))
    edges = [49,29,24,24,-1,-1,-1,2,23,-1,44,47,52,49,9,31,40,34,-1,53,33,-1,2,-1,18,31,0,9,47,35,-1,-1,-1,-1,4,12,14,19,-1,4,4,43,25,11,54,-1,25,39,17,-1,22,44,-1,44,29,50,-1,-1]
    print(Solution().longestCycle(edges = edges))


    print(Solution().longestCycle2(edges = [3,3,4,2,3]))
    print(Solution().longestCycle2(edges = [2,-1,3,1]))
    print(Solution().longestCycle2(edges = [-1,4,-1,2,0,4]))
    edges = [49,29,24,24,-1,-1,-1,2,23,-1,44,47,52,49,9,31,40,34,-1,53,33,-1,2,-1,18,31,0,9,47,35,-1,-1,-1,-1,4,12,14,19,-1,4,4,43,25,11,54,-1,25,39,17,-1,22,44,-1,44,29,50,-1,-1]
    print(Solution().longestCycle2(edges = edges))
        