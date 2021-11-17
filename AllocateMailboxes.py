'''

-Hard-

Given the array houses and an integer k. where houses[i] is the location of the ith 
house along a street, your task is to allocate k mailboxes in the street.

Return the minimum total distance between each house and its nearest mailbox.

The answer is guaranteed to fit in a 32-bit signed integer.

 

Example 1:



Input: houses = [1,4,8,10,20], k = 3
Output: 5
Explanation: Allocate mailboxes in position 3, 9 and 20.
Minimum total distance from each houses to nearest mailboxes is |3-1| + |4-3| + |9-8| + |10-9| + |20-20| = 5 
Example 2:



Input: houses = [2,3,5,12,18], k = 2
Output: 9
Explanation: Allocate mailboxes in position 3 and 14.
Minimum total distance from each houses to nearest mailboxes is |2-3| + |3-3| + |5-3| + |12-14| + |18-14| = 9.
Example 3:

Input: houses = [7,4,6,1], k = 1
Output: 8
Example 4:

Input: houses = [3,6,14,10], k = 4
Output: 0
 

Constraints:

n == houses.length
1 <= n <= 100
1 <= houses[i] <= 10^4
1 <= k <= n
Array houses contain unique integers.

'''

from typing import List
from functools import lru_cache
import math

class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        n = len(houses)
        houses = sorted(houses)
        dist = [[0] * n for _ in range(n)] # precompute this distance array
        for i in range(n):
            for j in range(n):
                medianPos = houses[(i + j) // 2] # put a mailbox at medianPos
                for m in range(i, j + 1):
                    dist[i][j] += abs(medianPos - houses[m]) # sum of distance of all houses[i:j] to that mail box


        @lru_cache(None)
        def dp(k, i):
            if k == 0 and i == n: return 0 # base case
            if k == 0 or i == n: return math.inf # impossible base cases
            ans = math.inf
            for j in range(i, n):
                cost = dist[i][j]  # Try to put a mailbox among house[i:j]
                ans = min(ans, cost + dp(k - 1, j + 1))
            return ans

        return dp(k, 0)

if __name__ == "__main__":
    print(Solution().minDistance(houses = [1,4,8,10,20], k = 3))        

