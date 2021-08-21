'''
-Medium-

Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.

 

Example 1:


Input: root = [1,2,3,4,null,2,4,null,null,4]
Output: [[2,4],[4]]
Example 2:


Input: root = [2,1,1]
Output: [[1]]
Example 3:


Input: root = [2,2,2,3,null,3,null]
Output: [[2,3],[3]]
 

Constraints:

The number of the nodes in the tree will be in the range [1, 10^4]
-200 <= Node.val <= 200


'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from BinaryTree import (null, constructBinaryTree, TreeNode)
from collections import defaultdict
class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        """
        m, res = defaultdict(list), []
        def helper(node, sign):
            if not node: return sign+'*'
            left = helper(node.left, '-')
            right = helper(node.right, '+')
            sig = str(node.val)+left+right
            m[sig].append(node)
            return sign+sig
        helper(root, '=')
        for s in m:
            if len(m[s]) > 1: 
                res.append(m[s][0])
        return res

if __name__ == "__main__":
    #'''
    root = constructBinaryTree([1,2,3,4,null,2,4,null,null,null, null,4])
    root.prettyPrint()
    res = Solution().findDuplicateSubtrees(root)
    for r in res:
        print(r.val)
    #'''
    root = constructBinaryTree([2,1,1])
    root.prettyPrint()
    res = Solution().findDuplicateSubtrees(root)
    for r in res:
        print(r.val)
    root = constructBinaryTree([2,2,2,3,null,3,null])
    root.prettyPrint()
    res = Solution().findDuplicateSubtrees(root)
    for r in res:
        print(r.val)