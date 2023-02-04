'''
-Medium-

Given the root of a binary tree, find the maximum value V for which there 
exist different nodes A and B where V = |A.val - B.val| and A is an 
ancestor of B.

A node A is an ancestor of B if either: any child of A is equal to B, or 
any child of A is an ancestor of B.

 

Example 1:


Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
Output: 7
Explanation: We have various ancestor-node differences, some of which 
are given below :
|8 - 3| = 5
|3 - 7| = 4
|8 - 1| = 7
|10 - 13| = 3
Among all possible differences, the maximum value of 7 is obtained by 
|8 - 1| = 7.
Example 2:


Input: root = [1,null,2,null,0,3]
Output: 3
 

Constraints:

The number of nodes in the tree is in the range [2, 5000].
0 <= Node.val <= 105

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from BinaryTree import (TreeNode, constructBinaryTree, inOrder, null) 

class Solution(object):

    def maxAncestorDiffFast(self, root):
        self.res = 0
        def helper(node, max_val, min_val):
            if not node:
                self.res = max(self.res, max_val - min_val)
                return
            helper(node.left, max(max_val, node.val), min(min_val, node.val))
            helper(node.right, max(max_val, node.val), min(min_val, node.val))
        helper(root, 0, 100000)
        return self.res

    def maxAncestorDiff(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        CMIN = 10**5+1
        CMAX = -1
        self.res = 0
        def helper(root):
            if not root: return CMIN, CMAX                
            li, lx = helper(root.left)
            ri, rx = helper(root.right)
            mi = min(li, ri)             
            mx = max(lx, rx)             
            if mi != CMIN:  
               self.res = max(self.res, abs(root.val - mi))
            if mx != CMAX:  
               self.res = max(self.res, abs(root.val - mx))
            return min(mi, root.val), max(mx, root.val) 
        helper(root)
        return self.res

if __name__ == "__main__":
  node = constructBinaryTree([8,3,10,1,6,null,14,null,null,4,7,null, null,13,null])
  #inOrder(node)
  #print(Solution().maxAncestorDiff(node))

  node = constructBinaryTree([1,null,2,null,null, null, 0, null, null, null, null, null, null, 3,null])
  #inOrder(node)
  #print(Solution().maxAncestorDiff(node))
  node = constructBinaryTree([2,null,0,null,4,null,3,null,1])