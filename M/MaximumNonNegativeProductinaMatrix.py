'''

-Medium-
*DP*

You are given a m x n matrix grid. Initially, you are located at the top-left corner (0, 0), and in each step, you can only move right or down in the matrix.

Among all possible paths starting from the top-left corner (0, 0) and ending in the bottom-right corner (m - 1, n - 1), find the path with the maximum non-negative product. The product of a path is the product of all integers in the grid cells visited along the path.

Return the maximum non-negative product modulo 109 + 7. If the maximum product is negative, return -1.

Notice that the modulo is performed after getting the maximum product.

 

Example 1:


Input: grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
Output: -1
Explanation: It is not possible to get non-negative product in the path from (0, 0) to (2, 2), so return -1.
Example 2:


Input: grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
Output: 8
Explanation: Maximum non-negative product is shown (1 * 1 * -2 * -4 * 1 = 8).
Example 3:


Input: grid = [[1,3],[0,-4]]
Output: 0
Explanation: Maximum non-negative product is shown (1 * 0 * -4 = 0).
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 15
-4 <= grid[i][j] <= 4


'''


from typing import List
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        pos = [[0]*(n+1) for _ in range(m+1)]
        neg = [[0]*(n+1) for _ in range(m+1)]
        for j in range(n+1):
            pos[0][j] = -float('inf') 
            neg[0][j] = float('inf') 
        for i in range(m+1):
            pos[i][0] = -float('inf') 
            neg[i][0] = float('inf') 
        pos[1][0] = 1
        pos[0][1] = 1
        neg[1][0] = 1
        neg[0][1] = 1
        for i in range(1, m+1):
            for j in range(1, n+1):
                val = grid[i-1][j-1]
                if  val > 0:
                    pos[i][j] = max(pos[i-1][j], pos[i][j-1])*val
                    neg[i][j] = min(neg[i-1][j], neg[i][j-1])*val
                elif val < 0:
                    pos[i][j] = min(neg[i-1][j], neg[i][j-1])*val
                    neg[i][j] = max(pos[i-1][j], pos[i][j-1])*val
                else:
                    pos[i][j] = 0
                    neg[i][j] = 0
        return -1 if pos[m][n] < 0 else pos[m][n]%(10**9+7)            






if __name__ == "__main__":
    grid = [[-1,-2,-3],[-2,-3,-3],[-3,-3,-2]]
    print(Solution().maxProductPath(grid))
    grid = [[1,-2,1],[1,-2,1],[3,-4,1]]
    print(Solution().maxProductPath(grid))
    grid = [[1,3],[0,-4]]
    print(Solution().maxProductPath(grid))

        