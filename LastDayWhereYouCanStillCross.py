'''
-Hard-

There is a 1-based binary matrix where 0 represents land and 1 represents water. 
You are given integers row and col representing the number of rows and columns 
in the matrix, respectively.

Initially on day 0, the entire matrix is land. However, each day a new cell 
becomes flooded with water. You are given a 1-based 2D array cells, where 
cells[i] = [ri, ci] represents that on the ith day, the cell on the rith row 
and cith column (1-based coordinates) will be covered with water (i.e., changed to 1).

You want to find the last day that it is possible to walk from the top to 
the bottom by only walking on land cells. You can start from any cell in the 
top row and end at any cell in the bottom row. You can only travel in the 
four cardinal directions (left, right, up, and down).

Return the last day where it is possible to walk from the top to the bottom 
by only walking on land cells.

 

Example 1:


Input: row = 2, col = 2, cells = [[1,1],[2,1],[1,2],[2,2]]
Output: 2
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 2.
Example 2:


Input: row = 2, col = 2, cells = [[1,1],[1,2],[2,1],[2,2]]
Output: 1
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 1.
Example 3:


Input: row = 3, col = 3, cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
Output: 3
Explanation: The above image depicts how the matrix changes each day starting from day 0.
The last day where it is possible to cross from top to bottom is on day 3.
 

Constraints:

2 <= row, col <= 2 * 104
4 <= row * col <= 2 * 104
cells.length == row * col
1 <= ri <= row
1 <= ci <= col
All the values of cells are unique.


'''


from typing import List

class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        m, n = row, col
        dirs = [(-1,0), (1,0), (0,-1), (0,1)]        
        par_up = [x*n+y for x in range(m) for y in range(n)]
        par_dn = [x*n+y for x in range(m) for y in range(n)]
        grid = [[1]*n for _ in range(m)]
        def row(idx):
            return idx//n
        def find(par, x):
            while x != par[x]:
                par[x] = par[par[x]]
                x = par[x]
            return x
        def union(x, y, par, up):
            fx, fy = find(par, x), find(par, y)
            if fx != fy:
                if up:
                    if row(fx) < row(fy):
                        par[fy] = fx
                    else:
                        par[fx] = fy
                else:
                    if row(fx) > row(fy):
                        par[fy] = fx
                    else:
                        par[fx] = fy

        for k in range(len(cells)-1, -1, -1):
            i, j = cells[k][0]-1,cells[k][1]-1 
            grid[i][j] = 0
            idx1 = i*n+j
            for dx,dy in dirs:
                x, y = i+dx, j+dy
                if 0<=x<m and 0<=y<n and grid[x][y] == 0:
                    idx2 = x*n+y
                    union(idx1, idx2, par_up, True)
                    union(idx1, idx2, par_dn, False)
            to_top, to_bot = False, False
            for dx, dy in dirs:
                x, y = i+dx, j+dy
                if 0<=x<m and 0<=y<n and grid[x][y] == 0:
                    idx2 = x*n+y
                    head = find(par_up, idx2)
                    if row(head) == 0: to_top = True
                    head = find(par_dn, idx2)
                    if row(head) == m-1: to_bot = True
            if to_top and to_bot:
                return k
        return -1




if __name__ == "__main__":
    row = 2; col = 2
    cells = [[1,1],[2,1],[1,2],[2,2]]
    print(Solution().latestDayToCross(row, col, cells))
    row = 2; col = 2
    cells = [[1,1],[1,2],[2,1],[2,2]]
    print(Solution().latestDayToCross(row, col, cells))
    row = 3; col = 3; 
    cells = [[1,2],[2,1],[3,3],[2,2],[1,1],[1,3],[2,3],[3,2],[3,1]]
    print(Solution().latestDayToCross(row, col, cells))
