'''

-Medium-

Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in ZigZag-order.

Example
Given a matrix:

[
  [1, 2,  3,  4],
  [5, 6,  7,  8],
  [9,10, 11, 12]
]
return [1, 2, 5, 9, 6, 3, 4, 7, 10, 11, 8, 12]

Solution
The example result can be achieved by 6(m + n - 1) linear scans:

1
2 5
9 6 3
4 7 10
11 8
12

'''

class Solution:
    """
    @param matrix: An array of integers
    @return: An array of integers
    """
    def printZMatrix(self, matrix):
        # write your code here
        if len(matrix) == 0:
            return []
            
        x, y = 0, 0
        n, m = len(matrix), len(matrix[0])
        rows, cols = range(n), range(m)
        
        dx = [1, -1]
        dy = [-1, 1]
        direct = 1
        
        result = []
        for i in range(len(matrix) * len(matrix[0])):
            result.append(matrix[x][y])
            
            nextX = x + dx[direct]
            nextY = y + dy[direct]
            if nextX not in rows or nextY not in cols:
                if direct == 1:
                    if nextY >= m:
                        nextX, nextY = x + 1, y
                    else:
                        nextX, nextY = x, y + 1
                else:
                    if nextX >= n:
                        nextX, nextY = x, y + 1
                    else:
                        nextX, nextY = x + 1, y
                direct = 1 - direct
            x, y = nextX, nextY
        return result