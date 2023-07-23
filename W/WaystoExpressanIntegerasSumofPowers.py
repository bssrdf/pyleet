'''

-Medium-
*DP*

Given two positive integers n and x.

Return the number of ways n can be expressed as the sum of the xth power of unique positive integers, in other words, the number of sets of unique integers [n1, n2, ..., nk] where n = n1x + n2x + ... + nkx.

Since the result can be very large, return it modulo 109 + 7.

For example, if n = 160 and x = 3, one way to express n is n = 23 + 33 + 53.

 

Example 1:

Input: n = 10, x = 2
Output: 1
Explanation: We can express n as the following: n = 32 + 12 = 10.
It can be shown that it is the only way to express 10 as the sum of the 2nd power of unique integers.
Example 2:

Input: n = 4, x = 1
Output: 2
Explanation: We can express n in the following ways:
- n = 41 = 4.
- n = 31 + 11 = 4.
 

Constraints:

1 <= n <= 300
1 <= x <= 5


'''
from functools import lru_cache

class Solution:
    def numberOfWays(self, n: int, x: int) -> int:
        # MLE
        nums = []
        MOD = 10**9 + 7
        for i in range(1, n+1):
            if i**x <= n:
                nums.append(i**x)
        m = len(nums)
        @lru_cache(None) 
        def dp(i, sm):
            if i == m:
                return 1 if sm == 0 else 0
            if sm == 0:
                return 1
            if sm < 0:
                return 0
            ret = dp(i+1, sm)
            ret = (ret + dp(i+1, sm - nums[i])) % MOD
            return ret
        return dp(0, n) 
    
    def numberOfWays2(self, n: int, x: int) -> int:
        nums = []
        MOD = 10**9 + 7
        for i in range(1, n+1):
            if i**x <= n:
                nums.append(i**x)
        m = len(nums)
        memo = [[-1]*(n+1) for _ in range(m)]
        def dp(i, sm):
            if i == m:
                return 1 if sm == 0 else 0
            if sm == 0:
                return 1
            if sm < 0:
                return 0
            if memo[i][sm] != -1: return memo[i][sm]
            memo[i][sm] = dp(i+1, sm)
            memo[i][sm] = (memo[i][sm] + dp(i+1, sm - nums[i])) % MOD
            return memo[i][sm]
        return dp(0, n) 

if __name__ == "__main__":
    print(Solution().numberOfWays(n = 10, x = 2))
    print(Solution().numberOfWays2(n = 10, x = 2))
    print(Solution().numberOfWays(n = 4, x = 1))