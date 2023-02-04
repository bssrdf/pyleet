'''
-Hard-

A series of highways connect n cities numbered from 0 to n - 1. You are given a 2D integer array highways where highways[i] = [city1i, city2i, tolli] indicates that there is a highway that connects city1i and city2i, allowing a car to go from city1i to city2i and vice versa for a cost of tolli.

You are also given an integer k. You are going on a trip that crosses exactly k highways. You may start at any city, but you may only visit each city at most once during your trip.

Return the maximum cost of your trip. If there is no trip that meets the requirements, return -1.

 

Example 1:



Input: n = 5, highways = [[0,1,4],[2,1,3],[1,4,11],[3,2,3],[3,4,2]], k = 3
Output: 17
Explanation:
One possible trip is to go from 0 -> 1 -> 4 -> 3. The cost of this trip is 4 + 11 + 2 = 17.
Another possible trip is to go from 4 -> 1 -> 2 -> 3. The cost of this trip is 11 + 3 + 3 = 17.
It can be proven that 17 is the maximum possible cost of any valid trip.
Note that the trip 4 -> 1 -> 0 -> 1 is not allowed because you visit the city 1 twice.


Example 2:



Input: n = 4, highways = [[0,1,3],[2,3,2]], k = 2
Output: -1
Explanation: There are no valid trips of length 2, so return -1.
 

Constraints:

2 <= n <= 15
1 <= highways.length <= 50
highways[i].length == 3
0 <= city1i, city2i <= n - 1
city1i != city2i
0 <= tolli <= 100
1 <= k <= 50
There are no duplicate highways.


'''

from typing import List
from collections import defaultdict, Counter
from functools import lru_cache

class Solution:
    def maximumCost(self, n, highways, k):
        if k + 1 > n:
            return -1
        graph = defaultdict(list)
        for u, v, w in highways:
            graph[u].append((v,w))
            graph[v].append((u,w))
        ans = [0]
        @lru_cache(None)
        def dfs(u, path, cost):
            # print(u, bin(path), i, cost)
            if bin(path).count('1') == k+1:
            # if i == k: 
                ans[0] = max(ans[0], cost)
                return
            for v, w in graph[u]:    
                if path & 1<<v == 0:
                    dfs(v, path | 1<<v, cost+w)
        for u in range(n):
            dfs(u, 1<<u, 0)   
        return -1 if ans[0] == 0 else ans[0]

    def maximumCost2(self, n: int, highways: List[List[int]], k: int) -> int:
        # TLE
        if k > n: return -1
        web = [[] for _ in range(n)]

        for u, v, w in highways:
            web[u].append((v, w))
            web[v].append((u, w))
        
        def dfs(u, cost, cnt):
            nonlocal res
            if cnt == k:
                res = max(res, cost)
                return
            for v, w in web[u]:
                if v not in vis:
                    vis.add(v)
                    dfs(v, cost + w, cnt + 1)
                    vis.remove(v)
        
        res = -1
        for u in range(n):
            vis = {u}
            dfs(u, 0, 0)
        return res
    
    def maximumCost3(self, n: int, highways: List[List[int]], k: int) -> int:
        if k + 1 > n:
            return -1

        graph = [[] for _ in range(n)]

        for u, v, w in highways:
            graph[u].append((v, w))
            graph[v].append((u, w))

        # dp(u, mask) := max cost of trip starting from u
        # given mask representing visited cities
        @lru_cache(None)
        def dp(u: int, mask: int) -> int:
            # if mask.bit_count() == k + 1:
            if bin(mask).count('1') == k + 1:
                return 0

            ans = -1
            for v, w in graph[u]:
                if mask >> v & 1:
                    continue
                res = dp(v, mask | 1 << v)
                if res != -1:
                    ans = max(ans, w + res)
            return ans

        return max(dp(i, 1 << i) for i in range(n))




if __name__ == "__main__":
    print(Solution().maximumCost(n = 5, highways = [[0,1,4],[2,1,3],[1,4,11],[3,2,3],[3,4,2]], k = 3))
    print(Solution().maximumCost(n = 4, highways = [[0,1,3],[2,3,2]], k = 2))
    highways = [[0,1,1],[1,2,1],[2,3,1],[3,4,1],[4,5,1],[5,6,1],[6,7,1],[7,8,1],[8,9,1],[9,10,1],[10,11,1],[11,12,1],[12,13,1],[13,14,1],[0,2,1],[1,3,1],[2,4,1],[3,5,1],[4,6,1],[5,7,1],[6,8,1],[7,9,1],[8,10,1],[9,11,1],[10,12,1],[11,13,1],[12,14,1],[0,3,1],[1,4,1],[2,5,1],[3,6,1],[4,7,1],[5,8,1],[6,9,1],[7,10,1],[8,11,1],[9,12,1],[10,13,1],[11,14,1],[0,4,1],[1,5,1],[2,6,1],[3,7,1],[4,8,1],[5,9,1],[6,10,1],[7,11,1],[8,12,1],[9,13,1],[10,14,1]]
    print(Solution().maximumCost(15, highways, 14))
    print(Solution().maximumCost3(15, highways, 14))
    highways =[[8,9,1],[4,13,1],[0,7,1],[0,1,1],[2,3,1],[3,7,1],[8,14,1],[9,11,1],[5,11,1],[5,6,1],[4,5,1],[7,11,1],[3,5,1],[5,9,1],[3,9,1],[3,6,1],[10,12,1],[9,12,1],[6,13,1],[9,13,1],[1,9,1],[6,14,1],[2,6,1],[4,10,1],[3,12,1],[3,8,1],[6,12,1],[2,11,1],[7,13,1],[0,5,1],[6,11,1],[12,14,1],[4,9,1],[3,11,1],[0,6,1],[2,4,1],[8,13,1],[2,7,1],[7,14,1],[9,10,1],[7,9,1],[1,7,1],[4,6,1],[1,13,1],[6,8,1],[0,13,1],[0,4,1],[0,8,1],[11,13,1],[2,14,1]]
    print(Solution().maximumCost(15, highways, 13))
    print(Solution().maximumCost3(15, highways, 13))