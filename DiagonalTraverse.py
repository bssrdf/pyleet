'''
-Medium-
*Matrix*

Given a matrix of M x N elements (M rows, N columns), return all elements 
of the matrix in diagonal order as shown in the below image.

 

Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output:  [1,2,4,7,5,3,6,8,9]

Note:

The total number of elements of the given matrix will not exceed 10,000.

'''

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]: return []
        m = len(matrix)
        n = len(matrix[0])
        res = [0]*(m*n)
        k, l = 0, 0
        dirs = [(-1,1), (1,-1)]
        row, col = 0, 0
        while k < m*n:
            res[k] = matrix[row][col]  
            row += dirs[l][0]
            col += dirs[l][1]
            if row >= m:
                row = m - 1
                col += 2
                l = 1 - l
            if col >= n:
                col = n - 1 
                row += 2 
                l = 1 - l
            if row < 0: 
                row = 0 
                l = 1 - l
            if col < 0: 
                col = 0 
                l = 1 - l            
            k += 1
        return res


if __name__ == "__main__":
    matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
    print(Solution().findDiagonalOrder(matrix))