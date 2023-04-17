'''

-Hard-
*DP*
*DFS*
*BFS*
*Tarjan's Offline LCA Algorithm"
*Difference Array*

There exists an undirected and unrooted tree with n nodes indexed from 0 to n - 1. You are given the integer n and a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Each node has an associated price. You are given an integer array price, where price[i] is the price of the ith node.

The price sum of a given path is the sum of the prices of all nodes lying on that path.

Additionally, you are given a 2D integer array trips, where trips[i] = [starti, endi] indicates that you start the ith trip from the node starti and travel to the node endi by any path you like.

Before performing your first trip, you can choose some non-adjacent nodes and halve the prices.

Return the minimum total price sum to perform all the given trips.

 

Example 1:


Input: n = 4, edges = [[0,1],[1,2],[1,3]], price = [2,2,10,6], trips = [[0,3],[2,1],[2,3]]
Output: 23
Explanation: The diagram above denotes the tree after rooting it at node 2. The first part shows the initial tree and the second part shows the tree after choosing nodes 0, 2, and 3, and making their price half.
For the 1st trip, we choose path [0,1,3]. The price sum of that path is 1 + 2 + 3 = 6.
For the 2nd trip, we choose path [2,1]. The price sum of that path is 2 + 5 = 7.
For the 3rd trip, we choose path [2,1,3]. The price sum of that path is 5 + 2 + 3 = 10.
The total price sum of all trips is 6 + 7 + 10 = 23.
It can be proven, that 23 is the minimum answer that we can achieve.
Example 2:


Input: n = 2, edges = [[0,1]], price = [2,2], trips = [[0,0]]
Output: 1
Explanation: The diagram above denotes the tree after rooting it at node 0. The first part shows the initial tree and the second part shows the tree after choosing node 0, and making its price half.
For the 1st trip, we choose path [0]. The price sum of that path is 1.
The total price sum of all trips is 1. It can be proven, that 1 is the minimum answer that we can achieve.
 

Constraints:

1 <= n <= 50
edges.length == n - 1
0 <= ai, bi <= n - 1
edges represents a valid tree.
price.length == n
price[i] is an even integer.
1 <= price[i] <= 1000
1 <= trips.length <= 100
0 <= starti, endi <= n - 1



'''

from typing import List
from math import inf
from collections import defaultdict
import heapq
class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        # Wrong
        ans = inf 
        G = defaultdict(list)
        for u,v in edges:
            G[u].append(v)
            G[v].append(u)

        def halve(u, half, vis, p):
            vis[u] = True
            if half: p[u] >>= 1
            for v in G[u]:
                if not vis[v]:
                    halve(v, half^1, vis, p)
                
        def trip(src, dst, p):
            pq = [(p[src], src)]
            dist = [inf]*n
            while pq:
                d, u = heapq.heappop(pq)
                if u == dst: return d
                dist[u] = d
                for v in G[u]:
                    if dist[v] > dist[u] + p[v]:
                        dist[v] = dist[u] + p[v]
                        heapq.heappush(pq, (dist[v], v))
                    
        for i in range(n):
            P = price[:]
            visited = [False]*n
            halve(i, 1, visited, P)            
            t = sum(trip(s,e,P) for s,e in trips)
            ans = min(ans, t)
        return ans

    def minimumTotalPrice2(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        G = defaultdict(list)
        for u,v in edges:
            G[u].append(v)
            G[v].append(u)

        cnt = [0]*n
        
        for s,e in trips:
            def dfs(u, fa):
                if u == e: 
                    cnt[u] += 1
                    return True
                for v in G[u]:
                    if v != fa and dfs(v, u):
                        cnt[u] += 1 # increment cnt only after finding dest
                        return True
                return False
            dfs(s, -1)
        # similar to House Robber III
        def dp(u, fa):
            not_halve = price[u] * cnt[u]
            halve = not_halve // 2
            for v in G[u]:
                if v != fa:
                    nh, h = dp(v, u)
                    not_halve += min(nh, h)
                    halve += nh
            return not_halve, halve  

        return min(dp(0, -1))
    
    def minimumTotalPrice3(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        # Faster: Tarjan 离线 LCA + 树上差分
        # 核心思路：利用树上差分打标记，再通过一次 DFS 算出 cnt 值。
        # https://leetcode.cn/problems/minimize-the-total-price-of-the-trips/solution/lei-si-da-jia-jie-she-iii-pythonjavacgo-4k3wq/
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)  # 建树

        qs = [[] for _ in range(n)]
        for s, e in trips:
            qs[s].append(e)  # 路径端点分组
            if s != e:
                qs[e].append(s)

        # 并查集模板
        pa = list(range(n))
        def find(x: int) -> int:
            if x != pa[x]:
                pa[x] = find(pa[x])
            return pa[x]

        diff = [0] * n
        father = [0] * n
        color = [0] * n
        def tarjan(x: int, fa: int) -> None:
            father[x] = fa
            color[x] = 1  # 递归中
            for y in g[x]:
                if color[y] == 0:  # 未递归
                    tarjan(y, x)
                    pa[y] = x  # 相当于把 y 的子树节点全部 merge 到 x
            for y in qs[x]:
                # color[y] == 2 意味着 y 所在子树已经遍历完
                # 也就意味着 y 已经 merge 到它和 x 的 lca 上了
                if y == x or color[y] == 2:  # 从 y 向上到达 lca 然后拐弯向下到达 x
                    diff[x] += 1
                    diff[y] += 1
                    lca = find(y)
                    diff[lca] -= 1
                    if father[lca] >= 0:
                        diff[father[lca]] -= 1
            color[x] = 2  # 递归结束
        tarjan(0, -1)

        def dfs(x, fa):
            not_halve, halve, cnt = 0, 0, diff[x]
            for y in g[x]:
                if y != fa:
                    nh, h, c = dfs(y, x)  # 计算 y 不变/减半的最小价值总和
                    not_halve += min(nh, h)  # x 不变，那么 y 可以不变，可以减半，取这两种情况的最小值
                    halve += nh  # x 减半，那么 y 只能不变
                    cnt += c  # 自底向上累加差分值
            not_halve += price[x] * cnt  # x 不变
            halve += price[x] * cnt // 2  # x 减半
            return not_halve, halve, cnt
        return min(dfs(0, -1)[:2])



if __name__ == '__main__':
    # print(Solution().minimumTotalPrice(n = 4, edges = [[0,1],[1,2],[1,3]], price = [2,2,10,6], trips = [[0,3],[2,1],[2,3]]))
    n = 9
    edges = [[2,5],[3,4],[4,1],[1,7],[6,7],[7,0],[0,5],[5,8]]
    price = [4,4,6,4,2,4,2,14,8]
    trips = [[1,5],[2,7],[4,3],[1,8],[2,8],[4,3],[1,5],[1,4],[2,1],[6,0],[0,7],[8,6],[4,0],[7,5],[7,5],[6,0],[5,1],[1,1],[7,5],[1,7],[8,7],[2,3],[4,1],[3,5],[2,5],[3,7],[0,1],[5,8],[5,3],[5,2]]
    print(Solution().minimumTotalPrice2(n = n, edges = edges, price = price, trips = trips))
    print(Solution().minimumTotalPrice3(n = n, edges = edges, price = price, trips = trips))