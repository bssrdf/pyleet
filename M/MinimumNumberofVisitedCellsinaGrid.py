'''

-Hard-
*DP*
*Priority Queue*

You are given a 0-indexed m x n integer matrix grid. Your initial position is at the top-left cell (0, 0).

Starting from the cell (i, j), you can move to one of the following cells:

Cells (i, k) with j < k <= grid[i][j] + j (rightward movement), or
Cells (k, j) with i < k <= grid[i][j] + i (downward movement).
Return the minimum number of cells you need to visit to reach the bottom-right cell (m - 1, n - 1). If there is no valid path, return -1.

 

Example 1:


Input: grid = [[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]
Output: 4
Explanation: The image above shows one of the paths that visits exactly 4 cells.
Example 2:


Input: grid = [[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]]
Output: 3
Explanation: The image above shows one of the paths that visits exactly 3 cells.
Example 3:


Input: grid = [[2,1,0],[1,0,0]]
Output: -1
Explanation: It can be proven that no path exists.
 

Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 105
1 <= m * n <= 105
0 <= grid[i][j] < m * n
grid[m - 1][n - 1] == 0


'''

from typing import List
from heapq import heappop, heappush
from bisect import bisect_left

class Solution:
    def minimumVisitedCells(self, grid: List[List[int]]) -> int:
        A = grid
        m, n = len(grid), len(grid[0])
        # print(m, n)
        inf = m+n+10
        pqs = [[] for _ in range(n)]
        dist = [[inf]*n for _ in range(m)]
        dist[0][0] = 1
        for i in range(m):
            pq = []
            for j in range(n):
                # for a particular cell (i,j), we need to determine the smallest dist[i][j]
                # by looking up (same column) and left (same row) to find a cell (x,y) with
                # smallest dist that can reach (i,j) in one step
                # We use two heaps to do it: 
                # one heap maintains (dist[i][j], j+A[i][j]) 
                # the other maintains (dist[i][j], i+A[i][j]) 
                # we can continuously pop pq[0] if pq[0][1] < j, because
                # for j, j+1, j+2, ..., all pq[i]'s where pq[i][1] < j are not needed
                while pq and pq[0][1] < j: heappop(pq)
                # similarly, we can continuously pop pqs[j] if pqs[j][0][1] < i, because
                # for i, i+1, i+2, ..., all pqs[j]'s where pqs[j][0][1] < i are not needed
                while pqs[j] and pqs[j][0][1] < i: heappop(pqs[j])
                # update dist[i][j] based on one-step neighbor of the smallest dist 
                # if one is available
                if pq: dist[i][j] = min(dist[i][j], pq[0][0] + 1)
                if pqs[j]: dist[i][j] = min(dist[i][j], pqs[j][0][0] + 1)
                if dist[i][j] < inf:
                    heappush(pq, (dist[i][j], j + A[i][j]))
                    heappush(pqs[j], (dist[i][j], i + A[i][j]))
        return dist[-1][-1] if dist[-1][-1] < inf else -1

    def minimumVisitedCells2(self, grid: List[List[int]]) -> int:
        # Dijkstra with pruning, slow but still AC
        m, n = len(grid), len(grid[0])
        if m == 1 and n == 1: return 1 # 特判
        inf = m + n + 10
        h = [(1, 0, 0)] # (d, pos)
        seen = set()
        dist = [[inf] * n for _ in range(m)]
        dist[0][0] = 1

        while h:
            d, i, j = heappop(h)
            if (i, j) in seen: continue
            seen.add((i, j))
            for k in range(1, grid[i][j] + 1):
                for x, y in ((i, j + k), (i + k, j)):
                    if x == m - 1 and y == n - 1: return d + 1                    
                    if m > x >= 0 <= y < n and d + 1 < dist[x][y]:
                        if grid[x][y] == 0: continue
                        dist[x][y] = d + 1
                        heappush(h, (d + 1, x, y))
        return -1
    
    def minimumVisitedCells3(self, grid: List[List[int]]) -> int:
        # DP + monotonic stack + binary search
        # https://leetcode.cn/problems/minimum-number-of-visited-cells-in-a-grid/solution/dan-diao-zhan-you-hua-dp-by-endlesscheng-mc50/
        m, n = len(grid), len(grid[0])
        col_st = [[] for _ in range(n)]  # 每列的单调栈
        inf = m + n + 10
        for i in range(m - 1, -1, -1):
            st = []  # 当前行的单调栈
            for j in range(n - 1, -1, -1):
                st2 = col_st[j]
                mn = inf
                g = grid[i][j]
                if i == m - 1 and j == n - 1:  # 特殊情况：已经是终点
                    mn = 0
                elif g:
                    # 在单调栈上二分
                    k = bisect_left(st, -(j + g), key=lambda p: p[1])
                    if k < len(st): mn = min(mn, st[k][0])
                    k = bisect_left(st2, -(i + g), key=lambda p: p[1])
                    if k < len(st2): mn = min(mn, st2[k][0])
                if mn == inf: continue

                mn += 1  # 加上 (i,j) 这个格子
                # 插入单调栈
                while st and mn <= st[-1][0]: # pop out larger dist from stack top
                    # why do we pop out larger ones?
                    # when going from right to left (on the same row), if we encounter
                    # a smaller dist, then we don't need previous bigger ones because 
                    # the current smaller dist has more chances to be found by cells
                    # to the left.  
                    # so what we need is a monotonic increasing stack going from right
                    # to left; the index is taken its negative to be increasing as well 
                    st.pop()
                st.append((mn, -j))  # 保证下标单调递增，方便调用 bisect_left
                while st2 and mn <= st2[-1][0]:
                    st2.pop()
                st2.append((mn, -i))  # 保证下标单调递增，方便调用 bisect_left
        return mn if mn < inf else -1  # 最后一个算出的 mn 就是 f[0][0]
    
    def minimumVisitedCells4(self, grid: List[List[int]]) -> int:
        # DP + fenwick tree        
        m, n = len(grid), len(grid[0])
        inf = m+n+10
        col_bits = [[inf]*(m+1) for _ in range(n)]  # BIT for each column
        def query(bit, r):
            ret = inf
            while r > 0:
                ret = min(ret, bit[r])
                r -= r & (-r)
            return ret
        def update(bit, idx, val):
            while idx < len(bit):
                bit[idx] = min(bit[idx], val)
                idx += idx & (-idx) 
        for i in range(m - 1, -1, -1):
            row = [inf]*(n+1)  # BIT for current row
            for j in range(n - 1, -1, -1):            
                col = col_bits[j]
                mn = inf
                g = grid[i][j]
                if i == m - 1 and j == n - 1:  # base case
                    mn = 0
                elif g:
                    mn = min(mn, query(row, min(j+g+1, n)))   
                    mn = min(mn, query(col, min(i+g+1, m)))                       
                if mn == inf: continue
                mn += 1  # add one more step
                update(row, j+1, mn)
                update(col, i+1, mn)                
        return mn if mn < inf else -1  # the last mn is f[0][0]


        




if __name__ == '__main__':
    print(Solution().minimumVisitedCells(grid = [[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]))
    print(Solution().minimumVisitedCells4(grid = [[3,4,2,1],[4,2,3,1],[2,1,0,0],[2,4,0,0]]))
    print(Solution().minimumVisitedCells(grid = [[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]]))
    print(Solution().minimumVisitedCells4(grid = [[3,4,2,1],[4,2,1,1],[2,1,1,0],[3,4,1,0]]))
    # print(Solution().minimumVisitedCells(grid = [[2,1,0],[1,0,0]]))
    grid = [[11,67,49,33,8,19,64,39,39,36,45,41,18,9,7,52,42,9,39,12,44,27,33,41,1],[37,15,43,1,53,57,13,11,6,10,6,49,8,41,18,54,0,6,12,26,40,14,26,35,27],[66,37,13,64,57,38,21,15,26,21,43,9,46,50,33,53,13,5,39,18,46,45,33,26,27],[19,51,31,23,5,1,44,49,1,2,1,27,46,0,6,43,23,23,22,31,45,27,1,27,19],[36,30,30,36,28,20,4,57,56,36,51,19,8,28,28,16,38,26,43,0,7,21,40,36,27],[40,47,34,44,28,35,16,21,1,34,14,18,24,4,32,43,0,19,42,20,29,21,37,2,25],[28,0,4,13,50,38,27,30,4,49,23,2,36,1,50,16,8,1,3,45,13,6,35,20,13],[55,2,26,17,43,38,0,32,28,20,53,24,13,25,34,33,29,32,24,41,40,15,22,30,22],[15,52,35,30,30,30,11,23,16,10,2,32,12,9,29,10,5,27,10,41,30,5,31,20,16],[45,6,45,28,42,30,46,53,2,22,12,12,17,13,5,14,6,25,14,7,21,10,28,16,12],[37,6,33,11,44,35,18,14,41,51,5,21,43,7,18,9,5,25,3,1,28,33,25,17,2],[28,23,30,40,23,42,46,25,41,0,23,37,7,4,5,29,43,20,5,29,34,31,10,13,17],[7,13,40,38,20,10,42,21,50,48,15,31,0,6,23,35,22,36,15,20,8,10,19,10,5],[18,31,28,11,28,16,8,49,0,28,29,35,4,30,25,17,5,11,6,26,16,28,2,25,13],[36,36,37,23,14,11,0,36,18,37,10,41,17,32,5,36,14,22,11,17,26,31,22,26,31],[46,44,47,23,38,50,25,36,41,23,44,26,25,14,15,25,5,4,8,21,13,28,13,20,12],[44,9,1,15,13,29,25,0,36,41,5,37,29,37,0,12,24,17,0,34,31,11,16,31,25],[10,24,21,17,9,0,10,5,29,18,23,0,17,36,28,27,26,2,9,24,9,6,14,7,22],[24,4,17,18,24,12,32,20,15,6,9,29,20,21,28,36,22,14,8,18,9,5,4,16,13],[42,36,15,41,46,15,30,38,7,25,32,31,3,30,8,1,35,3,27,27,11,10,21,8,4],[47,14,21,6,13,40,0,30,8,35,1,22,2,6,1,35,32,6,20,18,4,1,3,14,10],[49,27,1,39,14,15,16,19,17,36,5,10,5,29,34,27,3,0,6,17,4,4,2,3,2],[12,33,30,35,11,19,13,21,0,37,36,12,0,27,17,21,11,6,21,21,19,17,20,2,16],[4,29,32,30,5,1,28,13,33,12,23,7,25,33,2,23,25,22,23,4,27,16,2,16,19],[27,36,38,13,12,39,16,13,38,11,14,5,31,10,13,16,27,22,11,16,16,3,13,9,3],[9,11,13,13,23,17,14,8,13,18,17,14,19,17,8,21,12,14,12,10,3,19,18,21,6],[2,9,8,14,11,29,17,30,9,22,0,31,25,4,14,26,12,0,8,12,19,8,22,16,9],[18,23,30,23,0,17,24,28,16,8,2,28,22,8,8,8,17,8,21,14,3,20,16,9,9],[23,25,24,35,8,30,0,28,28,28,18,3,5,3,11,25,16,23,5,11,6,14,13,17,5],[10,34,37,28,17,1,5,31,26,11,16,1,15,7,8,23,8,0,13,11,2,17,17,10,14],[28,7,22,34,36,17,5,13,20,1,15,28,24,15,19,20,16,16,19,17,7,14,16,13,8],[19,5,25,5,22,26,16,15,3,13,2,13,6,22,3,11,13,5,2,19,7,9,7,13,2],[37,11,23,6,12,12,1,3,21,12,4,24,9,16,23,11,22,6,12,10,11,6,9,2,3],[7,25,7,0,0,1,24,3,22,25,1,15,24,22,2,14,20,0,4,13,6,11,1,11,9],[36,27,18,5,2,27,26,15,17,26,2,24,19,18,0,9,17,12,13,1,11,4,4,8,1],[5,27,33,11,29,21,27,17,2,10,23,18,6,15,5,6,2,5,17,8,8,14,0,11,6],[33,29,27,23,30,25,24,27,9,1,7,20,10,17,6,11,15,12,1,8,9,2,3,9,0],[6,14,9,12,3,18,26,2,21,1,4,6,17,17,17,8,4,13,4,4,4,0,10,5,3],[10,12,15,18,28,15,24,15,5,18,21,11,20,4,15,3,9,2,10,7,4,9,6,9,7],[29,15,19,27,15,16,20,11,1,14,21,10,3,3,5,10,4,0,13,9,4,7,9,6,2],[26,18,21,13,23,10,24,11,18,6,8,19,3,15,1,15,6,5,5,6,3,0,8,5,3],[15,13,0,20,1,21,20,7,18,16,1,2,10,7,11,11,7,10,8,3,4,5,6,0,3],[19,12,15,4,8,0,12,7,1,0,16,2,5,13,1,1,1,6,3,1,7,7,6,2,4],[22,20,16,0,5,5,9,9,19,13,3,11,6,8,8,11,0,8,5,6,0,5,1,3,2],[12,12,19,10,10,7,20,17,10,15,2,4,8,7,9,8,8,2,8,4,3,2,0,1,0],[13,22,4,5,1,0,8,17,16,10,0,10,8,6,4,7,2,1,3,3,3,4,2,2,2],[11,15,7,5,7,10,6,12,2,10,8,1,3,4,3,8,3,7,6,3,2,1,1,0,0]]
    print(Solution().minimumVisitedCells(grid = grid))
    print(Solution().minimumVisitedCells2(grid = grid))
    print(Solution().minimumVisitedCells4(grid = grid))