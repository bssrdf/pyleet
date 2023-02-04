'''
-Medium-

A matrix diagonal is a diagonal line of cells starting from some cell in either 
the topmost row or leftmost column and going in the bottom-right direction until 
reaching the matrix's end. For example, the matrix diagonal starting from mat[2][0], 
where mat is a 6 x 3 matrix, includes cells mat[2][0], mat[3][1], and mat[4][2].

Given an m x n matrix mat of integers, sort each matrix diagonal in ascending 
order and return the resulting matrix.

 

Example 1:


Input: mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
Output: [[1,1,1,1],[1,2,2,2],[1,2,3,3]]
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 100
1 <= mat[i][j] <= 100

'''
from collections import defaultdict

class Solution(object):
    def diagonalSort(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        """
        A[i][j] on the same diagonal have same value of i - j
        For each diagonal,
        put its elements together, sort, and set them back.

        Complexity
        Time O(MNlogD), where D is the length of diagonal with D = min(M,N).
        Space O(MN)
        """
        n, m = len(mat), len(mat[0])
        d = defaultdict(list)
        for i in range(n):
            for j in range(m):
                d[i - j].append(mat[i][j])
        for k in d:
            d[k].sort(reverse=1)
        for i in range(n):
            for j in range(m):
                mat[i][j] = d[i - j].pop()
        return mat

if __name__ == "__main__":
    mat = [[3,3,1,1],[2,2,1,2],[1,1,1,2]]
    Solution().diagonalSort(mat)
    for row in mat:
        print(row)