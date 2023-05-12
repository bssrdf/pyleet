'''

-Medium-

$$$

Given a circular linked list list of positive integers, your task is to split it into 2 circular linked lists so that the first one contains the first half of the nodes in list (exactly ceil(list.length / 2) nodes) in the same order they appeared in list, and the second one contains the rest of the nodes in list in the same order they appeared in list.

Return an array answer of length 2 in which the first element is a circular linked list representing the first half and the second element is a circular linked list representing the second half.

A circular linked list is a normal linked list with the only difference being that the last node's next node, is the first node.
 

Example 1:

Input: nums = [1,5,7]
Output: [[1,5],[7]]
Explanation: The initial list has 3 nodes so the first half would be the first 2 elements since ceil(3 / 2) = 2 and the rest which is 1 node is in the second half.
Example 2:

Input: nums = [2,6,1,5]
Output: [[2,6],[1,5]]
Explanation: The initial list has 4 nodes so the first half would be the first 2 elements since ceil(4 / 2) = 2 and the rest which is 2 nodes are in the second half.
 

Constraints:

The number of nodes in list is in the range [2, 105]
0 <= Node.val <= 109
LastNode.next = FirstNode where LastNode is the last node of the list and FirstNode is the first one
Solutions



'''
import sys
sys.path.append("o:\\Algorithms")

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional, List
from pyleet.LinkedList import constructList, ListNode, printList

# Definition for singly-linked list.
# class ListNode(object):
#      def __init__(self, val=0, next=None):
#          self.val = val
#          self.next = next


# def constructList(items):
#     node = ListNode(0)
#     head = node
#     for i in items:
#         node.next = ListNode(i)
#         node = node.next
#     return head.next  

# def printList(head):
#     while head:
#         print(str(head.val)+'->',end='')
#         head = head.next
#     print('null')


class Solution:
    def splitCircularLinkedList(
        self, head: Optional[ListNode]
    ) -> List[Optional[ListNode]]:
        # wrong
        fast, slow = head, head
        # print(fast.val, slow.val)
        prevf = fast.next
        fast = fast.next.next
        prevs = slow
        slow = slow.next
        while fast != head:
            prevf = fast.next
            fast = fast.next.next
            prevs = slow
            slow = slow.next
        prevs.next = head 
        prevf.next = slow
        return [head, slow]
    
    def splitCircularLinkedList2(
        self, list: Optional[ListNode]
    ) -> List[Optional[ListNode]]:
        slow = fast = list
        while fast.next != list and fast.next.next != list:
            slow = slow.next
            fast = fast.next.next
        if fast.next != list:
            fast = fast.next
        list2 = slow.next
        fast.next = list2
        slow.next = list
        return [list, list2]

        

if __name__ == "__main__":
    head = constructList([2,6,1,5])
    printList(head)
    prev = cur = head
    while cur:
        prev = cur
        cur = cur.next
    prev.next = head 
    sol = Solution().splitCircularLinkedList(head=head) 
    print(sol[0].val)
    print(sol[1].val)
    head = constructList([1,5,7])
    printList(head)
    prev = cur = head
    while cur:
        prev = cur
        cur = cur.next
    prev.next = head 
    sol = Solution().splitCircularLinkedList(head=head) 
    print(sol[0].val)
    print(sol[1].val)
