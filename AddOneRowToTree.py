# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 00:24:20 2017

@author: merli
"""
from collections import deque

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))
        else:
            return 0
            
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """
        if d==1:
            nr = TreeNode(v)
            nr.left = root
            return nr
        else:
            q=deque()
            q.append((root,1))
            while q:
                (node, depth) = q.popleft()
                if node.left:
                    q.append((node.left, depth+1))
                if node.right:
                    q.append((node.right, depth+1))
                if depth+1 == d:
                    nl = TreeNode(v)
                    nr = TreeNode(v)
                    nl.left = node.left
                    nr.right = node.right
                    node.left = nl
                    node.right = nr                    
            return root
        #print root.left.left.val      
                
if __name__ == "__main__":
    root=TreeNode(4)
    root.left = TreeNode(2)
    root.left.right = TreeNode(1)    
    root.right = TreeNode(6)
    root.right.left = TreeNode(5)
    root.left.left = TreeNode(3)
    print Solution().maxDepth(root)
    newtree = Solution().addOneRow(root, 1, 3)
    print Solution().maxDepth(newtree)