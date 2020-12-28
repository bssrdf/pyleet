'''
-Hard-

*DP*

Given a rows x cols matrix grid representing a field of cherries. Each cell in 
grid represents the number of cherries that you can collect.

You have two robots that can collect cherries for you, Robot #1 is located at 
the top-left corner (0,0) , and Robot #2 is located at the top-right corner 
(0, cols-1) of the grid.

Return the maximum number of cherries collection using both robots  by following 
the rules below:

From a cell (i,j), robots can move to cell (i+1, j-1) , (i+1, j) or (i+1, j+1).
When any robot is passing through a cell, It picks it up all cherries, and the 
cell becomes an empty cell (0).
When both robots stay on the same cell, only one of them takes the cherries.
Both robots cannot move outside of the grid at any moment.
Both robots should reach the bottom row in the grid.
 

Example 1:



Input: grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
Output: 24
Explanation: Path of robot #1 and #2 are described in color green and 
blue respectively.
Cherries taken by Robot #1, (3 + 2 + 5 + 2) = 12.
Cherries taken by Robot #2, (1 + 5 + 5 + 1) = 12.
Total of cherries: 12 + 12 = 24.
Example 2:



Input: grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],
[1,0,2,3,0,0,6]]
Output: 28
Explanation: Path of robot #1 and #2 are described in color green and blue 
respectively.
Cherries taken by Robot #1, (1 + 9 + 5 + 2) = 17.
Cherries taken by Robot #2, (1 + 3 + 4 + 3) = 11.
Total of cherries: 17 + 11 = 28.
Example 3:

Input: grid = [[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]]
Output: 22
Example 4:

Input: grid = [[1,1],[1,1]]
Output: 4
 

Constraints:

rows == grid.length
cols == grid[i].length
2 <= rows, cols <= 70
0 <= grid[i][j] <= 100 

'''

import sys
from itertools import product
class Solution(object):

    def cherryPickupMemo(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        """
        top-down dp (memoization)
        detailed explanation see
               
        """
        m = len(grid)
        n = len(grid[0])
        dp = [[[0 for _ in range(n)] for _ in range(n)] 
                   for _ in range(m)]
        dirs = list(product([-1,0,1], [-1,0,1]))                  

        def helper(r, c1, c2):         

           # check if current state is out of bounds 
            if c1 >= n or c1 < 0 or c2 >= n or c2 < 0:               
                return 0 

            # check if we have already computed a solution for this state
            if dp[r][c1][c2] > 0: return dp[r][c1][c2]

            # check if we reached the end state (note that if robot 1 reached 
            # the end row, 
            # this implies that robot 2 also reached the end row)
            if r == m - 1:
                return grid[r][c1] + (grid[r][c2] if c2 != c1 else 0)

            # compute and return answer for current state
            # in case the two robots are on the same position, 
            # (eg. they can't be on the same column), don't pick up the 
            # same cherry twice.
            result = grid[r][c1] + (grid[r][c2] if c2 != c1 else 0)

            # pick best possible next state
            bestNextStat = 0
            for d1,d2 in dirs:
                bestNextStat = max(helper(r+1, c1+d1, c2+d2), bestNextStat)  
            
            result += bestNextStat
            dp[r][c1][c2] = result   # store current state such that it can be 
                                     # re-used

            return result
        return helper(0, 0, n-1)  

if __name__ == "__main__":
    grid = [[3,1,1],[2,5,1],[1,5,5],[2,1,1]]
    print(Solution().cherryPickupMemo(grid))
    grid = [[1,0,0,0,0,0,1],[2,0,0,0,0,3,0],[2,0,9,0,0,0,0],[0,3,0,5,4,0,0],
            [1,0,2,3,0,0,6]]
    print(Solution().cherryPickupMemo(grid))
    grid = [[1,0,0,3],[0,0,0,3],[0,0,3,3],[9,0,3,3]]
    print(Solution().cherryPickupMemo(grid))
    grid = [[1,1],[1,1]]
    print(Solution().cherryPickupMemo(grid))