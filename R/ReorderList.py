'''
-Medium-

Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may 
be changed.

Example 1:

Given 1->2->3->4, reorder it to 1->4->2->3.
Example 2:

Given 1->2->3->4->5, reorder it to 1->5->2->4->3.


'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second = slow.next
        slow.next = None      
        # reverse the list starting at second  
        pre, cur, nxt = None, second, None
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt            
        cur1, cur2 = head, pre
        dummy = ListNode(-1)
        cur = dummy        
        while cur1 and cur2:                 
            cur.next = cur1
            cur1 = cur1.next
            cur = cur.next
            cur.next = cur2
            cur2 = cur2.next
            cur = cur.next
        cur.next = cur1 or cur2
        return dummy.next


if __name__=="__main__":
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    x = head
    while x:
       print(x.val)
       x = x.next
    print('===========')
    node = Solution().reorderList(head)
    x = node
    while x:
       print(x.val)
       x = x.next
    print('===========')

