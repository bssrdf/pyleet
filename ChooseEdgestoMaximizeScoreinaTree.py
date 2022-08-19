'''

-Medium-
$$$

You are given a weighted tree consisting of n nodes numbered from 0 to n - 1.

The tree is rooted at node 0 and represented with a 2D array edges of size n where edges[i] = [pari, weighti] indicates that node pari is the parent of node i, and the edge between them has a weight equal to weighti. Since the root does not have a parent, you have edges[0] = [-1, -1].

Choose some edges from the tree such that no two chosen edges are adjacent and the sum of the weights of the chosen edges is maximized.

Return the maximum sum of the chosen edges.

Note:

You are allowed to not choose any edges in the tree, the sum of weights in this case will be 0.
Two edges Edge1 and Edge2 in the tree are adjacent if they have a common node.
In other words, they are adjacent if Edge1 connects nodes a and b and Edge2 connects nodes b and c.
 

Example 1:



Input: edges = [[-1,-1],[0,5],[0,10],[2,6],[2,4]]
Output: 11
Explanation: The above diagram shows the edges that we have to choose colored in red.
The total score is 5 + 6 = 11.
It can be shown that no better score can be obtained.
Example 2:



Input: edges = [[-1,-1],[0,5],[0,-6],[0,7]]
Output: 7
Explanation: We choose the edge with weight 7.
Note that we cannot choose more than one edge because all edges are adjacent to each other.
 

Constraints:

n == edges.length
1 <= n <= 105
edges[i].length == 2
par0 == weight0 == -1
0 <= pari <= n - 1 for all i >= 1.
pari != i
-106 <= weighti <= 106 for all i >= 1.
edges represents a valid tree.


'''
from typing import List
from collections import defaultdict
from functools import lru_cache

class Solution:
    def maximumScore(self, edges: List[int]) -> int:
        n = len(edges)
        tree = defaultdict(list)
        for i,(u, w) in enumerate(edges):
            if u != -1:
                tree[u].append([i, w])
        def dfs(u, chosen):
            ans = 0            
            if not chosen:
                for v, w in tree[u]:
                    t = w + dfs(v, True)
                    s = 0
                    for v1, w1 in tree[u]:
                        if v1 != v:
                            s += max(0, dfs(v1, False)) 
                    ans = max(ans, t + s)
            ans1 = 0
            for v, w in tree[u]:
                ans1 += max(0, dfs(v, False))
            return max(ans1, ans) 
        return max(dfs(0, False),  dfs(0, True))
    
    def maximumScore2(self, edges: List[int]) -> int:
        n = len(edges)
        tree = defaultdict(list)
        for i,(u, w) in enumerate(edges):
            if u != -1:
                tree[u].append([i, w])
        @lru_cache(None)
        def dfs(u, chosen):
            ans = 0            
            b = 0
            bj = {}
            for v, w in tree[u]:
                bj[v] = max(0, dfs(v, False))
            b = max(b, sum(bj.values())) 
            if not chosen:
                for v, w in tree[u]:
                    t = w + dfs(v, True)                    
                    ans = max(ans, b + t - bj[v])            
            return max(b, ans) 
        # return max(dfs(0, False),  dfs(0, True))
        return dfs(0, False)




if __name__ == "__main__":
    print(Solution().maximumScore(edges = [[-1,-1],[0,5],[0,10],[2,6],[2,4]]))
    print(Solution().maximumScore(edges = [[-1,-1],[0,5],[0,-6],[0,7]]))
    print(Solution().maximumScore2(edges = [[-1,-1],[0,5],[0,10],[2,6],[2,4]]))
    print(Solution().maximumScore2(edges = [[-1,-1],[0,5],[0,-6],[0,7]]))
    print(Solution().maximumScore2(edges = [[-1,-1],[0,5],[0,10],[2,6],[2,4],[1,-2]]))