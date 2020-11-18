'''
Medium

*Merge Sort*

Given the head of a linked list, return the list after sorting it in ascending order.

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant 
space)?
Example 1:


Input: head = [4,2,1,3]
Output: [1,2,3,4]
Example 2:


Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is in the range [0, 5 * 104].
-10^5 <= Node.val <= 10^5

'''

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):

    def merge(self, l, r):
        if not l or not r:
            return l or r
        dummy = p = ListNode(0)
        while l and r:
            if l.val < r.val:
                p.next = l
                l = l.next
            else:
                p.next = r
                r = r.next
            p = p.next
        p.next = l or r
        return dummy.next
        

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next : return head
        pre = fast = slow = head
        while fast and fast.next:
            pre = slow
            fast = fast.next.next
            slow = slow.next        
        pre.next = None
        l, r = self.sortList(head), self.sortList(slow)        
        return self.merge(l, r)
        

if __name__ == "__main__":
    root = ListNode(4)
    five = ListNode(3)
    three = ListNode(2)
    four = ListNode(1)
    zero = ListNode(0)
    root.next = five
    five.next = three
    three.next = four
    #four.next = zero
    root = Solution().sortList(root)
    while root:
        print(root.val)
        root = root.next



