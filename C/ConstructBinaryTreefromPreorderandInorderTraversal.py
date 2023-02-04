# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 14:10:04 2019
105. Construct Binary Tree from Preorder and Inorder Traversal
iven preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

@author: merli
"""

# Definition for a binary tree node.
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

def pre_order(node):
    if not isinstance(node, TreeNode) or not node:
        return
    print(node.val, end=" ")
    pre_order(node.left)
    pre_order(node.right)


def in_order(node):
    if not isinstance(node, TreeNode) or not node:
        return
    in_order(node.left)
    print(node.val, end=" ")
    in_order(node.right)


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        if len(inorder) == 0:
            return None
        i = inorder.index(preorder[0])
        node = TreeNode(preorder[0])
        left = self.buildTree(preorder[1:i+1], inorder[:i])
        right = self.buildTree(preorder[i+1:], inorder[i+1:])
        node.left = left
        node.right= right
        return node        
        
        
if __name__ == '__main__':
    s = Solution()
    root = s.buildTree([3,9,20,15,7], [9,3,15,20,7])
    pre_order(root)
    print(" ")
    in_order(root)
    