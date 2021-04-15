'''

-Medium-

You are given a doubly linked list which in addition to the next and previous pointers, it could have a 
child pointer, which may or may not point to a separate doubly linked list. These child lists may have 
one or more children of their own, and so on, to produce a multilevel data structure, as shown in the 
example below.

Flatten the list so that all the nodes appear in a single-level, doubly linked list. You are given the 
head of the first level of the list.

 

Example 1:

Input: head = [1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
Output: [1,2,3,7,8,11,12,9,10,4,5,6]
Explanation:

The multilevel linked list in the input is as follows:



After flattening the multilevel linked list it becomes:


Example 2:

Input: head = [1,2,null,3]
Output: [1,3,2]
Explanation:

The input multilevel linked list is as follows:

  1---2---NULL
  |
  3---NULL
Example 3:

Input: head = []
Output: []
 

How multilevel linked list is represented in test case:

We use the multilevel linked list from Example 1 above:

 1---2---3---4---5---6--NULL
         |
         7---8---9---10--NULL
             |
             11--12--NULL
The serialization of each level is as follows:

[1,2,3,4,5,6,null]
[7,8,9,10,null]
[11,12,null]
To serialize all levels together we will add nulls in each level to signify no node connects to the 
upper node of the previous level. The serialization becomes:

[1,2,3,4,5,6,null]
[null,null,7,8,9,10,null]
[null,11,12,null]
Merging the serialization of each level and removing trailing nulls we obtain:

[1,2,3,4,5,6,null,null,null,7,8,9,10,null,null,11,12]
 

Constraints:

The number of Nodes will not exceed 1000.
1 <= Node.val <= 10^5

'''


# Definition for a Node.
class Node(object):
    def __init__(self, val, prev=None, next=None, child=None):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution(object):
    def flatten(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        dummy = Node(-1)
        dummy.next = head
        #head.prev = dummy
        def helper(node):
            if not node: return None
            cur = node
            prev = cur
            while cur: 
                prev = cur                             
                nxt = cur.next
                if cur.child:            
                   prev.next = cur.child
                   cur.child.prev = prev
                   last = helper(cur.child)
                   cur.child = None 
                   if not nxt:
                       return last
                   last.next = nxt
                   nxt.prev = last
                cur = nxt    
            return prev
        helper(head)
        return dummy.next

if __name__ == "__main__":
    '''
    root = Node(1)
    head = root
    node3, node7, node8 = None, None, None
    for i in range(2,7):
        node = Node(i)
        if i == 3: node3 = node
        root.next = node
        node.prev = root
        root = node
    root = Node(7)
    node7 = root
    for i in range(8,11):
        node = Node(i)
        if i == 8: node8 = node
        root.next = node
        node.prev = root
        root = node
    root = Node(11)
    node11 = root
    node = Node(12)
    root.next = node
    node.prev = root
    node3.child = node7 
    node8.child = node11
    root = Solution().flatten(head)
    cur = root
    while cur:
        print(cur.val, '->', end='')        
        cur = cur.next
    print()
    cur = root
    while cur:
        if cur.prev:
            print(cur.prev.val, '->', end='')        
        else:
            print(cur.val, '->', end='')        
        cur = cur.next
    print()
    '''
    node1 = Node(1)
    head = node1
    node2 = Node(2)
    node3 = Node(3)
    node1.child = node2
    node2.child = node3
    root = Solution().flatten(head)


    


    
    
    

