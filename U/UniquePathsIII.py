'''
-Hard-

*Backtracking*
*DFS*


On a 2-dimensional grid, there are 4 types of squares:

1 represents the starting square.  There is exactly one starting square.
2 represents the ending square.  There is exactly one ending square.
0 represents empty squares we can walk over.
-1 represents obstacles that we cannot walk over.

Return the number of 4-directional walks from the starting square to the ending square, 
that walk over every non-obstacle square exactly once.

 

Example 1:

Input: [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)
Example 2:

Input: [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)
Example 3:

Input: [[0,1],[2,0]]
Output: 0
Explanation: 
There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
 

Note:

1 <= grid.length * grid[0].length <= 20

'''

class Solution(object):
    def uniquePathsIII(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        '''
        The solution to this problem shows a way to walk along a path that includes
        all cells exactly once that satify certain conditions. 
        '''
        res = [0]
        # here empty initialized to 1 to account for the start
        m, n, empty = len(grid), len(grid[0]), 1
        def dfs(x, y, empty):
            if not (0 <= x < m and 0 <= y < n and grid[x][y] >= 0): return
            if grid[x][y] == 2:
                # only the path passes every 0 will count, that's when empty becomes 0
                res[0] += empty == 0
                return 
            grid[x][y] = -2 # trick done on grid for backtracing 
            # explore in all 4 directions; each one could be a unique path             
            dfs(x+1, y, empty-1)
            dfs(x-1, y, empty-1)
            dfs(x, y+1, empty-1)
            dfs(x, y-1, empty-1)
            grid[x][y] = 0 # trick for backtracing
            return
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    x, y = (i, j)
                if grid[i][j] == 0:
                    empty += 1
        dfs(x, y, empty)
        return res[0]






if __name__ == "__main__":
    #print(Solution().uniquePathsIII([[1,0,0,0],[0,0,0,0],[0,0,2,-1]]))
    print(Solution().uniquePathsIII([[1,0],[0,2]]))
