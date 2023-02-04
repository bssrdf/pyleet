'''
-Medium-

*DFS*

Given a m-by-n grid: every element is non-negative integer.

Constrains:
(1) a path only contain non-zero cells
(2) a path can extend to 4 directions: up, down, left, right
(3) no same cell in a path
Assumption
(4) cells with non-0 number will not form a cycle

Find the maximum path sum.

Example 1:

Input:
5 4 1 0
1 0 1 2
3 0 0 4
0 1 2 0

Output: 21
Explanation: 3 -> 1 -> 5 -> 4 -> 1 -> 1 -> 2 -> 4
Example 2:

Input:
5 4 1 3
1 0 1 0
3 0 0 4
0 1 2 0

Output: 17
Explanation: 3 -> 1 -> 5 -> 4 -> 1 -> 3

'''


class Solution(object):

    def max_path_sum(self,grid):
        def dfs(i, j):
            visited[i][j] = True
            neighbor_sums = []
            for di, dj in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
                x, y = i + di, j + dj
                if 0 <= x < M and 0 <= y < N and grid[x][y] != 0 and not visited[x][y]:
                    neighbor_sums.append(dfs(x, y))
            neighbor_sums.sort(reverse=True)
            if not neighbor_sums:
                max_sum[0] = max(max_sum[0], grid[i][j])
                return grid[i][j]
            else:
                max_sum[0] = max(max_sum[0], grid[i][j] + sum(neighbor_sums[:2]))
                return grid[i][j] + max(neighbor_sums)
                            
        if not grid or not grid[0]:
            return 0
        M, N = len(grid), len(grid[0])
        visited = [[False for _ in range(N)] for _ in range(M)]
        max_sum = [0]
        for i in range(M):
            for j in range(N):
                if grid[i][j] != 0 and not visited[i][j]:
                    dfs(i, j)
        return max_sum[0]

if __name__ == '__main__':
    matrix = [[5, 4, 1, 0],
              [1, 0, 1, 2],
              [3, 0, 0, 4],
              [0, 1, 2, 0]]
    print(Solution().max_path_sum(matrix))