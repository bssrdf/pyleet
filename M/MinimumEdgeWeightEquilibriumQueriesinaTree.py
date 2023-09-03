'''

-Hard-
*DFS*
*Tarjan LCA*
*Union Find*

There is an undirected tree with n nodes labeled from 0 to n - 1. You are given the integer n and a 2D integer array edges of length n - 1, where edges[i] = [ui, vi, wi] indicates that there is an edge between nodes ui and vi with weight wi in the tree.

You are also given a 2D integer array queries of length m, where queries[i] = [ai, bi]. For each query, find the minimum number of operations required to make the weight of every edge on the path from ai to bi equal. In one operation, you can choose any edge of the tree and change its weight to any value.

Note that:

Queries are independent of each other, meaning that the tree returns to its initial state on each new query.
The path from ai to bi is a sequence of distinct nodes starting with node ai and ending with node bi such that every two adjacent nodes in the sequence share an edge in the tree.
Return an array answer of length m where answer[i] is the answer to the ith query.

 

Example 1:


Input: n = 7, edges = [[0,1,1],[1,2,1],[2,3,1],[3,4,2],[4,5,2],[5,6,2]], queries = [[0,3],[3,6],[2,6],[0,6]]
Output: [0,0,1,3]
Explanation: In the first query, all the edges in the path from 0 to 3 have a weight of 1. Hence, the answer is 0.
In the second query, all the edges in the path from 3 to 6 have a weight of 2. Hence, the answer is 0.
In the third query, we change the weight of edge [2,3] to 2. After this operation, all the edges in the path from 2 to 6 have a weight of 2. Hence, the answer is 1.
In the fourth query, we change the weights of edges [0,1], [1,2] and [2,3] to 2. After these operations, all the edges in the path from 0 to 6 have a weight of 2. Hence, the answer is 3.
For each queries[i], it can be shown that answer[i] is the minimum number of operations needed to equalize all the edge weights in the path from ai to bi.
Example 2:


Input: n = 8, edges = [[1,2,6],[1,3,4],[2,4,6],[2,5,3],[3,6,6],[3,0,8],[7,0,2]], queries = [[4,6],[0,4],[6,5],[7,4]]
Output: [1,2,2,3]
Explanation: In the first query, we change the weight of edge [1,3] to 6. After this operation, all the edges in the path from 4 to 6 have a weight of 6. Hence, the answer is 1.
In the second query, we change the weight of edges [0,3] and [3,1] to 6. After these operations, all the edges in the path from 0 to 4 have a weight of 6. Hence, the answer is 2.
In the third query, we change the weight of edges [1,3] and [5,2] to 6. After these operations, all the edges in the path from 6 to 5 have a weight of 6. Hence, the answer is 2.
In the fourth query, we change the weights of edges [0,7], [0,3] and [1,3] to 6. After these operations, all the edges in the path from 7 to 4 have a weight of 6. Hence, the answer is 3.
For each queries[i], it can be shown that answer[i] is the minimum number of operations needed to equalize all the edge weights in the path from ai to bi.
 

Constraints:

1 <= n <= 104
edges.length == n - 1
edges[i].length == 3
0 <= ui, vi < n
1 <= wi <= 26
The input is generated such that edges represents a valid tree.
1 <= queries.length == m <= 2 * 104
queries[i].length == 2
0 <= ai, bi < n

'''

from typing import List
from collections import defaultdict
class Solution:
    def minOperationsQueries(self, n: int, edges: List[List[int]], queries: List[List[int]]) -> List[int]:
        G = [[] for _ in range(n)]
        for u,v,w in edges:
            G[u].append([v,w])
            G[v].append([u,w])
        pathLen = [0]*n
        M = (max(w for _,_,w in edges) if edges else 1) +1
        uniq = [[0]*M for _ in range(n)]
        def dfs(u, par, depth, cnt):
            pathLen[u] = depth
            for i in range(1,M):
               uniq[u][i] = cnt[i]
            for v,w in G[u]:
                if v == par: continue
                newc = cnt[:]  
                newc[w] += 1
                dfs(v, u, depth+1, newc)
        c = [0]*M        
        dfs(0, -1,  0, c)       
        # print(uniq) 
        # print(pathLen)
        def LCA(queries):
            color = [0] * n
            pa = list(range(n))
            def find(x:int) -> int:
                if x != pa[x]:
                    pa[x] = find(pa[x])
                return pa[x]
            qs = [[] for _ in range(n)]
            ans = [-1]*len(queries)
            for i, (s, e) in enumerate(queries):
                qs[s].append((e,i))  # 路径端点分组
                if s != e:
                    qs[e].append((s,i))
            def tarjan(x: int, fa: int) -> None:
                color[x] = 1  # 递归中
                for y,_ in G[x]:
                    if color[y] == 0:  # 未递归
                        tarjan(y, x)
                        pa[y] = x  # 相当于把 y 的子树节点全部 merge 到 x
                for y,i in qs[x]:
                    # color[y] == 2 意味着 y 所在子树已经遍历完
                    # 也就意味着 y 已经 merge 到它和 x 的 lca 上了
                    if y == x or color[y] == 2:  # 从 y 向上到达 lca 然后拐弯向下到达 x
                        lca = find(y)
                        ans[i] = (pathLen[x] + pathLen[y] - 2 * pathLen[lca] - 
                          max(uniq[x][k]+uniq[y][k]-2*uniq[lca][k] for k in range(1,M)))  
                               
                color[x] = 2  # 递归结束
            tarjan(0, -1)
            return ans
        
        return LCA(queries)
    

if __name__ == "__main__":
    print(Solution().minOperationsQueries(n = 7, edges = [[0,1,1],[1,2,1],[2,3,1],[3,4,2],[4,5,2],[5,6,2]], queries = [[0,3],[3,6],[2,6],[0,6]]))
    print(Solution().minOperationsQueries(n = 8, edges = [[1,2,6],[1,3,4],[2,4,6],[2,5,3],[3,6,6],[3,0,8],[7,0,2]], queries = [[4,6],[0,4],[6,5],[7,4]]))