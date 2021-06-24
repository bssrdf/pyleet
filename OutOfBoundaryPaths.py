'''

-Medium-
*DP*
*Memoization*
*DFS*

There is an m by n grid with a ball. Given the start coordinate (i,j) of the 
ball, you can move the ball to adjacent cell or cross the grid boundary in 
four directions (up, down, left, right). However, you can at most move N 
times. Find out the number of paths to move the ball out of grid boundary. 
The answer may be very large, return it after mod 10^9 + 7.

 

Example 1:

Input: m = 2, n = 2, N = 2, i = 0, j = 0
Output: 6
Explanation:

Example 2:

Input: m = 1, n = 3, N = 3, i = 0, j = 1
Output: 12
Explanation:

 

Note:

Once you move the ball out of boundary, you cannot move it back.
The length and height of the grid is in range [1,50].
N is in range [0,50].

'''

class Solution(object):
    #def findPaths(self, m, n, N, i, j):
    def findPaths(self, m, n, maxMove, startRow, startColumn):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        if maxMove == 0: return 0
        if m == 1 and n == 1 : return 4
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]                
        memo = [[[-1 for _ in range(maxMove)] for _ in range(n)] for _ in range(m)]  
        def dfs(i,j,k):
            if i < 0 or i > m-1 or j < 0 or j > n-1:
                return 1
            if k == maxMove:
                return 0
            if memo[i][j][k] != -1:
                return memo[i][j][k]   
            ib = 0    
            for di, dj in dirs:
                ib += dfs(i+di, j+dj, k+1)                
            memo[i][j][k] = ib 
            print(i,j,k,memo[i][j][k])               
            return memo[i][j][k]       
        return dfs(startRow,startColumn,0)% (10**9+7)

if __name__ == "__main__":
    print(Solution().findPaths(2, 2, 2, 0, 0))
    print(Solution().findPaths(1, 3, 3, 0, 1))
    print(Solution().findPaths(3, 2, 5, 1, 1))