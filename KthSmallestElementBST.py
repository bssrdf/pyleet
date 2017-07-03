# -*- coding: utf-8 -*-
"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Follow up:
What if the BST is modified (insert/delete operations) often and you need to find the kth smallest frequently? How would you optimize the kthSmallest routine?

Hint:
"""
__author__ = 'Daniel'


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.leftNodes = 0
        self.left = None
        self.right = None


class Solution:
    
    def kthSmallest(self, root, k):
        stack = []
        node = root
        while node:
            stack.append(node)
            node = node.left
        x = 1
        while stack and x <= k:
            node = stack.pop()
            x += 1
            right = node.right
            while right:
                stack.append(right)
                right = right.left
        return node.val    
    
    def kthSmallestRecursive(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        l = self.cnt(root.left)
        print 'l = ', l
        if l+1 == k:
            return root.val
        elif l+1 < k:
            return self.kthSmallest(root.right, k-(l+1))
        else:
            return self.kthSmallest(root.left, k)
        
    def cnt(self, root):
        if not root:
            return 0
        return 1+self.cnt(root.left)+self.cnt(root.right)
        
    def leftCnt(self, root):
        if root:
            root.leftNodes = self.cnt(root.left)            
            return root.leftNodes + 1 + self.leftCnt(root.right)
        else:
            return 0
        
    def kthSmallestRecurClean(self, root, k):
        self.k = k
        self.res = None
        self.helper(root)
        return self.res
    
    def helper(self, node):
        if not node:
            return
        self.helper(node.left) #inorder, first left subtree
        self.k -= 1  # inorde, current node
        if self.k == 0: # at any given node, if k == 0, we have found the kth smallest, return
            self.res = node.val
            return
        self.helper(node.right) #inorder, lastly right subtree
    
        
if __name__ == "__main__":
    root=TreeNode(70)
    root.left = TreeNode(31)
    root.left.right = TreeNode(40)
    root.left.right.right = TreeNode(45)    
    root.right = TreeNode(93)
    root.right.left = TreeNode(73)
    root.right.right = TreeNode(95)
    root.left.left = TreeNode(14)
    root.left.left.right = TreeNode(23)    
    #print Solution().kthSmallest(root, 4)
    print Solution().kthSmallestRecursive(root, 8)
    print Solution().cnt(root)
    Solution().leftCnt(root)
    print root.leftNodes