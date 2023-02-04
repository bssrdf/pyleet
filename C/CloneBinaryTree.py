'''
-Medium-
For the given binary tree, return a deep copy of it.

样例
Example 1:

Input:

{1,2,3}
Output:

{1,2,3}
Explanation:

The binary tree is look like this:

    1
   / \
  2   3
 / \
4   5
 

Example 2:

Input:

{1,2,3,4,5}
Output:

{1,2,3,4,5}
Explanation:

The binary tree is look like this:

  1
 / \
2   3

'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: The root of binary tree
    @return: root of new tree
    """
    def cloneTree(self, root):
        # write your code here
        if not root: return None
        node = TreeNode(root.val)
        node.left = self.cloneTree(root.left)
        node.right = self.cloneTree(root.right)
        return node