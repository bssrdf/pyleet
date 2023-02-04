'''
-Hard-

There is a group of n members, and a list of various crimes they could commit. 
The ith crime generates a profit[i] and requires group[i] members to participate in it. 
If a member participates in one crime, that member can't participate in another crime.

Let's call a profitable scheme any subset of these crimes that generates at least 
minProfit profit, and the total number of members participating in that subset of 
crimes is at most n.

Return the number of schemes that can be chosen. Since the answer may be very large, 
return it modulo 10**9 + 7.

 

Example 1:

Input: n = 5, minProfit = 3, group = [2,2], profit = [2,3]
Output: 2
Explanation: To make a profit of at least 3, the group could either commit crimes 0 and 1, or just crime 1.
In total, there are 2 schemes.
Example 2:

Input: n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]
Output: 7
Explanation: To make a profit of at least 5, the group could commit any crimes, as long as they commit one.
There are 7 possible schemes: (0), (1), (2), (0,1), (0,2), (1,2), and (0,1,2).
 

Constraints:

1 <= n <= 100
0 <= minProfit <= 100
1 <= group.length <= 100
1 <= group[i] <= 100
profit.length == group.length
0 <= profit[i] <= 100


'''
from typing import List

class Solution:
    def profitableSchemes(self, n: int, minProfit: int, 
                    group: List[int], profit: List[int]) -> int:
        m, p, MOD, res = len(profit), minProfit, 10**9+7, 0
        dp = [[[0]*(p+1) for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0][0] = 1
        for k in range(1, m+1):
            g, pr = group[k-1], profit[k-1]
            for i in range(n+1):
                for j in range(p+1):
                    dp[k][i][j] = dp[k-1][i][j]
                    if i >= g:
                        dp[k][i][j] = (dp[k][i][j] + dp[k-1][i-g][max(0,j-pr)])%MOD
        for i in range(n+1): 
            res = (res + dp[m][i][p])%MOD
        return res
    
    def profitableSchemesStateCompression(self, n: int, minProfit: int, 
                    group: List[int], profit: List[int]) -> int:
        m, p, MOD, res = len(profit), minProfit, 10**9+7, 0
        dp = [[0]*(p+1) for _ in range(n+1)]
        dp[0][0] = 1
        for k in range(1, m+1):
            g, pr = group[k-1], profit[k-1]
            for i in range(n, g-1, -1):
                for j in range(p, -1, -1):
                    dp[i][j] = (dp[i][j] + dp[i-g][max(0,j-pr)])%MOD
        for i in range(n+1): 
            res = (res + dp[i][p])%MOD
        return res

if __name__ == "__main__":
    print(Solution().profitableSchemes(n = 5, minProfit = 3, group = [2,2], profit = [2,3]))
    print(Solution().profitableSchemes(n = 10, minProfit = 5, group = [2,3,5], profit = [6,7,8]))
