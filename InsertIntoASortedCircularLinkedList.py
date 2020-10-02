'''
Given a node from a Circular Linked List which is sorted in ascending 
order, write a function to insert a value insertVal into the list such 
that it remains a sorted circular list. The given node can be a reference
 to any single node in the list, and may not be necessarily the smallest 
 value in the circular list.

If there are multiple suitable places for insertion, you may choose any 
place to insert the new value. After the insertion, the circular list 
should remain sorted.

If the list is empty (i.e., given node is null), you should create a new 
single circular list and return the reference to that single node. 
Otherwise, you should return the original given node.
'''
class Node(object):

    def __init__(self, value, next = None):
        self.val = value
        self.next = next

class Solution(object):

    def insert(self, head, insertVal):
        '''
        :type head: Node
        :type insertVal: int
        :rtype: Node
        '''
        if not head:
            head = Node(insertVal)
            head.next = head
            return head
        pre, cur = head, head.next
        while cur != head:
            if pre.val <= insertVal <= cur.val:
                break
            if pre.val > cur.val and (insertVal >= pre.val or 
               insertVal <= cur.val):
               break
            pre = cur
            cur = cur.next
        pre.next = Node(insertVal, cur)        
        return head

if __name__=="__main__":
    h = head = Node(3)
    head.next = Node(4)
    head = head.next
    head.next = Node(1)
    head = head.next
    head.next = h
    pre, cur = h, h.next     
    while cur != h:
        print(pre.val)
        pre = cur
        cur = cur.next
    print(pre.val)
    print('======================')
    head = Solution().insert(h, 2)
    pre, cur = head, head.next
    while cur != head:
        print(pre.val)
        pre = cur
        cur = pre.next
    print(pre.val)
    print('======================')
    head = Solution().insert(head, 5)
    pre, cur = head, head.next
    while cur != head:
        print(pre.val)
        pre = cur
        cur = pre.next
    print(pre.val)
