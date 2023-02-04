'''
-Hard-
*Priority Queue*
*Monotonic Queue*
*Sliding Window*

You are given an array points containing the coordinates of points on a 2D plane, sorted by the x-values, where points[i] = [xi, yi] such that xi < xj for all 1 <= i < j <= points.length. You are also given an integer k.

Return the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k and 1 <= i < j <= points.length.

It is guaranteed that there exists at least one pair of points that satisfy the constraint |xi - xj| <= k.

 

Example 1:

Input: points = [[1,3],[2,0],[5,10],[6,-10]], k = 1
Output: 4
Explanation: The first two points satisfy the condition |xi - xj| <= 1 and if we calculate the equation we get 3 + 0 + |1 - 2| = 4. Third and fourth points also satisfy the condition and give a value of 10 + -10 + |5 - 6| = 1.
No other pairs satisfy the condition, so we return the max of 4 and 1.
Example 2:

Input: points = [[0,0],[3,0],[9,2]], k = 3
Output: 3
Explanation: Only the first two points have an absolute difference of 3 or less in the x-values, and give the value of 0 + 0 + |0 - 3| = 3.
 

Constraints:

2 <= points.length <= 105
points[i].length == 2
-108 <= xi, yi <= 108
0 <= k <= 2 * 108
xi < xj for all 1 <= i < j <= points.length
xi form a strictly increasing sequence.

'''

from typing import List
import heapq
from collections import deque

class Solution:
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        pq = [] # max heap
        ans = -float('inf')
        for x, y in points:            
            while pq and x - pq[0][1] > k:
                heapq.heappop(pq)   
            if pq:
                ans = max(ans, -pq[0][0] + x + y)
            heapq.heappush(pq, (x-y, x))
        return ans

    def findMaxValueOfEquation2(self, points: List[List[int]], k: int) -> int:
        q = deque()
        res = -float('inf')
        for x, y in points:
            while q and q[0][1] < x - k: # sliding window
                q.popleft()
            if q: res = max(res, q[0][0] + y + x)
            while q and q[-1][0] <= y - x: # monotonic decreasing queue
                q.pop()
            q.append([y - x, x])
        return res




if __name__ == "__main__":
    print(Solution().findMaxValueOfEquation(points = [[1,3],[2,0],[5,10],[6,-10]], k = 1))
        