'''
-Medium-

Given the head of a linked list, we repeatedly delete consecutive sequences 
of nodes that sum to 0 until there are no such sequences.

After doing so, return the head of the final linked list.  
You may return any such answer.

 

(Note that in the examples below, all sequences are serializations of ListNode objects.)

Example 1:

Input: head = [1,2,-3,3,1]
Output: [3,1]
Note: The answer [1,2,1] would also be accepted.
Example 2:

Input: head = [1,2,3,-3,4]
Output: [1,2,4]
Example 3:

Input: head = [1,2,3,-3,-2]
Output: [1]
 

Constraints:

The given linked list will contain between 1 and 1000 nodes.
Each node in the linked list has -1000 <= node.val <= 1000.


'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from LinkedList import ListNode, constructList
from typing import Optional
from collections import defaultdict, OrderedDict

class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = dummy = ListNode(0)
        dummy.next = head
        prefix = 0
        seen = OrderedDict()
        while cur:
            prefix += cur.val
            node = seen.get(prefix, cur)
            while prefix in seen:
                seen.popitem()
            seen[prefix] = node
            node.next = cur = cur.next
        return dummy.next

    def removeZeroSumSublists2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prefix = 0
        seen = {}
        seen[0] = dummy = ListNode(0)
        dummy.next = head
        while head:
            prefix += head.val
            seen[prefix] = head
            head = head.next
        head = dummy
        prefix = 0
        while head:
            prefix += head.val
            head.next = seen[prefix].next
            head = head.next
        return dummy.next

            

if __name__ == "__main__":
    lis = constructList([1,2,-3,3,1])
    lis = Solution().removeZeroSumSublists(lis)
    cur = lis
    while cur:
        print(cur.val)
        cur = cur.next
    lis = constructList([1,2,3,-3,4])
    lis = Solution().removeZeroSumSublists(lis)
    cur = lis
    while cur:
        print(cur.val)
        cur = cur.next
    lis = constructList([0,0])
    lis = Solution().removeZeroSumSublists(lis)
    cur = lis
    while cur:
        print(cur.val)
        cur = cur.next
    lis = constructList([1,3,2,-3,-2,5,5,-5,1])
    lis = Solution().removeZeroSumSublists(lis)
    cur = lis
    while cur:
        print(cur.val)
        cur = cur.next