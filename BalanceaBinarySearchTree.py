'''
-Medium-


Given the root of a binary search tree, return a balanced binary search tree 
with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every 
node never differs by more than 1.

 

Example 1:


Input: root = [1,null,2,null,3,null,4,null,null]
Output: [2,1,3,null,null,null,4]
Explanation: This is not the only correct answer, [3,1,4,null,2] is also correct.
Example 2:


Input: root = [2,1,3]
Output: [2,1,3]
 

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
1 <= Node.val <= 10^5


'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from BinaryTree import (TreeNode, null)

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        v = []
        def dfs(node):
            if node:
                dfs(node.left)
                v.append(node.val)
                dfs(node.right)
        dfs(root)

        def bst(v):
            if not v:
                return None
            mid = len(v) // 2
            root = TreeNode(v[mid])
            root.left = bst(v[:mid])
            root.right = bst(v[mid + 1:])
            return root

        return bst(v)