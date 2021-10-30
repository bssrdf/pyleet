'''

-Medium-

*DP*

Given an integer array arr, partition the array into (contiguous) subarrays of 
length at most k. After partitioning, each subarray has their values changed to 
become the maximum value of that subarray.

Return the largest sum of the given array after partitioning. Test cases are 
generated so that the answer fits in a 32-bit integer.

 

Example 1:

Input: arr = [1,15,7,9,2,5,10], k = 3
Output: 84
Explanation: arr becomes [15,15,15,9,10,10,10]
Example 2:

Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
Output: 83
Example 3:

Input: arr = [1], k = 1
Output: 1
 

Constraints:

1 <= arr.length <= 500
0 <= arr[i] <= 10^9
1 <= k <= arr.length


'''


from typing import List

class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0]*(n+1)
        for i in range(1, n+1):
            for j in range(1, min(i+1,k+1)):
                dp[i] = max(dp[i], dp[i-j] + j * max(arr[i-j:i]))
        return dp[n] 

    def maxSumAfterPartitioning2(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0]*(n+1)
        for i in range(1, n+1):
            max_ = arr[i-1]
            for j in range(1, min(i+1,k+1)):
                max_ = max(max_, arr[i-j]) 
                #dp[i] = max(dp[i], dp[i-j] + j * max(arr[i-j:i]))
                dp[i] = max(dp[i], dp[i-j] + j * max_)
        return dp[n] 

if __name__ == "__main__":
    print(Solution().maxSumAfterPartitioning(arr = [1,15,7,9,2,5,10], k = 3))
    print(Solution().maxSumAfterPartitioning(arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4))
    print(Solution().maxSumAfterPartitioning(arr = [1], k = 1))
    print(Solution().maxSumAfterPartitioning2(arr = [1,15,7,9,2,5,10], k = 3))
    print(Solution().maxSumAfterPartitioning2(arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4))
    print(Solution().maxSumAfterPartitioning2(arr = [1], k = 1))