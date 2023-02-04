'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following is not:
    1
   / \
  2   2
   \   \
   3    3
Note:
Bonus points if you could solve it both recursively and iteratively.
'''

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    # Solve it recursively
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        def isSymLR(left, right):
            if not left and not right:
                return True
            elif not left and right or not right and left:
                return False
            else:
                return left.val == right.val and isSymLR(left.left, right.right) and isSymLR(left.right, right.left)
        return isSymLR(root.left, root.right)

    # Solve it iteratively
    def isSymmetric_iterate(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True

if __name__ == "__main__":
    None
