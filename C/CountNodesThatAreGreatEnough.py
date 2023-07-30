'''
-Medium-


You are given a root to a binary tree and an integer k. A node of this tree is called great enough if the followings hold:

Its subtree has at least k nodes.
Its value is greater than the value of at least k nodes in its subtree.
Return the number of nodes in this tree that are great enough.

The node u is in the subtree of the node v, if u == v or v is an ancestor of u.

 

Example 1:

Input: root = [7,6,5,4,3,2,1], k = 2
Output: 3
Explanation: Number the nodes from 1 to 7.
The values in the subtree of node 1: {1,2,3,4,5,6,7}. Since node.val == 7, there are 6 nodes having a smaller value than its value. So it's great enough.
The values in the subtree of node 2: {3,4,6}. Since node.val == 6, there are 2 nodes having a smaller value than its value. So it's great enough.
The values in the subtree of node 3: {1,2,5}. Since node.val == 5, there are 2 nodes having a smaller value than its value. So it's great enough.
It can be shown that other nodes are not great enough.
See the picture below for a better understanding.


Example 2:

Input: root = [1,2,3], k = 1
Output: 0
Explanation: Number the nodes from 1 to 3.
The values in the subtree of node 1: {1,2,3}. Since node.val == 1, there are no nodes having a smaller value than its value. So it's not great enough.
The values in the subtree of node 2: {2}. Since node.val == 2, there are no nodes having a smaller value than its value. So it's not great enough.
The values in the subtree of node 3: {3}. Since node.val == 3, there are no nodes having a smaller value than its value. So it's not great enough.
See the picture below for a better understanding.


Example 3:

Input: root = [3,2,2], k = 2
Output: 1
Explanation: Number the nodes from 1 to 3.
The values in the subtree of node 1: {2,2,3}. Since node.val == 3, there are 2 nodes having a smaller value than its value. So it's great enough.
The values in the subtree of node 2: {2}. Since node.val == 2, there are no nodes having a smaller value than its value. So it's not great enough.
The values in the subtree of node 3: {2}. Since node.val == 2, there are no nodes having a smaller value than its value. So it's not great enough.
See the picture below for a better understanding.


 

Constraints:

The number of nodes in the tree is in the range [1, 104]. 
1 <= Node.val <= 104
1 <= k <= 10



'''
import sys
sys.path.append("O:\\Algorithms\\pyleet")
from BinaryTree import (null, constructBinaryTree, TreeNode)
from typing import Optional
import heapq
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countGreatEnoughNodes(self, root: Optional[TreeNode], k: int) -> int:
        ans = 0
        def dfs(node):
            nonlocal ans
            if not node: return 0, []
            lc, lhp = dfs(node.left)
            rc, rhp = dfs(node.right)
            hp = []
            for i in lhp + rhp:
                heapq.heappush(hp, i)
                if len(hp) > k:
                    heapq.heappop(hp)
            if hp:
                if lc+rc >= k-1 and len(hp) >= k and node.val > -hp[0]:                    
                    ans += 1 
            heapq.heappush(hp, -node.val)     
            return lc+rc+1, hp 
        dfs(root)
        return ans



if __name__ == "__main__":
    root = constructBinaryTree([7,6,5,4,3,2,1])
    root.prettyPrint()
    print(Solution().countGreatEnoughNodes(root = root, k = 2))
    root = constructBinaryTree([1,2,3])
    root.prettyPrint()
    print(Solution().countGreatEnoughNodes(root = root, k = 1))
    root = constructBinaryTree([3,2,2])
    root.prettyPrint()
    print(Solution().countGreatEnoughNodes(root = root, k = 2))