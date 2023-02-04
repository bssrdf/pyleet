'''


-Hard-

*DFS*
*Cached DFS*

There exists an undirected and initially unrooted tree with n nodes indexed from 0 to n - 1. You are given the integer n and a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

Each node has an associated price. You are given an integer array price, where price[i] is the price of the ith node.

The price sum of a given path is the sum of the prices of all nodes lying on that path.

The tree can be rooted at any node root of your choice. The incurred cost after choosing root is the difference between the maximum and minimum price sum amongst all paths starting at root.

Return the maximum possible cost amongst all possible root choices.

 

Example 1:


Input: n = 6, edges = [[0,1],[1,2],[1,3],[3,4],[3,5]], price = [9,8,7,6,10,5]
Output: 24
Explanation: The diagram above denotes the tree after rooting it at node 2. The first part (colored in red) shows the path with the maximum price sum. The second part (colored in blue) shows the path with the minimum price sum.
- The first path contains nodes [2,1,3,4]: the prices are [7,8,6,10], and the sum of the prices is 31.
- The second path contains the node [2] with the price [7].
The difference between the maximum and minimum price sum is 24. It can be proved that 24 is the maximum cost.
Example 2:


Input: n = 3, edges = [[0,1],[1,2]], price = [1,1,1]
Output: 2
Explanation: The diagram above denotes the tree after rooting it at node 0. The first part (colored in red) shows the path with the maximum price sum. The second part (colored in blue) shows the path with the minimum price sum.
- The first path contains nodes [0,1,2]: the prices are [1,1,1], and the sum of the prices is 3.
- The second path contains node [0] with a price [1].
The difference between the maximum and minimum price sum is 2. It can be proved that 2 is the maximum cost.
 

Constraints:

1 <= n <= 105
edges.length == n - 1
0 <= ai, bi <= n - 1
edges represents a valid tree.
price.length == n
1 <= price[i] <= 105

'''

from typing import List
from functools import lru_cache
from collections import defaultdict
class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        '''
        For tree-based dp problems that give you edges as inputs, below is the template

        1. store edges into an adjancent list

        2. define a dfs function with two key parameters (cur, prev) to control the direction 
          we will move along an edge between cur and prev

        3. within dfs(cur,prev), the recursion is to call t(nxt,cur) for nxt in adj[cur]-{prev}

        4. we add memorization (@cache) so that each edge between cur and prev will only be 
        visited twice: one from cur to prev, one from prev to cur

        5. we call dfs(i,-1) for i in range(n). -1 denotes no prev for i, so i is the root.

        NOTE: this is more of cheat as the time complexity is still O(N^2). It will TLE on
          some edge cases (see the last test case below!!!)
        
        '''
        G = defaultdict(set)
        ans = 0
        for u, v in edges:
            G[u].add(v)
            G[v].add(u)
        @lru_cache(None)
        def dfs(node, parent):
            cur = price[node]
            m = 0
            for v in G[node]:
                if v != parent:
                    m = max(m, dfs(v, node))
            return cur + m
        for u in range(n):
            maxP = dfs(u, -1)
            minP = price[u]
            ans = max(ans, maxP - minP)        
        return ans   
    

    def maxOutput2(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        '''
        This question is similar to 124. Binary Tree Maximum Path Sum but a little different.

        The difference between this question and 124. :

        Only positive value
        Not a binary tree
        The answer is not the maximum path but the path that minus the smaller end point.
        Consider question 124 with only positive node :

        The DFS returns the maximum path from current root to one of leaf node.
        At each subtree, we update the final answer with left subtree return value (which is the max path sum) + current root node value + right sutree return value.
        We need to consider all subtree instead of left and right.

        Since we don't know which side of end point is the minimum we should remove and if the path is still maximum after we remove the end point, we maintain another value which is the path sum from root to leaf but minus its leaf node and try both two cases.

        In the for loop we iterate all neighbor(subtree) and update the answer with two cases:

        Current max path sum from previous subtree + path sum without leaf node from nei subtree
        Current max path sum without leaf node from previous subtree + path sum from nei subtree
        Design DFS returns two value:

        maximum path sum
        maximum (path sum - leaf node)
        '''
        G = defaultdict(set)
        ans = 0
        for u, v in edges:
            G[u].add(v)
            G[v].add(u)
        def dfs(cur, par):
            nonlocal ans
            cur_max = [price[cur], 0]
            for v in G[cur]:
                if v != par:
                    ret = dfs(v, cur)
                    ans = max(ans, cur_max[0] + ret[1]) 
                    ans = max(ans, cur_max[1] + ret[0]) 
                    cur_max[0] = max(cur_max[0], ret[0] + price[cur])
                    cur_max[1] = max(cur_max[1], ret[1] + price[cur])
            return cur_max 
        dfs(0, -1)
        return ans
    
    def maxOutput3(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        # This is a standard tree problem where it is required find the farthest 
        # node from every node. At first glance, the problem seems difficult but 
        # with a few observations, it can be made simple. You can practice similar 
        # problems on CSES (check out [this](https://cses.fi/problemset/task/1131), 
        # [this](https://cses.fi/problemset/task/1132/) and 
        # [this](https://cses.fi/problemset/task/1133)). There are many that are 
        # similar in nature on Leetcode too.
        G = defaultdict(set)
        ans = 0
        for u, v in edges:
            G[u].add(v)
            G[v].add(u)
        def findMax(arr):
            x, ret = 0, -1
            for i in range(len(arr)):
                if arr[i] > x:
                    ret = i
                    x = arr[i]
            return ret                   
        # For each node, we must find the distance to the farthest node.
        # we use this dfs function to do it
        # NOTE: here the depth is not the regular depth, but the price weighted one
        def dfs(u, depth):
            for v in G[u]:
                if depth[v] == -1:
                    depth[v] = depth[u] + price[v]
                    dfs(v, depth)

        # Start by finding the diameter of the tree. The diameter of a tree is the longest 
        # path between two leaf nodes. 
        depth_x = [-1]*n
        # This can be done by starting a DFS/BFS at any node        
        # Here we start from node 0
        depth_x[0] = price[0]        
        dfs(0, depth_x)

        # Select the farthest node as a diameter endpoint. Let this node be U.
        u = findMax(depth_x)
        
        depth_y = [-1]*n
        # Perform a DFS/BFS starting at node U and find the farthest node. 
        depth_y[u] = price[u]
        dfs(u, depth_y)
        # This is the other diameter endpoint. Let this node be V.
        v = findMax(depth_y)

        depth_x = [-1]*n
        depth_x[v] = price[v]
        dfs(v, depth_x)

        for i in range(n):
            # The farthest node from each node is the maximum distance from either 
            # of the diametric endpoints U or V
            # ans = max(ans, max(depth_x[i] - price[v], depth_x[i] - price[i]))
            # ans = max(ans, max(depth_y[i] - price[u], depth_y[i] - price[i]))
            ans = max(ans, depth_x[i] - price[i])
            ans = max(ans, depth_y[i] - price[i])
        return ans  






if __name__=="__main__":        
    print(Solution().maxOutput(n = 6, edges = [[0,1],[1,2],[1,3],[3,4],[3,5]], price = [9,8,7,6,10,5]))
    print(Solution().maxOutput2(n = 6, edges = [[0,1],[1,2],[1,3],[3,4],[3,5]], price = [9,8,7,6,10,5]))
    n = 50_000
    edges = []
    price = [10]*n
    for i in range(1, n):
        edges.append((0, i))
    print(Solution().maxOutput2(n = n, edges = edges, price = price))
    print(Solution().maxOutput3(n = n, edges = edges, price = price))
    #print(Solution().maxOutput(n = n, edges = edges, price = price)) #TLE


