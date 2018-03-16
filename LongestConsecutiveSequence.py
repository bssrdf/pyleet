# -*- coding: utf-8 -*-
"""
Created on Thu Mar 15 20:24:23 2018

@author: merli
"""

class Solution:
    def longestConsecutive(self, nums):
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                longest_streak = max(longest_streak, current_streak)

        return longest_streak


if __name__ == "__main__":
    candies = [100, 4, 200,  1, 2, 3]
    print(candies)
    print(Solution().longestConsecutive(candies))

    
    
