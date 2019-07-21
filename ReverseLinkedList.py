'''
Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?
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
       print(x.val)
       x = x.next
    print('===========')
    e=Solution().reverse(a)
    x = e 
    while x is not None:
       print(x.val)
       x = x.next

