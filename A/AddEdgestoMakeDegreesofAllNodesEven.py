'''
-Hard-

There is an undirected graph consisting of n nodes numbered from 1 to n. You are given the integer n and a 2D array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi. The graph can be disconnected.

You can add at most two additional edges (possibly none) to this graph so that there are no repeated edges and no self-loops.

Return true if it is possible to make the degree of each node in the graph even, otherwise return false.

The degree of a node is the number of edges connected to it.

 

Example 1:


Input: n = 5, edges = [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]
Output: true
Explanation: The above diagram shows a valid way of adding an edge.
Every node in the resulting graph is connected to an even number of edges.
Example 2:


Input: n = 4, edges = [[1,2],[3,4]]
Output: true
Explanation: The above diagram shows a valid way of adding two edges.
Example 3:


Input: n = 4, edges = [[1,2],[1,3],[1,4]]
Output: false
Explanation: It is not possible to obtain a valid graph with adding at most 2 edges.
 

Constraints:

3 <= n <= 105
2 <= edges.length <= 105
edges[i].length == 2
1 <= ai, bi <= n
ai != bi
There are no repeated edges.

'''

from typing import List

from collections import defaultdict, deque

class Solution:
    def isPossible(self, n: int, edges: List[List[int]]) -> bool:
        G = defaultdict(set)
        # degs = [0]*(n+1)
        for u,v in edges:
            G[u].append(v)
            G[v].append(u)
            # degs[u] += 1
            # degs[v] += 1
        cnt = []
        for u in range(1, n+1):
            if len(G[u]) % 2 == 1:
                cnt.append(u)
        # print(cnt)
        if len(cnt) == 0: return True
        if len(cnt) >= 5 or len(cnt) % 2 == 1: return False 
        if len(cnt) == 2:
            if cnt[1] not in G[cnt[0]]: 
                return True
            a, b = cnt
            for i in range(1, n+1):
                if a != i and b != i and i not in G[a] and i not in G[b]:
                    return True
            return False
        else:
            a, b, c, d = cnt
            if d not in G[a] and c not in G[b]: return True
            if b not in G[a] and d not in G[c]: return True
            if c not in G[a] and d not in G[b]: return True
            return False
    
    def isPossible2(self, n: int, edges: List[List[int]]) -> bool:
        G = [set() for i in range(n)]
        for i,j in edges:
            G[i-1].add(j-1)
            G[j-1].add(i-1)
        odd = [i for i in range(n) if len(G[i]) % 2]

        def f(a,b):
            return a not in G[b]

        if len(odd) == 2:
            a, b = odd
            return any(f(a,i) and f(b,i) for i in range(n))

        if len(odd) == 4:
            a,b,c,d = odd
            return  f(a,b) and f(c,d) or \
                    f(a,c) and f(b,d) or \
                    f(a,d) and f(c,b)
        return len(odd) == 0


        
    
if __name__ == "__main__":
    print(Solution().isPossible(n = 5, edges = [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]))
    print(Solution().isPossible(n = 4, edges = [[1,2],[1,3],[1,4]]))
    print(Solution().isPossible(n = 4, edges = [[1,2],[3,4]]))
    n = 16
    edges = [[3,14],[14,10],[10,15],[16,11],[11,7],[4,8],[15,12],[12,9],[1,10],[14,7],[8,5],[9,3],[15,11],[10,12],[15,6],[16,13],[2,13],[2,8],[13,1],[6,11],[7,15],[7,10],[13,12],[16,9],[10,2],[14,13],[13,3],[7,12],[14,16],[12,14],[11,8],[9,13],[15,16],[8,14],[3,4],[11,9],[1,16],[9,15],[13,15],[5,7],[12,5],[16,2],[5,14],[12,1]]
    print(Solution().isPossible(n = n, edges = edges))
    n = 17
    edges = [[11,12],[11,8],[4,2],[15,6],[6,11],[2,11],[12,16]]
    print(Solution().isPossible(n = n, edges = edges))

                
                               





        


        
