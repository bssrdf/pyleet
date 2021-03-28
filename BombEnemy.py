'''

-Medium-

Given a 2D grid, each cell is either a wall 'W', an enemy 'E' or empty '0' (the number zero), 
return the maximum enemies you can kill using one bomb.
The bomb kills all the enemies in the same row and column from the planted point until it 
hits the wall since the wall is too strong to be destroyed.

You can only put the bomb at an empty cell.

Example1

Input:
grid =[
     "0E00",
     "E0WE",
     "0E00"
]
Output: 3
Explanation:
Placing a bomb at (1,1) kills 3 enemies
Example2

Input:
grid =[
     "0E00",
     "EEWE",
     "0E00"
]
Output: 2
Explanation:
Placing a bomb at (0,0) or (0,3) or (2,0) or (2,3) kills 2 enemies

'''

class Solution:
    """
    @param grid: Given a 2D grid, each cell is either 'W', 'E' or '0'
    @return: an integer, the maximum enemies you can kill using one bomb
    """
    def maxKilledEnemies(self, grid):
        # write your code here
        if not grid: return 0
        m, n = len(grid), len(grid[0])
        row_e, col_e = [0]*m, [0]*n
        row_w, col_w = [0]*m, [0]*n
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 'W':
                    row_w[i] += 1
                    col_w[j] += 1
                if grid[i][j] == 'E':
                    row_e[i] += 1
                    col_e[j] += 1
        ans = 0
        def search_row(i, j):            
            k, cnt = i-1, 0
            while k >= 0 and grid[k][j] != 'W':
                if grid[k][j] == 'E': cnt += 1
                k -= 1
            k = i+1
            while k < m and grid[k][j] != 'W':
                if grid[k][j] == 'E': cnt += 1
                k += 1
            return cnt
        def search_col(i, j):            
            k, cnt = j-1, 0
            while k >= 0 and grid[i][k] != 'W':
                if grid[i][k] == 'E': cnt += 1
                k -= 1
            k = j+1
            while k < n and grid[i][k] != 'W':
                if grid[i][k] == 'E': cnt += 1
                k += 1
            return cnt
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '0':
                    cnt = 0
                    if row_w[i] == 0 and col_w[j] == 0:
                        cnt = row_e[i] + col_e[j]
                    elif row_w[i] == 0:                        
                        cnt = search_row(i,j) + row_e[i]
                    elif col_w[j] == 0:
                        cnt = search_col(i,j) + col_e[j] 
                    else:
                        cnt = search_row(i,j) + search_col(i,j)
                    ans = max(ans, cnt)
        return ans
                    
                        
                


if __name__ == "__main__":
    grid =[
     "0E00",
     "E0WE",
     "0E00"
          ]
    print(Solution().maxKilledEnemies(grid))
    grid =[
     "0E00",
     "EEWE",
     "0E00"
    ]
    print(Solution().maxKilledEnemies(grid))
    grid = ['0E']
    print(Solution().maxKilledEnemies(grid))
