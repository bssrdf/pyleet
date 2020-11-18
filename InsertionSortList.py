'''
Sort a linked list using insertion sort.



Algorithm of Insertion Sort:

Insertion sort iterates, consuming one input element each repetition, and growing a sorted 
output list.
At each iteration, insertion sort removes one element from the input data, finds the 
location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.

Example 1:

Input: 4->2->1->3
Output: 1->2->3->4
Example 2:

Input: -1->5->3->4->0
Output: -1->0->3->4->5

'''

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy = ListNode(-1)        
        while head:
            t = head.next
            cur = dummy
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            head.next = cur.next
            cur.next = head
            head = t            
        return dummy.next



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
    root = Solution().insertionSortList(root)
    while root:
        print(root.val)
        root = root.next