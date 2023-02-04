'''
A linked list is given such that each node contains an additional random 
pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. 
Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random 
pointer points to, or null if it does not point to any node.

'''

"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        def copyList(node, cache):
            if not node:
                return None
            if node in cache:
                return cache[node]
            clone = Node(node.val, None, None)
            cache[node] = clone
            clone.next = copyList(node.next, cache)
            clone.random = copyList(node.random, cache)
            return clone
        return copyList(head, {})

