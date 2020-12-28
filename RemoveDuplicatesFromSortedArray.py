# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 14:20:26 2017

Given a sorted array, remove the duplicates in place such that each element 
appear only once and return the new length.

Do not allocate extra space for another array, you must do this in place 
with constant memory.

For example,
Given input array nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums 
being 1 and 2 respectively. It doesn't
matter what you leave beyond the new length.

@author: merli
"""



class Solution(object):
        
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0        
        for num in nums:
            if i < 1 or num > nums[i - 1]:
                nums[i] = num
                i += 1        
        return i

      
        
        
if __name__ == "__main__":
    print(Solution().removeDuplicates([1,1,1,1,2,2,3,3,3,6,7,7]))
    print(Solution().removeDuplicates([1,1,1,1]))
    print(Solution().removeDuplicates([1]))
