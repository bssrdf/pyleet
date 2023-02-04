'''
-Medium-
*DP*

Given an n x n array of integers matrix, return the minimum sum of any falling path through 
matrix.

A falling path starts at any element in the first row and chooses the element in the next row 
that is either directly below or diagonally left/right. Specifically, the next element 
from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).

 

Example 1:

Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
Explanation: There are two falling paths with a minimum sum underlined below:
[[2,1,3],      [[2,1,3],
 [6,5,4],       [6,5,4],
 [7,8,9]]       [7,8,9]]
Example 2:

Input: matrix = [[-19,57],[-40,-5]]
Output: -59
Explanation: The falling path with a minimum sum is underlined below:
[[-19,57],
 [-40,-5]]
Example 3:

Input: matrix = [[-48]]
Output: -48
 

Constraints:

n == matrix.length
n == matrix[i].length
1 <= n <= 100
-100 <= matrix[i][j] <= 100


'''

class Solution(object):
    def minFallingPathSum(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        dp = [[0]*n for _ in range(n)]
        for j in range(n):
            dp[n-1][j] = matrix[n-1][j]
        for i in range(n-2, -1, -1):
            for j in range(n):
                if j == 0:
                    dp[i][j] = matrix[i][j] + min(dp[i+1][j], dp[i+1][j+1])
                elif j == n-1:
                    dp[i][j] = matrix[i][j] + min(dp[i+1][j], dp[i+1][j-1])
                else:
                    dp[i][j] = matrix[i][j] + min(dp[i+1][j+1], dp[i+1][j], dp[i+1][j-1])
        return min(dp[0][j] for j in range(n))

    def minFallingPathSumOnSpace(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        n = len(matrix)
        dp = [0 for _ in range(n)]
        #dp1 = [0 for _ in range(n)]
        for j in range(n):
            dp[j] = matrix[n-1][j]
        dp1 = dp[:]
        for i in range(n-2, -1, -1):
            for j in range(n-1,-1,-1):
                if j == 0:
                    dp[j] = matrix[i][j] + min(dp1[j], dp1[j+1])
                elif j == n-1:
                    dp[j] = matrix[i][j] + min(dp1[j], dp1[j-1])
                else:
                    dp[j] = matrix[i][j] + min(dp1[j+1], dp1[j], dp1[j-1])
            dp1 = dp[:]
        return min(dp)




    
if __name__ == "__main__":
    mat = [[2,1,3],[6,5,4],[7,8,9]]
    print(Solution().minFallingPathSum(mat))
    print(Solution().minFallingPathSumOnSpace(mat))
    mat = [[17,82],[1,-44]]
    print(Solution().minFallingPathSum(mat))
    print(Solution().minFallingPathSumOnSpace(mat))