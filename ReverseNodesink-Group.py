'''

-Hard-



Given a linked list, reverse the nodes of a linked list k at a time and return its 
modified list.

k is a positive integer and is less than or equal to the length of the linked list. If 
the number of nodes is not a multiple of k then left-out nodes, in the end, should 
remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
Example 3:

Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]
Example 4:

Input: head = [1], k = 1
Output: [1]
 

Constraints:

The number of nodes in the list is in the range sz.
1 <= sz <= 5000
0 <= Node.val <= 1000
1 <= k <= sz
 

Follow-up: Can you solve the problem in O(1) extra memory space?

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverse(self, head):
        if head is None or head.next is None:
           return head
        temp = self.reverse(head.next)
        head.next.next = head
        head.next = None
        return temp

    def reverseKGroup(self, head, k):    
        dummy = ListNode(-1)
        dummy.next = head       
        pre = dummy
        cur = head
        num = 0
        while cur:
            cur = cur.next
            num += 1
        while num >= k:
            cur = pre.next
                #    pre   cur    t
                #     |     |     |  
                #  dummy->  1  -> 2 -> 3 -> 4 -> 5
            for _ in range(1, k):                
                t = cur.next
                cur.next = t.next
                t.next = pre.next
                pre.next = t
                ''' after 1 exchange '''
                #    pre    t    cur
                #     |     |     | 
                #  dummy->  2  -> 1 -> 3 -> 4 -> 5
                ''' after 2 exchanges '''
                #    pre    t         cur
                #     |     |          |  
                #  dummy->  3  -> 2 -> 1 -> 4 -> 5
            pre = cur
            num -= k
        return dummy.next


if __name__ == "__main__":
    a = ListNode(10)
    b = ListNode(11)
    c = ListNode(12)
    d = ListNode(13)
    e = ListNode(14)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    x = a 
    while x is not None:
       print(str(x.val)+'->',end='')
       x = x.next
    print('\n===========\n')
    #e=Solution().reverse(a)
    e=Solution().reverseKGroup(a,3)
    x = e 
    while x is not None:
       print(str(x.val)+'->',end='')
       x = x.next
    print()
