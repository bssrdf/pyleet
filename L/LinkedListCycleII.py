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

    def detectCycle(self, head):        
        slow = fast = head
        while fast and fast.next: 
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                break
        else:
            return None      
        fast = head
        while slow != fast:
            slow, fast = slow.next, fast.next
        return slow
        '''
    def detectCycle(self, head):
        if head is None or head.next is None:
            return None
        slow, fast = head.next, head.next.next
        while fast and fast.next and slow != fast:
            fast = fast.next.next
            slow = slow.next
        if fast is None or fast.next is None:
            return None
        slow = head
        while slow != fast:
            slow, fast = slow.next, fast.next
        return slow
        '''


if __name__ == "__main__":
    a = ListNode(10)
    b = ListNode(11)
    c = ListNode(12)
    d = ListNode(13)
    e = ListNode(14)
    #a.next = b
    b.next = c
    c.next = d
    d.next = e
    e.next = b
    start = Solution().detectCycle(a)
    print(start.val)
    start = Solution().detectCycle(None)
    

