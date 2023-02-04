'''
-Easy-

You are given row x col grid representing a map where grid[i][j] = 1 represents 
land and grid[i][j] = 0 represents water.

Grid cells are connected horizontally/vertically (not diagonally). The grid 
is completely surrounded by water, and there is exactly one island (i.e., one 
or more connected land cells).

The island doesn't have "lakes", meaning the water inside isn't connected to the 
water around the island. One cell is a square with side length 1. The grid is 
rectangular, width and height don't exceed 100. Determine the perimeter of the 
island.
 
Example 1:


Input: grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
Output: 16
Explanation: The perimeter is the 16 yellow stripes in the image above.
Example 2:

Input: grid = [[1]]
Output: 4
Example 3:

Input: grid = [[1,0]]
Output: 4
 

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 100
grid[i][j] is 0 or 1.

'''

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dirs = [(-1,0), (0,-1), (1,0), (0,1)]
        res  = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    for r,c in dirs:
                        i1,j1=i+r,j+c
                        if i1<0 or i1>=m or j1<0 or j1>=n: 
                            res += 1
                            continue
                        if grid[i1][j1] == 0: res += 1
        return res




    
if __name__ == "__main__":
    grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
    print(Solution().islandPerimeter(grid))
    grid = [[1]]
    print(Solution().islandPerimeter(grid))
