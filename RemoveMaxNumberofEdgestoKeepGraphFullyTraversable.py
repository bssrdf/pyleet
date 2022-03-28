'''
-Hard-


Alice and Bob have an undirected graph of n nodes and 3 types of edges:

Type 1: Can be traversed by Alice only.
Type 2: Can be traversed by Bob only.
Type 3: Can by traversed by both Alice and Bob.
Given an array edges where edges[i] = [typei, ui, vi] represents a bidirectional 
edge of type typei between nodes ui and vi, find the maximum number of edges you 
can remove so that after removing the edges, the graph can still be fully 
traversed by both Alice and Bob. The graph is fully traversed by Alice and 
Bob if starting from any node, they can reach all other nodes.

Return the maximum number of edges you can remove, or return -1 if it's 
impossible for the graph to be fully traversed by Alice and Bob.

 

Example 1:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]
Output: 2
Explanation: If we remove the 2 edges [1,1,2] and [1,1,3]. The graph will still be fully traversable by Alice and Bob. Removing any additional edge will not make it so. So the maximum number of edges we can remove is 2.
Example 2:



Input: n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]
Output: 0
Explanation: Notice that removing any edge will not make the graph fully traversable by Alice and Bob.
Example 3:



Input: n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]
Output: -1
Explanation: In the current graph, Alice cannot reach node 4 from the other nodes. Likewise, Bob cannot reach 1. Therefore it's impossible to make the graph fully traversable.
 

 

Constraints:

1 <= n <= 10^5
1 <= edges.length <= min(10^5, 3 * n * (n-1) / 2)
edges[i].length == 3
1 <= edges[i][0] <= 3
1 <= edges[i][1] < edges[i][2] <= n
All tuples (typei, ui, vi) are distinct.
'''


from tkinter import N
from typing import List

class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        A, B = [i for i in range(n+1)], [i for i in range(n+1)]
        rA, rB = [0 for i in range(n+1)], [0 for i in range(n+1)]
        nA, nB = [n], [n] 
        ans = 0
        def find(par, x):
            while x != par[x]:
                par[x] = par[par[x]]
                x = par[x]
            return x
        def union(par, rk, nc, x, y):
            fx, fy = find(par, x), find(par, y)
            if fx != fy:
                if rk[fx] < rk[fy]:
                    par[fx] = fy
                else:
                    par[fy] = fx
                    if rk[fx] == rk[fy]:
                       rk[fx] += 1
                nc[0] -= 1
        edges.sort(key=lambda x: x[0], reverse=True)
        for t,x,y in edges:
            a, b = nA[0], nB[0]
            if t == 3:
                union(A, rA, nA, x, y)
                union(B, rB, nB, x, y)
            elif t == 2:
                union(B, rB, nB, x, y)
            else:
                union(A, rA, nA, x, y)
            if a == nA[0] and b == nB[0]:
                ans += 1
            # print(t, x, y, a, b, nA[0], nB[0], A, B)
        if nA[0] != 1 or nB[0] != 1:
            return -1
        return ans




 







if __name__ == "__main__":
    print(Solution().maxNumEdgesToRemove(n = 4, edges = [[3,1,2],[3,2,3],[1,1,3],[1,2,4],[1,1,2],[2,3,4]]))
    print(Solution().maxNumEdgesToRemove(n = 4, edges = [[3,1,2],[3,2,3],[1,1,4],[2,1,4]]))
    print(Solution().maxNumEdgesToRemove(n = 4, edges = [[3,2,3],[1,1,2],[2,3,4]]))