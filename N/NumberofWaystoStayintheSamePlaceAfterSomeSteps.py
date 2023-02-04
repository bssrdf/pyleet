'''

-Hard-
*DP*


You have a pointer at index 0 in an array of size arrLen. At each step, you can move 1 position to the left, 1 position to the right in the array, or stay in the same place (The pointer should not be placed outside the array at any time).

Given two integers steps and arrLen, return the number of ways such that your pointer still at index 0 after exactly steps steps. Since the answer may be too large, return it modulo 109 + 7.

 

Example 1:

Input: steps = 3, arrLen = 2
Output: 4
Explanation: There are 4 differents ways to stay at index 0 after 3 steps.
Right, Left, Stay
Stay, Right, Left
Right, Stay, Left
Stay, Stay, Stay
Example 2:

Input: steps = 2, arrLen = 4
Output: 2
Explanation: There are 2 differents ways to stay at index 0 after 2 steps
Right, Left
Stay, Stay
Example 3:

Input: steps = 4, arrLen = 2
Output: 8
 

Constraints:

1 <= steps <= 500
1 <= arrLen <= 106



'''

class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        n, m, MOD = arrLen, steps, 10**9+7
        # dp = [[0]*(m+1) for _ in range(min(m, n))]
        dp = [[0]*(m+1) for _ in range(min(m//2+1, n))]
        dp[0][0] = 1   
        for j in range(1, m+1):
            for i in range(len(dp)):            
                dp[i][j] = (dp[i][j-1]  # stay at i 
                            + (dp[i-1][j-1] if i > 0 else 0)  # come from left
                            + (dp[i+1][j-1] if i < len(dp)-1 else 0) # come from right
                            ) % MOD
        return dp[0][m]


            

        

if __name__ == "__main__":
    print(Solution().numWays(steps = 3, arrLen = 2))
    print(Solution().numWays(steps = 2, arrLen = 4))
    print(Solution().numWays(steps = 4, arrLen = 2))