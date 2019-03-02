'''
You are given an n x n 2D matrix representing an image.

Rotate the image by 90 degrees (clockwise).

Follow up:
Could you do this in-place?
'''

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if matrix is None or len(matrix)==0 or len(matrix[0]) == 0:
            return
        n = len(matrix)        
        for i in range(n//2):
            for j in range(i, n-i-1):
                tmp = matrix[i][j]
                matrix[i][j] = matrix[n-j-1][i]
                matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
                matrix[n-i-1][n-j-1] = matrix[j][n-i-1]
                matrix[j][n-i-1] = tmp
                
        

if __name__ == "__main__":
    #assert Solution().rotate([[1, 2, 3], [8, 9, 4], [7, 6, 5]]) == [[7, 8, 1], [6, 9, 2], [5, 4, 3]]
    a = [[1, 2, 3], [8, 9, 4], [7, 6, 5]]
    Solution().rotate(a)
    print(a)
    b = [[7, 8, 1], [6, 9, 2], [5, 4, 3]]
    print(b)
    assert a==b