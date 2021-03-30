'''
-Hard-
*DP*
Given two integers n and k, find how many different arrays consist of numbers from 1 to 
n such that there are exactly k inverse pairs.

We define an inverse pair as following: For ith and jth element in the array, if i < j and 
a[i] > a[j] then it's an inverse pair; Otherwise, it's not.

Since the answer may be very large, the answer should be modulo 109 + 7.

Example 1:

Input: n = 3, k = 0
Output: 1
Explanation: 
Only the array [1,2,3] which consists of numbers from 1 to 3 has exactly 0 inverse pair.
 

Example 2:

Input: n = 3, k = 1
Output: 2
Explanation: 
The array [1,3,2] and [2,1,3] have exactly 1 inverse pair.
 

Note:

The integer n is in the range [1, 1000] and k is in the range [0, 1000].

'''

class Solution(object):
    def kInversePairsTLE(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
        MOD = 10**9 +7
        dp[0][0] = 1
        for i in range(n+1):
            for j in range(i):
                for m in range(k+1): 
                    # dp[i][m] = dp[i - 1][m] + dp[i - 1][m-1] + ... + dp[i - 1][m - (n - 1)]
                    if m - j >= 0 and m - j <= k:
                        dp[i][m] = (dp[i][m] + dp[i - 1][m - j]) % MOD
        return dp[n][k]

    def kInversePairs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        dp = [[0 for _ in range(k+1)] for _ in range(n+1)]
        MOD = 10**9 +7
        dp[0][0] = 1
        for i in range(1,n+1):
            dp[i][0] = 1
            for j in range(1, k+1):
                # dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-i]
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % MOD
                if j >= i: 
                    dp[i][j] = (dp[i][j] - dp[i-1][j-i]+MOD) % MOD
        return dp[n][k]
        

if __name__ == "__main__":
    print(Solution().kInversePairs(3, 1))