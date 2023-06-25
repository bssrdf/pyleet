'''

-Medium-

You are given a binary array nums.

A subarray of an array is good if it contains exactly one element with the value 1.

Return an integer denoting the number of ways to split the array nums into good subarrays. As the number may be too large, return it modulo 109 + 7.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [0,1,0,0,1]
Output: 3
Explanation: There are 3 ways to split nums into good subarrays:
- [0,1] [0,0,1]
- [0,1,0] [0,1]
- [0,1,0,0] [1]
Example 2:

Input: nums = [0,1,0]
Output: 1
Explanation: There is 1 way to split nums into good subarrays:
- [0,1,0]
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 1


'''
from typing import List


class Solution:
    def numberOfGoodSubarraySplits(self, nums: List[int]) -> int:
        n = len(nums)
        lastP = -1
        dp = [0]*(n+1)
        MOD = 10**9 + 7
        for i in range(1,n+1):
            if nums[i-1] == 0:
                dp[i] = dp[i-1]
            else:
                if lastP == -1:
                    dp[i] = 1
                else: 
                    dp[i] = dp[lastP+1]*(i-1-lastP)
                dp[i] %= MOD
                lastP = i-1 
        return dp[n]         



if __name__ == "__main__":
    print(Solution().numberOfGoodSubarraySplits(nums = [0,1,0,0,1]))
    print(Solution().numberOfGoodSubarraySplits(nums = [0,1,0]))
    print(Solution().numberOfGoodSubarraySplits(nums = [1,0,0,0,0,0,1,0,1]))
          