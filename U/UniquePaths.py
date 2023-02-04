'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 3 x 7 grid. How many possible unique paths are there?

Note: m and n will be at most 100.
'''

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[1 for __ in range(n)] for __ in range(m)]
        for i in range(1,m):
            for j in range(1,n):                
                dp[i][j] = dp[i-1][j] + dp[i][j-1] 
                
        return dp[m-1][n-1]

    def uniquePaths2(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        dp[0][1] = 1        
        for i in range(1,m+1):
            for j in range(1,n+1):                
                dp[i][j] = dp[i][j-1] + dp[i-1][j] 
        return dp[m][n]
                

if __name__ == "__main__":
    assert Solution().uniquePaths(3, 7) == 28