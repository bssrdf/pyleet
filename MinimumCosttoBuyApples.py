'''

-Medium-

*Dijkstra's Algorithm*

$$$

You are given a positive integer n representing n cities numbered from 1 to n. You are also given a 2D array roads, where roads[i] = [ai, bi, costi] indicates that there is a bidirectional road between cities ai and bi with a cost of traveling equal to costi.

You can buy apples in any city you want, but some cities have different costs to buy apples. You are given the array appleCost where appleCost[i] is the cost of buying one apple from city i.

You start at some city, traverse through various roads, and eventually buy exactly one apple from any city. After you buy that apple, you have to return back to the city you started at, but now the cost of all the roads will be multiplied by a given factor k.

Given the integer k, return an array answer of size n where answer[i] is the minimum total cost to buy an apple if you start at city i.

 

Example 1:



Input: n = 4, roads = [[1,2,4],[2,3,2],[2,4,5],[3,4,1],[1,3,4]], appleCost = [56,42,102,301], k = 2
Output: [54,42,48,51]
Explanation: The minimum cost for each starting city is the following:
- Starting at city 1: You take the path 1 -> 2, buy an apple at city 2, and finally take the path 2 -> 1. The total cost is 4 + 42 + 4 * 2 = 54.
- Starting at city 2: You directly buy an apple at city 2. The total cost is 42.
- Starting at city 3: You take the path 3 -> 2, buy an apple at city 2, and finally take the path 2 -> 3. The total cost is 2 + 42 + 2 * 2 = 48.
- Starting at city 4: You take the path 4 -> 3 -> 2 then you buy at city 2, and finally take the path 2 -> 3 -> 4. The total cost is 1 + 2 + 42 + 1 * 2 + 2 * 2 = 51.
Example 2:



Input: n = 3, roads = [[1,2,5],[2,3,1],[3,1,2]], appleCost = [2,3,1], k = 3
Output: [2,3,1]
Explanation: It is always optimal to buy the apple in the starting city.
 

Constraints:

2 <= n <= 1000
1 <= roads.length <= 1000
1 <= ai, bi <= n
ai != bi
1 <= costi <= 105
appleCost.length == n
1 <= appleCost[i] <= 105
1 <= k <= 100
There are no repeated edges.




'''

from typing import List
import heapq
from collections import defaultdict

class Solution:
    def minCost(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        G = defaultdict(list)
        for u,v,c in roads:
            G[u].append((v, c))
            G[v].append((u, c))

        def dijkstra(city, C):
            pq = [(0, city)]
            while pq:
                cost, u = heapq.heappop(pq)
                if cost > C[u]: continue
                for v, c in G[u]:
                    if C[v] > cost + c:                        
                        C[v] = cost + c                        
                        heapq.heappush(pq, (C[v], v))
        ans = appleCost[:]
        for i in range(n):
            cost = [float('inf')]*(n+1)
            cost[i+1] = 0
            dijkstra(i+1, cost)
            # print(ans[i], cost)
            for j in range(n):
                if i != j:
                   ans[i] = min(ans[i], cost[j+1]*(k+1)+appleCost[j])
        return ans

    def minCost2(self, n: int, roads: List[List[int]], appleCost: List[int], k: int) -> List[int]:
        def dijkstra(i):
            q = [(0, i)]
            dist = [float('inf')] * n
            dist[i] = 0
            ans = float('inf')
            while q:
                d, u = heapq.heappop(q)
                ans = min(ans, appleCost[u] + d * (k + 1))
                for v, w in g[u]:
                    if dist[v] > dist[u] + w:
                        dist[v] = dist[u] + w
                        heapq.heappush(q, (dist[v], v))
            return ans

        g = defaultdict(list)
        for a, b, c in roads:
            a, b = a - 1, b - 1
            g[a].append((b, c))
            g[b].append((a, c))
        return [dijkstra(i) for i in range(n)]


from random import randint
if __name__=="__main__":
    print(Solution().minCost(n = 4, roads = [[1,2,4],[2,3,2],[2,4,5],[3,4,1],[1,3,4]], appleCost = [56,42,102,301], k = 2))
    print(Solution().minCost(n = 3, roads = [[1,2,5],[2,3,1],[3,1,2]], appleCost = [2,3,1], k = 3))
    N = 800
    roads = []
    appCost = [ randint(1, 100) for _ in range(N)] 
    conn = defaultdict(set)
    for i in range(1, N+1):
        k = randint(1, N)
        while k == i:
            k = randint(1, N)
        if k not in conn[i]:
           roads.append([i, k, randint(1, 100)])
           conn[i].add(k)
    print(len(roads))     
    sol1 = Solution().minCost(n = N, roads = roads, appleCost = appCost, k = 3)
    sol2 = Solution().minCost2(n = N, roads = roads, appleCost = appCost, k = 3)
        

