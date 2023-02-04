'''
-Medium-

You are given two non-empty linked lists representing two non-negative 
integers. The digits are stored in reverse order, and each of their 
nodes contains a single digit. Add the two numbers and return the 
sum as a linked list.

You may assume the two numbers do not contain any leading zero, 
except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not 
have leading zeros.

'''

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
        dummy = ListNode(-1)
        cur = dummy
        p1 = 0
        while l1 and l2:
            sums = l1.val + l2.val + p1 
            if sums >= 10:
                sums -= 10
                p1 = 1
            else:
                p1 = 0
            cur.next = ListNode(sums)
            cur = cur.next
            l1, l2 = l1.next, l2.next
        l = l1 or l2
        while l:
            sums = l.val + p1 
            if sums >= 10:
                sums -= 10
                p1 = 1
            else:
                p1 = 0
            cur.next = ListNode(sums)
            cur = cur.next
            l = l.next
        if p1 > 0:
            cur.next = ListNode(1)

        return dummy.next

if __name__ == "__main__":
    l1 = ListNode(9)
    l1.next  = ListNode(9)
    l1.next.next  = ListNode(9)
    l1.next.next.next  = ListNode(9)
    l1.next.next.next.next  = ListNode(9)
    l1.next.next.next.next.next  = ListNode(9)
    l1.next.next.next.next.next.next  = ListNode(9)

    l2 = ListNode(9)
    l2.next  = ListNode(9)
    l2.next.next  = ListNode(9)
    l2.next.next.next  = ListNode(9)
    
    l3 = Solution().addTwoNumbers(l1, l2)
    while l3:
        print(l3.val)
        l3 = l3.next