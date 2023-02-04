'''
-Medium-

Given a non-negative integer represented as non-empty a singly linked list of digits, 
plus one to the integer.

You may assume the integer do not contain any leading zero, except the number 0 itself.

The digits are stored such that the most significant digit is at the head of the list.

Example :

Input: [1,2,3]
Output: [1,2,4]

'''

#Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class Solution:
    """
    @param head: the first Node
    @return: the answer after plus one
    """
    def plusOne(self, head):
        # Write your code here
        def helper(node):
            if not node.next:
                node.val += 1
                if node.val > 9:
                    node.val = 0
                    return (1, node)
                else:
                    return (0, node)
            dec, child = helper(node.next)
            node.val += dec
            node.next = child
            if node.val > 9:
                node.val = 0
                return (1, node)
            else:
                return (0, node)
        dec, node = helper(head)
        if dec > 0:
            dummy = ListNode(1)
            node.val = 0
            dummy.next = node
            return dummy
        return node
            




        