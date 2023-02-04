'''
-Hard-
*Prefix Sum (2D)*
*Difference Array (2D)*

You are given an m x n binary matrix grid where each cell is either 0 (empty) or 1 (occupied).

You are then given stamps of size stampHeight x stampWidth. We want to fit the stamps 
such that they follow the given restrictions and requirements:

Cover all the empty cells.
Do not cover any of the occupied cells.
We can put as many stamps as we want.
Stamps can overlap with each other.
Stamps are not allowed to be rotated.
Stamps must stay completely inside the grid.
Return true if it is possible to fit the stamps while following the given 
restrictions and requirements. Otherwise, return false.

 

Example 1:


Input: grid = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]], stampHeight = 4, stampWidth = 3
Output: true
Explanation: We have two overlapping stamps (labeled 1 and 2 in the image) that are able to cover all the empty cells.
Example 2:


Input: grid = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], stampHeight = 2, stampWidth = 2 
Output: false 
Explanation: There is no way to fit the stamps onto all the empty cells without the stamps going outside the grid.
 

Constraints:

m == grid.length
n == grid[r].length
1 <= m, n <= 105
1 <= m * n <= 2 * 105
grid[r][c] is either 0 or 1.
1 <= stampHeight, stampWidth <= 105


'''
from typing import List

class Solution:
    def possibleToStamp(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        # Wrong!!!
        H, W = stampHeight, stampWidth
        if H == 1 and W == 1: return True
        m, n = len(grid), len(grid[0])
        rows = [[0]*n for _ in range(m)]
        cols = [[0]*n for _ in range(m)]
        for i in range(m):
            zeros, l, row = 0, 0, [0]*(n+1)
            for j in range(n):
                if grid[i][j] == 0:
                    zeros += 1                    
                else:
                    if zeros >= W:
                        row[l] += 1
                        row[j+1] += -1
                    zeros = 0
                    l = j+1 
            # print(l, j)
            if zeros >= W:
                row[l] += 1
                row[j+1] += -1
            rows[i][0] = row[0]
            for j in range(1, n):
                rows[i][j] = rows[i][j-1] + row[j]
        for j in range(n):
            zeros, t, col = 0, 0, [0]*(m+1)
            for i in range(m):
                if grid[i][j] == 0:
                    zeros += 1                    
                else:
                    if zeros >= H:
                        col[t] += 1
                        col[i+1] += -1
                    zeros = 0
                    t = i+1 
            # print(l, j)
            if zeros >= H:
                col[t] += 1
                col[i+1] += -1
            cols[0][j] = col[0]
            for i in range(1, m):
                cols[i][j] = cols[i-1][j] + col[i]
        for r in rows:
            print(r)    
        # for r in cols:
        #     print(r)  
        for i in range(m):
            for j in range(n):  
                if grid[i][j] == 0 and (rows[i][j] != 1 or cols[i][j] != 1):
                    return False
        return True 
    
    def possibleToStamp2(self, grid: List[List[int]], stampHeight: int, stampWidth: int) -> bool:
        H, W = stampHeight, stampWidth
        if H == 1 and W == 1: return True
        m, n = len(grid), len(grid[0])

        def acc_2d(grid):
            dp = [[0] * (n+1) for _ in range(m+1)] 
            for r in range(m):
                for c in range(n):
                    dp[r+1][c+1] = dp[r+1][c] + dp[r][c+1] - dp[r][c] + grid[r][c]
            return dp

        def sumRegion(r1, c1, r2, c2):
            return dp[r2+1][c2+1] - dp[r1][c2+1] - dp[r2+1][c1] + dp[r1][c1]  

        m, n = len(grid), len(grid[0])
        dp = acc_2d(grid)

        diff = [[0] * (n+1) for _ in range(m+1)] 
        for c in range(n - W + 1):
            for r in range(m - H + 1):
                # use preFix sum to find out whether the region [r, c] -> [r+H-1, c+W-1]
                # can be stamped. 
                if sumRegion(r, c, r + H - 1, c + W - 1) == 0:
                    # If yes, mark the region using the 2D difference array
                    diff[r][c] += 1
                    diff[r][c+W] -= 1
                    diff[r+H][c] -= 1
                    diff[r+H][c+W] += 1
        
        dp2 = acc_2d(diff) # sum up difference to get the actual mark
                           # dp2[i][j] tells how many times cell [i,j] can
                           # be stamped differently
        # for r in dp2:
        #     print(r)
        for r in range(m):
            for c in range(n):
                if dp2[r+1][c+1] == 0 and grid[r][c] != 1: return False
        return True

                






if __name__ == "__main__":
    grid = [[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0],[1,0,0,0]]
    stampHeight = 4; stampWidth = 3
    print(Solution().possibleToStamp(grid, stampHeight, stampWidth))
    grid = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
    stampHeight = 2; stampWidth = 2 
    print(Solution().possibleToStamp(grid, stampHeight, stampWidth))
    grid = [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,1,0,0],
            [0,0,0,0,1],
            [0,0,0,1,1]]
    stampHeight = 2; stampWidth = 2 
    print(Solution().possibleToStamp2(grid, stampHeight, stampWidth))

