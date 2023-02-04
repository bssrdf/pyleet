'''
-Medium-

Given two integer arrays inorder and postorder where inorder is the inorder traversal of 
a binary tree and postorder is the postorder traversal of the same tree, construct and 
return the binary tree.

 

Example 1:


Input: inorder = [9,3,15,20,7], postorder = [9,15,7,20,3]
Output: [3,9,20,null,null,15,7]
Example 2:

Input: inorder = [-1], postorder = [-1]
Output: [-1]
 

Constraints:

1 <= inorder.length <= 3000
postorder.length == inorder.length
-3000 <= inorder[i], postorder[i] <= 3000
inorder and postorder consist of unique values.
Each value of postorder also appears in inorder.
inorder is guaranteed to be the inorder traversal of the tree.
postorder is guaranteed to be the postorder traversal of the tree.
'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from BinaryTree import (null, TreeNode)

class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        def helper(io, po):
            if not io and not po: return None
            root = TreeNode(po[-1])
            if len(po) == 1 or len(io) == 1:  return root
            indexL = io.index(po[-1])
            indexR = len(io) - (indexL+1)
            root.left = helper(io[:indexL], po[:-(indexR+1)])
            root.right = helper(io[indexL+1:], po[-(indexR+1):-1])
            return root
        return helper(inorder, postorder)


if __name__ == '__main__':
    s = Solution()
    root = s.buildTree(inorder = [9,3,15,20,7], postorder = [9,15,7,20,3])
    root.prettyPrint()
    root = s.buildTree(inorder = [-1], postorder = [-1])
    root.prettyPrint()
    root = s.buildTree(inorder = [2, 1], postorder = [2, 1])
    root.prettyPrint()
    root = s.buildTree(inorder = [1, 2, 3], postorder = [3, 2, 1])
    root.prettyPrint()
    root = s.buildTree(inorder = [1, 2, 3, 4], postorder = [1, 4, 3, 2])
    root.prettyPrint()
    root = s.buildTree(inorder = [1,2,3,4,5], postorder = [1,4,5,3,2])
    root.prettyPrint()
    
    
    
