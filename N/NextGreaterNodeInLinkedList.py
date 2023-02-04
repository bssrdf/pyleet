'''
-Medium-

*Monotonic Queue*

We are given a linked list with head as the first node.  Let's number the nodes in the list: 
node_1, node_2, node_3, ... etc.

Each node may have a next larger value: for node_i, next_larger(node_i) is the node_j.val 
such that j > i, node_j.val > node_i.val, and j is the smallest possible choice.  If such 
a j does not exist, the next larger value is 0.

Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).

Note that in the example inputs (not outputs) below, arrays such as [2,1,5] represent 
the serialization of a linked list with a head node value of 2, second node value of 1, and 
third node value of 5.

 

Example 1:

Input: [2,1,5]
Output: [5,5,0]
Example 2:

Input: [2,7,4,3,5]
Output: [7,0,5,5,0]
Example 3:

Input: [1,7,5,1,9,2,5,1]
Output: [7,9,9,9,0,5,0,0]
 

Note:

1 <= node.val <= 10^9 for each node in the linked list.
The given list has length in the range [0, 10000].

'''
from LinkedList import (ListNode, constructList)
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def nextLargerNodesWrong(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        res = []
        def helper(node):
            if not node:
                return 0
            val = helper(node.next)
            if val == 0: 
                res.append(0)
                return node.val
            else:
                if node.val > val:
                    res.append(0)  
                    return node.val
                else:
                    res.append(val)
                    return val
        helper(head)
        return res[::-1]     

    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """   
        stack = []
        cur = head
        n = 0
        while cur:
            n += 1
            cur = cur.next
        res = [0]*n
        i = 0
        while head:
            if not stack:
                stack.append((head.val, i))
                i += 1
            else:
                while stack and head.val > stack[-1][0]:
                    _, idx = stack.pop()
                    res[idx] = head.val
                stack.append((head.val, i))
                i += 1     
            head = head.next
        return res

            
            

if __name__ == "__main__": 
    head = constructList([2,7,4,3,5])
    print(Solution().nextLargerNodes(head))
    head = constructList([1,7,5,1,9,2,5,1])
    print(Solution().nextLargerNodes(head))
    head = constructList([2,1,5])
    print(Solution().nextLargerNodes(head))
