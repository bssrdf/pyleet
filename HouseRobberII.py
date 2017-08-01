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

class Solution(object):
    def rob(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        F0 = nums[0]
        F1 = max(nums[0], nums[1])
        F2 = max(F0, F1)
        for i in range(2, len(nums)):
            F2 = max(nums[i]+F0, F1)         
            F0 = F1
            F1 = F2
        return F2
    
   


if __name__ == "__main__":
    assert Solution().rob([1, 3, 4, 7, 6, 5]) == 15
    