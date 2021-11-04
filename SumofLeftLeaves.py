'''
-Easy-

Given the root of a binary tree, return the sum of all left leaves.

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: 24
Explanation: There are two left leaves in the binary tree, with values 9 and 15 respectively.
Example 2:

Input: root = [1]
Output: 0
 

Constraints:

The number of nodes in the tree is in the range [1, 1000].
-1000 <= Node.val <= 1000


'''

from BinaryTree import (null, TreeNode, constructBinaryTree)
from typing import Optional

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def helper(node, direct):
            if not node.left and not node.right:
                return node.val if direct > 0 else 0
            ans = 0
            if node.left:
                ans += helper(node.left, 1)
            if node.right:
                ans += helper(node.right, -1)
            return ans
        return helper(root, 0)



if __name__ == "__main__":
    root = constructBinaryTree([3,9,20,null,null,15,7])
    root.prettyPrint()
    print(Solution().sumOfLeftLeaves(root))

        