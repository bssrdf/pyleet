'''
-Easy-

Given the root of a binary tree and an integer targetSum, return true if the 
tree has a root-to-leaf path such that adding up all the values along the path 
equals targetSum.

A leaf is a node with no children.

 

Example 1:


Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Example 2:


Input: root = [1,2,3], targetSum = 5
Output: false
Example 3:

Input: root = [1,2], targetSum = 0
Output: false
 

Constraints:

The number of nodes in the tree is in the range [0, 5000].
-1000 <= Node.val <= 1000
-1000 <= targetSum <= 1000

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from BinaryTree import (TreeNode, null, constructBinaryTree)

class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        :type root: TreeNode
        :type targetSum: int
        :rtype: bool
        """
        if not root: return False
        if not root.left and not root.right:
            if targetSum == root.val: return True
            else: return False
        if root.left and self.hasPathSum(root.left, targetSum-root.val):
            return True
        if root.right and self.hasPathSum(root.right, targetSum-root.val):
            return True
        return False


if __name__ == "__main__":
    root = constructBinaryTree([5,4,8,11,null,13,4,7,2,null,null,null,1])
    print(Solution().hasPathSum(root, 22))
    root = constructBinaryTree([1, 2, 3])
    print(Solution().hasPathSum(root, 5))
    root = constructBinaryTree([1, 2, null])
    print(Solution().hasPathSum(root, 1))
