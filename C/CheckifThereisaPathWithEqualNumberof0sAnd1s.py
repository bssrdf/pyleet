'''
-Medium-



You are given a 0-indexed m x n binary matrix grid. You can move from a cell (row, col) to any of the cells (row + 1, col) or (row, col + 1).

Return true if there is a path from (0, 0) to (m - 1, n - 1) that visits an equal number of 0's and 1's. Otherwise return false.

 

Example 1:



Input: grid = [[0,1,0,0],[0,1,0,0],[1,0,1,0]]
Output: true
Explanation: The path colored in blue in the above diagram is a valid path because we have 3 cells with a value of 1 and 3 with a value of 0. Since there is a valid path, we return true.
Example 2:



Input: grid = [[1,1,0],[0,0,1],[1,0,0]]
Output: false
Explanation: There is no path in this grid with an equal number of 0's and 1's.
 

Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 100
grid[i][j] is either 0 or 1.


'''

from typing import List
from collections import deque
from functools import lru_cache

class Solution:
    def isThereAPath(self, grid: List[List[int]]) -> bool:
        # TLE
        m, n = len(grid), len(grid[0])
        que = deque([(-1 if grid[0][0] == 0 else 1, 0, 0)])
        while que:
            val, x, y = que.popleft()
            if x == m-1 and y == n-1 and val == 0:
                return True
            for dx, dy in [(0, 1), (1, 0)]:
                i, j = x + dx, y + dy
                if 0 <= i < m and 0 <= j < n:
                    que.append((val + (-1 if grid[i][j] == 0 else 1), i, j))
        return False            
    
    def isThereAPath2(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])
        s = m + n - 1
        if s & 1: return False
        s >>= 1
        dp = [[set() for _ in range(n)] for _ in range(m)]
        dp[0][0].add(-1 if grid[0][0] == 0 else 1)
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: continue
                if j > 0:
                    for x in dp[i][j-1]:
                        k = x + (-1 if grid[i][j] == 0 else 1)
                        if k > s or k < -s : continue
                        dp[i][j].add(k)
                if i > 0:
                    for x in dp[i-1][j]:
                        k = x + (-1 if grid[i][j] == 0 else 1)
                        if k > s or k < -s : continue
                        dp[i][j].add(k)
        return 0 in dp[m-1][n-1]
    
    def isThereAPath3(self, grid: List[List[int]]) -> bool:
        @lru_cache(None)
        def dfs(i, j, k):
            if i >= m or j >= n:
                return False
            k += grid[i][j]
            if k > s or i + j + 1 - k > s:
                return False
            if i == m - 1 and j == n - 1:
                return k == s
            return dfs(i + 1, j, k) or dfs(i, j + 1, k)

        m, n = len(grid), len(grid[0])
        s = m + n - 1
        if s & 1:
            return False
        s >>= 1
        return dfs(0, 0, 0)


import time
import random
if __name__ == "__main__":
    grid = [[0,1,0,0],[0,1,0,0],[1,0,1,0]]
    print(Solution().isThereAPath(grid=grid))
    print(Solution().isThereAPath2(grid=grid))
    grid = [[1,1,0],[0,0,1],[1,0,0]]
    print(Solution().isThereAPath(grid=grid))
    print(Solution().isThereAPath2(grid=grid))
    m, n = 100, 99
    grid = []
    for i in range(m):
        t = []
        for j in range(n):
            t.append(1 if random.random() > 0.7 else 0)
        grid.append(t)
    start = time.time()
    print(Solution().isThereAPath2(grid=grid))
    end = time.time()
    print('elapsed time: ', end-start)
    start = time.time()
    print(Solution().isThereAPath3(grid=grid))
    end = time.time()
    print('elapsed time: ', end-start)
        


