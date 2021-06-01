'''
-Medium-
*DFS*
*Union Find*

Given a non-empty 2D array grid of 0's and 1's, an island is a group of 1's 
(representing land) connected 4-directionally (horizontal or vertical.) You 
may assume all four edges of the grid are surrounded by water.

Find the maximum area of an island in the given 2D array. (If there is no 
island, the maximum area is 0.)

Example 1:

[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
Given the above grid, return 6. Note the answer is not 11, because the 
island must be connected 4-directionally.

Example 2:

[[0,0,0,0,0,0,0,0]]
Given the above grid, return 0.
Note: The length of each dimension in the given grid does not exceed 50.


'''

class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        roots = [-1]*(m*n)
        ranks = [1]*(m*n)
        def find(roots, i):        
            while roots[i] != i:            
               roots[i] = roots[roots[i]] 
               i = roots[i]
            return i        
        def union(i,j):
            x, y = find(roots, i), find(roots, j)
            if x != y: 
                if ranks[x] < ranks[y]:
                    roots[x] = y 
                    ranks[y] += ranks[x]
                else:
                    roots[y] = x 
                    ranks[x] += ranks[y]
        dirs = [(-1,0), (0,-1), (1,0), (0,1)]
        cnt = 0
        for i in range(m):
            for j in range(n):
                roots[i*n+j] = i*n+j                
                if grid[i][j] == 1: cnt += 1
        for i in range(m):
            for j in range(n):                
                if grid[i][j] == 1:
                    idx = i*n+j
                    for r,c in dirs:
                        i1,j1=i+r,j+c
                        if i1<0 or i1>=m or j1<0 or j1>=n:
                            continue
                        if grid[i1][j1] == 1:
                            idx1 = n*i1+j1
                            union(idx, idx1)
        res = 0       
        for i in range(m*n):
            res = max(res, ranks[i])                             
        return 0 if cnt == 0 else res
    
    def maxAreaOfIslandDFS(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dirs = [(-1,0), (0,-1), (1,0), (0,1)]
        area = 0
        def dfs(x, y):
            grid[x][y] = 2
            cur = 1
            for r,c in dirs:
                i1,j1=x+r,y+c
                if i1<0 or i1>=m or j1<0 or j1>=n or grid[i1][j1] != 1:
                    continue
                cur += dfs(i1, j1)
            return cur
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1: 
                    area = max(area, dfs(i,j))
        return area




if __name__ == "__main__":
    grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
    print(Solution().maxAreaOfIsland(grid))
    print(Solution().maxAreaOfIslandDFS(grid))