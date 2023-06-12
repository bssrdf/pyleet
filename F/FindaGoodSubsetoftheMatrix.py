'''

-Hard-

You are given a 0-indexed m x n binary matrix grid.

Let us call a non-empty subset of rows good if the sum of each column of the subset is at most half of the length of the subset.

More formally, if the length of the chosen subset of rows is k, then the sum of each column should be at most floor(k / 2).

Return an integer array that contains row indices of a good subset sorted in ascending order.

If there are multiple good subsets, you can return any of them. If there are no good subsets, return an empty array.

A subset of rows of the matrix grid is any matrix that can be obtained by deleting some (possibly none or all) rows from grid.

 

Example 1:

Input: grid = [[0,1,1,0],[0,0,0,1],[1,1,1,1]]
Output: [0,1]
Explanation: We can choose the 0th and 1st rows to create a good subset of rows.
The length of the chosen subset is 2.
- The sum of the 0th column is 0 + 0 = 0, which is at most half of the length of the subset.
- The sum of the 1st column is 1 + 0 = 1, which is at most half of the length of the subset.
- The sum of the 2nd column is 1 + 0 = 1, which is at most half of the length of the subset.
- The sum of the 3rd column is 0 + 1 = 1, which is at most half of the length of the subset.
Example 2:

Input: grid = [[0]]
Output: [0]
Explanation: We can choose the 0th row to create a good subset of rows.
The length of the chosen subset is 1.
- The sum of the 0th column is 0, which is at most half of the length of the subset.
Example 3:

Input: grid = [[1,1,1],[1,1,1]]
Output: []
Explanation: It is impossible to choose any subset of rows to create a good subset.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m <= 104
1 <= n <= 5
grid[i][j] is either 0 or 1.



'''

from typing import List
from math import floor
from functools import lru_cache
class Solution:
    def goodSubsetofBinaryMatrix(self, grid: List[List[int]]) -> List[int]:
        # TLE
        m , n = len(grid), len(grid[0])
        @lru_cache(None)
        def dp(i, lth, sums):
            if i == m:
                if lth == 0: return False,set()
                succ = True
                for j in range(n):
                    if sums[j] > int(lth/2):
                        succ = False
                if not succ: return False, set()
                return True,set()
            suc1, ret1 = dp(i+1, lth, sums)
            newsums = tuple((grid[i][k]+sums[k] for k in range(n)))
            suc2, ret2 = dp(i+1, lth+1, newsums)
            if suc1 and suc2 or suc1:
                return True, ret1
            elif suc2:
                return True, {i} | ret2
            return False, set()
        s = tuple([0]*n)
        suc, ret = dp(0, 0, s)
        return sorted(list(ret)) if suc else []

    def goodSubsetofBinaryMatrix2(self, grid: List[List[int]]) -> List[int]:
        if len(grid) == 1:
            return [0] if all(num == 0 for num in grid[0]) else []
        d = {}
        for r, row in enumerate(grid):
            num = sum(cell << c for c, cell in enumerate(row))
            for i in range(32):
                if (i & num) == 0 and i in d:
                    return [d[i], r]
            d.setdefault(num, r)    
        return []




            




if __name__ == "__main__":
    print(Solution().goodSubsetofBinaryMatrix(grid = [[0,1,1,0],[0,0,0,1],[1,1,1,1]]))
    print(Solution().goodSubsetofBinaryMatrix(grid = [[1,1,1],[1,1,1]]))
    grid = [[1,0,1],[0,1,1],[0,1,0],[1,1,0],[1,1,0],[0,1,0],[1,1,1],[0,1,1],[1,0,1],[0,1,0],[0,0,1],[0,0,0],[0,1,0],[0,0,0],[1,0,0],[1,1,1],[0,0,1],[0,0,0],[1,1,0],[0,1,1],[0,1,1],[1,1,0],[1,0,0],[1,0,1],[1,1,0],[0,0,0]]
    print(Solution().goodSubsetofBinaryMatrix(grid = grid))
    grid = [[1,0,1],[0,1,1],[1,0,0],[1,1,0],[0,0,1],[0,0,1],[1,1,0],[1,1,0],[0,1,0],[0,0,0],[1,1,0],[0,1,0],[0,1,0],[0,0,0],[1,1,0],[1,1,1],[0,0,1],[0,1,1],[1,1,1],[1,1,1],[1,1,1],[1,0,0],[0,0,0],[0,0,1],[1,0,0],[0,1,0],[1,0,1],[0,0,0],[1,0,0],[1,0,0],[1,0,0],[0,0,1],[0,0,1],[0,0,1],[0,0,0],[1,0,0],[1,0,1],[1,1,1],[0,0,0],[0,1,1],[1,1,1],[0,1,0]]
    print(Solution().goodSubsetofBinaryMatrix(grid = grid))


