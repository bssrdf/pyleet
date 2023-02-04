'''
-Easy-

Given the root of a Binary Search Tree and a target number k, return true if there exist two 
elements in the BST such that their sum is equal to the given target.

 

Example 1:


Input: root = [5,3,6,2,4,null,7], k = 9
Output: true
Example 2:


Input: root = [5,3,6,2,4,null,7], k = 28
Output: false
Example 3:

Input: root = [2,1,3], k = 4
Output: true
Example 4:

Input: root = [2,1,3], k = 1
Output: false
Example 5:

Input: root = [2,1,3], k = 3
Output: true
 

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
-10^4 <= Node.val <= 10^4
root is guaranteed to be a valid binary search tree.
-10^5 <= k <= 10^5

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from BinaryTree import (null, constructBinaryTree, TreeNode)
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        m =  set()
        def helper(node):
            if not node: return False
            if k - node.val in m:
                return True
            m.add(node.val)
            return helper(node.left) or helper(node.right)
        return helper(root)

if __name__ == "__main__":
    root = constructBinaryTree([5,3,6,2,4,null,7])
    root.prettyPrint()
    print(Solution().findTarget(root, 9))
    root = constructBinaryTree([5,3,6,2,4,null,7])
    root.prettyPrint()
    print(Solution().findTarget(root, 28))
    root = constructBinaryTree([2,1,3])
    root.prettyPrint()
    print(Solution().findTarget(root, 4))
    root = constructBinaryTree([2,1,3])
    root.prettyPrint()
    print(Solution().findTarget(root, 1))
    root = constructBinaryTree([2,1,3])
    root.prettyPrint()
    print(Solution().findTarget(root, 3))

        