'''

Given the root of a Binary Search Tree (BST), convert it to a Greater Tree 
such that every key of the original BST is changed to the original key plus 
sum of all keys greater than the original key in BST.

As a reminder, a binary search tree is a tree that satisfies these 
constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.

Note: This question is the same as 1038: https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/

'''

from BinaryTree import (TreeNode, constructBinaryTree, inOrder, null) 
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.sm = 0
        def inOrder(root):
            if not root: return 
            inOrder(root.right)
            self.sm += root.val
            root.val = self.sm
            inOrder(root.left)
        inOrder(root)
        return root


if __name__ == '__main__':   
    root = constructBinaryTree([6,2,7,1,4,null,9,null, null, 3,5, 
    null, null, 8, null])    
    inOrder(root)
    print()
    root=Solution().convertBST(root)
    inOrder(root)
    print()
