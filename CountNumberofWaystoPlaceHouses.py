'''
-Medium-
*DP*

There is a street with n * 2 plots, where there are n plots on each side of the street. The plots on each side are numbered from 1 to n. On each plot, a house can be placed.

Return the number of ways houses can be placed such that no two houses are adjacent to each other on the same side of the street. Since the answer may be very large, return it modulo 109 + 7.

Note that if a house is placed on the ith plot on one side of the street, a house can also be placed on the ith plot on the other side of the street.

 

Example 1:

Input: n = 1
Output: 4
Explanation: 
Possible arrangements:
1. All plots are empty.
2. A house is placed on one side of the street.
3. A house is placed on the other side of the street.
4. Two houses are placed, one on each side of the street.
Example 2:


Input: n = 2
Output: 9
Explanation: The 9 possible arrangements are shown in the diagram above.
 

Constraints:

1 <= n <= 104



'''


class Solution:
    def countHousePlacements(self, n: int) -> int:
        dp = [[0]*4 for _ in range(n+1)]
        dp[0][2] = 1
        mod = 10**9 +7
        for i in range(1, n+1):

            dp[i][0] = (dp[i-1][1] + dp[i-1][2] ) % mod
            dp[i][1] = (dp[i-1][0] + dp[i-1][2] ) % mod
            dp[i][2] = (dp[i-1][0] + dp[i-1][1] + dp[i-1][2] + dp[i-1][3]) % mod
            dp[i][3] = dp[i-1][2] % mod
        
        return sum(dp[n]) % mod
    
    def countHousePlacements2(self, n: int) -> int:
        dp, dp1 = [0]*4, [0]*4
        dp[2] = 1
        mod = 10**9 +7
        for i in range(1, n+1):
            dp1[0] = (dp[1] + dp[2]) % mod
            dp1[1] = (dp[0] + dp[2]) % mod
            dp1[2] = (dp[0] + dp[1] + dp[2] + dp[3]) % mod
            dp1[3] = dp[2] % mod
            dp, dp1 = dp1, dp
        
        return sum(dp) % mod
        
        

if __name__ == "__main__":
    print(Solution().countHousePlacements(2))
    print(Solution().countHousePlacements(3))
    print(Solution().countHousePlacements2(2))
    print(Solution().countHousePlacements2(3))