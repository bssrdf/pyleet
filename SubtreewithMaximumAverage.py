'''
-Medium-

Given a binary tree, find the subtree with maximum average. Return the root of the subtree.

LintCode will print the subtree which root is your return node.
It's guaranteed that there is only one subtree with maximum average.

样例
Example 1

Input：
{1,-5,11,1,2,4,-2}
Output：11
Explanation:
The tree is look like this:
     1
   /   \
 -5     11
 / \   /  \
1   2 4    -2 
The average of subtree of 11 is 4.3333, is the maximun.
Example 2

Input：
{1,-5,11}
Output：11
Explanation:
     1
   /   \
 -5     11
The average of subtree of 1,-5,11 is 2.333,-5,11. So the subtree of 11 is the maximun.
标签
企业
Amazon
相关题目
632
Binary Tree Maximum Node
简单
628
Maximum Subtree
简单
596
Minimum Subtree
简单




'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

from BinaryTree import (null, constructBinaryTree, TreeNode)
class Solution:
    """
    @param root: the root of binary tree
    @return: the root of the maximum average of subtree
    """
    def findSubtree2(self, root):
        # write your code here
        self.ans = None
        maxAve = [-float('inf')]
        def helper(node):
            if not node: return (0, 0)
            ls, ln = helper(node.left)
            rs, rn = helper(node.right)
            n = rn + ln + 1
            s = ls + rs + node.val
            ave = s/n
            if maxAve[0] < ave:
                maxAve[0] = ave
                self.ans = node
            return s, n
        helper(root)
        return self.ans 




if __name__ == "__main__":
    root = constructBinaryTree([1,-5,11,1,2,4,-2])
    root.prettyPrint()
    ans = Solution().findSubtree2(root)
    print(ans.val)
    root = constructBinaryTree([1,-5,11])
    root.prettyPrint()
    ans = Solution().findSubtree2(root)
    print(ans.val)