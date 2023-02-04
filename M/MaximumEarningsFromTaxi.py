'''
-Medium-

There are n points on a road you are driving your taxi on. The n points on the road are 
labeled from 1 to n in the direction you are going, and you want to drive from point 1 to 
point n to make money by picking up passengers. You cannot change the direction of the taxi.

The passengers are represented by a 0-indexed 2D integer array rides, where 
rides[i] = [starti, endi, tipi] denotes the ith passenger requesting a ride from point 
start_i to point end_i who is willing to give a tip_i dollar tip.

For each passenger i you pick up, you earn endi - starti + tipi dollars. You may only 
drive at most one passenger at a time.

Given n and rides, return the maximum number of dollars you can earn by picking up the 
passengers optimally.

Note: You may drop off a passenger and pick up a different passenger at the same point.

 

Example 1:

Input: n = 5, rides = [[2,5,4],[1,5,1]]
Output: 7
Explanation: We can pick up passenger 0 to earn 5 - 2 + 4 = 7 dollars.
Example 2:

Input: n = 20, rides = [[1,6,1],[3,10,2],[10,12,3],[11,12,2],[12,15,2],[13,18,1]]
Output: 20
Explanation: We will pick up the following passengers:
- Drive passenger 1 from point 3 to point 10 for a profit of 10 - 3 + 2 = 9 dollars.
- Drive passenger 2 from point 10 to point 12 for a profit of 12 - 10 + 3 = 5 dollars.
- Drive passenger 5 from point 13 to point 18 for a profit of 18 - 13 + 1 = 6 dollars.
We earn 9 + 5 + 6 = 20 dollars in total.
 

Constraints:

1 <= n <= 10^5
1 <= rides.length <= 3 * 10^4
rides[i].length == 3
1 <= start_i < end_i <= n
1 <= tip_i <= 10^5


'''

from typing import List
from collections import defaultdict
from bisect import bisect_left
class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        rideStartAt = defaultdict(list)
        for s, e, t in rides:
            rideStartAt[s].append([e, e - s + t])  # [end, dollar]

        dp = [0] * (n + 1)
        for i in range(n - 1, 0, -1):
            for e, d in rideStartAt[i]:
                dp[i] = max(dp[i], dp[e] + d)
            dp[i] = max(dp[i], dp[i + 1])

        return dp[1]

    def maxTaxiEarnings2(self, n, rides):        
        rides = sorted(rides)
        S = [i[0] for i in rides]
        
        m = len(rides)
        dp = [0]*(m+1)
        # dp[i] is the max earning starting at i-th ride
        # base case: dp[m] = 0 (zero earnings)
        # work backwards        
        for k in range(m-1, -1, -1):
            s,e,t = rides[k]
            temp = bisect_left(S, e) # the ride which start at temp has eranings dp[temp]
            dp[k] = max(dp[k+1], e - s + t + dp[temp]) # earning at ride k 
            
        return dp[0]    

if __name__ == "__main__":
    print(Solution().maxTaxiEarnings(5, [[2,5,4],[1,5,1]]))
    print(Solution().maxTaxiEarnings2(5, [[2,5,4],[1,5,1]]))