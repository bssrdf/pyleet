'''

-Medium-
*Monotonic Stack*

Given an array of numbers, verify whether it is the correct preorder traversal sequence of 
a binary search tree.

You may assume each number in the sequence is unique.

Consider the following binary search tree: 

     5
    / \
   2   6
  / \
 1   3
Example 1:

Input: [5,2,6,1,3]
Output: false
Example 2:

Input: [5,2,1,3,6]
Output: true
Follow up:
Could you do it using only constant space complexity?


'''

from collections import deque

class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        A = preorder
        n = len(preorder)
        stack = []
        for i in range(n):
            while stack and A[stack[-1]] < A[i]:
                stack.pop()
            stack.append(i)
        return len(stack) == 1

    
    def verifyPreorder4(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        # eg: 8 6 4 2 1 3 5 7 10 9 11
        low = float('-inf')
        stack = []
        for x in preorder:
            if x < low:
                return False
            
            while stack and stack[-1] < x:
                low = stack.pop()

            stack.append(x)
        return True

    def verifyPreorderO1Space(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        idx = [0]  
        n = len(preorder)
        def helper(L, R):
            if idx[0] >= n: return
            val = preorder[idx[0]]
            if val < L or val > R: return
            idx[0] += 1
            helper(L, val)
            helper(val, R)
        helper(-float('inf'), float('inf'))
        return idx[0] == n


    


if __name__ == "__main__": 
    print(Solution().verifyPreorder([5,2,6,1,3]))
    print(Solution().verifyPreorder4([5,2,6,1,3]))
    print(Solution().verifyPreorderO1Space([5,2,6,1,3]))
    print(Solution().verifyPreorder([5,2,1,3,6]))
    print(Solution().verifyPreorder([1,2]))
    print(Solution().verifyPreorder([1,3,2]))
    print(Solution().verifyPreorder4([1,3,2]))
    print(Solution().verifyPreorderO1Space([1,3,2]))
