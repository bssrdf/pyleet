'''
-Medium-

描述
Given a binary tree, count the number of uni-value subtrees.

A Uni-value subtree means all nodes of the subtree have the same value.

样例
Example1

Input:  root = {5,1,5,5,5,#,5}
Output: 4
Explanation:
              5
             / \
            1   5
           / \   \
          5   5   5
Example2

Input:  root = {1,3,2,4,5,#,6}
Output: 3
Explanation:
              1
             / \
            3   2
           / \   \
          4   5   6



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
    @param root: the given tree
    @return: the number of uni-value subtrees.
    """
    def countUnivalSubtreesAC(self, root):
        # write your code here
        def helper(node):
            if not node: return (0, True)
            if not node.left and not node.right: return (1, True)            
            l, lb = helper(node.left)
            r, rb = helper(node.right)
            b = lb and rb and (node.val == node.left.val if node.left else True) and (node.val == node.right.val if node.right else True)
            return (l+r+b, b)
        ans,_ = helper(root)
        return ans 

    def countUnivalSubtrees(self, root):
        bb = [True]
        def isUnival(root, b):
            if not root: return 0
            l, r = [True], [True]
            left = isUnival(root.left, l) 
            right = isUnival(root.right, r)
            res = left + right
            b[0] = l[0] and r[0] and (root.val == root.left.val if root.left else True) and (root.val == root.right.val if root.right else True)
            return res + b[0]
        return isUnival(root, bb)

if __name__ == "__main__":
    '''
    root = constructBinaryTree([5,1,5,5,5,null,5])
    print(Solution().countUnivalSubtreesWrong(root))
    root = constructBinaryTree([1,3,2,4,5,null,6])
    print(Solution().countUnivalSubtreesWrong(root))

    '''
    #root = constructBinaryTree([1,1,-1,1,1,1,1,1,1,1,1,1,1,1,-1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,-1])
    root = constructBinaryTree([1,1,1,1,1,-1])
    root.prettyPrint()
    print(Solution().countUnivalSubtrees(root))
    print(Solution().countUnivalSubtreesAC(root))
