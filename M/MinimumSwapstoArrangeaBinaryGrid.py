'''

-Medium-


Given an n x n binary grid, in one step you can choose two adjacent rows of the 
grid and swap them.

A grid is said to be valid if all the cells above the main diagonal are zeros.

Return the minimum number of steps needed to make the grid valid, or -1 if the grid 
cannot be valid.

The main diagonal of a grid is the diagonal that starts at cell (1, 1) and ends 
at cell (n, n).

 

Example 1:


Input: grid = [[0,0,1],[1,1,0],[1,0,0]]
Output: 3
Example 2:


Input: grid = [[0,1,1,0],[0,1,1,0],[0,1,1,0],[0,1,1,0]]
Output: -1
Explanation: All rows are similar, swaps have no effect on the grid.
Example 3:


Input: grid = [[1,0,0],[1,1,0],[1,1,1]]
Output: 0
 

Constraints:

n == grid.length == grid[i].length
1 <= n <= 200
grid[i][j] is either 0 or 1


'''

from typing import List

class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        
        def zerosAtEnd(arr):
            n = len(arr)
            i = n-1
            while i >= 0 and arr[i] == 0:
                i -= 1
            return n-i-1
        def gridToVec(grid):
            ans = []
            for x in grid:
               ans.append(zerosAtEnd(x))
            return ans
        arr = gridToVec(grid)
        n = len(arr)
        ans = 0
        for i in range(n):
            if arr[i] < (n-i-1):
                j = i
                while j < n and arr[j] < (n-i-1):
                    j += 1
                if j == n:      # Did not find any number greater than or equal to n-i-1.
                    return -1   # so its impossible to get the answer.
                while j > i :
                    arr[j], arr[j-1] = arr[j-1], arr[j]
                    ans += 1
                    j -= 1
        return ans


if __name__ == "__main__":
     grid = [[0,0,1],[1,1,0],[1,0,0]]
     print(Solution().minSwaps(grid))
