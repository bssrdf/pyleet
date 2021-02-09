'''
-Medium-

Given a binary tree, find the length of the longest consecutive sequence 
path.

The path refers to any sequence of nodes from some starting node to 
any node in the tree along the parent-child connections. The longest 
consecutive path need to be from parent to child (cannot be the reverse).

Example 1:

Input:

   1
    \
     3
    / \
   2   4
        \
         5

Output: 3

Explanation: Longest consecutive sequence path is 3-4-5, so return 3.
Example 2:

Input:

   2
    \
     3
    / 
   2    
  / 
 1

Output: 2 

Explanation: Longest consecutive sequence path is 2-3, not 3-2-1, so return 2.

'''

from BinaryTree import (TreeNode, null, constructBinaryTree)

class Solution(object):

    def longestConsecutive(self, root):
        self.res = 0
        def preorder(root, val, out):
            if not root: return
            if root.val == val + 1: out += 1
            else: out = 1
            self.res = max(self.res, out)
            preorder(root.left, root.val, out)
            preorder(root.right, root.val, out)
        preorder(root, root.val, 0)
        return self.res


if __name__ == "__main__":
    root = constructBinaryTree([1,null,3,null,null,2,4,null,null,null,null,null,null,null,5])
    root.prettyPrint()
    print(Solution().longestConsecutive(root))
    root = constructBinaryTree([2,null,3,null,null,2,null,null,null,null,null,1])
    root.prettyPrint()
    print(Solution().longestConsecutive(root))