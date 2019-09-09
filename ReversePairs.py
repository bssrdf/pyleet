'''
Given an array nums, we call (i, j) an important reverse pair if i < j 
and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.

Example1:

Input: [1,3,2,3,1]
Output: 2
Example2:

Input: [2,4,3,5,1]
Output: 3
Note:
The length of the given array will not exceed 50,000.
All the numbers in the input array are in the range of 32-bit integer.


'''

from collections import deque

class Solution(object):    


    def reversePairs(self, nums):
        count = [0]
        def merge(nums):
            if len(nums) <= 1: return nums
            
            left, right = merge(nums[:len(nums)//2]), merge(nums[len(nums)//2:])
            l = r = 0
            
            while l < len(left) and r < len(right):
                if left[l] <= 2 * right[r]:
                    l += 1
                else:
                    count[0] += len(left) - l
                    r += 1
            return sorted(left+right)

        merge(nums)
        return count[0]
        



print(Solution().reversePairs([1,3,2,3,1]))
print(Solution().reversePairs([2,4,3,5,1]))