'''
-Medium-


The alternating sum of a 0-indexed array is defined as the sum of the elements 
at even indices minus the sum of the elements at odd indices.

For example, the alternating sum of [4,2,5,3] is (4 + 5) - (2 + 3) = 4.
Given an array nums, return the maximum alternating sum of any subsequence of nums 
(after reindexing the elements of the subsequence).

A subsequence of an array is a new array generated from the original array by deleting 
some elements (possibly none) without changing the remaining elements' relative order. 
For example, [2,7,4] is a subsequence of [4,2,3,7,2,1,4] (the underlined elements), 
while [2,4,2] is not.

 

Example 1:

Input: nums = [4,2,5,3]
Output: 7
Explanation: It is optimal to choose the subsequence [4,2,5] with alternating sum (4 + 5) - 2 = 7.
Example 2:

Input: nums = [5,6,7,8]
Output: 8
Explanation: It is optimal to choose the subsequence [8] with alternating sum 8.
Example 3:

Input: nums = [6,2,1,2,4,5]
Output: 10
Explanation: It is optimal to choose the subsequence [6,1,5] with alternating sum (6 + 5) - 1 = 10.
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^5


'''
from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        # Use dynamic programming. For 0 <= i < nums.length, let
        # dp[i][0] represent the maximum alternating subsequence sum at index i 
        # when nums[i] is used as an even index or not used, and 
        # dp[i][1] represent the maximum alternating subsequence sum at index i 
        # when nums[i] is used as an odd index or not used.

        # Initially, dp[0][0] = nums[0] and dp[0][1] = 0 
        # (since all elements in nums are nonnegative). 
        # For 1 <= i < nums.length, there exist relations 
        # dp[i][0] = Math.max(Math.max(dp[i - 1][1], 0) + nums[i], dp[i - 1][0]) and 
        # dp[i][1] = Math.max(Math.max(dp[i - 1][0] - nums[i], 0), dp[i - 1][1]).

        #Finally, return the maximum of dp[nums.length - 1][0] and dp[nums.length - 1][1].  
        length = len(nums)
        dp = [[0]*2 for _ in range(length)]
        dp[0][0] = nums[0]
        for i in range(1, length):
            dp[i][0] = max(max(dp[i - 1][1], 0) + nums[i], dp[i - 1][0])
            dp[i][1] = max(max(dp[i - 1][0] - nums[i], 0), dp[i - 1][1])
        return max(dp[-1][0], dp[-1][1])
    
    def maxAlternatingSum2(self, nums: List[int]) -> int:
        # Use dynamic programming. For 0 <= i < nums.length, let
        # dp[i][0] represent the maximum alternating subsequence sum at index i 
        # when nums[i] is used as an even index or not used, and 
        # dp[i][1] represent the maximum alternating subsequence sum at index i 
        # when nums[i] is used as an odd index or not used.

        # Initially, dp[0][0] = nums[0] and dp[0][1] = 0 
        # (since all elements in nums are nonnegative). 
        # For 1 <= i < nums.length, there exist relations 
        # dp[i][0] = Math.max(Math.max(dp[i - 1][1], 0) + nums[i], dp[i - 1][0]) and 
        # dp[i][1] = Math.max(Math.max(dp[i - 1][0] - nums[i], 0), dp[i - 1][1]).

        #Finally, return the maximum of dp[nums.length - 1][0] and dp[nums.length - 1][1].  
        n = len(nums)
        even, odd = nums[0], 0
        for i in range(1, n):
            even = max(max(odd, 0) + nums[i], even)
            odd  = max(max(even - nums[i], 0), odd)
        print(even, odd)
        return max(odd, even)

if __name__ == "__main__":
    print(Solution().maxAlternatingSum([4,2,5,3]))
    print(Solution().maxAlternatingSum2([4,2,5,3]))