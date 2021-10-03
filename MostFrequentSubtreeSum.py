'''

-Medium-

Given the root of a binary tree, return the most frequent subtree sum. If there is a tie, 
return all the values with the highest frequency in any order.

The subtree sum of a node is defined as the sum of all the node values formed by the subtree 
rooted at that node (including the node itself).

 

Example 1:


Input: root = [5,2,-3]
Output: [2,-3,4]
Example 2:


Input: root = [5,2,-5]
Output: [2]
 

Constraints:

The number of nodes in the tree is in the range [1, 10^4].
-10^5 <= Node.val <= 10^5

'''
from BinaryTree import (TreeNode, null, constructBinaryTree)
from typing import Optional, List
from collections import defaultdict
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        m = defaultdict(int)
        def helper(node):
            if not node: return 0
            l = helper(node.left)
            r = helper(node.right)
            subsm = l + r + node.val
            m[subsm] += 1
            return subsm
        helper(root)
        fr = max(m.values())
        return [k for k in m if m[k] == fr] 

if __name__ == "__main__":
    root = constructBinaryTree([5,2,-3])
    root.prettyPrint()
    print(Solution().findFrequentTreeSum(root))
    root = constructBinaryTree([5,2,-5])
    root.prettyPrint()
    print(Solution().findFrequentTreeSum(root))
        