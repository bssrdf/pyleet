'''
-Medium-

Given a m * n matrix mat and an integer K, return a matrix answer where 
each answer[i][j] is the sum of all elements mat[r][c] for i - K <= r <= i + K, 
j - K <= c <= j + K, and (r, c) is a valid position in the matrix.
 

Example 1:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 1
Output: [[12,21,16],[27,45,33],[24,39,28]]
Example 2:

Input: mat = [[1,2,3],[4,5,6],[7,8,9]], K = 2
Output: [[45,45,45],[45,45,45],[45,45,45]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n, K <= 100
1 <= mat[i][j] <= 100



'''

class Solution(object):
    def matrixBlockSum(self, mat, K):
        """
        :type mat: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        preSum = [[0 for _ in range(n+1)] for _ in range(m+1)]
        res = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                preSum[i][j] = preSum[i-1][j] + preSum[i][j-1] + mat[i-1][j-1] \
                               - preSum[i-1][j-1]
        '''  
        i1 , j1 = 0, 1 
        i2,  j2 = 1, 2
        print(preSum[i2+1][j2+1], preSum[i1][j1],
              preSum[i1][j2+1], preSum[i2+1][j1])
        print(preSum[i2+1][j2+1] + preSum[i1][j1] \
                          - preSum[i1][j2+1] - preSum[i2+1][j1])
        '''
        for i in range(m):
            for j in range(n):
                i1, j1 = max(i-K, 0), max(j-K, 0)
                i2, j2 = min(i+K, m-1), min(j+K, n-1)
                res[i][j] = preSum[i2+1][j2+1] + preSum[i1][j1] \
                          - preSum[i1][j2+1] - preSum[i2+1][j1]
        return res


if __name__ == "__main__":
    print(Solution().matrixBlockSum([[1,2,3],
                                     [4,5,6],
                                     [7,8,9]], 1))