'''

-Medium-

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the 
beginning and the kth node from the end (the list is 1-indexed).

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]
Example 2:

Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
Example 3:

Input: head = [1], k = 1
Output: [1]
Example 4:

Input: head = [1,2], k = 1
Output: [2,1]
Example 5:

Input: head = [1,2,3], k = 2
Output: [1,2,3]
 

Constraints:

The number of nodes in the list is n.
1 <= k <= n <= 10^5
0 <= Node.val <= 100

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 54%, 48%
        arr = []
        cur = head
        while cur:
            arr.append(cur.val)
            cur = cur.next
        arr[k-1], arr[-k] = arr[-k], arr[k-1]
        cur, i = head, 0
        while cur:
            cur.val = arr[i]
            i, cur = i+1, cur.next
        return head

    def swapNodesTwoPointers(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        # 98%, 33%
        dummy = ListNode(-1)
        dummy.next = head
        fast, slow = dummy, dummy
        for _ in range(k):
            fast = fast.next
        cur = fast
        while fast:
            fast = fast.next
            slow = slow.next
        cur.val, slow.val = slow.val, cur.val
        return dummy.next

    # 22%
    def swapNodesRecursion(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        self.prev = -1
        self.next = -1
        def helper(node, lev):
            if not node: return 1
            if lev == k: self.prev = node
            m = helper(node.next, lev+1)
            if m == k: self.next = node
            return m+1
        helper(head, 1)
        t = self.prev.val
        self.prev.val = self.next.val
        self.next.val = t
        return head
        
