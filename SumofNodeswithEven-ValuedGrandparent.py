'''
-Medium-

Given the root of a binary tree, return the sum of values of nodes with an even-valued 
grandparent. If there are no nodes with an even-valued grandparent, return 0.

A grandparent of a node is the parent of its parent if it exists.

 

Example 1:


Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents.
Example 2:


Input: root = [1]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 104].
1 <= Node.val <= 100

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from BinaryTree import (null, constructBinaryTree, TreeNode)

class Solution(object):
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        res = [0]
        def helper(node, par):
            if not node: return
            if par and par.val%2 == 0:
                if node.left: res[0] += node.left.val
                if node.right: res[0] += node.right.val
            helper(node.left, node)
            helper(node.right, node)
        helper(root, None)
        return res[0]

if __name__ == "__main__":
    root = constructBinaryTree([6,7,8,2,7,1,3,9,null,1,4,null,null,null,5])
    root.prettyPrint()
    print(Solution().sumEvenGrandparent(root))