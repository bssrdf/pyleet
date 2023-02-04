'''

-Medium-

$$$


Given the head of a singly linked list that is sorted in non-decreasing order using the absolute values of its nodes, return the list sorted in non-decreasing order using the actual values of its nodes.

 

Example 1:



Input: head = [0,2,-5,5,10,-10]
Output: [-10,-5,0,2,5,10]
Explanation:
The list sorted in non-descending order using the absolute values of the nodes is [0,2,-5,5,10,-10].
The list sorted in non-descending order using the actual values is [-10,-5,0,2,5,10].
Example 2:



Input: head = [0,1,2]
Output: [0,1,2]
Explanation:
The linked list is already sorted in non-decreasing order.
Example 3:

Input: head = [1]
Output: [1]
Explanation:
The linked list is already sorted in non-decreasing order.
 

Constraints:

The number of nodes in the list is the range [1, 105].
-5000 <= Node.val <= 5000
head is sorted in non-decreasing order using the absolute value of its nodes.
 

Follow up:
Can you think of a solution with O(n) time complexity?




'''

from typing import Optional
from LinkedList import (ListNode, constructList, printList)

class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        dpos = ListNode(1)
        dneg = ListNode(-1)
        pos, neg = dpos, dneg
        while cur:
            if cur.val >= 0:
                pos.next = cur
                cur = cur.next
                pos = pos.next
                pos.next = None
            else:
                neg.next = cur
                cur = cur.next
                neg = neg.next
                neg.next = None
        pre = dneg.next
        if not pre: return dpos.next 
        cur = pre.next
        while cur:
            nxt = cur.next            
            cur.next = pre
            pre = cur
            cur = nxt
        neg = pre
        dneg.next.next = dpos.next
        return neg 
    
    def sortLinkedList2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, curr = head, head.next
        while curr:
            if curr.val < 0:
                t = curr.next
                prev.next = t
                curr.next = head
                head = curr
                curr = t
            else:
                prev, curr = curr, curr.next
        return head


            

        

if __name__ == "__main__":
    head = constructList([0,2,-5,5,10,-10])
    printList(head)
    printList(Solution().sortLinkedList(head))
    head = constructList([0,1,2])
    printList(head)
    printList(Solution().sortLinkedList(head))
    head = constructList([1])
    printList(head)
    printList(Solution().sortLinkedList(head))
    head = constructList([-1, -5, -6])
    printList(head)
    printList(Solution().sortLinkedList(head))