'''

-Hard-

*DFS*
*Rerooting*
*DP*
*Tree DP*

There is an undirected tree with n nodes labeled from 1 to n. You are given the integer n and a 2D integer array edges of length n - 1, where edges[i] = [ui, vi] indicates that there is an edge between nodes ui and vi in the tree.

Return the number of valid paths in the tree.

A path (a, b) is valid if there exists exactly one prime number among the node labels in the path from a to b.

Note that:

The path (a, b) is a sequence of distinct nodes starting with node a and ending with node b such that every two adjacent nodes in the sequence share an edge in the tree.
Path (a, b) and path (b, a) are considered the same and counted only once.
 

Example 1:


Input: n = 5, edges = [[1,2],[1,3],[2,4],[2,5]]
Output: 4
Explanation: The pairs with exactly one prime number on the path between them are: 
- (1, 2) since the path from 1 to 2 contains prime number 2. 
- (1, 3) since the path from 1 to 3 contains prime number 3.
- (1, 4) since the path from 1 to 4 contains prime number 2.
- (2, 4) since the path from 2 to 4 contains prime number 2.
It can be shown that there are only 4 valid paths.
Example 2:


Input: n = 6, edges = [[1,2],[1,3],[2,4],[3,5],[3,6]]
Output: 6
Explanation: The pairs with exactly one prime number on the path between them are: 
- (1, 2) since the path from 1 to 2 contains prime number 2.
- (1, 3) since the path from 1 to 3 contains prime number 3.
- (1, 4) since the path from 1 to 4 contains prime number 2.
- (1, 6) since the path from 1 to 6 contains prime number 3.
- (2, 4) since the path from 2 to 4 contains prime number 2.
- (3, 6) since the path from 3 to 6 contains prime number 3.
It can be shown that there are only 6 valid paths.
 

Constraints:

1 <= n <= 105
edges.length == n - 1
edges[i].length == 2
1 <= ui, vi <= n
The input is generated such that edges represent a valid tree.

'''

from typing import List
import math

def sieve(n):
    A = [i for i in range(n+1)]
    A[1] = 0
    for p in range(2, math.floor(math.sqrt(n))+1):
        if A[p]:
            j = p*p
            while j <= n:
                A[j] = 0
                j += p
    L = []
    for p in range(2, n+1):
        if A[p]:
            L.append(A[p])
    return L

class Solution:
    def countPaths(self, n: int, edges: List[List[int]]) -> int:
        #TLE
        prims = set(sieve(n))
        G = [[] for _ in range(n+1)]
        for u,v in edges:
            G[u].append(v)
            G[v].append(u)

        def dfs(u, par):
            ret = 0 if u in prims else 1
            for v in G[u]:
                if v == par: continue
                ret += dfs(v, u)

            return 0 if u in prims else ret
        ans = 0
        for p in prims:
            t  = []
            for v in G[p]:
                r = dfs(v, p)
                if r != 0:
                    t.append(r)
            # print(p, t)
            if not t:
                continue
            elif len(t) == 1:  
                ans += t[0]
            else:
                ans += sum(t)
                x = 0
                for i in range(len(t)):
                    for j in range(len(t)):
                        if i != j:
                           x += t[i] * t[j]
                ans += x//2           
            # print(p, ans)    
        return ans    
        
    def countPaths2(self, n: int, edges: List[List[int]]) -> int:
        prims = set(sieve(n))
        G = [[] for _ in range(n+1)]
        for u,v in edges:
            G[u].append(v)
            G[v].append(u)
        ans = 0
        record = [0]*(n+1)    
        def dfs1(u, par):
            nonlocal ans
            total, subtotal = 0, 0
            for v in G[u]:
                if v == par: continue
                ret = dfs1(v, u)
                total += ret
                subtotal += ret * ret
            record[u] = total    
            if u in prims:
                ans += (total*total - subtotal)//2
                ans += total
                return 0
            return total + 1
        up = [0]*(n+1)
        def dfs2(u, par):
            nonlocal ans
            flag = 0
            if u in prims:
                ans += up[u] + up[u]*record[u]
                flag = 1
            for v in G[u]:
                if v == par: continue
                if flag == 1:
                    up[v] = 0
                    dfs2(v, u)
                elif v in prims:
                    up[v] = record[u] + 1 + up[u]
                    dfs2(v, u)
                else:
                    up[v] = up[u] + record[u] - record[v]
                    dfs2(v,u)

        dfs1(1,0)    
        dfs2(1,0)     
        return ans        
               


if __name__ == "__main__":
    print(Solution().countPaths(n = 5, edges = [[1,2],[1,3],[2,4],[2,5]]))
    print(Solution().countPaths(n = 6, edges = [[1,2],[1,3],[2,4],[3,5],[3,6]]))
    print(Solution().countPaths(n = 9, edges =
[[7,4],[3,4],[5,4],[1,5],[6,4],[9,5],[8,7],[2,8]]))