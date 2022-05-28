'''

-Hard-

*BFS*
*Bit Manipulation*

Given a m x n binary matrix mat. In one step, you can choose one cell and flip it and all the four neighbors of it if they exist (Flip is changing 1 to 0 and 0 to 1). A pair of cells are called neighbors if they share one edge.

Return the minimum number of steps required to convert mat to a zero matrix or -1 if you cannot.

A binary matrix is a matrix with all cells equal to 0 or 1 only.

A zero matrix is a matrix with all cells equal to 0.

 

Example 1:


Input: mat = [[0,0],[0,1]]
Output: 3
Explanation: One possible solution is to flip (1, 0) then (0, 1) and finally (1, 1) as shown.
Example 2:

Input: mat = [[0]]
Output: 0
Explanation: Given matrix is a zero matrix. We do not need to change it.
Example 3:

Input: mat = [[1,0,0],[1,0,0]]
Output: -1
Explanation: Given matrix cannot be a zero matrix.
 

Constraints:

m == mat.length
n == mat[i].length
1 <= m, n <= 3
mat[i][j] is either 0 or 1.

'''
from typing import List
from collections import deque

class Solution:
    def minFlips(self, mat: List[List[int]]) -> int:
        d = [0, 0, 1, 0, -1, 0]
        start, m, n = 0,  len(mat), len(mat[0])
        for i in range(m):
            for j in range(n):
                start |= mat[i][j] << (i * n + j) # convert the matrix to an int.
        q = deque([start])
        seen = {start}
        step = 0
        while q:
            newq = deque()
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == 0: # All 0s matrix found.
                    return step
                # try to flip every cell and its neighbors       
                for i in range(m):
                    for j in range(n): 
                        next = cur
                        for k in range(5): # flip the cell (i, j) and its neighbors.                                
                            r, c = i + d[k], j + d[k + 1]
                            if r >= 0 and r < m and c >= 0 and c < n:
                                next ^= 1 << (r * n + c)
                        if next not in seen: # seen it before ?
                            seen.add(next)
                            newq.append(next)  # no, put it into the Queue.
            step += 1
            q = newq
        return -1 # impossible to get all 0s matrix.

        

if __name__ == "__main__":
    print(Solution().minFlips(mat = [[0,0],[0,1]]))