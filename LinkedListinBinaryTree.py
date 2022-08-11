'''
-Medium-


Given a binary tree root and a linked list with head as the first node. 

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.

 

Example 1:



Input: head = [4,2,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Explanation: Nodes in blue form a subpath in the binary Tree.  
Example 2:



Input: head = [1,4,2,6], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: true
Example 3:

Input: head = [1,4,2,6,8], root = [1,4,4,null,2,2,null,1,null,6,8,null,null,null,null,1,3]
Output: false
Explanation: There is no path in the binary tree that contains all the elements of the linked list from head.
 

Constraints:

The number of nodes in the tree will be in the range [1, 2500].
The number of nodes in the list will be in the range [1, 100].
1 <= Node.val <= 100 for each node in the linked list and binary tree.


'''

from typing import Optional
from BinaryTree import (null, TreeNode, constructBinaryTree)

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.

# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(node, cur):
            if not cur: return True
            if not node: return False            
            if cur.val == node.val:
                if dfs(node.left, cur.next):
                    return True
                if dfs(node.right, cur.next):
                    return True            
            return False
        if not head: return True
        if not root: return False 
        return (dfs(root, head)                    
               # if we arrive here, it means matching starting from a particular tree node 
               # and the head failed; we have to start over from a left/right child and head 
               # again; this is exactly the original problem, so we do a recursion of isSubPath
               or self.isSubPath(head, root.left)
               or self.isSubPath(head, root.right))
        


        