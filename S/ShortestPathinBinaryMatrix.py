'''

-Medium-
*BFS*


In an N by N square grid, each cell is either empty (0) or blocked (1).

A clear path from top-left to bottom-right has length k if and only if it is 
composed of cells C_1, C_2, ..., C_k such that:

Adjacent cells C_i and C_{i+1} are connected 8-directionally (ie., they are 
different and share an edge or corner)
C_1 is at location (0, 0) (ie. has value grid[0][0])
C_k is at location (N-1, N-1) (ie. has value grid[N-1][N-1])
If C_i is located at (r, c), then grid[r][c] is empty (ie. grid[r][c] == 0).
Return the length of the shortest such clear path from top-left to bottom-right.  
If such a path does not exist, return -1.

 

Example 1:

Input: [[0,1],[1,0]]


Output: 2

Example 2:

Input: [[0,0,0],[1,1,0],[1,1,0]]


Output: 4

 

Note:

1 <= grid.length == grid[0].length <= 100
grid[r][c] is 0 or 1


'''
from collections import deque

class Solution(object):
    def shortestPathBinaryMatrix(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        n = len(grid)
        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1
        dirs = [(-1,0), (1,0), (0,-1), (0,1), 
                (-1,-1), (-1,1), (1,-1), (1,1)]
        visited = [[False for _ in range(n)] for _ in range(n)]
        dq = deque([((0,0),0)])
        while dq:
            (i,j), steps = dq.popleft()
            if i == n-1 and j == n-1:
                return steps+1
            for dx, dy in dirs:
                x, y = i+dx, j+dy
                if x < 0 or x > n-1 or y < 0 or y > n-1 or grid[x][y] == 1:
                    continue
                if not visited[x][y]:
                    visited[x][y] = True
                    dq.append(((x,y),steps+1))
        return -1

        
if __name__ == '__main__':   
    print(Solution().shortestPathBinaryMatrix([[0,0,0],[1,1,0],[1,1,0]]))