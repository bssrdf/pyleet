'''
-Medium-
*DP*

Given a 2D grid of 0s and 1s, return the number of elements in 
the largest square subgrid that has all 1s on its border, or 0 if 
such a subgrid doesn't exist in the grid.

 

Example 1:

Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: 9
Example 2:

Input: grid = [[1,1,0,0]]
Output: 1
 

Constraints:

1 <= grid.length <= 100
1 <= grid[0].length <= 100
grid[i][j] is 0 or 1


'''

from typing import List

class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dp = [[[0, 0] for _ in range(n + 1)] for _ in range(m + 1)]
        # dp[i][j][0] the number of 1's at and above [i,j]
        # dp[i][j][1] the number of 1's to the left of and at [i,j]
        ans = 0
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if grid[i - 1][j - 1] == 1:
                    dp[i][j][0] = dp[i-1][j][0] + 1
                    dp[i][j][1] = dp[i][j-1][1] + 1
                    upper = min(dp[i][j][0], dp[i][j][1])
                    for k in range(upper):
                        if min(dp[i-k][j][1], dp[i][j-k][0]) >= k + 1:
                            if k + 1 > ans:
                                ans = k + 1

        return ans**2



if __name__ == "__main__":
    grid = [[1,1,1],[1,0,1],[1,1,1]]
    print(Solution().largest1BorderedSquare(grid))
    grid = [[1,1,0,0]]
    print(Solution().largest1BorderedSquare(grid))
    grid = [[0,0], [0,0]]
    print(Solution().largest1BorderedSquare(grid))
