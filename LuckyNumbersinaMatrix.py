'''
-Easy-

Given an m x n matrix of distinct numbers, return all lucky numbers in the matrix in any order.

A lucky number is an element of the matrix such that it is the minimum element in its row and maximum in its column.

 

Example 1:

Input: matrix = [[3,7,8],[9,11,13],[15,16,17]]
Output: [15]
Explanation: 15 is the only lucky number since it is the minimum in its row and the maximum in its column
Example 2:

Input: matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
Output: [12]
Explanation: 12 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 3:

Input: matrix = [[7,8],[1,2]]
Output: [7]
Explanation: 7 is the only lucky number since it is the minimum in its row and the maximum in its column.
Example 4:

Input: matrix = [[3,6],[7,1],[5,2],[4,8]]
Output: []
Explanation: There is no lucky number.
 

Constraints:

m == mat.length
n == mat[i].length
1 <= n, m <= 50
1 <= matrix[i][j] <= 105.
All elements in the matrix are distinct.

'''

from typing import List


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        M = matrix
        m, n = len(M), len(M[0])
        rows, cols = set(), set()
        mx = 0
        for i in range(m):
            mi = 10**5+1
            c = -1
            for j in range(n):
                if M[i][j] < mi:
                    mi, c = M[i][j], j
            rows.add((i,c))
        for j in range(n):
            mx = 0
            r = -1
            for i in range(m):
                if M[i][j] > mx:
                    mx, r = M[i][j], i
            cols.add((r,j))
        res = []
        for r in rows:
            if r in cols:
               res.append(M[r[0]][r[1]]) 
        return res