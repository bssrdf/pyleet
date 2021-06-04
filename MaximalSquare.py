'''

-Medium-

Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's 
and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4
Example 2:


Input: matrix = [["0","1"],["1","0"]]
Output: 1
Example 3:

Input: matrix = [["0"]]
Output: 0
 

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.

'''

class Solution(object):
    def maximalSquare(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]        
        res = 0
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                   dp[i][j] = 1 if matrix[i][j] == '1' else 0
                elif matrix[i][j] == '1': 
                    dp[i][j] = min(dp[i - 1][j - 1], min(dp[i][j - 1], dp[i - 1][j])) + 1                    
                res = max(res, dp[i][j])
        return res*res

    def maximalSquareOnSpace(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        m = len(matrix)
        n = len(matrix[0])
        dp = [0]*(m+1) # a (m+1)-row column vector
        res, pre = 0, 0
        for j in range(n):
            # sweep from left to right with the column vector
            for i in range(1, m+1):
                t = dp[i]
                if matrix[i - 1][j] == '1': 
                    dp[i] = min(dp[i], min(dp[i - 1],  pre)) + 1
                            #     ^            ^        ^
                            #     |            |        | 
                            #  column         last     upper 
                            #  to the         row      left
                            #   left 
                            #  [i,j-1]       [i-1,j]  [i-1,j-1] 
                    res = max(res, dp[i])
                else:
                    dp[i] = 0
                pre = t
        return res*res
            
        
if __name__=="__main__":
    matrix = [["1","0","1","0","0"],
              ["1","0","1","1","1"],
              ["1","1","1","1","1"],
              ["1","0","0","1","0"]]
    print(Solution().maximalSquare(matrix))
    print(Solution().maximalSquareOnSpace(matrix))
    matrix = [["0","1"],
            ["1","0"]]
    print(Solution().maximalSquare(matrix))
