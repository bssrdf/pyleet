'''

-Medium-

You are given the root of a binary tree with unique values.

In one operation, you can choose any two nodes at the same level and swap their values.

Return the minimum number of operations needed to make the values at each level sorted in a strictly increasing order.

The level of a node is the number of edges along the path between it and the root node.

 

Example 1:


Input: root = [1,4,3,7,6,8,5,null,null,null,null,9,null,10]
Output: 3
Explanation:
- Swap 4 and 3. The 2nd level becomes [3,4].
- Swap 7 and 5. The 3rd level becomes [5,6,8,7].
- Swap 8 and 7. The 3rd level becomes [5,6,7,8].
We used 3 operations so return 3.
It can be proven that 3 is the minimum number of operations needed.
Example 2:


Input: root = [1,3,2,7,6,5,4]
Output: 3
Explanation:
- Swap 3 and 2. The 2nd level becomes [2,3].
- Swap 7 and 4. The 3rd level becomes [4,6,5,7].
- Swap 6 and 5. The 3rd level becomes [4,5,6,7].
We used 3 operations so return 3.
It can be proven that 3 is the minimum number of operations needed.
Example 3:


Input: root = [1,2,3,4,5,6]
Output: 0
Explanation: Each level is already sorted in increasing order so return 0.
 

Constraints:

The number of nodes in the tree is in the range [1, 105].
1 <= Node.val <= 105
All the values of the tree are unique.


'''
from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        que = deque([root])
        ans = 0
        while que:
            nq = deque()
            nn = [] 
            for i in range(len(que)):
                node = que.popleft()                
                nn.append((node.val, i))
                if node.left:
                    nq.append(node.left)
                if node.right:
                    nq.append(node.right)
            k = 0
            ns = {v : j for j,v in enumerate(nn)}
            for i,v in enumerate(sorted(nn)):
                j = ns[v] # j is the current index of the number which should be at i
                w = nn[i]
                if nn[i] != nn[j]:
                    k += 1
                    nn[i], nn[j] = nn[j], nn[i] # swap numbers at index i and j
                    ns[v], ns[w] = i, j # swap indices 
                
            # print(arr, nums, k)
            ans += k
            que = nq
        return ans  
         
    def minimumOperations2(self, root: Optional[TreeNode]) -> int:
        
        nodes, count = deque([root]), 0
        
        def perm(arr):                                            # this function simulates cycle sort,
            pos = {m:j for j,m in enumerate(sorted(arr))}         # namely, traverses every cycle in
            vis, tot = [0] * len(arr), 0                          # the permutation of elements and 
            for i in range(len(arr)):                             # counts the number of swaps 
                cnt = 0
                while not vis[i] and i != pos[arr[i]]:            # it is known that cycle sort is the
                    vis[i], i = 1, pos[arr[i]]                    # sorting algorithm with the minmal
                    cnt += 1                                      # number of memory operations (swaps)
                tot += max(0, cnt-1)                              # needed to sort an array
            return tot
                    
        while nodes:
            vals = []
            for _ in range(len(nodes)):                            # [1] this code performs a level-by-level
                n = nodes.popleft()                                #     BFS scan of the tree and extracts
                vals.append(n.val)                                 #     a list of values 'vals' for each level
                if n.left  : nodes.append(n.left)
                if n.right : nodes.append(n.right)
            count += perm(vals)                                    # [2] each level is sorted independently
            
        return count
    
    def minimumOperations3(self, root: TreeNode) -> int:                     #           _____1____
                                                                            #          /          \
        ans, queue, level = 0, [root],[]                                    #         4___         3___
                                                                            #        /    \       /    \
        while queue :                                                       #       7     _6     8     _5
                                                                            #            /      /     /
            for node in queue:                                              #           11     9     10
                    if node:  level.extend([node.left, node.right])         #
                                                                            #  level         idx             ans
            arr = [(v,i) for i,v in enumerate([c.val for c in level if c])] #  –––––        –––––           –––––
            idx = [i for _,i in sorted(arr)]                                #  [4,3]        [1,0]             1
                                                                            #  [7,6,8,5]    [2,1,3,0]         2
            for i in range(len(idx)):                                       #  [11,9,10]    [1,2,0]           2
                while idx[i] != i:                                          #                               –––––
                    j = idx[i]                                              #                                 5   <--- ans
                    idx[i], idx[j] = idx[j], idx[i]
                    ans += 1

            queue, level = level, []
        
        return ans
            