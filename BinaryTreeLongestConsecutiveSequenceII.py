'''
-Medium-

Given a binary tree, you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing. For example, [1,2,3,4] and [4,3,2,1] are both considered valid, but the path [1,2,4,3] is not valid. On the other hand, the path can be in the child-Parent-child order, where not necessarily be parent-child order.

Example 1:

Input:
        1
       / \
      2   3
Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
 

Example 2:

Input:
        2
       / \
      1   3
Output: 3
Explanation: The longest consecutive path is [1, 2, 3] or [3, 2, 1].
 

Note: All the values of tree nodes are in the range of [-1e7, 1e7].

'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

from BinaryTree import (TreeNode, null, constructBinaryTree)

class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive2(self, root):
        # write your code here
        self.res = 0
        def helper(root, parent):
            if not root: return (0, 0)
            left = helper(root.left, root.val)
            right = helper(root.right, root.val)
            self.res = max(self.res, left[0]+right[1]+1)
            self.res = max(self.res, left[1]+right[0]+1)
            inc, dec = 0, 0
            if root.val == parent + 1:
                inc = max(left[0], right[0]) + 1
            elif root.val == parent -1: 
                dec = max(left[1], right[1]) + 1
            return (inc, dec) 
        helper(root, root.val)
        return self.res

    def longestConsecutive2Clean(self, root):
        # TLE on Lintcode
        def helper(root, diff):
            if not root: return 0
            left, right = 0, 0
            if root.left and root.val - root.left.val == diff:
                left = 1 + helper(root.left, diff)
            if root.right and root.val - root.right.val == diff:
                right = 1 + helper(root.right, diff)
            return max(left, right)
        if not root: return 0
        res = helper(root, 1) + helper(root, -1) + 1
        return max(res, self.longestConsecutive2Clean(root.left), 
                        self.longestConsecutive2Clean(root.right))

                 


if __name__ == "__main__":
    root = constructBinaryTree([1,2,0,3])
    root.prettyPrint()
    print(Solution().longestConsecutive2(root))

