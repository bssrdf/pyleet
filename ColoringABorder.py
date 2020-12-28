'''
-Medium-
*DFS*

Given a 2-dimensional grid of integers, each value in the grid represents the 
color of the grid square at that location.

Two squares belong to the same connected component if and only if they have 
the same color and are next to each other in any of the 4 directions.

The border of a connected component is all the squares in the connected 
component that are either 4-directionally adjacent to a square not in 
the component, or on the boundary of the grid (the first or last row or column).

Given a square at location (r0, c0) in the grid and a color, color the border 
of the connected component of that square with the given color, and return 
the final grid.

 

Example 1:

Input: grid = [[1,1],[1,2]], r0 = 0, c0 = 0, color = 3
Output: [[3, 3], [3, 2]]
Example 2:

Input: grid = [[1,2,2],[2,3,2]], r0 = 0, c0 = 1, color = 3
Output: [[1, 3, 3], [2, 3, 3]]
Example 3:

Input: grid = [[1,1,1],[1,1,1],[1,1,1]], r0 = 1, c0 = 1, color = 2
Output: [[2, 2, 2], [2, 1, 2], [2, 2, 2]]
 

Note:

1 <= grid.length <= 50
1 <= grid[0].length <= 50
1 <= grid[i][j] <= 1000
0 <= r0 < grid.length
0 <= c0 < grid[0].length
1 <= color <= 1000

'''

class Solution(object):
    def colorBorder(self, grid, r0, c0, color):
        """
        :type grid: List[List[int]]
        :type r0: int
        :type c0: int
        :type color: int
        :rtype: List[List[int]]
        """
        m = len(grid)
        n = len(grid[0])
        sc = grid[r0][c0]
        dirs = [(-1,0), (1,0), (0,1), (0,-1)]
        visited = [[False for _ in range(n)] for _ in range(m)]
        visited[r0][c0] = True
        def dfs(i, j):            
            for r,c in dirs:
                i1, j1 = i+r, j+c                
                if i1 < 0 or i1 > m-1 or j1 < 0 or j1 > n-1:
                    grid[i][j] = color 
                    continue           
                if visited[i1][j1]: continue
                if grid[i1][j1] != sc:
                   grid[i][j] = color                          
                else:
                    visited[i1][j1] = True
                    dfs(i1, j1)
        dfs(r0,c0)
        return grid

if __name__ == "__main__":
    print(Solution().colorBorder([[1,1],[1,2]],  0,  0, 3))
    print(Solution().colorBorder([[1,2,2],[2,3,2]],  0, 1, 3))
    print(Solution().colorBorder([[1,1,1],[1,1,1],[1,1,1]], 1, 1, 2))
    print(Solution().colorBorder([[1,2,1,2,1,2],
                                  [2,2,2,2,1,2],
                                  [1,2,2,2,1,2]], 1,3,1))