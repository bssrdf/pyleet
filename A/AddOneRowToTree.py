# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 00:24:20 2017

@author: merli

-Medium-
*Recursion*
*DFS*


Given the root of a binary tree, then value v and depth d, you need to add a row 
of nodes with value v at the given depth d. The root node is at depth 1.

The adding rule is: given a positive integer depth d, for each NOT null tree nodes 
N in depth d-1, create two tree nodes with value v as N's left subtree root and 
right subtree root. And N's original left subtree should be the left subtree of 
the new left subtree root, its original right subtree should be the right subtree 
of the new right subtree root. If depth d is 1 that means there is no depth d-1 at 
all, then create a tree node with value v as the new root of the whole original tree, 
and the original tree is the new root's left subtree.

Example 1:
Input: 
A binary tree as following:
       4
     /   \
    2     6
   / \   / 
  3   1 5   

v = 1

d = 2

Output: 
       4
      / \
     1   1
    /     \
   2       6
  / \     / 
 3   1   5   

Example 2:
Input: 
A binary tree as following:
      4
     /   
    2    
   / \   
  3   1    

v = 1

d = 3

Output: 
      4
     /   
    2
   / \    
  1   1
 /     \  
3       1
Note:
The given d is in range [1, maximum depth of the given tree + 1].
The given binary tree has at least one tree node.

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
                        row1.append(kid)
            row = row1
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

    def addOneRowDFS(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        """     
        def helper(node, depth):
            if not node: return
            if depth == d-1:
                orig_left = node.left
                orig_right = node.right
                node.left = TreeNode(v)
                node.right = TreeNode(v)
                node.left.left = orig_left
                node.right.right = orig_right
                return
            helper(node.left, depth+1)
            helper(node.right, depth+1)
        if d == 1: 
            node = TreeNode(v)
            node.left = root
            return node
        helper(root, 1)
        return root    
                
if __name__ == "__main__":
    root=TreeNode(4)
    root.left = TreeNode(2)
    root.left.right = TreeNode(1)    
    root.right = TreeNode(6)
    root.right.left = TreeNode(5)
    root.left.left = TreeNode(3)
    print(Solution().maxDepth(root))
    #newtree = Solution().addOneRow(root, 1, 3)
    #newtree = Solution().addOneRowSP(root, 1, 3)
    newtree = Solution().addOneRowDFS(root, 1, 3)
    print(Solution().maxDepth(newtree))