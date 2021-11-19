'''

-Medium-

In a given 2D binary array grid, there are two islands.  (An island 
is a 4-directionally connected group of 1s not connected to any other 1's.)

Now, we may change 0s to 1s so as to connect the two islands together 
to form 1 island.

Return the smallest number of 0s that must be flipped.  (It is guaranteed 
that the answer is at least 1.)

 

Example 1:

Input: grid = [[0,1],[1,0]]
Output: 1
Example 2:

Input: grid = [[0,1,0],[0,0,0],[0,0,1]]
Output: 2
Example 3:

Input: grid = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
Output: 1
 

Constraints:

2 <= grid.length == grid[0].length <= 100
grid[i][j] == 0 or grid[i][j] == 1

'''

from typing import List

from collections import deque
class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]
#        visited = [[False]*n  for _ in range(m)] 
        def dfs(i, j):            
            for di, dj in dirs:
                x, y = i+di, j+dj
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    grid[x][y] = 2
                    dfs(x,y)
        def modify():
            for i in range(m):
                for j in range(n): 
                    if grid[i][j] == 1:
                        grid[i][j] = 2
                        dfs(i,j)
                        return
        modify()
        print(grid)
        que = deque()
        for i in range(m):
           for j in range(n): 
                if grid[i][j] == 2:
                   que.append((i,j,0))
        while que:
            i, j, steps = que.popleft()
            for di, dj in dirs:
                x, y = i+di, j+dj
                if not (0 <= x < m and 0 <= y < n):
                    continue
                if grid[x][y] == 0:
                    grid[x][y] = 2
                    que.append((x, y, steps+1))
                elif grid[x][y] == 1:
                    return steps    
        return 1

        
            

        

if __name__ == "__main__":
    grid =  [[1,1,1,1,1],
             [1,0,0,0,1],
             [1,0,1,0,1],
             [1,0,0,0,1],
             [1,1,1,1,1]]
    print(Solution().shortestBridge(grid))
    grid = [[0,1,0],[0,0,0],[0,0,1]]
    print(Solution().shortestBridge(grid))
