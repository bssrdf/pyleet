'''
-Medium-

Given a linked list and two values v1 and v2. Swap the two nodes in the linked 
list with values v1 and v2. It's guaranteed there is no duplicate values in the linked list. 
If v1 or v2 does not exist in the given linked list, do nothing.

You should swap the two nodes with values v1 and v2. Do not directly swap the values of the two nodes.

样例
Example 1:

Input: 1->2->3->4->null, v1 = 2, v2 = 4
Output: 1->4->3->2->null
Example 2:

Input: 1->null, v1 = 2, v2 = 1
Output: 1->null


'''
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""
from LinkedList import(ListNode, constructList, printList)
class Solution:
    """
    @param head: a ListNode
    @param v1: An integer
    @param v2: An integer
    @return: a new head of singly-linked list
    """
    def swapNodes(self, head, v1, v2):
        # write your code here
        dummy = ListNode(-1)
        dummy.next = head
        pre, cur = dummy, head
        n1, n2 = None, None
        n1p, n2p = None, None
        n1x, n2x = None, None
        while cur:
            if cur.val == v1:
                n1, n1p, n1x = cur, pre, cur.next
            if cur.val == v2:
                n2, n2p, n2x = cur, pre, cur.next
            pre = cur
            cur = cur.next
        if n1 and n2:
            if n1.next == n2:
                n1p.next = n2
                n2.next = n1
                n1.next = n2x
            elif n2.next == n1:
                n2p.next = n1
                n1.next = n2
                n2.next = n1x
            else:
                n1p.next = n2
                n2.next = n1x
                n2p.next = n1
                n1.next = n2x
        return dummy.next
        
if __name__ == "__main__":
    head = constructList([10, 8, 7, 6, 4, 3])   
    printList(head)         
    res = Solution().swapNodes(head, 7, 8)
    printList(res)         





