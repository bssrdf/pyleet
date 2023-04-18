'''

-Medium-

A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.

Given a row x col grid of integers, how many 3 x 3 "magic square" subgrids are there?  (Each subgrid is contiguous).

 

Example 1:


Input: grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]
Output: 1
Explanation: 
The following subgrid is a 3 x 3 magic square:

while this one is not:

In total, there is only one magic square inside the given grid.
Example 2:

Input: grid = [[8]]
Output: 0
 

Constraints:

row == grid.length
col == grid[i].length
1 <= row, col <= 10
0 <= grid[i][j] <= 15

'''
from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        if m < 3 or n < 3: return 0
        dig = set(range(1, 10))
        ans = 0
        for i in range(m-2):
            for j in range(n-2):
                cnt = set()
                r, c, d, d1 = [0]*3, [0]*3, 0, 0
                for x in range(3):
                    for y in range(3):
                        cnt.add(grid[i+x][j+y])
                        r[x] += grid[i+x][j+y]
                        c[y] += grid[i+x][j+y]
                for l in range(3):
                    d += grid[i+l][j+l]
                    d1 += grid[i+l][j+3-l-1]
                if cnt == dig and (r[0] == r[1] == r[2] 
                       == c[0] == c[1] == c[2] == d == d1):
                    ans += 1
        return ans   


if __name__ == '__main__':
    print(Solution().numMagicSquaresInside(grid = [[4,3,8,4],[9,5,1,9],[2,7,6,2]]))