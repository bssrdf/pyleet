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
    def hasCycle(self, head):
        slow = head
        fast = head
        while fast.next:
            slow = slow.next
            if fast.next != None:
                fast = fast.next.next
            else:
                return False
            if slow == fast:
                return True
        return False


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
    e.next = b
    if Solution().hasCycle(a):
        print('list has cycle')
    else:
        print('list has no cycle')

