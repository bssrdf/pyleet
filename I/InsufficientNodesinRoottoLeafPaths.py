'''

-Medium-
*DFS*
*Hash Table*

Given the root of a binary tree and an integer limit, delete all insufficient nodes in the tree simultaneously, and return the root of the resulting binary tree.

A node is insufficient if every root to leaf path intersecting this node has a sum strictly less than limit.

A leaf is a node with no children.

 

Example 1:


Input: root = [1,2,3,4,-99,-99,7,8,9,-99,-99,12,13,-99,14], limit = 1
Output: [1,2,3,4,null,null,7,8,9,null,14]
Example 2:


Input: root = [5,4,8,11,null,17,4,7,1,null,null,5,3], limit = 22
Output: [5,4,8,11,null,17,4,7,null,null,null,5]
Example 3:


Input: root = [1,2,-3,-5,null,4,null], limit = -1
Output: [1,null,-3,4]
 

Constraints:

The number of nodes in the tree is in the range [1, 5000].
-105 <= Node.val <= 105
-109 <= limit <= 109


'''

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        m = set()
        def helper(node, total):
            if not node: return set()
            l = helper(node.left, total + node.val)
            r = helper(node.right, total + node.val)
            ret = set()
            todelete = True 
            dset = l | r 
            for v in dset:
                if v + node.val + total >= limit: 
                    todelete = False
                ret.add(v + node.val)
            if not dset:
               ret.add(node.val)    
               if node.val + total >= limit: 
                    todelete = False 
            if todelete: m.add(node)
            return ret
        helper(root, 0)
        # print(m)
        if root in m: return None
        def helper1(node):
            if not node: return
            if node.left in m:
                node.left = None
            else:
                helper1(node.left)
            if node.right in m:
                node.right = None
            else:
                helper1(node.right)

        helper1(root)
        return root
    
    def sufficientSubset2(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:
        m = set()
        def helper(node, total):
            if not node: return set()
            l = helper(node.left, total + node.val)
            r = helper(node.right, total + node.val)
            ret = set()
            todelete = True 
            dset = l | r or {0}
            for v in dset:
                if v + node.val + total >= limit: 
                    todelete = False
                ret.add(v + node.val)
            if todelete: m.add(node)
            return ret
        helper(root, 0)
        if root in m: return None
        def helper1(node):
            if not node: return
            if node.left in m:
                node.left = None
            else:
                helper1(node.left)
            if node.right in m:
                node.right = None
            else:
                helper1(node.right)

        helper1(root)
        return root