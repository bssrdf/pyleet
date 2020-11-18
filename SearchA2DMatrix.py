'''

Write an efficient algorithm that searches for a value in an m x n matrix. This matrix 
has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.

Example 1:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
Output: true
Example 2:


Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13
Output: false
Example 3:

Input: matrix = [], target = 0
Output: false
 

Constraints:

m == matrix.length
n == matrix[i].length
0 <= m, n <= 100
-10^4 <= matrix[i][j], target <= 10^4
'''
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False
        m = len(matrix)
        n = len(matrix[0])        
        mr, mc = 0, n-1
        while 0 <= mr < m and 0 <= mc < n:
            if matrix[mr][mc] == target: return True
            elif matrix[mr][mc] > target:
                mc -= 1
            elif matrix[mr][mc] < target:    
                mr += 1    
        return False

if __name__ == "__main__":
    print(Solution().searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 3))

