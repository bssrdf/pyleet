'''


-Hard-
*DP*
*Bitmask*
*Shortest Path*

There is a company with n branches across the country, some of which are connected by roads. Initially, all branches are reachable from each other by traveling some roads.

The company has realized that they are spending an excessive amount of time traveling between their branches. As a result, they have decided to close down some of these branches (possibly none). However, they want to ensure that the remaining branches have a distance of at most maxDistance from each other.

The distance between two branches is the minimum total traveled length needed to reach one branch from another.

You are given integers n, maxDistance, and a 0-indexed 2D array roads, where roads[i] = [ui, vi, wi] represents the undirected road between branches ui and vi with length wi.

Return the number of possible sets of closing branches, so that any branch has a distance of at most maxDistance from any other.

Note that, after closing a branch, the company will no longer have access to any roads connected to it.

Note that, multiple roads are allowed.

 

Example 1:


Input: n = 3, maxDistance = 5, roads = [[0,1,2],[1,2,10],[0,2,10]]
Output: 5
Explanation: The possible sets of closing branches are:
- The set [2], after closing, active branches are [0,1] and they are reachable to each other within distance 2.
- The set [0,1], after closing, the active branch is [2].
- The set [1,2], after closing, the active branch is [0].
- The set [0,2], after closing, the active branch is [1].
- The set [0,1,2], after closing, there are no active branches.
It can be proven, that there are only 5 possible sets of closing branches.
Example 2:


Input: n = 3, maxDistance = 5, roads = [[0,1,20],[0,1,10],[1,2,2],[0,2,2]]
Output: 7
Explanation: The possible sets of closing branches are:
- The set [], after closing, active branches are [0,1,2] and they are reachable to each other within distance 4.
- The set [0], after closing, active branches are [1,2] and they are reachable to each other within distance 2.
- The set [1], after closing, active branches are [0,2] and they are reachable to each other within distance 2.
- The set [0,1], after closing, the active branch is [2].
- The set [1,2], after closing, the active branch is [0].
- The set [0,2], after closing, the active branch is [1].
- The set [0,1,2], after closing, there are no active branches.
It can be proven, that there are only 7 possible sets of closing branches.
Example 3:

Input: n = 1, maxDistance = 10, roads = []
Output: 2
Explanation: The possible sets of closing branches are:
- The set [], after closing, the active branch is [0].
- The set [0], after closing, there are no active branches.
It can be proven, that there are only 2 possible sets of closing branches.
 

Constraints:

1 <= n <= 10
1 <= maxDistance <= 105
0 <= roads.length <= 1000
roads[i].length == 3
0 <= ui, vi <= n - 1
ui != vi
1 <= wi <= 1000
All branches are reachable from each other by traveling some roads.


'''

from typing import List
from math import inf
class Solution:
    def numberOfSets(self, n: int, maxDistance: int, roads: List[List[int]]) -> int:
        ans, mxmask = 0, 2**n-1
        def find(mask):           
            dist = [[inf]*n for _ in range(n)]
            dist0 = [[inf]*n for _ in range(n)]
            for i in range(n):
                dist0[i][i] = 0
            for u,v,w in roads:
                if (1 << u) & mask > 0 or (1 << v) & mask > 0:
                    continue                                                
                if w < dist0[u][v]:
                    dist0[u][v] = w
                    dist0[v][u] = w
               
            for k in range(n):
                for i in range(n):
                    for j in range(n):
                       dist[i][j] = min(dist0[i][j], dist0[i][k] + dist0[k][j]) 
                dist, dist0 = dist0, dist

            for i in range(n):
                if (1 << i) & mask == 0:     
                    for j in range(n):    
                        if (1 << j) & mask == 0:     
                            if dist0[i][j] > maxDistance:
                                return 0
            return 1

        for i in range(mxmask+1):
            x = find(i)
            ans += x
        return ans



if __name__ == "__main__":
    print(Solution().numberOfSets(n = 3, maxDistance = 5, roads = [[0,1,2],[1,2,10],[0,2,10]]))
    print(Solution().numberOfSets(n = 3, maxDistance = 5, roads = [[0,1,20],[0,1,10],[1,2,2],[0,2,2]]))
        