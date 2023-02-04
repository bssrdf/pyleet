'''
-Medium-
*Union Find*


You are given an integer n. There is an undirected graph with n nodes, numbered from 0 to n - 1. You are given a 2D integer array edges where edges[i] = [ai, bi] denotes that there exists an undirected edge connecting nodes ai and bi.

Return the number of pairs of different nodes that are unreachable from each other.

 

Example 1:


Input: n = 3, edges = [[0,1],[0,2],[1,2]]
Output: 0
Explanation: There are no pairs of nodes that are unreachable from each other. Therefore, we return 0.
Example 2:


Input: n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]
Output: 14
Explanation: There are 14 pairs of nodes that are unreachable from each other:
[[0,1],[0,3],[0,6],[1,2],[1,3],[1,4],[1,5],[2,3],[2,6],[3,4],[3,5],[3,6],[4,6],[5,6]].
Therefore, we return 14.
 

Constraints:

1 <= n <= 105
0 <= edges.length <= 2 * 105
edges[i].length == 2
0 <= ai, bi < n
ai != bi
There are no repeated edges.


'''

from typing import List

class Solution:
    def countPairs(self, n: int, edges: List[List[int]]) -> int:
        roots = [i for i in range(n)]
        sizes = [1]*n
        def find(x):
            while x != roots[x]:
                roots[x] = roots[roots[x]]
                x = roots[x]
            return x

        def union(x, y):
            px, py = find(x), find(y)
            if px > py:
                roots[px] = py                
                sizes[py] += sizes[px]
            elif px < py:
                roots[py] = px                
                sizes[px] += sizes[py]

        for u,v in edges:
            union(u, v)

        s, t = set(), 0
        for i in range(n):
            pi = find(i)
            if pi not in s:
                s.add(i)
                t += sizes[i]*(sizes[i]-1)//2
        return n*(n-1)//2 - t


        

        

if __name__ == "__main__":
    print(Solution().countPairs(n = 7, edges = [[0,2],[0,5],[2,4],[1,6],[5,4]]))
    
    print(Solution().countPairs(11, [[5,0],[1,0],[10,7],[9,8],[7,2],[1,3],[0,2],[8,5],[4,6],[4,2]]))