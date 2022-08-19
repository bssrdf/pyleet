'''

-Medium-
$$$
*DP*
*DFS*

You are given a weighted tree consisting of n nodes numbered from 0 to n - 1.

The tree is rooted at node 0 and represented with a 2D array edges of size n 
where edges[i] = [pari, weighti] indicates that node pari is the parent of node i, and the edge between them has a weight equal to weighti. Since the root does not have a parent, you have edges[0] = [-1, -1].

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
    def maximumScore(self, edges: List[List[int]]) -> int:
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
    
    def maximumScore2(self, edges: List[List[int]]) -> int:
        n = len(edges)
        tree = defaultdict(list)
        for i,(u, w) in enumerate(edges):
            if u != -1:
                tree[u].append([i, w])
        @lru_cache(None)
        def dfs(u, chosen):
            b, ans = 0, 0            
            for v, w in tree[u]:
                b += max(0, dfs(v, False))
            if not chosen:
                for v, w in tree[u]:
                    t = w + dfs(v, True)                    
                    ans = max(ans, b + t - max(0, dfs(v, False)))            
            return max(b, ans) 
        # return max(dfs(0, False),  dfs(0, True))
        return dfs(0, False)

    def maximumScore3(self, edges: List[List[int]]) -> int:
        n = len(edges)
        tree = defaultdict(lambda : defaultdict(int))
        for i,(u, w) in enumerate(edges):
            if u != -1:
                tree[u][i] = w
        @lru_cache(None)
        def dfs(u):
            # return (s1, s2)
            # s1: max sum if we can use u->v edge
            # s2: max sum if we do not use any u->v edge
            if not tree[u]: return [0, 0]
            s1, s2 = 0, 0
            nbs = tree[u]
            for v in nbs:
                s2 += max(dfs(v))
            for v in nbs:
                tmp = s2 - max(dfs(v)) + max(nbs[v], 0) + dfs(v)[1]
                s1 = max(s1, tmp)
            return (s1, s2) 
        return max(dfs(0))


from random import random, randint

leaf_count = 0

def rand_tree(prefixes, d, MAX_D, MAX_N, index, prefix):
    global leaf_count
    
    # return a tree with maximum depth MAX_D that branches with probability p at most N times for each internal node
    # p starts from 1 and decreases linearly with d, reaching zero at MAX_D
    
    # this still seems to be necessary to avoid infinite recursion (floating point precision?)
    if d == MAX_D:
        prefixes.append(prefix[1:])
        leaf_count += 1
        print(leaf_count, end='\r')
        
    p = float(MAX_D-d)/MAX_D
    
    # if the tree branches, at least one branch is made
    n = randint(1, MAX_N)
    
    child_i = 0
    
    for i in range(n):
        if p >= random():
            child_i += 1
            rand_tree(prefixes, d+1, MAX_D, MAX_N, child_i, prefix+(index,))
        else:
            prefixes.append(prefix[1:])
            leaf_count += 1
            print(leaf_count, end='\r')
            
def generate(max_d, max_n):
    global leaf_count
    
    leaf_count = 0
    
    prefixes = []

    rand_tree(prefixes, 1, max_d, max_n, 0, ())
    prefixes.sort()
    
    # write prefix tuples to the output file
    # i = 0
    # for prefix in prefixes:
    #     print(i, prefix)
    #     i += 1
    return prefixes

if __name__ == "__main__":
    # print(Solution().maximumScore(edges = [[-1,-1],[0,5],[0,10],[2,6],[2,4]]))
    # print(Solution().maximumScore(edges = [[-1,-1],[0,5],[0,-6],[0,7]]))
    # print(Solution().maximumScore2(edges = [[-1,-1],[0,5],[0,10],[2,6],[2,4]]))
    # print(Solution().maximumScore2(edges = [[-1,-1],[0,5],[0,-6],[0,7]]))
    # print(Solution().maximumScore2(edges = [[-1,-1],[0,5],[0,10],[2,6],[2,4],[1,-2]]))
    # print(Solution().maximumScore3(edges = [[-1,-1],[0,5],[0,10],[2,6],[2,4]]))
    # print(Solution().maximumScore3(edges = [[-1,-1],[0,5],[0,-6],[0,7]]))
    # print(Solution().maximumScore3(edges = [[-1,-1],[0,5],[0,10],[2,6],[2,4],[1,-2]]))
    # edges = [[-1, -1], [-1, -38], [1, -5], [1, -8], [1, 81], [1, -40], [1, 23], [6, -19], [6, -42], [6, 9], [6, -44], [10, -32], [10, -49], [10, 85], [10, -15], [14, 99], [14, 79], [14, 97], [14, -5], [18, -29], [18, 10], [18, -23], [18, -42], [18, 75], [18, 57], [18, -7], [25, 20], [25, 24], [25, 32], [28, -12], [28, 16], [28, 40], [25, 41], [25, -31], [25, -24], [25, 22], [10, 40], [10, -27], [10, 54], [10, 56], [39, 95], [39, -3], [-1, -28], [-1, -39], [-1, -39], [-1, 29], [45, 65], [45, -20], [45, 86], [48, 41], [48, 45], [48, 28], [51, -31], [51, -32], [51, -45], [51, 98], [51, 35], [51, -2], [51, -41], [58, -32], [58, 75], [58, 57], [61, 42], [58, 25], [58, 31], [58, -5], [58, 16], [51, 4], [67, 2], [67, 61], [67, 36], [67, 33], [67, -22], [67, -18], [73, 16], [73, 89], [75, -37], [75, 73], [75, 60], [75, 91], [75, 96], [75, 70], [75, -50], [75, 88], [75, 12], [75, -12], [85, 99], [85, 41], [85, 25], [85, 3], [85, -27], [85, 0], [75, -24], [73, -48], [73, 99], [73, -40], [73, 37], [73, 46], [73, 92], [98, -46], [98, 46], [98, 5], [98, -29], [102, 32], [102, -33], [102, 97], [102, -40], [102, 94], [102, 13], [45, -32], [45, 18], [45, 90], [45, 64], [45, -42], [113, 46], [114, 94], [114, -11], [114, 64], [114, 11], [114, -14], [114, -12], [114, 12], [114, 2], [122, -10], [122, -19], [124, 86], [124, -50], [124, -11], [124, 48], [124, -4], [124, 12], [130, 45], [130, 75], [130, 43], [130, -39], [130, 51], [130, 82], [130, 90], [130, -40], [138, 96], [138, -39], [138, 64], [138, -32], [138, -32], [138, -22], [138, 81], [138, 65], [138, 61], [130, 15], [130, -25], [130, 40], [130, 99], [151, 37], [151, 7], [122, -14], [122, 88], [122, 58], [122, 21], [122, 3], [-1, 92], [159, 64], [159, 43], [159, 25], [159, 65], [159, -9], [159, 17], [159, 76], [159, -35], [167, 40], [167, 58], [169, 32], [169, 28], [169, 46], [172, 78], [172, 92], [172, 89], [-1, 43], [-1, -44], [-1, -43], [-1, 37], [-1, 31], [-1, -44], [-1, -4], [167, -15], [167, -10], [167, -1], [-1, -7], [-1, 26], [187, 10]]
    # print(Solution().maximumScore3(edges = edges))
    # '''
    for _ in range(100):
        pref = generate(10, 5)
        i = 0
        m = {}
        edges = []
        for pr in pref:
            w = randint(-100, 100)
            v, w0 = m[pr[:-1]] if pr[:-1] in m else -1, w if i > 0 else -1
            if v == -1 and i > 0:
                # print('erorr', i, v, pr) 
                continue
            edges.append([v, w0])        
            m[pr] = i
            i += 1
        # i = 0
        # for pr in pref:
        #     print(i, pr)
        #     i += 1
        # print(edges)
        s1 = Solution().maximumScore2(edges = edges)
        s2 = Solution().maximumScore3(edges = edges)
        print(s1, s2)
        if s2 == 0:
            print(edges)
    # '''




