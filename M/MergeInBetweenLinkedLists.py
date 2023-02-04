'''
-Medium-
You are given two linked lists: list1 and list2 of sizes n and m respectively.

Remove list1's nodes from the ath node to the bth node, and put list2 in their place.

The blue edges and nodes in the following figure incidate the result:


Build the result list and return its head.

 

Example 1:


Input: list1 = [0,1,2,3,4,5], a = 3, b = 4, list2 = [1000000,1000001,1000002]
Output: [0,1,2,1000000,1000001,1000002,5]
Explanation: We remove the nodes 3 and 4 and put the entire list2 in their place. The blue 
edges and nodes in the above figure indicate the result.
Example 2:


Input: list1 = [0,1,2,3,4,5,6], a = 2, b = 5, list2 = [1000000,1000001,1000002,1000003,1000004]
Output: [0,1,1000000,1000001,1000002,1000003,1000004,6]
Explanation: The blue edges and nodes in the above figure indicate the result.
 

Constraints:

3 <= list1.length <= 10^4
1 <= a <= b < list1.length - 1
1 <= list2.length <= 10^4

'''
from LinkedList import (ListNode, constructList,printList)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeInBetween(self, list1, a, b, list2):
        """
        :type list1: ListNode
        :type a: int
        :type b: int
        :type list2: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = list1
        cur = dummy
        cnt, a, b = 0, a+1, b+2
        tail1, head1 = None, None 
        while cur:
            pre = cur
            cur = cur.next
            cnt += 1
            if cnt == a: tail1 = pre
            if cnt == b: 
                head1 = cur
                pre.next = None
                break
        cur = list2
        while cur.next:
             cur = cur.next    
        tail1.next = list2
        cur.next = head1
        return dummy.next
        
            


if __name__ == "__main__":
    head1 = constructList([0,1,2,3,4,5])
    head2 = constructList([1000000,1000001,1000002])
    head = Solution().mergeInBetween(head1, 3,4, head2)
    printList(head)
