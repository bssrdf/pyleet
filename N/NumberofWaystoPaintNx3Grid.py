'''
-Hard-
*DP*

You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: Red, Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).

Given n the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 109 + 7.

 

Example 1:


Input: n = 1
Output: 12
Explanation: There are 12 possible way to paint the grid as shown.
Example 2:

Input: n = 5000
Output: 30228214
 

Constraints:

n == grid.length
1 <= n <= 5000


'''

from functools import lru_cache
from itertools import product
class Solution:
    def numOfWays(self, n: int) -> int:
        MOD = 10**9 + 7
        dp = [[[[0]*3 for _ in range(3)] for _ in range(3)] for _ in range(n+1)]
        for j,k,l in product(range(3), range(3), range(3)):
            if j != k and k != l:            
                dp[1][j][k][l] = 1
        for i in range(2, n+1):
            for j,k,l in product(range(3), range(3), range(3)):
                if j != k and k != l:                   
                    for j1,k1,l1 in product(range(3), range(3), range(3)):
                        if j != j1 and k != k1 and l != l1:
                            dp[i][j][k][l] = (dp[i][j][k][l] + dp[i-1][j1][k1][l1]) % MOD
        ans = 0
        for j,k,l in product(range(3), range(3), range(3)):
            if j != k and k != l:
                ans = (ans + dp[n][j][k][l]) % MOD
        return ans
        

if __name__ == "__main__":
    print(Solution().numOfWays(1))
    #
    print(Solution().numOfWays(2))
    print(Solution().numOfWays(5000))