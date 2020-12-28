'''

-Medium-

*Reservoir sampling*


Given a singly linked list, return a random node's value from the linked list. Each 
node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you? Could 
you solve this efficiently without using extra space?

Example:

// Init a singly linked list [1,2,3].
ListNode head = new ListNode(1);
head.next = new ListNode(2);
head.next.next = new ListNode(3);
Solution solution = new Solution(head);

// getRandom() should return either 1, 2, or 3 randomly. Each element should have 
equal probability of returning.
solution.getRandom();

'''

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from random import randint

class Solution(object):

    def __init__(self, head):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        :type head: ListNode
        """
        self.head = head

    def getRandom(self):
        """
        Returns a random node's value.
        :rtype: int
        """
        count = 0
        cur = self.head
        #res = cur.val
        while cur:
            count += 1
            chance = randint(1,count)
            if chance == 1:
                res = cur.val
            cur = cur.next
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()