'''

-Medium-


You are given the head of a linked list.

The nodes in the linked list are sequentially assigned to non-empty groups whose lengths form the sequence of the natural numbers (1, 2, 3, 4, ...). The length of a group is the number of nodes assigned to it. In other words,

The 1st node is assigned to the first group.
The 2nd and the 3rd nodes are assigned to the second group.
The 4th, 5th, and 6th nodes are assigned to the third group, and so on.
Note that the length of the last group may be less than or equal to 1 + the length of the second to last group.

Reverse the nodes in each group with an even length, and return the head of the modified linked list.

 

Example 1:


Input: head = [5,2,6,3,9,1,7,3,8,4]
Output: [5,6,2,3,9,1,4,8,3,7]
Explanation:
- The length of the first group is 1, which is odd, hence no reversal occurs.
- The length of the second group is 2, which is even, hence the nodes are reversed.
- The length of the third group is 3, which is odd, hence no reversal occurs.
- The length of the last group is 4, which is even, hence the nodes are reversed.
Example 2:


Input: head = [1,1,0,6]
Output: [1,0,1,6]
Explanation:
- The length of the first group is 1. No reversal occurs.
- The length of the second group is 2. The nodes are reversed.
- The length of the last group is 1. No reversal occurs.
Example 3:


Input: head = [1,1,0,6,5]
Output: [1,0,1,5,6]
Explanation:
- The length of the first group is 1. No reversal occurs.
- The length of the second group is 2. The nodes are reversed.
- The length of the last group is 2. The nodes are reversed.
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 105


'''
from typing import Optional
from LinkedList import (ListNode,constructList, printList)


class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def move(pre, start, steps):
            cur, i = start, 0
            while cur and i < steps:
                pre = cur
                cur = cur.next
                i += 1            
            return (pre, cur, i)
        def reverse(left, right):
            t = left
            pre = cur = left.next
            while cur != right:
                nxt = cur.next
                cur.next = t
                t = cur
                cur = nxt
            pre.next = cur
            left.next = t
            return pre
        steps, pre, prev = 2, head, head
        cur = head.next
        while cur:
            prev, cur, step = move(prev, cur, steps)
            if step % 2 == 0:
                prev = reverse(pre, cur)
            pre = prev
            steps += 1
        return head

    def reverseEvenLengthGroups2(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # wrong
        def move(pre, start, steps):
            cur, i = start, 0
            t, prev = pre, pre            
            while cur and i < steps:                
                nxt = cur.next
                if steps % 2 == 0:
                    cur.next = t
                    t = cur
                prev = cur
                cur = nxt
                i += 1
            if steps % 2 == 0:
                start.next = cur
                pre.next = t
            return (start, cur, i) if steps % 2 == 0 else (prev, cur, i) 
        
        steps, pre = 2, head
        prev = pre 
        if not head.next: return head
        prev, cur, step = move(prev, head.next, steps)
        while cur:            
            steps += 1
            prev, cur, step = move(prev, cur, steps)         
        return head
            
if __name__ == "__main__":
    head = constructList([5,2,6,3,9,1,7,3,8,4])
    printList(head)
    sol = Solution().reverseEvenLengthGroups(head)
    printList(sol)
    head = constructList([5,2,6,3,9,1,7,3,8,4])
    printList(head)
    sol = Solution().reverseEvenLengthGroups2(head)
    printList(sol)

    head = constructList([1,1,0,6])
    printList(head)
    sol = Solution().reverseEvenLengthGroups(head)
    printList(sol)

    head = constructList([1,1,0,6,5])
    printList(head)
    sol = Solution().reverseEvenLengthGroups(head)
    printList(sol)


    head = constructList([6, 2, 1])
    printList(head)
    sol = Solution().reverseEvenLengthGroups(head)
    printList(sol)

    head = constructList([6, 2])
    printList(head)
    sol = Solution().reverseEvenLengthGroups(head)
    printList(sol)

    head = constructList([6])
    printList(head)
    sol = Solution().reverseEvenLengthGroups(head)
    printList(sol)