'''

-Hard-
*BFS*
*Hash Table*
*Priority Queue*
*Dijkstra's Algorithm*


You are given an m x n integer matrix grid and an array queries of size k.

Find an array answer of size k such that for each integer queres[i] you start in the top left cell of the matrix and repeat the following process:

If queries[i] is strictly greater than the value of the current cell that you are in, then you get one point if it is your first time visiting this cell, and you can move to any adjacent cell in all 4 directions: up, down, left, and right.
Otherwise, you do not get any points, and you end this process.
After the process, answer[i] is the maximum number of points you can get. Note that for each query you are allowed to visit the same cell multiple times.

Return the resulting array answer.

 

Example 1:


Input: grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]
Output: [5,8,1]
Explanation: The diagrams above show which cells we visit to get points for each query.
Example 2:


Input: grid = [[5,2,1],[1,1,2]], queries = [3]
Output: [0]
Explanation: We can not get any points because the value of the top left cell is already greater than or equal to 3.
 

Constraints:

m == grid.length
n == grid[i].length
2 <= m, n <= 1000
4 <= m * n <= 105
k == queries.length
1 <= k <= 104
1 <= grid[i][j], queries[i] <= 106


'''
from typing import List
from collections import defaultdict
import heapq
import bisect

class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        sums = defaultdict(int)
        m, n = len(grid), len(grid[0])
        visited = [[False]*n for _ in range(m)]
        tl = grid[0][0]
        visited[0][0] = True
        pq = [(tl, 0, 0)]
        maxsofar, cnt = 0, 0
        ans = [0]*len(queries)
        while pq:
            val, x, y = heapq.heappop(pq)
            cnt += 1
            maxsofar = max(maxsofar, val+1)
            sums[maxsofar] = cnt
            for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                i, j = x+dx, y+dy
                if 0 <= i < m and 0 <= j < n and not visited[i][j]:
                    visited[i][j] = True
                    heapq.heappush(pq, (grid[i][j], i, j))
        nums = sorted(sums)
        for i, q in enumerate(queries):
            if q <= tl: ans[i] = 0
            else: 
                idx = bisect.bisect_left(nums, q)
                ans[i] = sums[nums[idx-1]] if idx == len(nums) or nums[idx] != q else sums[nums[idx]]
        return ans








if __name__ == "__main__":
    print(Solution().maxPoints(grid = [[1,2,3],[2,5,7],[3,5,1]], queries = [5,6,2]))
    # print(Solution().maxPoints(grid = [[5,2,1],[1,1,2]], queries = [3]))
    grid = [[444424,409221,703419,11307,578382,330430,522887,38831,267101,315541,148425,360873],[353160,3217,718922,509568,494803,327636,715882,456279,374061,701863,711832,644822],[459535,264294,246310,405317,275802,948618,449015,176733,921040,56692,632708,556696],[167402,594284,8377,766746,728202,329140,399028,907843,68783,149661,244321,861358],[727577,582470,946680,222674,152875,128658,389710,581164,512061,367464,883657,78004],[463513,473823,328325,888670,267782,435621,153221,877511,900231,72761,825121,532939],[992835,33883,587426,680675,674055,682929,750368,241142,241026,369751,462134,785672],[915635,918034,398025,400424,695630,594801,748962,278900,705889,570212,42410,823342],[644602,961002,489119,606936,327139,664880,455045,231423,114466,315707,25092,961268],[962857,647428,139005,221262,469484,669734,66022,473118,258066,67408,545435,316643],[977028,938186,277400,756609,491213,704014,292941,392893,280499,650462,270100,477276],[393574,562825,637562,639836,8932,540799,758836,403682,79851,17885,851550,499020],[403665,119906,305796,88211,759076,441097,164887,709599,194,468995,922288,359913],[696749,265394,517399,161062,512967,205098,814158,627951,286474,763625,370987,798077],[166098,940946,871758,690278,903705,368584,576209,94794,25522,255261,209835,540769],[8088,89612,457088,492467,511285,900536,734726,683046,515695,14749,988608,977041],[76149,112648,515127,257871,912674,880020,32805,688253,722582,931114,734057,939655],[395351,377494,543729,368629,913310,69242,737795,849175,870860,278493,575561,111787]]
    queries = [483649,690923,317026,408761,985459,619592,287085,302896,241756,557463,914140,994632,511904,377570,272415,840485,578955,797418,609746,388421,517504,170621,188489,169881,466574]
    print(Solution().maxPoints(grid = grid, queries = queries))