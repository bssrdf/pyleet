'''

-Medium-





You are given an m x n integer matrix grid​​​.

A rhombus sum is the sum of the elements that form the border of a regular rhombus shape in grid​​​. The rhombus must have the shape of a square rotated 45 degrees with each of the corners centered in a grid cell. Below is an image of four valid rhombus shapes with the corresponding colored cells that should be included in each rhombus sum:


Note that the rhombus can have an area of 0, which is depicted by the purple rhombus in the bottom right corner.

Return the biggest three distinct rhombus sums in the grid in descending order. If there are less than three distinct values, return all of them.

 

Example 1:


Input: grid = [[3,4,5,1,3],[3,3,4,2,3],[20,30,200,40,10],[1,5,5,4,1],[4,3,2,2,5]]
Output: [228,216,211]
Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 20 + 3 + 200 + 5 = 228
- Red: 200 + 2 + 10 + 4 = 216
- Green: 5 + 200 + 4 + 2 = 211
Example 2:


Input: grid = [[1,2,3],[4,5,6],[7,8,9]]
Output: [20,9,8]
Explanation: The rhombus shapes for the three biggest distinct rhombus sums are depicted above.
- Blue: 4 + 2 + 6 + 8 = 20
- Red: 9 (area 0 rhombus in the bottom right corner)
- Green: 8 (area 0 rhombus in the bottom middle)
Example 3:

Input: grid = [[7,7,7]]
Output: [7]
Explanation: All three possible rhombus sums are the same, so return [7].
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 50
1 <= grid[i][j] <= 105

'''

from typing import List

class Solution:
    def getBiggestThree(self, grid: List[List[int]]) -> List[int]:
        _r, _c = len(grid), len(grid[0])
        def rsum(h): # here h+1 represents length of each side of rhombus
            ret = []
            for r in range(_r):
                for c in range(_c):
                    if r - h >= 0 and r + h < _r and c - h >= 0 and c + h < _c:
                        tsm = 0
                        for i, rr in enumerate(range(r-h, r+1)):
                            tsm += grid[rr][c+i] + (0 if i == 0 else grid[rr][c-i])
                        for i, rr in enumerate(range(r+1, r+h+1)[::-1]):
                            tsm += grid[rr][c+i] + (0 if i == 0 else grid[rr][c-i])
                        ret.append(tsm)
            return ret
        sms = []
        for i in range(min(_r, _c)):
            sms += rsum(i)
        sms = sorted(set(sms))[::-1]
        return sms if len(sms) < 3 else sms[:3]