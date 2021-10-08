'''

-Medium-

Given a m * n matrix of ones and zeros, return how many square submatrices have all ones.

 

Example 1:

Input: matrix =
[
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
]
Output: 15
Explanation: 
There are 10 squares of side 1.
There are 4 squares of side 2.
There is  1 square of side 3.
Total number of squares = 10 + 4 + 1 = 15.
Example 2:

Input: matrix = 
[
  [1,0,1],
  [1,1,0],
  [1,1,0]
]
Output: 7
Explanation: 
There are 6 squares of side 1.  
There is 1 square of side 2. 
Total number of squares = 6 + 1 = 7.
 

Constraints:

1 <= arr.length <= 300
1 <= arr[0].length <= 300
0 <= arr[i][j] <= 1


'''

from typing import List

class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        sums = [[0]*(n+1) for _ in range(m+1)]
        ans = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                sums[i][j] = sums[i-1][j] + sums[i][j-1] - sums[i-1][j-1] + matrix[i-1][j-1]
        for i in range(m):
            for j in range(n):
                for k in range(min(m-i, n-j)):
                    t = sums[i+k+1][j+k+1]-sums[i+k+1][j]-sums[i][j+k+1]+sums[i][j] 
                    if t == (k+1)**2:
                        ans += 1
        return ans

    def countSquares2(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 1:
                    if i == 0 or j == 0:
                        ans += 1
                    else:
                        cell_val = min(matrix[i-1][j], matrix[i][j-1],
                                   matrix[i-1][j-1]) +1
                        ans += cell_val
                        matrix[i][j] = cell_val
                
        return ans

        
if __name__ == '__main__':
    mat = [
        [0,1,1,1],
        [1,1,1,1],
        [0,1,1,1]
        ]
    print(Solution().countSquares(mat))
    print(Solution().countSquares2(mat))
    mat = [
        [1,0,1],
        [1,1,0],
        [1,1,0]
        ]
    print(Solution().countSquares(mat))
    print(Solution().countSquares2(mat))

