'''

-Hard-

Given an array nums of positive integers, return the longest possible length of 
an array prefix of nums, such that it is possible to remove exactly one element 
from this prefix so that every number that has appeared in it will have the same 
number of occurrences.

If after removing one element there are no remaining elements, it's still considered 
that every appeared number has the same number of ocurrences (0).

 

Example 1:

Input: nums = [2,2,1,1,5,3,3,5]
Output: 7
Explanation: For the subarray [2,2,1,1,5,3,3] of length 7, if we remove nums[4] = 5, we will get [2,2,1,1,3,3], so that each number will appear exactly twice.
Example 2:

Input: nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]
Output: 13
 

Constraints:

2 <= nums.length <= 10^5
1 <= nums[i] <= 10^5


'''
from typing import List
import collections

class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        # cnt records the occurence of each num, freq records the frequence of number of 
        # occurences. max_F is the largest frequence.
        cnt,freq,maxF,res = collections.defaultdict(int), collections.defaultdict(int),0,0
        for i,num in enumerate(nums):
            cnt[num] += 1
            freq[cnt[num]-1] -= 1
            freq[cnt[num]] += 1
            maxF = max(maxF,cnt[num])
            if (maxF*freq[maxF] == i              # all elements appear max_F times, except one appears once.  
               or (maxF-1)*(freq[maxF-1]+1) == i  # all elements appear max_F-1 times, except one appears max_F.
               or maxF == 1): # all elements appear exact once. 
                res = i + 1
        return res


if __name__ == "__main__":
    print(Solution().maxEqualFreq([2,2,1,1,5,3,3,5]))
    print(Solution().maxEqualFreq([1,1,1,2,2,2,3,3,3,4,4,4,5]))
