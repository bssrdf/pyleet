'''
-Hard-

You are given an array nums consisting of positive integers and an integer k.

Partition the array into two ordered groups such that each element is in exactly one group. A partition is called great if the sum of elements of each group is greater than or equal to k.

Return the number of distinct great partitions. Since the answer may be too large, return it modulo 109 + 7.

Two partitions are considered distinct if some element nums[i] is in different groups in the two partitions.

 

Example 1:

Input: nums = [1,2,3,4], k = 4
Output: 6
Explanation: The great partitions are: ([1,2,3], [4]), ([1,3], [2,4]), ([1,4], [2,3]), ([2,3], [1,4]), ([2,4], [1,3]) and ([4], [1,2,3]).
Example 2:

Input: nums = [3,3,3], k = 4
Output: 0
Explanation: There are no great partitions for this array.
Example 3:

Input: nums = [6,6], k = 2
Output: 2
Explanation: We can either put nums[0] in the first partition or in the second partition.
The great partitions will be ([6], [6]) and ([6], [6]).
 

Constraints:

1 <= nums.length, k <= 1000
1 <= nums[i] <= 109



'''

from typing import List


class Solution:
    def countPartitions(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        A = nums
        if sum(A) < k * 2: return 0
        dp = [1] + [0] * (k - 1)
        for a in A:
            for i in range(k - 1 - a, -1, -1):
                dp[i + a] += dp[i]
        return (pow(2, len(A), MOD) - sum(dp) * 2) % MOD
    
    def countPartitions2(self, nums: List[int], k: int) -> int:
        n = len(nums)
        dp = [[0] * (k + 1)] + [[-1] * (k + 1) for _ in range(n)]
        dp[0][0] = 1
        def subsetSumCounts(s, idx):
            if s < 0:
                return 0
            if dp[idx][s] < 0:
                dp[idx][s] = subsetSumCounts(s, idx - 1) + subsetSumCounts(s - nums[idx - 1], idx - 1)
            return dp[idx][s]
                
        invalid_pairs = sum([subsetSumCounts(i, n) for i in range(k)]) * 2
        return max(2**n - invalid_pairs, 0) % (10**9 + 7)
    

    def countPartitions3(self, nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(nums)
        dp = [[0] * k for _ in range(n)]
        for i in range(n):
            for j in range(k):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                    continue
                if i == 0:
                    if j == nums[i]: dp[i][j] = 1
                    continue
                if nums[i] > j: dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i-1][j-nums[i]]
                    dp[i][j] %= MOD
        invalid = sum(dp[n-1]) % MOD
        return max(2**n - 2*invalid, 0) % MOD
        




if __name__ == "__main__":
    print(Solution().countPartitions(nums = [1,2,3,4], k = 4))