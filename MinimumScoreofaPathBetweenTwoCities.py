'''




'''
from typing import List
from collections import defaultdict

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        G = defaultdict(list)
        for u,v,w in roads:
            G[u].append((v,w))
            G[v].append((u,w))
        visited = [False]*(n+1)
        dmin = 10**4+1
        def dfs(u):
            nonlocal dmin
            visited[u] = True
            for v,w in G[u]:
                if not visited[v]:
                    dmin = min(dmin, w)
                    dfs(v)
        dfs(1)
        return dmin    
    
    def minScore2(self, n: int, roads: List[List[int]]) -> int:
        roots = [i for i in range(n)]
        dist = [10**4+1]*n
        def find(x):
            while x != roots[x]:
                roots[x] = roots[roots[x]]
                x = roots[x]
            return x
        def union(x, y, w):
            fx, fy = find(x), find(y)
            if fx < fy:
                roots[fy] = fx
                dist[fx] = min(dist[fx], dist[fy], w)
            else:
                roots[fx] = fy
                dist[fy] = min(dist[fy], dist[fx], w)
        for u,v,w in roads:
            union(u-1,v-1,w)
        print(roots)
        print(dist)

        return dist[0]



# print(Solution().minScore2(n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]))
    
# print(Solution().minScore2(6,
# [[4,5,7468],[6,2,7173],[6,3,8365],[2,3,7674],[5,6,7852],[1,2,8547],[2,4,1885],[2,5,5192],[1,3,4065],[1,4,7357]]))

print(Solution().minScore2(7,
[[1,3,1484],[3,2,3876],[2,4,6823],[6,7,579],[5,6,4436],[4,5,8830]]))