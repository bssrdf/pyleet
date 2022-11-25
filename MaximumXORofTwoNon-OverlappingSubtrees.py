'''

-Hard-
*DFS*
*Trie (Integer)*

There is an undirected tree with n nodes labeled from 0 to n - 1. You are given the integer n and a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Each node has an associated value. You are given an array values of length n, where values[i] is the value of the ith node.

Select any two non-overlapping subtrees. Your score is the bitwise XOR of the sum of the values within those subtrees.

Return the maximum possible score you can achieve. If it is impossible to find two nonoverlapping subtrees, return 0.

Note that:

The subtree of a node is the tree consisting of that node and all of its descendants.
Two subtrees are non-overlapping if they do not share any common node.
 

Example 1:



Input: n = 6, edges = [[0,1],[0,2],[1,3],[1,4],[2,5]], values = [2,8,3,6,2,5]
Output: 24
Explanation: Node 1's subtree has sum of values 16, while node 2's subtree has sum of values 8, so choosing these nodes will yield a score of 16 XOR 8 = 24. It can be proved that is the maximum possible score we can obtain.
Example 2:



Input: n = 3, edges = [[0,1],[1,2]], values = [4,6,1]
Output: 0
Explanation: There is no possible way to select two non-overlapping subtrees, so we just return 0.
 

Constraints:

2 <= n <= 5 * 104
edges.length == n - 1
0 <= ai, bi < n
values.length == n
1 <= values[i] <= 109
It is guaranteed that edges represents a valid tree.



'''

from typing import List
from collections import defaultdict

class Trie:
    def __init__(self):
        self.children = [None] * 2

    def insert(self, x):
        node = self
        for i in range(47, -1, -1):
            v = (x >> i) & 1
            if node.children[v] is None:
                node.children[v] = Trie()
            node = node.children[v]

    def search(self, x):
        node = self
        res = 0
        for i in range(47, -1, -1):
            v = (x >> i) & 1
            if node is None:
                return res
            if node.children[v ^ 1]:
                res = res << 1 | 1
                node = node.children[v ^ 1]
            else:
                res <<= 1
                node = node.children[v]
        return res

class TrieNode:
    def __init__(self):
        self.child = {}
        self.go = 0  # Number of elements goes through this node

    def increase(self, number, d):
        cur = self
        for i in range(47, -1, -1):
            bit = (number >> i) & 1
            if bit not in cur.child: 
                cur.child[bit] = TrieNode()
            cur = cur.child[bit]
            cur.go += d

    def findMax(self, number):
        cur, ans = self, 0
        for i in range(47, -1, -1):
            bit = (number >> i) & 1
            if (1-bit) in cur.child and cur.child[1-bit].go > 0:
                cur = cur.child[1 - bit]
                ans |= (1 << i)
            elif bit in cur.child:
                cur = cur.child[bit]
            else:
                return ans
        return ans


class Solution:
    def maxXor(self, n: int, edges: List[List[int]], values: List[int]) -> int:        
        '''
        Similar to Maximum Genetic Difference Query
        https://leetcode.com/problems/maximum-genetic-difference-query/
        
        '''
        def dfs1(i, fa):
            t = values[i]
            for j in g[i]:
                if j != fa:
                    t += dfs1(j, i)
            s[i] = t
            return t

        def dfs2(i, fa):
            nonlocal ans
            ans = max(ans, tree.search(s[i]))
            for j in g[i]:
                if j != fa:
                    dfs2(j, i)
            tree.insert(s[i])

        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        s = [0] * n
        dfs1(0, -1)
        ans = 0
        tree = Trie()
        dfs2(0, -1)
        return ans

    def maxXor2(self, n: int, edges: List[List[int]], values: List[int]) -> int:        
        '''
        Similar to Maximum Genetic Difference Query
        https://leetcode.com/problems/maximum-genetic-difference-query/
        
        '''
        def dfs1(i, fa):
            t = values[i]
            for j in g[i]:
                if j != fa:
                    t += dfs1(j, i)
            s[i] = t
            return t

        def dfs2(i, fa):
            nonlocal ans
            ans = max(ans, tree.findMax(s[i]))
            for j in g[i]:
                if j != fa:
                    dfs2(j, i)
            tree.increase(s[i], 1)

        g = defaultdict(list)
        for a, b in edges:
            g[a].append(b)
            g[b].append(a)
        s = [0] * n
        dfs1(0, -1)
        ans = 0
        tree = TrieNode()
        dfs2(0, -1)
        return ans



if __name__=="__main__":
    print(Solution().maxXor(n = 6, edges = [[0,1],[0,2],[1,3],[1,4],[2,5]], values = [2,8,3,6,2,5]))
    print(Solution().maxXor2(n = 6, edges = [[0,1],[0,2],[1,3],[1,4],[2,5]], values = [2,8,3,6,2,5]))