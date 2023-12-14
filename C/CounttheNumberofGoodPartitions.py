'''

-Hard-

You are given a 0-indexed array nums consisting of positive integers.

A partition of an array into one or more contiguous subarrays is called good if no two subarrays contain the same number.

Return the total number of good partitions of nums.

Since the answer may be large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [1,2,3,4]
Output: 8
Explanation: The 8 possible good partitions are: ([1], [2], [3], [4]), ([1], [2], [3,4]), ([1], [2,3], [4]), ([1], [2,3,4]), ([1,2], [3], [4]), ([1,2], [3,4]), ([1,2,3], [4]), and ([1,2,3,4]).
Example 2:

Input: nums = [1,1,1,1]
Output: 1
Explanation: The only possible good partition is: ([1,1,1,1]).
Example 3:

Input: nums = [1,2,1,3]
Output: 2
Explanation: The 2 possible good partitions are: ([1,2,1], [3]) and ([1,2,1,3]).
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i] <= 109




'''

from typing import List
from math import comb
from functools import cache
import sys
sys.setrecursionlimit(100000)
class Solution:
    def numberOfGoodPartitions(self, nums: List[int]) -> int:
        n, MOD = len(nums), 10**9 + 7
        left, right = {}, {}
        for i in range(n):
            if nums[i] not in left:
                left[nums[i]] = i
        for i in range(n-1, -1, -1):
            if nums[i] not in right:
                right[nums[i]] = i 
        m, i = 0, 0
        while i < n:
            if left[nums[i]] != right[nums[i]]:
                j = right[nums[i]]
                while i < j:
                    if right[nums[i]] > j:
                        j = right[nums[i]]
                    i += 1    
            i += 1        
            m += 1        
        return pow(2, m-1, MOD)    
 
 



if __name__ == "__main__":
    print(Solution().numberOfGoodPartitions(nums = [1,2,3,4])) 
    print(Solution().numberOfGoodPartitions(nums = [1,2,1,3]))
    print(Solution().numberOfGoodPartitions(nums = [1,1,1,1]))
    print(Solution().numberOfGoodPartitions(nums = [1,5,1,5,6]))
    nums = list(range(1, 100001))
    print(Solution().numberOfGoodPartitions(nums = nums))