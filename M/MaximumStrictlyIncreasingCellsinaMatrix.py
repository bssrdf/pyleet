'''

-Hard-
*DP*

Given a 1-indexed m x n integer matrix mat, you can select any cell in the matrix as your starting cell.

From the starting cell, you can move to any other cell in the same row or column, but only if the value of the destination cell is strictly greater than the value of the current cell. You can repeat this process as many times as possible, moving from cell to cell until you can no longer make any moves.

Your task is to find the maximum number of cells that you can visit in the matrix by starting from some cell.

Return an integer denoting the maximum number of cells that can be visited.

 

Example 1:



Input: mat = [[3,1],[3,4]]
Output: 2
Explanation: The image shows how we can visit 2 cells starting from row 1, column 2. It can be shown that we cannot visit more than 2 cells no matter where we start from, so the answer is 2. 
Example 2:



Input: mat = [[1,1],[1,1]]
Output: 1
Explanation: Since the cells must be strictly increasing, we can only visit one cell in this example. 
Example 3:



Input: mat = [[3,1,6],[-9,5,7]]
Output: 4
Explanation: The image above shows how we can visit 4 cells starting from row 2, column 1. It can be shown that we cannot visit more than 4 cells no matter where we start from, so the answer is 4. 
 

Constraints:

m == mat.length 
n == mat[i].length 
1 <= m, n <= 105
1 <= m * n <= 105
-105 <= mat[i][j] <= 105

'''
from collections import defaultdict
from typing import List

class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        ranks = [1]*(m*n) 
        mat1 = [0]*(m*n) 
        for i in range(m):
            for j in range(n): 
                mat1[i*n+j] = mat[i][j]
        arr = []
        row, col = {}, {}
        
        for i in range(m):
            for j in range(n):
                arr.append((mat[i][j], i, j))
        arr.sort() 
        for a,(v,i,j) in enumerate(arr):
            idx = i*n+j
            k, l = 0, 0  
            if i in row or j in col:
                # print(ranks[row[i]], ranks[col[j]])
                k = ranks[row[i]] if i in row and v > mat1[row[i]] else 0
                l = ranks[col[j]] if j in col and v > mat1[col[j]] else 0
                print(k,l, idx, row, col)
                ranks[idx] = 1 + max(k, l)
            # else:
            if a == 0 or ( a > 0 and v > arr[a-1][0]):
                row[i] = idx
                col[j] = idx            
            print(i, j, v, row, col, ranks)
        return max(ranks)
    
    def maxIncreasingCells2(self, mat: List[List[int]]) -> int:
        # Wrong
        m, n = len(mat), len(mat[0])
        ranks = [1]*(m*n) 
        dp = [[1]*n for _ in range(m)] 
        arr = []
        row, col = {}, {}
        ans = 1
        for i in range(m):
            for j in range(n):
                arr.append((mat[i][j], i, j))
        arr.sort() 
        for a,(v,i,j) in enumerate(arr):
            idx = i*n+j
            k, l = 0, 0  
            # print('A', i, j, v, row, col)
            if i in row or j in col:
                # print(ranks[row[i]], ranks[col[j]])
                old_x1, old_y1 = -1, -1
                old_x2, old_y2 = -1, -1
                if i in row and v > row[i][1]:
                    old_x1, old_y1 = row[i][2], row[i][3]
                    row[i] = (row[i][0]+1, v, i, j)
                if j in col and v > col[j][1]:
                    old_x2, old_y2 = col[j][2], col[j][3]
                    col[j] = (col[j][0]+1, v, i, j)
                if i not in row:
                    row[i] = (1, v, i, j)
                if j not in col:
                    col[j] = (1, v, i, j)    
                # print('C', i, j, v, row[i], col[j])               
                dp[i][j] = max(row[i][0], col[j][0], 1 + max(dp[old_x1][old_y1] if old_x1 != -1 else 0, dp[old_x2][old_y2] if old_x2 != -1 else 0))
            else:           
                row[i] = (1, v, i, j)
                col[j] = (1, v, i, j)           
            # print('B', i, j, v, row, col)
        # for r in dp:
        #     print(r)
        return max(max(r) for r in dp)
    
    def maxIncreasingCells3(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        A = defaultdict(list)
        for i in range(m):
            for j in range(n):
                A[mat[i][j]].append([i, j])
        dp = [[0] * n for i in range(m)]
        res = [0] * (n + m)
        for a in sorted(A):
            for i, j in A[a]:
                dp[i][j] = max(res[i], res[m + j]) + 1
            for i, j in A[a]:
                res[m + j] = max(res[m + j], dp[i][j])
                res[i] = max(res[i], dp[i][j])
        return max(res)
    
    def maxIncreasingCells4(self, mat: List[List[int]]) -> int:
        m, n = len(mat), len(mat[0])
        A = defaultdict(list)
        for i in range(m):
            for j in range(n):
                A[mat[i][j]].append([i, j])
        dp = [[0] * n for i in range(m)]
        row, col = [0]*m, [0]*n
        # row[i] the longest increasing path so far for row i
        # col[j] the longest increasing path so far for col j
        for a in sorted(A):
            # the key insight here is to update all duplicated cells all together in one iteration
            # separately, first for dp values
            for i, j in A[a]: # update all i/j's dp value using current row/col values
                dp[i][j] = max(row[i], col[j]) + 1
            # and then for row/col array
            for i, j in A[a]: # update row/col values using new dp 
                # a common mistake here is to do
                # row[i] = col[j] = dp[i][j] which is conflicting with the definition of row/col above
                col[j] = max(col[j], dp[i][j])
                row[i] = max(row[i], dp[i][j])
        return max(max(col), max(row))

if __name__ == "__main__":
    # print(Solution().maxIncreasingCells2(mat = [[3,1],[3,4]]))
    # print(Solution().maxIncreasingCells2(mat = [[1,1],[1,1]]))
    # print(Solution().maxIncreasingCells2(mat = [[3,1,6],[-9,5,7]]))
    # print(Solution().maxIncreasingCells2(mat = [[2,-4,2,-2,6]]))
    # print(Solution().maxIncreasingCells2(mat = [[0,-1],[-6,-6],[-1,8]]))
    # print(Solution().maxIncreasingCells2(mat = [[7,6,3],[-7,-5,6],[-7,0,-4],[6,6,0],[-8,6,0]]))
    print(Solution().maxIncreasingCells2(mat = [[9,-3,-2,0,-3],[-1,-4,7,5,9],[1,8,0,-7,-6]]))
