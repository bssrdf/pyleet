'''

-Medium-
*DFS*
*Union Find*

You are given a positive integer n representing n cities numbered from 1 to n. You are also given a 2D array roads where roads[i] = [ai, bi, distancei] indicates that there is a bidirectional road between cities ai and bi with a distance equal to distancei. The cities graph is not necessarily connected.

The score of a path between two cities is defined as the minimum distance of a road in this path.

Return the minimum possible score of a path between cities 1 and n.

Note:

A path is a sequence of roads between two cities.
It is allowed for a path to contain the same road multiple times, and you can visit cities 1 and n multiple times along the path.
The test cases are generated such that there is at least one path between 1 and n.
 

Example 1:


Input: n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]
Output: 5
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 4. The score of this path is min(9,5) = 5.
It can be shown that no other path has less score.
Example 2:


Input: n = 4, roads = [[1,2,2],[1,3,4],[3,4,7]]
Output: 2
Explanation: The path from city 1 to 4 with the minimum score is: 1 -> 2 -> 1 -> 3 -> 4. The score of this path is min(2,2,4,7) = 2.
 

Constraints:

2 <= n <= 105
1 <= roads.length <= 105
roads[i].length == 3
1 <= ai, bi <= n
ai != bi
1 <= distancei <= 104
There are no repeated edges.
There is at least one path between 1 and n.


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
                dmin = min(dmin, w) # still explore this edge even if v has already been visited before
                if not visited[v]:
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
        # print(roots)
        # print(dist)

        return dist[0]


if __name__ == "__main__":
    print(Solution().minScore(n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]))
    print(Solution().minScore2(n = 4, roads = [[1,2,9],[2,3,6],[2,4,5],[1,4,7]]))


    print(Solution().minScore(6,
    [[4,5,7468],[6,2,7173],[6,3,8365],[2,3,7674],[5,6,7852],[1,2,8547],[2,4,1885],[2,5,5192],[1,3,4065],[1,4,7357]]))    
    print(Solution().minScore2(6,
    [[4,5,7468],[6,2,7173],[6,3,8365],[2,3,7674],[5,6,7852],[1,2,8547],[2,4,1885],[2,5,5192],[1,3,4065],[1,4,7357]]))

    print(Solution().minScore(7,
    [[1,3,1484],[3,2,3876],[2,4,6823],[6,7,579],[5,6,4436],[4,5,8830]]))
    print(Solution().minScore2(7,
    [[1,3,1484],[3,2,3876],[2,4,6823],[6,7,579],[5,6,4436],[4,5,8830]]))