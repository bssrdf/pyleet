'''
-Medium-

Given the head of a singly linked list and two integers left and right where 
left <= right, reverse the nodes of the list from position left to position right, 
and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5], left = 2, right = 4
Output: [1,4,3,2,5]
Example 2:

Input: head = [5], left = 1, right = 1
Output: [5]
 

Constraints:

The number of nodes in the list is n.
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n


'''

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        pre, cur = dummy, head
        cnt = 0
        while cur:
            cnt += 1
            if cnt == left: break
            pre = cur
            cur = cur.next
        for _ in range(left, right):
            nxt = cur.next
            cur.next = nxt.next
            nxt.next = pre.next
            pre.next = nxt
        return dummy.next

    def reverseListBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        pre, prev, cur = dummy, None, head
        for _ in range(left-1):    
            pre = cur
            cur = cur.next
        tail = cur
        for _ in range(left, right+1):
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        pre.next = prev
        tail.next = cur    
        return dummy.next    

if __name__ == "__main__":
    a = ListNode(1)
    b = ListNode(2)
    c = ListNode(3)
    d = ListNode(4)
    e = ListNode(5)
    a.next = b
    b.next = c
    c.next = d
    d.next = e
    x = a 
    while x is not None:
       print(str(x.val)+'->',end='')
       x = x.next
    print('\n===========\n')
    #e=Solution().reverseBetween(a, 2, 4)
    e=Solution().reverseListBetween(a, 2, 4)
    x = e 
    while x is not None:
       print(str(x.val)+'->',end='')
       x = x.next
    print('\n=========')
    c = ListNode(3)
    e = ListNode(5)
    c.next = e
    x = c
    while x:
       print(str(x.val)+'->',end='')
       x = x.next
    print('\n===========\n')   
    #x = Solution().reverseBetween(c, 1, 2)
    x = Solution().reverseListBetween(c, 1, 2)
    while x is not None:
       print(str(x.val)+'->',end='')
       x = x.next
    print('\n=========')

    e = ListNode(5)
    x = Solution().reverseListBetween(e, 1, 1)
    while x is not None:
       print(str(x.val)+'->',end='')
       x = x.next
    print('\n=========')
     

