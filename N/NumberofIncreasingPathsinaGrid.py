'''

-Hard-

*DP*

You are given an m x n integer matrix grid, where you can move from a cell to any adjacent cell in all 4 directions.

Return the number of strictly increasing paths in the grid such that you can start from any cell and end at any cell. Since the answer may be very large, return it modulo 109 + 7.

Two paths are considered different if they do not have exactly the same sequence of visited cells.

 

Example 1:


Input: grid = [[1,1],[3,4]]
Output: 8
Explanation: The strictly increasing paths are:
- Paths with length 1: [1], [1], [3], [4].
- Paths with length 2: [1 -> 3], [1 -> 4], [3 -> 4].
- Paths with length 3: [1 -> 3 -> 4].
The total number of paths is 4 + 3 + 1 = 8.
Example 2:

Input: grid = [[1],[2]]
Output: 3
Explanation: The strictly increasing paths are:
- Paths with length 1: [1], [2].
- Paths with length 2: [1 -> 2].
The total number of paths is 2 + 1 = 3.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
1 <= grid[i][j] <= 105


'''

from typing import List
from functools import lru_cache

class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        mod = 10**9 + 7
        @lru_cache(None)
        def dfs(i, j):
            # dfs(i,j) # of increasing paths starting at (i,j)
            res = 1
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                x, y = i + dx, j + dy
                if 0 <= x < m and 0 <= y < n and grid[x][y] > grid[i][j]:
                    res += dfs(x, y) % mod
            return res 
        return sum(dfs(x,y) for x in range(m) for y in range(n)) % mod


if __name__ == "__main__":
    print(Solution().countPaths(grid = [[1,1],[3,4]]))