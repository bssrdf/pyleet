'''

-Hard-
*Union Find*
*Greedy*
*MST*

There is a tree (i.e. a connected, undirected graph with no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges.

You are given a 0-indexed integer array vals of length n where vals[i] denotes the value of the ith node. You are also given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

A good path is a simple path that satisfies the following conditions:

The starting node and the ending node have the same value.
All nodes between the starting node and the ending node have values less than or equal to the starting node (i.e. the starting node's value should be the maximum value along the path).
Return the number of distinct good paths.

Note that a path and its reverse are counted as the same path. For example, 0 -> 1 is considered to be the same as 1 -> 0. A single node is also considered as a valid path.

 

Example 1:


Input: vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]
Output: 6
Explanation: There are 5 good paths consisting of a single node.
There is 1 additional good path: 1 -> 0 -> 2 -> 4.
(The reverse path 4 -> 2 -> 0 -> 1 is treated as the same as 1 -> 0 -> 2 -> 4.)
Note that 0 -> 2 -> 3 is not a good path because vals[2] > vals[0].
Example 2:


Input: vals = [1,1,2,2,3], edges = [[0,1],[1,2],[2,3],[2,4]]
Output: 7
Explanation: There are 5 good paths consisting of a single node.
There are 2 additional good paths: 0 -> 1 and 2 -> 3.
Example 3:


Input: vals = [1], edges = []
Output: 1
Explanation: The tree consists of only one node, so there is one good path.
 

Constraints:

n == vals.length
1 <= n <= 3 * 104
0 <= vals[i] <= 105
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
edges represents a valid tree.


'''

from typing import List
from collections import defaultdict, deque, Counter

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        # Wrong
        n = len(vals)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        ans = 0 
        def bfs(target):
            ret = 0
            que = deque()
            visited = [False]*n
            srcs = [0]*n
            for i in range(n):
                if vals[i] == target:
                    que.append(i)
                    visited[i] = True
                    srcs[i] = 1
            while que:
                u = que.popleft()                
                if target == 3:
                    print('X',target, u, ret, visited)
                for v in graph[u]:
                    if not visited and vals[v] <= target:
                        que.append(v)
                        if visited[v] == 0:
                            
                            visited[v] = visited[u]
                        else:
                            ret += visited[v]
                            visited[v] += visited[u]
            print(target, 'ret=', ret)
            return ret
        counter = Counter(vals)              
        for c in counter:
            if counter[c] > 1: ans += bfs(c)
            ans += counter[c]
            print(c, counter[c], ans)
        return ans
    
    def numberOfGoodPaths2(self, vals: List[int], edges: List[List[int]]) -> int:
        # // key concept
        # // gradually build up the graph from the nodes with small value
        # // so that whenever nodes with larger value are connected with other existing nodes (with smaller values)
        # // it ensures that any connection of the nodes (i.e., path) with larger value would be valid!
        res = n = len(vals)
        f = list(range(n))
        count = [Counter({vals[i]: 1}) for i in range(n)]
        # print(count)
        edges = sorted([max(vals[i], vals[j]),i,j] for i,j in edges)

        def find(x):
            while f[x] != x:
                f[x] = f[f[x]]
                x = f[x]
            return x

        for v,i,j in edges:
            fi, fj = find(i), find(j)
            cj, ci = count[fi][v], count[fj][v]
            res += ci * cj
            # print(v, i, j, fi, fj, ci, cj, count)
            f[fj] = fi
            count[fi] = Counter({v: ci + cj})
        return res


          

if __name__ == "__main__":
    # print(Solution().numberOfGoodPaths(vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]))
    print(Solution().numberOfGoodPaths2(vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]))
        