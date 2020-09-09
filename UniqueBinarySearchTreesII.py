'''
Given an integer n, generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from BinaryTree import (TreeNode, preOrder)

class Solution(object):



    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 1:
            return [TreeNode(n)]
        ans = []
        subtrees = self.generateTrees(n-1)
        def copy(root):
            if not root:
                return None
            node = TreeNode(root.val)            
            if root.left:
                node.left = copy(root.left)
            if root.right:
                node.right = copy(root.right)            
            return node
        #print(n, len(subtrees))
        for st in subtrees:
            # current n as root with subtree as left child
            root = TreeNode(n)
            root.left = copy(st)
            ans.append(root)
        
            # current n as far right leaf child
            root = copy(st)
            node = root
            while node.right:
                node = node.right
            node.right = TreeNode(n)                
            ans.append(root)
             
           
            node = st.right
            path = [st.val]
            lev = 1
            while node:    
                root = copy(st)
                newnode = root
                cur = 1
                while cur < lev:
                   newnode = newnode.right
                   cur += 1
                newleft = newnode.right         
                newnode.right = TreeNode(n)
                newnode.right.left = newleft                
                ans.append(root)
                node = node.right
                lev += 1
            
        return ans

if __name__ == "__main__":
    bsts = Solution().generateTrees(4)
    print(len(bsts))
    #for t in bsts:
    #    preOrder(t)
    #    print('')
