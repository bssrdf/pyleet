'''

-Medium-

Given a binary tree, imagine yourself standing on the right side of it, return the values of 
the nodes you can see ordered from top to bottom.

Example:

Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]
Explanation:

   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---

'''

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        res = []
        if not root: return res
        queue = deque([root])
        while queue:
            newq = deque()
            while len(queue) > 1:                
                node = queue.popleft()
                if node.left:
                   newq.append(node.left)
                if node.right:
                   newq.append(node.right)
            node = queue.popleft()
            res.append(node.val)            
            if node.left:
                newq.append(node.left)
            if node.right:
                newq.append(node.right)
            queue = newq 
        return res
                