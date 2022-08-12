'''

-Hard-


You are given an m x n integer matrix grid containing distinct positive integers.

You have to replace each integer in the matrix with a positive integer satisfying the following conditions:

The relative order of every two elements that are in the same row or column should stay the same after the replacements.
The maximum number in the matrix after the replacements should be as small as possible.
The relative order stays the same if for all pairs of elements in the original matrix such that grid[r1][c1] > grid[r2][c2] where either r1 == r2 or c1 == c2, then it must be true that grid[r1][c1] > grid[r2][c2] after the replacements.

For example, if grid = [[2, 4, 5], [7, 3, 9]] then a good replacement could be either grid = [[1, 2, 3], [2, 1, 4]] or grid = [[1, 2, 3], [3, 1, 4]].

Return the resulting matrix. If there are multiple answers, return any of them.

 

Example 1:



Input: grid = [[3,1],[2,5]]
Output: [[2,1],[1,2]]
Explanation: The above diagram shows a valid replacement.
The maximum number in the matrix is 2. It can be shown that no smaller value can be obtained.
Example 2:

Input: grid = [[10]]
Output: [[1]]
Explanation: We replace the only number in the matrix with 1.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 1000
1 <= m * n <= 105
1 <= grid[i][j] <= 109
grid consists of distinct integers.



'''


class Solution:
    def maximumValue(self, grid):
        m, n = len(grid), len(grid[0])
        A = []
        for i in range(m):
            for j in range(n):
                A.append((grid[i][j], i, j))
        row, col = [1]*m, [1]*n        
        A.sort()
        for _, i, j in A:
            grid[i][j] = max(row[i], col[j])
            row[i] = grid[i][j] + 1
            col[j] = grid[i][j] + 1
        return grid

if __name__ == "__main__":
    grid =  [[3,1],[2,5]]
    print(Solution().maximumValue(grid))
    grid =  [[2, 4, 5],[7, 3, 9]]
    print(Solution().maximumValue(grid))
    grid =  [[10]]
    print(Solution().maximumValue(grid))


