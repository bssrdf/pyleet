'''

-Medium-

You are given an integer array nums. You must perform exactly one operation where you 
can replace one element nums[i] with nums[i] * nums[i].

Return the maximum possible subarray sum after exactly one operation. The subarray 
must be non-empty.

Example 1:

Input: nums = [2,-1,-4,-3]

Output: 17

Explanation: You can perform the operation on index 2 (0-indexed) to make nums = [2,-1,16,-3]. Now, the maximum subarray sum is 2 + -1 + 16 = 17.

Example 2:

Input: nums = [1,-1,1,1,-1,-1,1]

Output: 4

Explanation: You can perform the operation on index 1 (0-indexed) to make nums = [1,1,1,1,-1,-1,1]. Now, the maximum subarray sum is 1 + 1 + 1 + 1 = 4.

Constraints:

1 <= nums.length <= 10^5
-10^4 <= nums[i] <= 10^4

'''

from typing import List

class Solution:
    def maximumSum(self, arr: List[int]) -> int:
        # Use dynamic programming. Let n be the length of nums. 
        # Create a 2D array dp of n rows and 3 columns, where

        # dp[i][0] represents the maximum subarray sum that ends at index i 
        # when no operation is performed,
        
        # dp[i][1] represents the maximum subarray sum that ends at index i 
        # when the one operation is performed at index i, and
        
        # dp[i][2] represents the maximum subarray sum that ends at index i 
        # when the one operation is performed before index i.
        
        # Initially, dp[0][0] = nums[0], dp[0][1] = nums[0] * nums[0] and 
        # dp[0][2] = Integer.MIN_VALUE, which means dp[0][2] is an 
        # impossible value.

        # Loop over i from 1 to n - 1. For each i, there is 
        # dp[i][0] = Math.max(dp[i - 1][0], 0) + nums[i], 
        # dp[i][1] = Math.max(dp[i - 1][0], 0) + nums[i] * nums[i] and 
        # dp[i][2] = Math.max(Math.max(dp[i - 1][1], dp[i - 1][2]), 0) + nums[i].

        # update the maximum value during the loop using the last two columns of dp.


        n = len(arr)
        dp = [[0]*3 for _ in range(n)]
        dp[0][0] = arr[0]
        dp[0][1] = arr[0]*arr[0]
        dp[0][2] = -float('inf')
        res = dp[0][1]
        for i in range(1, n):
            dp[i][0] = max(dp[i-1][0], 0) + arr[i]
            dp[i][1] = max(dp[i-1][0], 0) + arr[i] * arr[i]
            dp[i][2] = max(max(dp[i-1][1], dp[i-1][2]), 0) + arr[i]
            curMax = max(dp[i][1], dp[i][2])
            res = max(res, curMax)
        return res

if __name__ == "__main__":
    s = Solution()
    print(s.maximumSum([2,-1,-4,-3]))
    print(s.maximumSum([1,-1,1,1,-1,-1,1]))