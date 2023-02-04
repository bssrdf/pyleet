'''

-Easy-

Given the head of a singly linked list, return true if it is a palindrome.



Example 1:


Input: head = [1,2,2,1]
Output: true
Example 2:


Input: head = [1,2]
Output: false
 

Constraints:

The number of nodes in the list is in the range [1, 105].
0 <= Node.val <= 9
 

Follow up: Could you do it in O(n) time and O(1) space?


'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next: return True
        prev, slow, fast = None, head, head
        while fast and fast.next:
            prev = slow 
            slow = slow.next            
            fast = fast.next.next
        prev.next = None
        prev, cur = None, slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        slow, fast = head, prev    
        while slow and fast:
            if slow.val != fast.val: return False
            slow = slow.next
            fast = fast.next
        return True

if __name__ == "__main__":    
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(2)
    e = ListNode(1)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    x = a 
    while x is not None:
       print(str(x.val)+'->',end='')
       x = x.next
    print('\n===========\n')
    print(Solution().isPalindromeFast(a))
    
        



