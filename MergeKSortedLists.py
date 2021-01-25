'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

Example:

Input:
[
  1->4->5,
  1->3->4,
  2->6
]
Output: 1->1->2->3->4->4->5->6

'''

from heapq import *
# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None
     def __lt__(self, other):
         return (self.val < other.val)

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = temp = ListNode(-1)
        pq = []
        for lis in lists:
          if lis: heappush(pq, lis)
        while pq:
            node = heappop(pq)
            if node.next:
                heappush(pq, node.next)
            temp.next = node
            temp = temp.next
        return head.next  

if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next= ListNode(5)
    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next= ListNode(4)
    l3 = ListNode(2)
    l3.next = ListNode(6)
    l = Solution().mergeKLists([l1, l2, l3])
    head = l
    while head:
      print(head.val)
      head = head.next
    l = Solution().mergeKLists([])
    print(l)


