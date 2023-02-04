'''

-Hard-

There is a strange printer with the following two special requirements:

On each turn, the printer will print a solid rectangular pattern of a single color on the grid. 
This will cover up the existing colors in the rectangle.

Once the printer has used a color for the above operation, the same color cannot be used again.
You are given a m x n matrix targetGrid, where targetGrid[row][col] is the color in the 
position (row, col) of the grid.

Return true if it is possible to print the matrix targetGrid, otherwise, return false.

 

Example 1:



Input: targetGrid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]
Output: true
Example 2:



Input: targetGrid = [[1,1,1,1],[1,1,3,3],[1,1,3,4],[5,5,1,4]]
Output: true
Example 3:

Input: targetGrid = [[1,2,1],[2,1,2],[1,2,1]]
Output: false
Explanation: It is impossible to form targetGrid because it is not allowed to print the same color in different turns.
Example 4:

Input: targetGrid = [[1,1,1],[3,1,3]]
Output: false
 

Constraints:

m == targetGrid.length
n == targetGrid[i].length
1 <= m, n <= 60
1 <= targetGrid[row][col] <= 60

'''
from typing import List

class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        # Solution: Dependency graph
        # For each color C find the maximum rectangle to cover it. Any other color C' in this rectangle 
        # is a dependency of C, e.g. C' must be print first in order to print C.

        # Then this problem reduced to check if there is any cycle in the dependency graph.

        # e.g.
        # 1 2 1
        # 2 1 2
        # 1 2 1
        # The maximum rectangle for 1 and 2 are both [0, 0] ~ [2, 2]. 1 depends on 2, and 2 depends on 1. 
        # This is a circular reference and no way to print.

        # Time complexity: O(C*M*N)
        # Space complexity: O(C*C)
        kMaxC = 60
        A = targetGrid
        m, n = len(A), len(A[0])
        deps = [set() for _ in range(kMaxC+1)]
        for k in range(1, kMaxC+1):
            l, r, t, b = n, -1, m, -1
            for i in range(m):
                for j in range(n):
                    if A[i][j] == k:
                        l = min(l, j)
                        r = max(r, j)
                        t = min(t, i)
                        b = max(b, i)
            if l == -1: continue
            for i in range(t, b+1):
                for j in range(l, r+1):
                    if A[i][j] != k:
                        deps[k].add(A[i][j]) 
        print(deps)
        seen = [0]*(kMaxC + 1)
        def  hasCycle(c):
            if (seen[c] == 1): return True
            if (seen[c] == 2): return False
            seen[c] = 1
            for t in deps[c]:
                if hasCycle(t): return True
            seen[c] = 2
            return False
        for c in range(1, kMaxC+1):
            if hasCycle(c): return False
        return True        





if __name__ == '__main__':
    grid = [[1,1,1,1],[1,2,2,1],[1,2,2,1],[1,1,1,1]]
    print(Solution().isPrintable(grid))
    grid = [[1,2,1],[2,1,2],[1,2,1]]
    print(Solution().isPrintable(grid))

        