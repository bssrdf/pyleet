'''
-Medium-

*BFS*

Given an m x n matrix of non-negative integers representing the height of each unit cell 
in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the 
"Atlantic ocean" touches the right and bottom edges.

Water can only flow in four directions (up, down, left, or right) from a cell to another 
one with height equal or lower.

Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.

Note:

The order of returned grid coordinates does not matter.
Both m and n are less than 150.
 

Example:

Given the following 5x5 matrix:

  Pacific ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * Atlantic

Return:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in 
above matrix).

'''
from collections import deque

class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix or not matrix[0]: return []
        m, n = len(matrix), len(matrix[0])
        res = []
        visited_p = [[False for _ in range(n)] for _ in range(m)]        
        visited_a = [[False for _ in range(n)] for _ in range(m)]        
        qp, qa = deque(), deque()
        for i in range(m):
            qp.append((i,0))
            visited_p[i][0] = True
            qa.append((i,n-1))
            visited_a[i][n-1] = True
        for j in range(n):
            qp.append((0,j))
            visited_p[0][j] = True
            qa.append((m-1,j))
            visited_a[m-1][j] = True
        def bfs(q, visited):
            while q:
                i,j = q.popleft()    
                for di, dj in [(-1,0), (1,0), (0,-1), (0,1)]:
                    x, y = i+di, j+dj 
                    if x < 0 or x >= m or y < 0 or y >= n or visited[x][y] or \
                       matrix[x][y] < matrix[i][j]: continue 
                    visited[x][y] = True
                    q.append((x,y))
        bfs(qp, visited_p)
        bfs(qa, visited_a)
        for i in range(m):
            for j in range(n):
                if visited_p[i][j] and visited_a[i][j]:
                    res.append([i,j])
        return res
        
if __name__ == '__main__':
    grid = [[1,   2,   2,   3,   5],
            [3,   2,   3,   4,   4], 
            [2,   4,   5,   3,   1],  
            [6,   7,   1,   4,   5],  
            [5,   1,   1,   2,   4]] 
    print(Solution().pacificAtlantic(grid))

