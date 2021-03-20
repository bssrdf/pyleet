'''
-Medium-

Given a (singly) linked list with head node root, write a function to split the linked list into k consecutive linked list "parts".

The length of each part should be as equal as possible: no two parts should have a size differing by more than 1. This may lead to some parts being null.

The parts should be in order of occurrence in the input list, and parts occurring earlier should always have a size greater than or equal parts occurring later.

Return a List of ListNode's representing the linked list parts that are formed.

Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
Example 1:
Input:
root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The input and each element of the output are ListNodes, not arrays.
For example, the input root has root.val = 1, root.next.val = 2, \root.next.next.val = 3, and root.next.next.next = null.
The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null, but it's string representation as a ListNode is [].
Example 2:
Input: 
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1, and earlier parts are a larger size than the later parts.
Note:

The length of root will be in the range [0, 1000].
Each value of a node in the input will be an integer in the range [0, 999].
k will be an integer in the range [1, 50].

'''

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """        
        if not root: return [ None for _ in range(k)]
        n, cur = 0, root
        while cur:
            n += 1
            cur = cur.next
        nums = [n//k]*k
        for i in range(n%k):
            nums[i] += 1
        cur, res, i = root, [], 0
        while i < k:
            j, prev = 0, cur
            res.append(cur)
            while j < nums[i]:
                prev, cur = cur, cur.next                
                if not cur: break                
                j += 1
            if j < nums[i]: break
            prev.next = None
            i += 1
        while i < k-1:
            res.append(None)
            i += 1    
        return res    
        
    def splitListToPartsCleanCode(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """        
        # Count the length of the linked list
        curr, length = root, 0
        while curr:
            curr, length = curr.next, length + 1
        # Determine the length of each chunk
        chunk_size, longer_chunks = length // k, length % k
        res = [chunk_size + 1] * longer_chunks + [chunk_size] * (k - longer_chunks)
        # Split up the list
        prev, curr = None, root
        for index, num in enumerate(res):
            if prev:
                prev.next = None
            res[index] = curr
            for i in range(num):
                prev, curr = curr, curr.next
        return res


if __name__ == "__main__":
    dummy = ListNode(0)
    cur = dummy
    for i in range(1, 11):
        node = ListNode(i)
        cur.next = node
        cur = cur.next
    root = dummy.next
    nodes = Solution().splitListToParts(root, 3)
    for i,node in enumerate(nodes):
        if node: print(i, node.val)
        else: print(i, 'None')
    

    dummy = ListNode(0)
    cur = dummy
    for i in range(1, 4):
        node = ListNode(i)
        cur.next = node
        cur = cur.next
    root = dummy.next
    nodes = Solution().splitListToParts(root, 5)
    
    for i,node in enumerate(nodes):
        if node: print(i, node.val)
        else: print(i, 'None')



