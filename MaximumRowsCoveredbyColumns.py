'''
-Medium-

You are given a 0-indexed m x n binary matrix mat and an integer cols, which denotes the number of columns you must choose.

A row is covered by a set of columns if each cell in the row that has a value of 1 also lies in one of the columns of the chosen set.

Return the maximum number of rows that can be covered by a set of cols columns.

 

Example 1:



Input: mat = [[0,0,0],[1,0,1],[0,1,1],[0,0,1]], cols = 2
Output: 3
Explanation:
As shown in the diagram above, one possible way of covering 3 rows is by selecting the 0th and 2nd columns.
It can be shown that no more than 3 rows can be covered, so we return 3.
Example 2:



Input: mat = [[1],[0]], cols = 1
Output: 2
Explanation:
Selecting the only column will result in both rows being covered, since the entire matrix is selected.
Therefore, we return 2.
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 12
mat[i][j] is either 0 or 1.
1 <= cols <= n


'''

from typing import List
from functools import lru_cache

class Solution:
    def maximumRows(self, mat: List[List[int]], cols: int) -> int:
        m, n = len(mat), len(mat[0])
        rows = [int(''.join(str(c) for c in r), 2) for r in mat]
        ans = 0
        @lru_cache(None) 
        def backtrack(cur, msk):
            nonlocal ans
            cnt = bin(msk).count('1') 
            if cnt > cols:
                return
            if cnt == cols:
                t = 0
                for i in rows:
                    if (i | msk) == msk: t += 1 
                ans = max(ans, t)
                return    
            for i in range(cur, n):
                # if msk & (1 << i) == 0:
                backtrack(i+1, msk | 1<<i)
                backtrack(i+1, msk)

        backtrack(0, 0)    
        return ans



if __name__ == "__main__":
    print(Solution().maximumRows(mat = [[0,0,0],[1,0,1],[0,1,1],[0,0,1]], cols = 2))
    print(Solution().maximumRows(mat = [[1],[0]], cols = 1))
    print(Solution().maximumRows(mat = [[1,0,1,0],[1,0,1,0],[0,1,1,1],[0,1,0,0]], cols=3))
    print(Solution().maximumRows(mat = [[0,0],[0,1],[0,0],[1,1]], cols = 1))
        
