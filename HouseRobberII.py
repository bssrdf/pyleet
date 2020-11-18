# -*- coding: utf-8 -*-
"""
Created on Tue Aug 01 01:01:03 2017

@author: merli
"""

'''
: This is an extension of House Robber.

After robbing those houses on that street, the thief has found himself a new
 place for his thievery so that he will not get too much attention. This time,
 all houses at this place are arranged in a circle. That means the first house
 is the neighbor of the last one. Meanwhile, the security system for these 
 houses remain the same as for those in the previous street.

Given a list of non-negative integers representing the amount of money of each
house, determine the maximum amount of money you can rob tonight without
alerting the police.

'''
from typing import List

class Solution(object):
    
    
    def helper(self, nums, lo, hi):
        inc,exl=0,0
        for j in range(lo, hi):
            i=inc
            e=exl
            inc = e+nums[j]
            exl = max(i,e)
        return max(inc,exl)
    
    def rob(self, nums: List[int]) -> int:
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums, 0, len(nums)-1),  
                   self.helper(nums, 1, len(nums)))
   
    
   


if __name__ == "__main__":
    assert Solution().rob([1, 3, 4, 7, 6, 5]) == 15
    