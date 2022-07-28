'''

-Medium-
*Hashing*

Given a 0-indexed n x n integer matrix grid, return the number of pairs (Ri, Cj) such that row Ri and column Cj are equal.

A row and column pair is considered equal if they contain the same elements in the same order (i.e. an equal array).

 

Example 1:


Input: grid = [[3,2,1],[1,7,6],[2,7,7]]
Output: 1
Explanation: There is 1 equal row and column pair:
- (Row 2, Column 1): [2,7,7]
Example 2:


Input: grid = [[3,1,2,2],[1,4,4,5],[2,4,2,2],[2,4,2,2]]
Output: 3
Explanation: There are 3 equal row and column pairs:
- (Row 0, Column 0): [3,1,2,2]
- (Row 2, Column 2): [2,4,2,2]
- (Row 3, Column 2): [2,4,2,2]
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
1 <= grid[i][j] <= 105



'''

from collections import Counter
from typing import List

class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        pairs = 0
        cnt = Counter(tuple(row) for row in grid)
        for tpl in zip(*grid):
            # print(tpl)
            pairs += cnt[tpl]
        return pairs
    
    def equalPairs2(self, grid: List[List[int]]) -> int:
        pairs, M = 0, 10**9+7
        m, n = len(grid), len(grid[0])
        def rowhash(r):
            ret = 0
            for i in range(n):
                ret = (ret + grid[r][i]) * 7 % M
            return ret    
        def colhash(c):
            ret = 0
            for i in range(m):
                ret = (ret + grid[i][c]) * 7 % M
            return ret    
        rows, cols = [0]*m, [0]*n
        for i in range(m):
            rows[i] = rowhash(i)
        for i in range(n):
            cols[i] = colhash(i)
        for i in range(m):
            for j in range(n):
                if rows[i] == cols[j]: pairs += 1
        return pairs 
        


if __name__ == "__main__":
    grid = [[3,2,1],[1,7,6],[2,7,7]]
    print(Solution().equalPairs(grid))
    print(Solution().equalPairs2(grid))


                        
            
        