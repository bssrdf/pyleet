'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, you should return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

Subscribe to see which companies asked this question
'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = ListNode(-1) # sentinel node
        prev.next = head
        temp = prev
        while temp.next and temp.next.next:
            node1 = temp.next
            node2 = temp.next.next
            temp.next = node2
            node1.next = node2.next
            node2.next = node1
            temp = temp.next.next
        return prev.next
    
    def swapPairs2(self, head):
        # write your code here
        dummy = ListNode(-1)
        dummy.next = head
        pre, cur, nxt = dummy, head, head.next
        while nxt:
            t = nxt.next
            nxt.next = cur
            cur.next = t            
            pre.next = nxt            
            pre = cur
            cur = cur.next
            if not cur: break
            nxt = cur.next
        return dummy.next
