'''
-Medium-

Given the head of a linked list, find all the values that appear more than once in the 
list and delete the nodes that have any of those values.

Return the linked list after the deletions.

 

Example 1:


Input: head = [1,2,3,2]
Output: [1,3]
Explanation: 2 appears twice in the linked list, so all 2's should be deleted. After deleting all 2's, we are left with [1,3].
Example 2:


Input: head = [2,1,1,2]
Output: []
Explanation: 2 and 1 both appear twice. All the elements should be deleted.
Example 3:


Input: head = [3,2,2,1,3,2,4]
Output: [1,4]
Explanation: 3 appears twice and 2 appears three times. After deleting all 3's and 2's, we are left with [1,4].
 

Constraints:

The number of nodes in the list is in the range [1, 10^5]
1 <= Node.val <= 10^5



'''

from collections import defaultdict
from typing import List
from LinkedList import (ListNode, constructList, printList)

class Solution(object):
    def removeDuplicates(self, head):
        m = defaultdict(int)
        dummy = ListNode(-1)
        dummy.next = head
        cur = head
        while cur:
            m[cur.val] += 1
            cur = cur.next
        pre = dummy
        cur = head 
        while cur:
            if m[cur.val] == 1:
                pre.next = cur
                pre = cur
            cur = cur.next    
        pre.next = None
        return dummy.next    

    

if __name__ == "__main__":
    head = constructList([3,2,2,1,3,2,4])  
    printList(head)
    head = Solution().removeDuplicates(head)
    printList(head)

    head = constructList([1,2,3,2])  
    printList(head)
    head = Solution().removeDuplicates(head)
    printList(head)

    head = constructList([2,1,1,2])  
    printList(head)
    head = Solution().removeDuplicates(head)
    printList(head)

