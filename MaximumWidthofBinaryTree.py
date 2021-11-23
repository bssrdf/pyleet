'''
-Medium-


Given the root of a binary tree, return the maximum width of the given tree.

The maximum width of a tree is the maximum width among all levels.

The width of one level is defined as the length between the end-nodes 
(the leftmost and rightmost non-null nodes), where the null nodes 
between the end-nodes are also counted into the length calculation.

It is guaranteed that the answer will in the range of 32-bit signed integer.

 

Example 1:


Input: root = [1,3,2,5,3,null,9]
Output: 4
Explanation: The maximum width existing in the third level with the length 4 (5,3,null,9).
Example 2:


Input: root = [1,3,null,5,3]
Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).
Example 3:


Input: root = [1,3,2,5]
Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).
Example 4:


Input: root = [1,3,2,5,null,null,9,6,null,null,7]
Output: 8
Explanation: The maximum width existing in the fourth level with the length 8 (6,null,null,null,null,null,null,7).
 

Constraints:

The number of nodes in the tree is in the range [1, 3000].
-100 <= Node.val <= 100


'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

from BinaryTree import null, TreeNode, constructBinaryTree 

from collections import deque

class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        que = deque([(root,0)])
        res = 1
        while que:
            nxt = deque()
            i, j = -1, -1
            for _ in range(len(que)):
                node, lvl = que.popleft()
                if node.left:
                    idx = 2*lvl
                    if i == -1: i = idx
                    else: j = idx
                    nxt.append((node.left,idx))
                if node.right:
                    idx = 2*lvl+1
                    if i == -1: i = idx
                    else: j = idx
                    nxt.append((node.right, idx))
            if i >= 0 and j >= 0:
                res = max(res, j-i+1)
            que = nxt    
        return res 



if __name__ == "__main__":
    root = constructBinaryTree([1,3,2,5,3,null,9])
    print(Solution().widthOfBinaryTree(root))
    root = constructBinaryTree([1,3,null,5,3])
    root.prettyPrint()
    print(Solution().widthOfBinaryTree(root))
    root = constructBinaryTree([1,3,2,5])
    root.prettyPrint()
    print(Solution().widthOfBinaryTree(root))
    root = constructBinaryTree([1,3,2,5,null,null,9,6,null,null,null,null,null,null,7])
    root.prettyPrint()
    print(Solution().widthOfBinaryTree(root))
