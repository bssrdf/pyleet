'''

-Medium-
*DP*

Given n points on a 1-D plane, where the ith point (from 0 to n-1) is at x = i, find the number of ways we can draw exactly k non-overlapping line segments such that each segment covers two or more points. The endpoints of each segment must have integral coordinates. The k line segments do not have to cover all n points, and they are allowed to share endpoints.

Return the number of ways we can draw k non-overlapping line segments. Since this number can be huge, return it modulo 109 + 7.

 

Example 1:


Input: n = 4, k = 2
Output: 5
Explanation: The two line segments are shown in red and blue.
The image above shows the 5 different ways {(0,2),(2,3)}, {(0,1),(1,3)}, {(0,1),(2,3)}, {(1,2),(2,3)}, {(0,1),(1,2)}.
Example 2:

Input: n = 3, k = 1
Output: 3
Explanation: The 3 ways are {(0,1)}, {(0,2)}, {(1,2)}.
Example 3:

Input: n = 30, k = 7
Output: 796297179
Explanation: The total number of possible ways to draw 7 line segments is 3796297200. Taking this number modulo 109 + 7 gives us 796297179.
 

Constraints:

2 <= n <= 1000
1 <= k <= n-1


'''



class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [[0]*(k+1) for _ in range(n)]
        sum0, sum1 = [0]*n, [0]*n
        for i in range(1,n):
            dp[i][1] = i*(i+1)//2
            sum0[i] = (sum0[i-1] + dp[i][1]) 
        for j in range(2, k+1):
            for i in range(j, n):                                        
                if i == j:
                    dp[i][j] = 1
                else:     
                    dp[i][j] = (sum0[i-1] + dp[i-1][j]) % MOD
                sum1[i] = (sum1[i-1] + dp[i][j]) 
            sum0 = sum1
            sum1 = [0]*n
        return dp[n-1][k]    
    
    def numberOfSets2(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        dp = [0]*n
        sum0, sum1 = [0]*n, [0]*n
        for i in range(1,n):
            dp[i] = i*(i+1)//2
            sum0[i] = sum0[i-1] + dp[i] 
        for j in range(2, k+1):
            for i in range(j, n):                                        
                if i == j:
                    dp[i] = 1
                else:     
                    dp[i] = (sum0[i-1] + dp[i-1]) % MOD
                sum1[i] = (sum1[i-1] + dp[i]) 
            sum0 = sum1
            sum1 = [0]*n
        return dp[n-1]    

            


if __name__ == "__main__":        
    print(Solution().numberOfSets(n = 4, k = 2))
    print(Solution().numberOfSets(n = 5, k = 2))
    print(Solution().numberOfSets(n = 3, k = 1))
    print(Solution().numberOfSets(n = 30, k = 7))

    print(Solution().numberOfSets2(n = 4, k = 2))
    print(Solution().numberOfSets2(n = 5, k = 2))
    print(Solution().numberOfSets2(n = 3, k = 1))
    print(Solution().numberOfSets2(n = 30, k = 7))