'''
Given a sorted linked list, delete all nodes that have duplicate numbers, 
leaving only distinct numbers from the original list.

Return the linked list sorted as well.

Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5
Example 2:

Input: 1->1->1->2->3
Output: 2->3


'''

from LinkedList import (ListNode, constructList, printList)


class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = ListNode()
        node.next = head
        res = node
        pre = node
        while pre.next is not None:
            cur = pre.next
            value = cur.val
            dup = 0
            while cur.next is not None and cur.next.val == value:
                dup += 1
                cur = cur.next
            if dup > 0:
                pre.next = cur.next
            else:
                pre = pre.next    
        return res.next  
    


if __name__ == "__main__":
     head = constructList([1, 2, 3, 3, 4, 4, 5, 5, 5])   
     printList(head)
     head = Solution().deleteDuplicates(head) 
     printList(head)
     head = constructList([1, 1, 1, 2, 3])   
     printList(head)
     head = Solution().deleteDuplicates(head) 
     printList(head)