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
    
    def addOneRowSP(self, root, v, d):
        dummy, dummy.left = TreeNode(None), root
        row = [dummy]
        #for _ in range(d - 1):
         #   row = [kid for node in row for kid in (node.left, node.right) if kid]
        for _ in range(d-1):
            row1 = []
            for node in row:
                for kid in (node.left, node.right):
                    if kid:
                        print kid.val                        
                        row1.append(kid)
            row = row1
        print row
        for node in row:
            node.left, node.left.left = TreeNode(v), node.left
            node.right, node.right.right = TreeNode(v), node.right
        return dummy.left    
    
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
            depth = 1
            q.append((root, depth))            
            while q and depth < d:
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
    #newtree = Solution().addOneRow(root, 1, 3)
    newtree = Solution().addOneRowSP(root, 1, 3)
    print Solution().maxDepth(newtree)