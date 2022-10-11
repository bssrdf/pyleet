'''

-Medium-

*DP*


You are currently designing a dynamic array. You are given a 0-indexed integer array nums, where nums[i] is the number of elements that will be in the array at time i. In addition, you are given an integer k, the maximum number of times you can resize the array (to any size).

The size of the array at time t, sizet, must be at least nums[t] because there needs to be enough space in the array to hold all the elements. The space wasted at time t is defined as sizet - nums[t], and the total space wasted is the sum of the space wasted across every time t where 0 <= t < nums.length.

Return the minimum total space wasted if you can resize the array at most k times.

Note: The array can have any size at the start and does not count towards the number of resizing operations.

 

Example 1:

Input: nums = [10,20], k = 0
Output: 10
Explanation: size = [20,20].
We can set the initial size to be 20.
The total wasted space is (20 - 10) + (20 - 20) = 10.
Example 2:

Input: nums = [10,20,30], k = 1
Output: 10
Explanation: size = [20,20,30].
We can set the initial size to be 20 and resize to 30 at time 2. 
The total wasted space is (20 - 10) + (20 - 20) + (30 - 30) = 10.
Example 3:

Input: nums = [10,20,15,30,20], k = 2
Output: 15
Explanation: size = [10,20,20,30,30].
We can set the initial size to 10, resize to 20 at time 1, and resize to 30 at time 3.
The total wasted space is (10 - 10) + (20 - 20) + (20 - 15) + (30 - 30) + (30 - 20) = 15.
 

Constraints:

1 <= nums.length <= 200
1 <= nums[i] <= 106
0 <= k <= nums.length - 1

'''

from typing import List
from functools import lru_cache

class Solution:
    def minSpaceWastedKResizing(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[float('inf')]*(k+1) for _ in range(n)]
        mx, sm = 0, 0
        for i in range(n):
            mx = max(mx, nums[i])
            sm += nums[i]
            dp[i][0] = mx*(i+1) - sm
        for i in range(1, n):
            for j in range(1, min(i,k)+1):
                mx, invsum = 0, 0
                for s in range(i, max(j-2, 0), -1):
                    mx = max(mx, nums[s])
                    invsum += nums[s]
                    dp[i][j] = min(dp[i][j], dp[s-1][j-1]+mx*(i-s+1)-invsum)
        return min(dp[n-1]) 
    
    def minSpaceWastedKResizing2(self, nums: List[int], k: int) -> int:
        # Solution similar to 1335. Minimum Difficulty of a Job Schedule
        # https://leetcode.com/problems/minimum-difficulty-of-a-job-schedule/
        n, INF = len(nums), 200 * 1e6

        # dp(i, k) denote the minimum space wasted if we can resize k times of nums[i..n-1].
        @lru_cache(None)
        def dp(i, k):
            if i == n: return 0
            if k == -1: return INF
            ans = INF
            maxNum = 0
            totalSum = 0
            for j in range(i, n-k):
                # make 1 adjustment in range [i, j]
                maxNum = max(maxNum, nums[j])
                totalSum += nums[j]
                # total space wasted in range [i, j]
                wasted = maxNum * (j - i + 1) - totalSum
                ans = min(ans, dp(j + 1, k - 1) + wasted)
            return ans

        return dp(0, k)




if __name__ == "__main__":
    print(Solution().minSpaceWastedKResizing(nums = [10,20,15,30,20], k = 2))
        