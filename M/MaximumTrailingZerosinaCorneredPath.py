'''
-Medium-
*Prefix Sum*


You are given a 2D integer array grid of size m x n, where each cell contains a positive integer.

A cornered path is defined as a set of adjacent cells with at most one turn. More specifically, the path should exclusively move either horizontally or vertically up to the turn (if there is one), without returning to a previously visited cell. After the turn, the path will then move exclusively in the alternate direction: move vertically if it moved horizontally, and vice versa, also without returning to a previously visited cell.

The product of a path is defined as the product of all the values in the path.

Return the maximum number of trailing zeros in the product of a cornered path found in grid.

Note:

Horizontal movement means moving in either the left or right direction.
Vertical movement means moving in either the up or down direction.
 

Example 1:


Input: grid = [[23,17,15,3,20],[8,1,20,27,11],[9,4,6,2,21],[40,9,1,10,6],[22,7,4,5,3]]
Output: 3
Explanation: The grid on the left shows a valid cornered path.
It has a product of 15 * 20 * 6 * 1 * 10 = 18000 which has 3 trailing zeros.
It can be shown that this is the maximum trailing zeros in the product of a cornered path.

The grid in the middle is not a cornered path as it has more than one turn.
The grid on the right is not a cornered path as it requires a return to a previously visited cell.
Example 2:


Input: grid = [[4,3,2],[7,6,1],[8,8,8]]
Output: 0
Explanation: The grid is shown in the figure above.
There are no cornered paths in the grid that result in a product with a trailing zero.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 105
1 <= m * n <= 105
1 <= grid[i][j] <= 1000



'''

from typing import List

class Solution:
    def maxTrailingZeros(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        left = [[[0, 0] for _ in range(n)] for _ in range(m)]
        top  = [[[0, 0] for _ in range(n)] for _ in range(m)]
        
        def helper(num):
            a, b = 0, 0
            while num % 2 == 0:
                num //= 2
                a += 1
            while num % 5 == 0:
                num //= 5
                b += 1
            return [a, b]
        
        for i in range(m):
            for j in range(n):
                if j == 0:
                    left[i][j] = helper(A[i][j])
                else:
                    a, b = helper(A[i][j])
                    left[i][j][0] = left[i][j - 1][0] + a
                    left[i][j][1] = left[i][j - 1][1] + b
        for j in range(n):
            for i in range(m):
                if i == 0:
                    top[i][j] = helper(A[i][j])
                else:
                    a, b, = helper(A[i][j])
                    top[i][j][0] = top[i - 1][j][0] + a               
                    top[i][j][1] = top[i - 1][j][1] + b


        ans = 0
        for i in range(m):
            for j in range(n):
                a, b = top[m - 1][j]
                d, e = left[i][n - 1]
                x, y = helper(A[i][j])
                a1, b1 = top[i][j]
                a2, b2 = left[i][j]
                tmp = [a1 + a2 - x, b1 + b2 - y]
                ans = max(ans, min(tmp))
                tmp = [d - a2 + a1, e - b2 + b1]
                ans = max(ans, min(tmp))             
                tmp = [a - a1 + a2, b - b1 + b2]
                ans = max(ans, min(tmp))
                tmp = [a + d - a1 - a2 + x, b + e - b1 - b2 + y]
                ans = max(ans, min(tmp))
                
        return ans