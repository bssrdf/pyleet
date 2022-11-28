'''
-Medium-

You are given the head of a linked list.

Remove every node which has a node with a strictly greater value anywhere to the right side of it.

Return the head of the modified linked list.

 

Example 1:


Input: head = [5,2,13,3,8]
Output: [13,8]
Explanation: The nodes that should be removed are 5, 2 and 3.
- Node 13 is to the right of node 5.
- Node 13 is to the right of node 2.
- Node 8 is to the right of node 3.
Example 2:

Input: head = [1,1,1,1]
Output: [1,1,1,1]
Explanation: Every node has value 1, so no nodes are removed.
 

Constraints:

The number of the nodes in the given list is in the range [1, 105].
1 <= Node.val <= 105


'''
from typing import Optional

from LinkedList import (ListNode,constructList, printList)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        stack = []
        while cur:
            while stack and stack[-1].val < cur.val:
                node = stack.pop()
                node.next = None
            # stack[-1].next = cur
            stack.append(cur)
            cur = cur.next
        head = stack[0]
        cur = head
        for node in stack[1:]:
            cur.next = node
            cur = cur.next 
        cur.next = None
        return head
    
    def removeNodes2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(10**5+1)
        cur = head
        stack = [dummy]
        while cur:
            while stack and stack[-1].val < cur.val:
                node = stack.pop()
                node.next = None
            stack[-1].next = cur
            stack.append(cur)
            cur = cur.next
        return stack[0].next

            

        
if __name__=="__main__":
    head = constructList([5,2,13,3,8])    
    printList(head)
    res = Solution().removeNodes(head)
    printList(res)
    head = constructList([5,2,13,3,8])    
    printList(head)
    res = Solution().removeNodes2(head)
    printList(res)

    head = constructList([1, 1, 1, 1])    
    printList(head)
    res = Solution().removeNodes(head)
    printList(res)