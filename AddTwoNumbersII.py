'''
-Medium-

You are given two non-empty linked lists representing two non-negative 
integers. The most significant digit comes first and each of their nodes 
contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except 
the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the 
lists is not allowed.

Example:

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        s1, s2 = [], []
        head = l1
        while head:
            s1.append(head.val)
            head = head.next
        head = l2
        while head:
            s2.append(head.val)
            head = head.next
        b = 0
        last = None
        def increment(num, nxt):            
            if num >= 10:                
                return  ListNode(num-10, nxt), 1 
            else:                
                return  ListNode(num, nxt), 0
        while s1 and s2:
            num = s1.pop()+s2.pop()+b
            node, b = increment(num, last)            
            last = node
        s = s1 or s2
        while s:
            num = s.pop()+b
            node, b = increment(num, last)                        
            last = node
        if b > 0:
           node = ListNode(b, last)
           last = node 
        return last
            









if __name__ == "__main__":
    l1 = ListNode(7)
    l1.next  = ListNode(2)
    l1.next.next  = ListNode(4)
    l1.next.next.next  = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    l3 = Solution().addTwoNumbers(l1, l2)
    while l3:
        print(l3.val)
        l3 = l3.next

