'''
-Medium-

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 
4-directionally connected group of 0s and a closed island is an island totally 
(all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

 

Example 1:



Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],
     [1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:



Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2
 

Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1

'''

from typing import List

class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        ans = 0
        def dfs(i,j):
            grid[i][j] = -1
            for dx, dy in dirs:
                x = i + dx;  y = j + dy                
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 0:
                    dfs(x, y) 
            return 
        for i in range(m):
            if grid[i][0] == 0:
                dfs(i, 0)
            if grid[i][n-1] == 0:
                dfs(i, n-1)
        for j in range(n):
            if grid[0][j] == 0:
                dfs(0, j)
            if grid[m-1][j] == 0:
                dfs(m-1, j)    
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    dfs(i,j)                 
                    ans += 1 
        return ans



        

if __name__ == "__main__":
    grid = [[1,1,1,1,1,1,1,0],
            [1,0,0,0,0,1,1,0],
            [1,0,1,0,1,1,1,0],
            [1,0,0,0,0,1,0,1],
            [1,1,1,1,1,1,1,0]]
    print(Solution().closedIsland(grid))
    grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
    print(Solution().closedIsland(grid))
    grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
    print(Solution().closedIsland(grid))
    grid = [[0,0,1,1,0,1,0,0,1,0],
            [1,1,0,1,1,0,1,1,1,0],
            [1,0,1,1,1,0,0,1,1,0],
            [0,1,1,0,0,0,0,1,0,1],
            [0,0,0,0,0,0,1,1,1,0],
            [0,1,0,1,0,1,0,1,1,1],
            [1,0,1,0,1,1,0,0,0,1],
            [1,1,1,1,1,1,0,0,0,0],
            [1,1,1,0,0,1,0,1,0,1],
            [1,1,1,0,1,1,0,1,1,0]]
    print(Solution().closedIsland(grid))
    for r in grid:
        print(r)
