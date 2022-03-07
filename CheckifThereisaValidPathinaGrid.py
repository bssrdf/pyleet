'''
-Medium-

*DFS*
*BFS*
*Union Find*

You are given an m x n grid. Each cell of grid represents a street. The 
street of grid[i][j] can be:

1 which means a street connecting the left cell and the right cell.
2 which means a street connecting the upper cell and the lower cell.
3 which means a street connecting the left cell and the lower cell.
4 which means a street connecting the right cell and the lower cell.
5 which means a street connecting the left cell and the upper cell.
6 which means a street connecting the right cell and the upper cell.

You will initially start at the street of the upper-left cell (0, 0). 
A valid path in the grid is a path that starts from the upper left cell (0, 0) 
and ends at the bottom-right cell (m - 1, n - 1). The path should only follow the streets.

Notice that you are not allowed to change any street.

Return true if there is a valid path in the grid or false otherwise.

 

Example 1:


Input: grid = [[2,4,3],[6,5,2]]
Output: true
Explanation: As shown you can start at cell (0, 0) and visit all the cells of the grid to reach (m - 1, n - 1).
Example 2:


Input: grid = [[1,2,1],[1,2,1]]
Output: false
Explanation: As shown you the street at cell (0, 0) is not connected with any street of any other cell and you will get stuck at cell (0, 0)
Example 3:

Input: grid = [[1,1,2]]
Output: false
Explanation: You will get stuck at cell (0, 1) and you cannot reach cell (0, 2).
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
1 <= grid[i][j] <= 6

'''

from typing import List
from collections import deque
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        m, n, A = len(grid), len(grid[0]), grid
        uf = {(i,j):(i,j) for i in range(-1, m * 2) for j in range(-1, n * 2)}
        def find(x):
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]
        def merge(i,j,di,dj):
            uf[find((i,j))] = find((i+di, j+dj))
        for i in range(m):
            for j in range(n):
                if A[i][j] in [2, 5, 6]: merge(i * 2, j * 2, -1, 0)
                if A[i][j] in [1, 3, 5]: merge(i * 2, j * 2, 0, -1)
                if A[i][j] in [2, 3, 4]: merge(i * 2, j * 2, 1, 0)
                if A[i][j] in [1, 4, 6]: merge(i * 2, j * 2, 0, 1)
        return find((0, 0)) == find((m * 2 - 2, n * 2 - 2))

    def hasValidPath2(self, grid: List[List[int]]) -> bool:
        '''
        This is the entire idea/ difficulty of the question

        When traversing from one cell to the next. the next cell must have a direction 
        that is the opposite of the direction we are moving in for the cells to be 
        connected. For example, if we are moving one unit to the right, then from 
        the next cell it must be possible to go one unit to the left, otherwise it's 
        not actually connected.

        So you need to

        1. Limit the degrees of freedom of each cell from Up, Down, Left, Right to 
           the 2 directions that are valid for this cells value.
        2. To have a valid path from cell A to cell B you should be able to move from 
           cell A to cell B and be able to move from cell B to cell A too.
        3. Then proceed with a normal DFS or BFS to check if there is a path between 
            cell (0,0) and cell (m-1, n-1)
        '''
        if not grid: return True
        directions = {1: [(0,-1),(0,1)],
                      2: [(-1,0),(1,0)],
                      3: [(0,-1),(1,0)],
                      4: [(0,1),(1,0)],
                      5: [(0,-1),(-1,0)],
                      6: [(0,1),(-1,0)]}
        visited = set()
        goal = (len(grid)-1, len(grid[0]) - 1)
        def dfs(i, j):
            visited.add((i,j))
            if (i,j) == goal:
                return True
            for d in directions[grid[i][j]]:
                ni, nj = i+d[0], j+d[1]
                if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and \
                        (ni, nj) not in visited and  \
                        (-d[0], -d[1]) in directions[grid[ni][nj]]:
                    if dfs(ni, nj):
                        return True
            return False
        return dfs(0,0)

    def hasValidPath3(self, grid: List[List[int]]) -> bool:      
        m, n, A = len(grid), len(grid[0]), grid  
        if not grid: return True
        directions = {1: [(0,-1),(0,1)],
                      2: [(-1,0),(1,0)],
                      3: [(0,-1),(1,0)],
                      4: [(0,1),(1,0)],
                      5: [(0,-1),(-1,0)],
                      6: [(0,1),(-1,0)]}
        visited = [[False]*n for _ in range(m)]
        que = deque([(0,0)])
        visited[0][0] = True
        while que:
            x, y = que.popleft()
            for dx, dy in directions[A[x][y]]:
                nx, ny = x + dx, y + dy  
                if (nx < 0 or nx >= m or ny < 0 or ny >= n or visited[nx][ny]): continue
                for bd in directions[A[nx][ny]]:
                    if nx + bd[0] == x and ny + bd[1] == y:
                        visited[nx][ny] = True
                        que.append((nx, ny))
        return visited[m-1][n-1]
        
        


if __name__ == "__main__":
    grid = [[2,4,3],[6,5,2]]
    print(Solution().hasValidPath(grid))