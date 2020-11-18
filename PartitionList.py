'''
Given a linked list and a value x, partition it such that all nodes less than x come 
before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two 
partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        small = ListNode(-1)
        large = ListNode(-1)
        curs, curl, cur = small, large, head        
        while cur:
            if cur.val < x:
                curs.next = cur
                cur = cur.next                
                curs = curs.next 
                curs.next = None
            else:
                curl.next = cur
                cur = cur.next                
                curl = curl.next
                curl.next = None
        curs.next = large.next
        return small.next
         



if __name__ == "__main__":
    node1 = ListNode(1)
    node2 = ListNode(4)
    node3 = ListNode(3)
    node4 = ListNode(2)
    node5 = ListNode(5)
    node6 = ListNode(2)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    node5.next = node6
    head = Solution().partition(node1, 3)
    while head:
        print(head.val)
        head = head.next



