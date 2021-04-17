'''
-Medium-

Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. 
(i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100


'''


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from BinaryTree import (null, TreeNode, constructBinaryTree)

from collections import deque

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root: return []
        q = deque([root])
        res = []
        lev = 1
        while q:
            nxt = deque()
            nums = []
            while q:
                node = q.popleft()
                if node.left: nxt.append(node.left)
                if node.right: nxt.append(node.right)
                nums.append(node.val)
            if lev % 2 == 0:
                nums = nums[::-1] 
            res.append(nums)
            q = nxt
            lev += 1
        return res



if __name__ == "__main__":
    root = constructBinaryTree([3,9,20,null,null,15,7])
    root.prettyPrint()
    print(Solution().zigzagLevelOrder(root))