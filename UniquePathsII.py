'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram 
below).

The robot can only move either down or right at any point in time. The robot is trying 
to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

Now consider if some obstacles are added to the grids. How many unique paths would 
there be?

An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Note: m and n will be at most 100.

Example 1:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]
Output: 2
Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

'''


class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        if not obstacleGrid:
            return 0
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        dp[0][1] = 1        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] != 0:
                    continue              
                dp[i+1][j+1] = dp[i+1][j] + dp[i][j+1] 
        return dp[m][n]



if __name__ == "__main__":
    
    grid = [ [0,0,0],
             [0,1,0],
             [0,0,0] ]
    print(Solution().uniquePathsWithObstacles(grid))