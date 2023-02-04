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
        if not nums:
            return []
        # initially set candidates to two different numbers    
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for n in nums:
            # if we get the same number as either candidate, increment the counter 
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            # if either counter becomes zero, reset it to 1 for a new candidate     
            elif count1 == 0:
                candidate1, count1 = n, 1
            elif count2 == 0:
                candidate2, count2 = n, 1
            # if the given # is differnt from either candidate, decrement both counters
            else:
                count1, count2 = count1 - 1, count2 - 1
        # finally check both candidates to see if they are truly majority    
        return [n for n in (candidate1, candidate2)
                if nums.count(n) > len(nums) // 3]

if __name__=="__main__":
    #assert Solution().majorityElement([1, 2, 2, 3, 3, 3, 3]) == 3
    #assert Solution().majorityElement([3, 3, 3, 3, 1, 1, 2]) == 3
    #assert Solution().majorityElementMoore([1, 2, 2, 3, 3, 3, 3]) == 3
    #print(Solution().majorityElementMoore([3, 3, 3, 1, 1, 1, 2]))
    #print(Solution().majorityElementMoore([3, 3, 3, 1, 5, 8, 2])) 
    print(Solution().majorityElementMoore([1,2,1,1,1,3,3,4,3,3,3,4,4,4]))
