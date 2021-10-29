'''
-Medium-

A ramp in an integer array nums is a pair (i, j) for which i < j and 
nums[i] <= nums[j]. The width of such a ramp is j - i.

Given an integer array nums, return the maximum width of a ramp in nums. 
If there is no ramp in nums, return 0.

 

Example 1:

Input: nums = [6,0,8,2,1,5]
Output: 4
Explanation: The maximum width ramp is achieved at (i, j) = (1, 5): nums[1] = 0 and nums[5] = 5.
Example 2:

Input: nums = [9,8,1,0,1,9,4,0,4,1]
Output: 7
Explanation: The maximum width ramp is achieved at (i, j) = (2, 9): nums[2] = 1 and nums[9] = 1.
 

Constraints:

2 <= nums.length <= 5 * 10^4
0 <= nums[i] <= 5 * 10^4


'''
from typing import List

class Solution:
    def maxWidthRamp(self, nums: List[int]) -> int:
        '''
        stack, res = [], 0
        for i in range(len(nums)):
            while stack and nums[stack[-1]] > nums[i]:
                #res = max(res, i-stack[-1])
                stack.pop()
            if stack: 
                res = max(res, i-stack[0])                
            stack.append(i)
        return res

        res, n = 0, len(nums)
        indx = [-1]*n 
        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] >= nums[i]:
                stack.pop() 
            if stack:
                #indx[i] = stack[-1]-1
                res = max(res, stack[0]-i) 
            else:
                res = max(res, n-i) 
            stack.append(i) 
        return res
        '''
        A = nums
        s = []
        res = 0
        for i, a in enumerate(A):
            if not s or A[s[-1]] > a:
                s.append(i)
        print(s)  
        for j in range(len(A))[::-1]:
            while s and A[s[-1]] <= A[j]:
                res = max(res, j - s.pop())
        return res
        

if __name__ == "__main__":
    print(Solution().maxWidthRamp([6,0,8,2,1,5]))
    print(Solution().maxWidthRamp([9,8,1,0,1,9,4,0,4,1]))