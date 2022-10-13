'''

-Easy-
*Greedy*
*Sorting*


Given an integer array nums, return the largest perimeter of a triangle with a non-zero area, formed from three of these lengths. If it is impossible to form any triangle of a non-zero area, return 0.

 

Example 1:

Input: nums = [2,1,2]
Output: 5
Example 2:

Input: nums = [1,2,1]
Output: 0
 

Constraints:

3 <= nums.length <= 104
1 <= nums[i] <= 106


'''
from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        # I think there's no doubt if the last three numbers in 
        # the sorted array is valid, they should form the biggest answer.
        # But if they don't, that means nums[i] + nums[i+1] <= nums[i+2]
        # From this point, if we dont give up on nums[i+2], since nums[i] and nums[i+1] 
        # are the largest two numbers in the remaining, there's no way we can find another 
        # two numbers that the sum is greater than nums[i+2]. So we must move on 
        # to nums[i-1], nums[i] and nums[i+1] since they are the biggest three number 
        # that might be valid. So the answer should always be three consecutive numbers.
        A = sorted(nums, reverse=True)
        for i in range(len(A)-2):
            if A[i] < A[i+1] + A[i+2]:
                return  A[i] + A[i+1] + A[i+2]
        return 0    

        