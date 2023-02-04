'''

-Medium-

Given the root of a binary tree, return the length of the longest path, where 
each node in the path has the same value. This path may or may not pass through the root.

The length of the path between two nodes is represented by the number of edges between them.

 

Example 1:


Input: root = [5,4,5,1,1,5]
Output: 2
Example 2:


Input: root = [1,4,5,4,4,5]
Output: 2
 

Constraints:

The number of nodes in the tree is in the range [0, 10^4].
-1000 <= Node.val <= 1000
The depth of the tree will not exceed 1000.



'''
from typing import Optional
from BinaryTree import (null, TreeNode, constructBinaryTree)

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        res = [0] 
        def helper(node, parent):
            if not node: return 0
            l = helper(node.left, node.val)
            r = helper(node.right, node.val)
            res[0] = max(res[0], l+r)
            if node.val == parent:
                return max(l,r)+1
            return 0
        helper(root, root.val)
        return res[0]

if __name__ == "__main__":
    s = Solution()
    root = constructBinaryTree([5,4,5,1,1,null,5])
    root.prettyPrint()
    print(s.longestUnivaluePath(root))
    root = constructBinaryTree([1,4,5,4,4,null,5])
    root.prettyPrint()
    print(s.longestUnivaluePath(root))