'''

Given an integer matrix, find the length of the longest increasing path.

From each cell, you can either move to four directions: left, right, up or down.
 You may NOT move diagonally or move outside of the boundary (i.e. wrap-around is 
 not allowed).

Example 1:

Input: nums = 
[
  [9,9,4],
  [6,6,8],
  [2,1,1]
] 
Output: 4 
Explanation: The longest increasing path is [1, 2, 6, 9].
Example 2:

Input: nums = 
[
  [3,4,5],
  [3,2,6],
  [2,2,1]
] 
Output: 4 
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

'''

class Solution(object):
    def longestIncreasingPath(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not matrix:
            return 0
        m,n = len(matrix), len(matrix[0])
        cache = [ [-1 for _ in range (n)] for _ in range(m) ]
        long = 0 
        for i in range(m):
           for j in range(n):
               long = max(long, self.longest(matrix, cache, m, n, i, j))
        return long
        
    def longest(self, matrix, cache, m, n, i, j):
        """
        Strictly increasing, thus no need to have a visited matrix
        """
        
        dirs = ((-1, 0), (1, 0), (0, -1), (0, 1))
        if cache[i][j] >= 0:
            return cache[i][j]
        l = 1
        for d in dirs:
            ik,jk = i+d[0],j+d[1]
            if ik >=0 and ik < m and jk >= 0 and jk < n and matrix[i][j] < matrix[ik][jk]:
                l = max(l, 1+self.longest(matrix, cache, m, n, ik, jk))  
        cache[i][j] = max(cache[i][j], l)
        return l 
m = [
  [3,4,5],
  [3,2,6],
  [2,2,1]
  ] 

print(Solution().longestIncreasingPath(m))
