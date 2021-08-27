'''
-Medium-
Given a binary tree where all the right nodes are either leaf nodes with a 
sibling (a left node that shares the same parent node) or empty, flip it 
upside down and turn it into a tree where the original right nodes turned 
into left leaf nodes. Return the new root.

样例
Example1

Input: {1,2,3,4,5}
Output: {4,5,2,#,#,3,1}
Explanation:
The input is
    1
   / \
  2   3
 / \
4   5
and the output is
   4
  / \
 5   2
    / \
   3   1
Example2

Input: {1,2,3,4}
Output: {4,#,2,3,1}
Explanation:
The input is
    1
   / \
  2   3
 /
4
and the output is
   4
    \
     2
    / \
   3   1


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
    @return: new root
    """
    def upsideDownBinaryTree(self, root):
        # write your code here
        stack = []
        cur = root
        while cur:
            stack.append(cur)
            cur = cur.left
        newroot = stack.pop()
        cur = newroot
        print(cur.val)
        while stack:
            node = stack.pop()
            print(node.val)
            cur.right = node
            if node.right:
                cur.left = node.right
                node.right = None
            node.left = None
            cur = node
        return newroot


if __name__ == "__main__": 
    root = constructBinaryTree([1,2,3,4,5])
    root.prettyPrint()
    uroot = Solution().upsideDownBinaryTree(root)
    uroot.prettyPrint()
    root = constructBinaryTree([1,2,3,4])
    root.prettyPrint()
    uroot = Solution().upsideDownBinaryTree(root)
    uroot.prettyPrint()
