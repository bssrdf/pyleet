# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from BinaryTree import (TreeNode, constructBinaryTree, null) 

class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def dfs(root, rsum):
            if root is None:
                return                
            dfs(root.right, rsum)
            rsum[0] += root.val
            root.val = rsum[0]
            dfs(root.left, rsum)
            return
        dfs(root, [0])
        return root

if __name__ == "__main__":
   root = constructBinaryTree([4,1,6,0,2,5,7,null,null,null,3,null,null,null,8])    
   print(root.val) 
   Solution().bstToGst(root)
   print(root.left.right.right.val)