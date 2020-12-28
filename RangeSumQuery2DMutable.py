'''
$$$
-Hard-
*Binary Index Tree*

Given a 2D matrix matrix, find the sum of the elements inside the rectangle 
defined by its upper left corner (row1, col1) and lower right corner (row2, col2).

Range Sum Query 2D
The above rectangle (with the red border) is defined by (row1, col1) = 
(2, 1) and (row2, col2) = (4, 3), which contains sum = 8.

Example:
Given matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
sumRegion(2, 1, 4, 3) -> 8
update(3, 2, 2)
sumRegion(2, 1, 4, 3) -> 10


Note:
The matrix is only modifiable by the update function.
You may assume the number of calls to update and sumRegion function is 
distributed evenly.
You may assume that row1 ≤ row2 and col1 ≤ col2.

'''

class NumMatrix:
    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        if not matrix:
            self.bit = None
            self.mat = None  
        else:
            m = len(matrix)
            n = len(matrix[0])
            self.mat = [[0 for _ in range(n+1)] for _ in range(m+1)]
            self.bit = [[0 for _ in range(n+1)] for _ in range(m+1)]
            for i in range(m):
                for j in range(n):
                    self.update(i,j,matrix[i][j])
                    
    def update(self, row, col, val):
        diff = val - self.mat[row + 1][col + 1]        
        i = row + 1
        while i < len(self.mat):
            j = col + 1
            while j < len(self.mat[i]):
                self.bit[i][j] += diff
                j += j & (-j)
            i += i & (-i)
        self.mat[row + 1][col + 1] = val

    def getSum(self, row, col):
        res = 0
        i = row
        while i > 0:
            j = col 
            while j > 0:                
                res += self.bit[i][j]
                j -= j & (-j)
            i -= i & (-i)
        return res

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        if not self.bit: return 0
        return self.getSum(row2+1, col2+1) - self.getSum(row2+1,col1) \
              -self.getSum(row1, col2+1) + self.getSum(row1,col1) 
        
 
        

if __name__ == "__main__":
# Your NumMatrix object will be instantiated and called as such:
    matrix =  [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
    obj = NumMatrix(matrix)    
    print(obj.sumRegion(2,1,4,3))
    obj.update(3,2,2)
    print(obj.sumRegion(2,1,4,3))
    