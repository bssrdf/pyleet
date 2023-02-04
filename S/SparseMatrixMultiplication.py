'''
-Medium-

Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.

Example:

Input:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]

Output:

     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
 

Constraints:

1 <= A.length, B.length <= 100
1 <= A[i].length, B[i].length <= 100
-100 <= A[i][j], B[i][j] <= 100


'''

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        rowA = len(A)
        colA = len(A[0])
        rowB = len(B)    # colA must == rowB
        colB = len(B[0])
        
        arrayA = []
        for i in range(rowA):
            for j in range(colA):
                if A[i][j] != 0:
                    arrayA.append((i, j))
        
        arrayB = []
        for i in range(rowB):
            for j in range(colB):
                if B[i][j] != 0:
                    arrayB.append((i, j))
        
        C = [[0 for i in range(colB)] for j in range(rowA)]
        
        for a_x, a_y in arrayA:
            for b_x, b_y in arrayB:
                if a_y == b_x:
                    C[a_x][b_y] += A[a_x][a_y] * B[b_x][b_y]
        
        return C

if __name__ == "__main__":
    A = [
    [ 1, 0, 0],
    [-1, 0, 3]
    ]

    B = [
    [ 7, 0, 0 ],
    [ 0, 0, 0 ],
    [ 0, 0, 1 ]
    ]
    print(Solution().multiply(A, B))