# -*- coding: utf-8 -*-
"""
Given an array of size n, find the majority element. The majority element is the 
element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist 
in the array.
"""
__author__ = 'Daniel'


class Solution:
    def majorityElement(self, nums):
        """
        Algorithm:
        O(n lgn) sort and take the middle one
        O(n) Moore's Voting Algorithm
        :type nums: list[int]
        :rtype int
        """
        tally={}
        for i in nums:
            if not i in tally:
                tally[i] = 1
            else:
                tally[i] += 1
        num,n=(nums[0],0)
        for i,t in tally.items():
            if t>n:
                num,n=(i,t)
        return num

    def majorityElementMoore(self, nums):
        """
        Algorithm:
        O(n lgn) sort and take the middle one
        O(n) Moore's Voting Algorithm
        :type nums: list[int]
        :rtype int
        """
        candidate = 0
        tally = 1
        for i in range(1, len(nums)):
            if nums[i] == nums[candidate]:
                tally += 1
            else:
                tally -= 1
                if tally==0:
                    candidate = i
                    tally = 1
        return nums[candidate]    


if __name__=="__main__":
    #assert Solution().majorityElement([1, 2, 2, 3, 3, 3, 3]) == 3
    #assert Solution().majorityElement([3, 3, 3, 3, 1, 1, 2]) == 3
    assert Solution().majorityElementMoore([1, 2, 2, 3, 3, 3, 3]) == 3
    assert Solution().majorityElementMoore([3, 3, 3, 3, 1, 1, 2]) == 3
