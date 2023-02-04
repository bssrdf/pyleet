'''
-Hard-
*DFS*
*Tarjan's Algorithm*

You are given an m x n binary grid grid where 1 represents land and 0 represents water. 
An island is a maximal 4-directionally (horizontal or vertical) connected group of 1's.

The grid is said to be connected if we have exactly one island, otherwise is 
said disconnected.

In one day, we are allowed to change any single land cell (1) into a water cell (0).

Return the minimum number of days to disconnect the grid.

 

Example 1:


Input: grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]

Output: 2
Explanation: We need at least 2 days to get a disconnected grid.
Change land grid[1][1] and grid[0][2] to water and get 2 disconnected island.
Example 2:


Input: grid = [[1,1]]
Output: 2
Explanation: Grid of full water is also disconnected ([[1,1]] -> [[0,0]]), 0 islands.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 30
grid[i][j] is either 0 or 1.




'''

from typing import List
import copy

class Solution:
    
    
	
    #find how many islands the given grid has        
    def no_islands(self, grid):
        ret, count = 0, [0]
        m, n = len(grid), len(grid[0])
        def no_islands_recur(i, j, m, n):
            if grid[i][j]==0:
                return
            count[0] += 1
            grid[i][j]=0
            if i-1>=0:
                no_islands_recur(i-1, j, m, n)
            if i+1<m:
                no_islands_recur(i+1, j, m, n)
            if j-1>=0:
                no_islands_recur(i, j-1, m, n)
            if j+1<n:
                no_islands_recur(i, j+1, m, n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ret += 1
                    no_islands_recur(i, j, m, n)
        return ret, count[0]
    
    

    def minDays(self, grid: List[List[int]]) -> int:
        time = 0
        grid_copy = copy.deepcopy(grid)
        n,count = self.no_islands(grid_copy)
        if n != 1:
            return time
        if count == 1: return 1
        if count == 2: return 2
        m, n = len(grid), len(grid[0])    
        levels = [[-1]*n for _ in range(m)]
        pre = [[-1]*n for _ in range(m)]
        hasCritial = [False]
        dirs = [(0,-1),(0,1),(-1,0),(1,0)]
        time = [0]
        def dfs(curr, parent):
            x, y = curr
            time[0] += 1
            levels[x][y] = time[0]
            pre[x][y] = levels[x][y]
            for dx, dy in dirs:
                i,j = x+dx, y+dy 
                if i < 0 or i >= m or j < 0 or j >= n or (i,j) == parent or grid[i][j] == 0:
                    continue
                if pre[i][j] == -1:
                    dfs((i,j), (x,y))                    
                    if levels[i][j] > pre[x][y]:    
                        hasCritial[0] = True
                levels[x][y] = min(levels[x][y], levels[i][j])
            return
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if levels[i][j] == -1:
                        dfs((i,j), (-1,-1))
        if hasCritial[0]: return 1
        return 2
    
    def minDays2(self, grid: List[List[int]]) -> int:
        time = 0
        grid_copy = copy.deepcopy(grid)
        n,count = self.no_islands(grid_copy)
        if n != 1: return time
        if count == 1: return 1
        if count == 2: return 2
        m, n = len(grid), len(grid[0])    
        levels = [[-1]*n for _ in range(m)]
        hasCritial = [False]
        dirs = [(0,-1),(0,1),(-1,0),(1,0)]
        def dfs(curr, level, parent):
            x, y = curr
            levels[x][y] = level
            for dx, dy in dirs:
                i,j = x+dx, y+dy 
                if i < 0 or i >= m or j < 0 or j >= n or (i,j) == parent or grid[i][j] == 0:
                    continue
                elif levels[i][j] == -1:
                    levels[x][y] = min(levels[x][y], dfs((i,j), level+1, (x,y)))
                else:
                    levels[x][y] = min(levels[x][y], levels[i][j])
                if levels[i][j] >= level + 1:
                    hasCritial[0] = True
            return levels[x][y]
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    if levels[i][j] == -1:
                        dfs((i,j), 0, (-1,-1))
        if hasCritial[0]: return 1
        return 2
                    
        

if __name__ == "__main__":
    grid = [[0,1,1,0],[0,1,1,0],[0,0,0,0]]
    print(Solution().minDays(grid))
    grid = [[1,1]]
    print(Solution().minDays(grid))
    grid = [[1,1,1]]
    print(Solution().minDays(grid))
    grid = [[1,1],[1,0]]
    print(Solution().minDays(grid))
    grid = [[1,1,0,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,1,1,1]]
    print(Solution().minDays(grid))
    grid = [[1,1,0,1,1],[1,1,1,1,1],[1,1,0,1,1],[1,1,0,1,1]]
    print(Solution().minDays(grid))
    grid = [[0,0,0],[0,1,0],[0,0,0]]
    print(Solution().minDays(grid))
    grid = [[0,1,0,1,1],
            [1,1,1,1,1],
            [1,1,1,1,1],
            [1,1,1,1,0]]
    print(Solution().minDays(grid))

