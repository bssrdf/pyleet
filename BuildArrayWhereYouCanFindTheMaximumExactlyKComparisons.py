'''
-Hard-


You are given three integers n, m and k. Consider the following algorithm to find the maximum element of an array of positive integers:


You should build the array arr which has the following properties:

arr has exactly n integers.
1 <= arr[i] <= m where (0 <= i < n).
After applying the mentioned algorithm to arr, the value search_cost is equal to k.
Return the number of ways to build the array arr under the mentioned conditions. As the answer may grow large, the answer must be computed modulo 109 + 7.

 

Example 1:

Input: n = 2, m = 3, k = 1
Output: 6
Explanation: The possible arrays are [1, 1], [2, 1], [2, 2], [3, 1], [3, 2] [3, 3]
Example 2:

Input: n = 5, m = 2, k = 3
Output: 0
Explanation: There are no possible arrays that satisify the mentioned conditions.
Example 3:

Input: n = 9, m = 1, k = 1
Output: 1
Explanation: The only possible array is [1, 1, 1, 1, 1, 1, 1, 1, 1]
 

Constraints:

1 <= n <= 50
1 <= m <= 100
0 <= k <= n


'''
import bisect
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        ans, MOD = 0, 10**9 + 7
        dp = [[[0]*(k+1) for _ in range(m+1)] for _ in range(n+1)]
        for j in range(1,m+1):
            dp[1][j][1] = 1
        for i in range(1,n+1):
            for j in range(1,m+1):
                for l in range(1, k+1):
                    s = j*dp[i-1][j][l] % MOD
                    for x in range(1,j):
                       s = (s + dp[i-1][x][l-1]) % MOD
                    dp[i][j][l] = (dp[i][j][l] + s) % MOD
        for j in range(1,m+1):
            ans = (ans + dp[n][j][k]) % MOD
        return ans
         
if __name__ == "__main__":
    print(Solution().numOfArrays(n = 2, m = 3, k = 1))
    print(Solution().numOfArrays(n = 5, m = 2, k = 3))
    print(Solution().numOfArrays(n = 9, m = 1, k = 1))
    print(Solution().numOfArrays(n = 11, m = 20, k = 8))