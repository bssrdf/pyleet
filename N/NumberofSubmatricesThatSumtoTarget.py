'''
-Hard-

Given a matrix and a target, return the number of non-empty submatrices that sum to target.

A submatrix x1, y1, x2, y2 is the set of all cells matrix[x][y] with x1 <= x <= x2 and y1 <= y <= y2.

Two submatrices (x1, y1, x2, y2) and (x1', y1', x2', y2') are different if they have some coordinate 
that is different: for example, if x1 != x1'.

 

Example 1:


Input: matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0
Output: 4
Explanation: The four 1x1 submatrices that only contain 0.
Example 2:

Input: matrix = [[1,-1],[-1,1]], target = 0
Output: 5
Explanation: The two 1x2 submatrices, plus the two 2x1 submatrices, plus the 2x2 submatrix.
Example 3:

Input: matrix = [[904]], target = 0
Output: 0


'''

from collections import defaultdict
class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: int
        """ 
        m, n = len(matrix), len(matrix[0])
        res = 0
        for i in range(m):
            for j in range(1, n):
                # compute prefix sum for each row
                # reuse the input arry
                matrix[i][j] += matrix[i][j-1]
        for i in range(n): # index of left col
            for j in range(i, n): # index of right col (j can be the same as i)  
                count = defaultdict(int)
                sums, count[0] = 0, 1
                for k in range(m):
                    sums += matrix[k][j] - (matrix[k][i-1] if i > 0 else 0)
                    # sums[k] is the total sum of submatrix (0, i) - (k, j)
                    # supposed there is a l such that sums[k] - sums[l] = target
                    # we got one or more candidates. look up sums[l] in the hash table  
                    res += count[sums-target]
                    count[sums] += 1
        return res            

               

        
if __name__ == "__main__":
    matrix = [[0,1,0],[1,1,1],[0,1,0]]
    print(Solution().numSubmatrixSumTarget(matrix, 0))

