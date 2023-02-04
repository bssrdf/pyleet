'''
-Medium-


You are given two m x n binary matrices grid1 and grid2 containing only 0's (representing water) 
and 1's (representing land). An island is a group of 1's connected 4-directionally 
(horizontal or vertical). Any cells outside of the grid are considered water cells.

An island in grid2 is considered a sub-island if there is an island in grid1 that contains 
all the cells that make up this island in grid2.

Return the number of islands in grid2 that are considered sub-islands.

 

Example 1:


Input: grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]], grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
Output: 3
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are three sub-islands.
Example 2:


Input: grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]], grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
Output: 2 
Explanation: In the picture above, the grid on the left is grid1 and the grid on the right is grid2.
The 1s colored red in grid2 are those considered to be part of a sub-island. There are two sub-islands.
 

Constraints:

m == grid1.length == grid2.length
n == grid1[i].length == grid2[i].length
1 <= m, n <= 500
grid1[i][j] and grid2[i][j] are either 0 or 1.

'''
from typing import List

class Solution:
    def countSubIslands(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]
        isSub, cnt = [True], 0
        def dfs1(grid, i, j):       
            grid[i][j] = 2
            for di,dj in dirs:
                x, y = i+di, j+dj
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    dfs1(grid, x, y)
        
        def dfs2(i, j):            
            if grid1[i][j] != 2: isSub[0] = False    
            grid2[i][j] = 2
            for di,dj in dirs:
                x, y = i+di, j+dj
                if 0 <= x < m and 0 <= y < n and grid2[x][y] == 1:
                    dfs2(x, y)
        for i in range(m):
            for j in range(n):
                if grid1[i][j] == 1:
                    dfs1(grid1, i, j)
        for i in range(m):
            for j in range(n):
                if grid2[i][j] == 1:
                    isSub = [True]
                    dfs2(i, j)
                    if isSub[0]: cnt += 1
        return cnt 

    def countSubIslandsUF(self, grid1: List[List[int]], grid2: List[List[int]]) -> int:
        m, n = len(grid1), len(grid1[0])
        roots = [-1]*(m*n)
        cnt = 0
        dirs = [(-1,0), (0,-1), (1,0), (0,1)]
        def find(i):
            while roots[i] != i:
                roots[i] = roots[roots[i]]
                i = roots[i]
            return i
        isSub = [True]
        def dfs(grid, i, j):
            idx = i*n+j
            if roots[idx] == -1: 
                isSub[0] = False            
            grid[i][j] = 2
            for di,dj in dirs:
                x, y = i+di, j+dj
                if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                    dfs(grid, x, y)

        for i in range(m):
            for j in range(n):
                if grid1[i][j] == 1:
                   roots[i*n+j] = i*n+j
        for i in range(m):
            for j in range(n):                
                if grid1[i][j] == 1:
                    idx = i*n+j
                    for r,c in dirs:
                        i1,j1=i+r,j+c
                        if i1<0 or i1>=m or j1<0 or j1>=n:
                            continue
                        if grid1[i1][j1] == 1:
                            idx1 = n*i1+j1
                            x, y = find(idx), find(idx1) 
                            if x != y:
                                roots[x] = y
        for i in range(m):
            for j in range(n):                
                if grid2[i][j] == 1:
                    isSub = [True]
                    dfs(grid2, i, j)
                    if isSub[0]: cnt += 1
        return cnt 
        
        
        
        


if __name__ == "__main__":
    grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
    grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
    print(Solution().countSubIslands(grid1, grid2))
    grid1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
    grid2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
    print(Solution().countSubIslandsUF(grid1, grid2))
    grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
    grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
    print(Solution().countSubIslands(grid1, grid2))
    grid1 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
    grid2 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
    print(Solution().countSubIslandsUF(grid1, grid2))