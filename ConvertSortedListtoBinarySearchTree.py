'''
-Medium-

Given the head of a singly linked list where elements are sorted in ascending order, convert it 
to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth 
of the two subtrees of every node never differ by more than 1.

 

Example 1:


Input: head = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: One possible answer is [0,-3,9,-10,null,5], which represents the shown height balanced BST.
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [0]
Output: [0]
Example 4:

Input: head = [1,3]
Output: [3,1]
 

Constraints:

The number of nodes in head is in the range [0, 2 * 104].
-10^5 <= Node.val <= 10^5


'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from BinaryTree import (null, TreeNode)
class Solution(object):

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        """
        if not head: return None
        if not head.next: return TreeNode(head.val)
        slow, fast, pre = head, head, None
        while fast and fast.next:
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None   # cut off the left half

        root = TreeNode(slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(slow.next)
        return root
        """

        def findMiddle(node):
            slow, fast, pre = node, node, None
            while fast and fast.next:
                pre  = slow
                slow = slow.next
                fast = fast.next.next
            return pre
        if not head: return None
        nxt = head.next
        if not nxt: return TreeNode(head.val)
        middle = findMiddle(head)
        lnode, middle = middle, middle.next
        rnode = middle.next if middle else None
        lnode.next = None
        root = TreeNode(middle.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(rnode)
        
        return root

if __name__ == "__main__":
    node = ListNode(-10)
    head = node
    for i in [-3, 0, 5, 9]:
       newnode = ListNode(i)
       node.next = newnode
       node = node.next
    root = Solution().sortedListToBST(head)
    root.prettyPrint()

    
