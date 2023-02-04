'''
-Hard-

Given a rows x cols binary matrix filled with 0's and 1's, find the largest 
rectangle containing only 1's and return its area.

 

Example 1:


Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],
                 ["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 6
Explanation: The maximal rectangle is shown in the above picture.
Example 2:

Input: matrix = []
Output: 0
Example 3:

Input: matrix = [["0"]]
Output: 0
Example 4:

Input: matrix = [["1"]]
Output: 1
Example 5:

Input: matrix = [["0","0"]]
Output: 0
 

Constraints:

rows == matrix.length
cols == matrix.length
0 <= row, cols <= 200
matrix[i][j] is '0' or '1'.

'''

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]: return 0
        height = [0]*len(matrix[0])
        res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                height[j] = 1+height[j] if matrix[i][j] == '1' else 0
            res = max(res, self.largestRectangleArea(height))
        return res               

    def largestRectangleArea(self, heights):        

        if not heights: 
          return 0
        n = len(heights)        
        lessFromLeft = [-1] * n
        lessFromRight = [n] * n        
        stack = []    
        for i,v in enumerate(heights):
            while stack and heights[stack[-1]] >= v: # right is from the popping out
                lessFromRight[stack.pop()] = i
            if stack:  #left is from the pushing in
                lessFromLeft[i] = stack[-1]
            stack.append(i)          
        maxArea = 0
        for i in range(n):
            maxArea = max(maxArea, heights[i]*(lessFromRight[i]-lessFromLeft[i]-1))
        return maxArea

    def maximalRectangleDP(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        if not matrix or not matrix[0]: return 0
        m = len(matrix)
        n = len(matrix[0])
        hmax = [[0 for _ in range(n)] for _ in range(m)]
        res = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0': continue
                if j > 0: hmax[i][j] = hmax[i][j-1]+1
                else: hmax[i][j] = 1
        for i in range(m):
            for j in range(n):
                if hmax[i][j] == 0: continue
                mn = hmax[i][j]
                res = max(res, mn)
                for k in range(i-1, -1, -1):
                    if hmax[i][j] == 0: break
                    mn = min(mn, hmax[k][j])
                    res = max(res, mn*(i-k+1))
        return res               
        
if __name__ == "__main__":
    matrix = [["1","0","1","0","0"],
              ["1","0","1","1","1"],
              ["1","1","1","1","1"],
              ["1","0","0","1","0"]]
    print(Solution().maximalRectangle(matrix))
    print(Solution().maximalRectangleDP(matrix))