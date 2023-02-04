'''

-Medium-
*DFS*

You are given a 0-indexed m x n binary matrix grid. You can move from a cell (row, col) to any of the cells (row + 1, col) or (row, col + 1) that has the value 1. The matrix is disconnected if there is no path from (0, 0) to (m - 1, n - 1).

You can flip the value of at most one (possibly none) cell. You cannot flip the cells (0, 0) and (m - 1, n - 1).

Return true if it is possible to make the matrix disconnect or false otherwise.

Note that flipping a cell changes its value from 0 to 1 or from 1 to 0.

 

Example 1:


Input: grid = [[1,1,1],[1,0,0],[1,1,1]]
Output: true
Explanation: We can change the cell shown in the diagram above. There is no path from (0, 0) to (2, 2) in the resulting grid.
Example 2:


Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
Output: false
Explanation: It is not possible to change at most one cell such that there is not path from (0, 0) to (2, 2).
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
grid[i][j] is either 0 or 1.
grid[0][0] == grid[m - 1][n - 1] == 1



'''

from typing import List
from collections import deque

class Solution:
    def isPossibleToCutPath(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0]) 
        def dfs(i, j): 
            if i == m-1 and j == n-1:
                return True
            if i >= m or j >= n or grid[i][j] == 0:
                return False
            grid[i][j] = 0                
            return dfs(i+1, j) or dfs(i,j+1)
 
                
        if not dfs(0,0): return True # cannot reach target, disconnected
        grid[0][0] = 1 # reset the start
        if not dfs(0,0): return True
        return False
    

    def isPossibleToCutPath2(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0]) 
        cnt = [[0]*n for _ in range(m)] 
        if m == 1 and n == 2 or m == 2 and n == 1:
            return False
        que = deque([(0,0)])
        while que:
            x,y = que.popleft()            
            if x+1 < m and grid[x+1][y] == 1:
                cnt[x+1][y] += 1
                que.append((x+1,y))
            if y+1 < n and grid[x][y+1] == 1:
                cnt[x][y+1] += 1
                que.append((x,y+1))
               
        
        for r in cnt:
            print(r)
        return cnt[m-1][n-1] <= 1
            
        


if __name__ == '__main__':
    print(Solution().isPossibleToCutPath2(grid = [[1,1,1],[1,0,0],[1,1,1]]))
    print(Solution().isPossibleToCutPath2(grid = [[1,1,1],[1,0,1],[1,1,1]]))
    # print(Solution().isPossibleToCutPath2(grid = [[1,1,0],[1,1,0],[1,1,1]]))
    # print(Solution().isPossibleToCutPath2(grid = [[1,1,1],[0,0,0],[1,1,1]]))
    # print(Solution().isPossibleToCutPath(grid = [[1,1]]))
    # print(Solution().isPossibleToCutPath(grid = [[1,1,1,0,0],[1,0,1,0,0],[1,1,1,1,1],[0,0,1,1,1],[0,0,1,1,1]]))
    print(Solution().isPossibleToCutPath2(grid = [[1,1,1,0,0],[1,0,1,0,0],[1,1,1,1,1],[0,0,1,1,1],[0,0,1,1,1]]))