'''
-Medium-

Given a rows * columns matrix mat of ones and zeros, return how many submatrices have all ones.

 

Example 1:

Input: mat = [[1,0,1],
              [1,1,0],
              [1,1,0]]
Output: 13
Explanation:
There are 6 rectangles of side 1x1.
There are 2 rectangles of side 1x2.
There are 3 rectangles of side 2x1.
There is 1 rectangle of side 2x2. 
There is 1 rectangle of side 3x1.
Total number of rectangles = 6 + 2 + 3 + 1 + 1 = 13.
Example 2:

Input: mat = [[0,1,1,0],
              [0,1,1,1],
              [1,1,1,0]]
Output: 24
Explanation:
There are 8 rectangles of side 1x1.
There are 5 rectangles of side 1x2.
There are 2 rectangles of side 1x3. 
There are 4 rectangles of side 2x1.
There are 2 rectangles of side 2x2. 
There are 2 rectangles of side 3x1. 
There is 1 rectangle of side 3x2. 
Total number of rectangles = 8 + 5 + 2 + 4 + 2 + 2 + 1 = 24.
Example 3:

Input: mat = [[1,1,1,1,1,1]]
Output: 21
Example 4:

Input: mat = [[1,0,1],[0,1,0],[1,0,1]]
Output: 5
 

Constraints:

1 <= rows <= 150
1 <= columns <= 150
0 <= mat[i][j] <= 1


'''

class Solution(object):
    def numSubmat(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        
        #precipitate mat to histogram 
        for i in range(m):
            for j in range(n):
                if mat[i][j] and i > 0: 
                    mat[i][j] += mat[i-1][j] #histogram 
        
        ans = 0
        for i in range(m):
            stack = [] #mono-stack of indices of non-decreasing height
            cnt = 0
            for j in range(n):
                while stack and mat[i][stack[-1]] > mat[i][j]: 
                    jj = stack.pop()                          #start
                    kk = stack[-1] if stack else -1           #end
                    cnt -= (mat[i][jj] - mat[i][j])*(jj - kk) #adjust to reflect lower height

                cnt += mat[i][j] #count submatrices bottom-right at (i, j)
                ans += cnt
                stack.append(j)

        return ans
    
    def numSubmat2(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])
        h = [0]*n
        ans = 0
        #precipitate mat to histogram 
        def helper(heights):
            stack = [] #mono-stack of indices of non-decreasing height
            sm = [0]*n
            for j in range(n):
                while stack and heights[stack[-1]] >= heights[j]: 
                    stack.pop() 
                if stack:
                    sm[j] = sm[stack[-1]]
                    sm[j] += heights[j]*(j-stack[-1])
                else:
                    sm[j] = heights[j]*(j+1)    
                stack.append(j)
            #print(sm)
            return sum(sm)           
 
        for i in range(m):
            for j in range(n):
                if mat[i][j]: h[j] += 1 #histogram 
                else: h[j] = 0
            ans += helper(h)

        return ans
       

        

if __name__ == "__main__": 
    mat = [[1,0,1],
           [1,1,0],
           [1,1,0]]
    print(Solution().numSubmat(mat))
    print(Solution().numSubmat2(mat))
    
