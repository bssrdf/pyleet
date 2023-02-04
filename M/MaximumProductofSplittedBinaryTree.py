'''
-Medium-

Given the root of a binary tree, split the binary tree into two subtrees by removing one 
edge such that the product of the sums of the subtrees is maximized.

Return the maximum product of the sums of the two subtrees. Since the answer may be too large, 
return it modulo 109 + 7.

Note that you need to maximize the answer before taking the mod and not after taking it.

 

Example 1:


Input: root = [1,2,3,4,5,6]
Output: 110
Explanation: Remove the red edge and get 2 binary trees with sum 11 and 10. Their product is 110 (11*10)
Example 2:


Input: root = [1,null,2,3,4,null,null,5,6]
Output: 90
Explanation: Remove the red edge and get 2 binary trees with sum 15 and 6.Their product is 90 (15*6)
Example 3:

Input: root = [2,3,9,10,7,8,6,5,4,11,1]
Output: 1025
Example 4:

Input: root = [1,1]
Output: 1
 

Constraints:

The number of nodes in the tree is in the range [2, 5 * 10^4].
1 <= Node.val <= 10^4


'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from BinaryTree import (null, constructBinaryTree, TreeNode)

class Solution(object):
    def maxProduct(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def total(node):
            if not node: return 0
            return node.val + total(node.left) + total(node.right)
        sm = total(root)
        res = [0]
        def helper(node):
            if not node: return 0
            left = helper(node.left)
            right = helper(node.right)
            res[0] = max(res[0], right*(sm-right))
            res[0] = max(res[0], left*(sm-left))
            return node.val + helper(node.left) + helper(node.right)
        helper(root)
        return res[0]

    def maxProductDP(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        m = set()
        res = 0
        def total(node):
            if not node: return 0
            t = node.val + total(node.left) + total(node.right)
            m.add(t)
            return t 
        sm = total(root)       
        for i in m:
            res = max(res, i*(sm-i)) 
        return res%(10**9+7)

if __name__ == "__main__":
    root = constructBinaryTree([1,2,3,4,5,6])
    root.prettyPrint()
    #rint(Solution().maxProduct(root))
    print(Solution().maxProductDP(root))
