'''
-Medium-

Given the root of a binary tree, return the bottom-up level order traversal of 
its nodes' values. (i.e., from left to right, level by level from leaf to root).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-1000 <= Node.val <= 1000
'''
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = deque([root])
        res = []
        if not root: return res
        while queue:
            newqueue, lev = deque(), []
            while queue:
                node = queue.popleft()
                lev.append(node.val)
                if node.left: newqueue.append(node.left)
                if node.right: newqueue.append(node.right)
            queue = newqueue
            res.append(lev)
        return res[::-1]