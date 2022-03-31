'''
-Hard-

We have n cities and m bi-directional roads where roads[i] = [a_i, b_i] connects 
city a_i with city b_i. Each city has a name consisting of exactly 3 upper-case 
English letters given in the string array names. Starting at any city x, you can 
reach any city y where y != x (i.e. the cities and the roads are forming an 
undirected connected graph).

You will be given a string array targetPath. You should find a path in the graph 
of the same length and with the minimum edit distance to targetPath.

You need to return the order of the nodes in the path with the minimum edit distance. 
The path should be of the same length of targetPath and should be valid (i.e. 
there should be a direct road between ans[i] and ans[i + 1]). If there are 
multiple answers return any one of them.

The edit distance is defined as follows:

Image text

Follow-up: If each node can be visited only once in the path, What should you 
change in your solution?

Example 1:

Image text

Input: n = 5, roads = [[0,2],[0,3],[1,2],[1,3],[1,4],[2,4]], names = [“ATL”,”PEK”,”LAX”,”DXB”,”HND”], targetPath = [“ATL”,”DXB”,”HND”,”LAX”]

Output: [0,2,4,2]

Explanation: [0,2,4,2], [0,3,0,2] and [0,3,1,2] are accepted answers.

[0,2,4,2] is equivalent to [“ATL”,”LAX”,”HND”,”LAX”] which has edit distance = 1 with targetPath.

[0,3,0,2] is equivalent to [“ATL”,”DXB”,”ATL”,”LAX”] which has edit distance = 1 with targetPath.

[0,3,1,2] is equivalent to [“ATL”,”DXB”,”PEK”,”LAX”] which has edit distance = 1 with targetPath.

Example 2:

Image text


n = 4, roads = [[1,0],[2,0],[3,0],[2,1],[3,1],[3,2]], names = ["ATL","PEK","LAX","DXB"], targetPath = ["ABC","DEF","GHI","JKL","MNO","PQR","STU","VWX"]


Output: [0,1,0,1,0,1,0,1]

Explanation: Any path in this graph has edit distance = 8 with targetPath.

Example 3:

Image text

n = 6, roads = [[0,1],[1,2],[2,3],[3,4],[4,5]], names = ["ATL","PEK","LAX","ATL","DXB","HND"], targetPath = ["ATL","DXB","HND","DXB","ATL","LAX","PEK"]


Output: [3,4,5,4,3,2,1]

Explanation: [3,4,5,4,3,2,1] is the only path with edit distance = 0 with targetPath.

It’s equivalent to [“ATL”,”DXB”,”HND”,”DXB”,”ATL”,”LAX”,”PEK”]

Constraints:

2 <= n <= 100
m == roads.length
n - 1 <= m <= (n * (n - 1) / 2)
0 <= a_i, b_i <= n - 1
a_i != b_i
The graph is guaranteed to be connected and each pair of nodes may have at most one direct road.
names.length == n
names[i].length == 3
names[i] consists of upper-case English letters.
There can be two cities with the same name.
1 <= targetPath.length <= 100
targetPath[i].length == 3
targetPath[i] consists of upper-case English letters.


'''

from collections import defaultdict
from functools  import lru_cache
class Solution(object):
    def mostSimilar(self, n, roads, names, targetPath):
        graph = defaultdict(list)
        m = len(targetPath)
        paths = [[] for _ in range(n)]
        for u,v in roads:
            graph[u].append(v)
            graph[v].append(u)
        @lru_cache(None)
        def dfs(u, l):
            if l == m-1: 
                return (0,[u]) if names[u] == targetPath[l] else (1,[u])   
            ret, pa = float('inf'), []             
            for v in graph[u]:
                ed, path = dfs(v, l+1)
                if ret > ed:
                    ret, pa = ed, path
            return (ret + (0 if names[u] == targetPath[l] else 1), [u]+pa)     
        res, ans = [], m+1
        for i in range(n):
            d, p = dfs(i, 0)
            if ans > d:
                ans, res = d, p
        return res

    def mostSimilar2(self, n, roads, names, targetPath):
        """
        :type n: int
        :type roads: List[List[int]]
        :type names: List[str]
        :type targetPath: List[str]
        :rtype: List[int]
        """
        adj = [[] for _ in range(n)]
        for u, v in roads:
            adj[u].append(v)
            adj[v].append(u)

        dp = [[0]*n for _ in range(len(targetPath)+1)]
        for i in range(1, len(targetPath)+1):
            for v in range(n):
                dp[i][v] = (names[v] != targetPath[i-1]) + min(dp[i-1][u] for u in adj[v]) 

        path = [dp[-1].index(min(dp[-1]))]
        for i in reversed(range(2, len(targetPath)+1)):
            for u in adj[path[-1]]:
                if dp[i-1][u]+(names[path[-1]] != targetPath[i-1]) == dp[i][path[-1]]:
                    path.append(u)
                    break
        return path[::-1]


if __name__ == "__main__":
    n = 5
    roads = [[0,2],[0,3],[1,2],[1,3],[1,4],[2,4]]
    names = ['ATL','PEK','LAX','DXB','HND']
    targetPath = ['ATL', 'DXB', 'HND', 'LAX']
    print(Solution().mostSimilar(n, roads, names, targetPath))
    n = 4
    roads = [[1,0],[2,0],[3,0],[2,1],[3,1],[3,2]]
    names = ["ATL","PEK","LAX","DXB"]
    targetPath = ["ABC","DEF","GHI","JKL","MNO","PQR","STU","VWX"]
    print(Solution().mostSimilar(n, roads, names, targetPath))
    n = 6 
    roads = [[0,1],[1,2],[2,3],[3,4],[4,5]] 
    names = ["ATL","PEK","LAX","ATL","DXB","HND"]
    targetPath = ["ATL","DXB","HND","DXB","ATL","LAX","PEK"]
    print(Solution().mostSimilar(n, roads, names, targetPath))
