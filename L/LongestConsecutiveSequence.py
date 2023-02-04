# -*- coding: utf-8 -*-
"""
-Medium-
*Union Find*
*Set*

Created on Thu Mar 15 20:24:23 2018
   
Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length: 4.

Your algorithm should run in O(n) complexity.

Constraints:

0 <= nums.length <= 10^5
-10^9 <= nums[i] <= 10^9

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


    def longestConsecutiveUF(self, nums):
        self._parents = {}
        self._ranks = {}
        for t in nums:
            self._parents.setdefault(t, t)            
            self._ranks[t] = 1
        for i in nums:
            if i-1 in self._parents:
                self.union(i, i-1)
            if i+1 in self._parents:
                self.union(i, i+1)
        return max(self._ranks.values()) if nums else 0 

    def find(self, u):
        while u != self._parents[u]:
            self._parents[u] = self._parents[self._parents[u]]
            u = self._parents[u]
        return u

    def union(self, u, v):
        pu, pv = self.find(u), self.find(v)
        if pu == pv: return False
        if self._ranks[pu] < self._ranks[pv]:
            self._parents[pu] = pv
            self._ranks[pv] += self._ranks[pu]
        else:
            self._parents[pv] = pu
            self._ranks[pu] += self._ranks[pv]
        return True

if __name__ == "__main__":
    candies = [100, 4, 200,  1, 2, 3]
    print(candies)
    print(Solution().longestConsecutive(candies))
    print(Solution().longestConsecutiveUF(candies))

    
    
