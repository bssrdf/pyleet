# -*- coding: utf-8 -*0
"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times. The algorithm should run in 
linear time and in O(1) space.
"""
__author__ = 'Daniel'
from collections import defaultdict


class Solution:
    def majorityElement(self, nums):
        """
        Since majority elements appears more than ⌊ n/3 ⌋ times, there are at most 2 majority number
        :type nums: list[int]
        :rtype: list[int]
        """
        return 1

    def majorityElementMoore(self, nums):
        """
        Algorithm:
        O(n lgn) sort and take the middle one
        O(n) Moore's Voting Algorithm
        :type nums: list[int]
        :rtype int
        """
        candidates = []
        candidate1 = 0
        candidate2 = 1
        tally1 = tally2 = 1
        for i in range(2, len(nums)):
            if nums[i] == nums[candidate1]:
                tally1 += 1
            elif nums[i] == nums[candidate2]:
                tally2 += 1
            else:
                if tally1 > 0:
                    tally1 -= 1
                    if tally1 == 0:
                        candidate1 = i
                        tally1 = 1
                elif tally2 > 0:
                    tally2 -= 1
                    if tally2==0:
                        candidate2 = i
                        tally2 = 1
        tally1 = tally2 = 0
        for i in nums:
            if i == nums[candidate1]:
                tally1 += 1
            if i == nums[candidate2]:
                tally2 += 1
        if tally1 > len(nums)/3:
            candidates.append(nums[candidate1])
        if tally2 > len(nums)/3:
            candidates.append(nums[candidate2])
        return candidates 

if __name__=="__main__":
    #assert Solution().majorityElement([1, 2, 2, 3, 3, 3, 3]) == 3
    #assert Solution().majorityElement([3, 3, 3, 3, 1, 1, 2]) == 3
    #assert Solution().majorityElementMoore([1, 2, 2, 3, 3, 3, 3]) == 3
    print Solution().majorityElementMoore([3, 3, 3, 1, 1, 1, 2]) 
    print Solution().majorityElementMoore([3, 3, 3, 1, 5, 8, 2]) 
