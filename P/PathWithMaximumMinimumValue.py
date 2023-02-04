'''
-Medium-

Given a matrix of integers A with R rows and C columns, find the maximum 
score of a path starting at [0,0] and ending at [R-1,C-1].

The score of a path is the minimum value in that path. For example, the 
value of the path 8 -> 4 -> 5 -> 9 is 4.

A path moves some number of times from one visited cell to any neighbouring 
unvisited cell in one of the 4 cardinal directions (north, east, west, south).

Example 1:
Leetcode: Path With Maximum Minimum Value

Input: [[5,4,5],[1,2,6],[7,4,6]]
Output: 4
Explanation: 
The path with the maximum score is highlighted in yellow. 
Example 2:
Leetcode: Path With Maximum Minimum Value

Input: [[2,2,1,2,2,2],[1,2,2,2,1,2]]
Output: 2
Example 3:
Leetcode: Path With Maximum Minimum Value

Input: [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
Output: 3
Note:

1 <= R, C <= 100
0 <= A[i][j] <= 10^9



'''
import heapq

class Solution(object):

    def maximumMinimumPath(self, A):
        m, n = len(A), len(A[0])
        visited = [[False]*n for _ in range(m)]
        dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        maxQ = [(-A[0][0], 0, 0)]
        visited[0][0] = True
        res = A[0][0]
        while maxQ:
            cur, i, j = heapq.heappop(maxQ)
            res = min(res, -cur)
            if (i,j) == (m-1, n-1):
                return res
            for d in dirs:
                x, y = i+d[0], j+d[1] 
                if x >= 0 and x < m and y >= 0 and y < n and not visited[x][y]:
                    heapq.heappush(maxQ, (-A[x][y], x, y)) 
                    visited[x][y] = True
        return res
            


if __name__ == "__main__":
    A = [[5,4,5],[1,2,6],[7,4,6]]
    print(Solution().maximumMinimumPath(A))
    A = [[2,2,1,2,2,2],[1,2,2,2,1,2]]
    print(Solution().maximumMinimumPath(A))
    A = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
    print(Solution().maximumMinimumPath(A))
