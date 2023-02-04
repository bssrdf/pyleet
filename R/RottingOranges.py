'''
-Medium-
*BFS*


You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. 
If this is impossible, return -1.

 

Example 1:


Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4
Example 2:

Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because 
rotting only happens 4-directionally.

Example 3:

Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 10
grid[i][j] is 0, 1, or 2.


'''

from typing import List

from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        A = grid
        que = deque()
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        fresh = 0
        for i in range(m):
            for j in range(n):
                if A[i][j] == 2:
                    que.append((i,j))
                if A[i][j] == 1:
                    fresh += 1
        res = 0
        if fresh == 0: return res
        if not que: return -1
        while que:
            nxt = deque()
            for _ in range(len(que)):
                (i, j) = que.popleft()
                for di, dj  in dirs:
                    x, y = i + di, j + dj
                    if 0 <= x < m and 0 <= y < n and A[x][y] == 1:
                        A[x][y] = 2
                        fresh -= 1
                        nxt.append((x,y)) 
            que = nxt
            res += 1    
        return -1 if fresh > 0 else res-1
        
        

if __name__ == "__main__":
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    print(Solution().orangesRotting(grid))
    grid = [[2,1,1],[0,1,1],[1,0,1]]
    print(Solution().orangesRotting(grid))
    grid = [[0,2]]
    print(Solution().orangesRotting(grid))