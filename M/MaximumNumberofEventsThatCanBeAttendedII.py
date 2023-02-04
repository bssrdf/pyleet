'''
-Hard-
*DP*
*Binary Search*

You are given an array of events where events[i] = [startDayi, endDayi, valuei]. The ith 
event starts at startDay_i and ends at endDay_i, and if you attend this event, you will 
receive a value of value_i. You are also given an integer k which represents the maximum 
number of events you can attend.

You can only attend one event at a time. If you choose to attend an event, you must attend 
the entire event. Note that the end day is inclusive: that is, you cannot attend two events 
where one of them starts and the other ends on the same day.

Return the maximum sum of values that you can receive by attending events.

 

Example 1:



Input: events = [[1,2,4],[3,4,3],[2,3,1]], k = 2
Output: 7
Explanation: Choose the green events, 0 and 1 (0-indexed) for a total value of 4 + 3 = 7.
Example 2:



Input: events = [[1,2,4],[3,4,3],[2,3,10]], k = 2
Output: 10
Explanation: Choose event 2 for a total value of 10.
Notice that you cannot attend any other event as they overlap, and that you do not have to attend k events.
Example 3:



Input: events = [[1,1,1],[2,2,2],[3,3,3],[4,4,4]], k = 3
Output: 9
Explanation: Although the events do not overlap, you can only attend 3 events. Pick the highest valued three.
 

Constraints:

1 <= k <= events.length
1 <= k * events.length <= 10^6
1 <= startDayi <= endDayi <= 10^9
1 <= valuei <= 10^6


'''
from typing import List
from bisect import bisect_left

class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events = sorted(events)
        S = [i[0] for i in events]
        
        m = len(events)
        dp = [[0]*(k+1) for _ in range(m+1)]
        # dp[i] is the max earning starting at i-th ride
        # base case: dp[m] = 0 (zero earnings)
        # work backwards        
        for j in range(1,k+1):
            for i in range(m-1, -1, -1):
                s, e, v = events[i]
                temp = bisect_left(S, e) # 
                dp[i][j] = max(dp[i+1][j], dp[i][j-1], v + dp[temp][j-1]) # 
        return dp[0][k]

    def maxValue2(self, events: List[List[int]], k: int) -> int:
        events = sorted(events, key=lambda x: x[1])
        E = [i[1] for i in events]
        
        m = len(events)
        dp = [[0]*(k+1) for _ in range(m+1)]
        # dp[i] is the max earning ending i-th event
        # base case: dp[0] = 0 (zero earnings)
        # work forward
        for j in range(1,k+1):
            for i in range(1,m+1):
                s, e, v = events[i-1]
                temp = bisect_left(E, s) # 
                # the maximum value by attending at most j events can be the same 
                # as what achieved by attending at most j - 1 events.
                # dp[i][j]= Math.max(dp[i][j], dp[i][j-1]);

                # the maximum value by attending j events from 0 to i-th events can be the same
                # as what achieved by attending at most the same number of events from the first 0 to (i-1)-th events
                # dp[i][j] = Math.max(dp[i][j], dp[i-1][j]);

                # attend i-th event. In this case, add event value (= events[i][2]) to dp[prev[i]][j-1]
                dp[i][j] = max(dp[i-1][j], dp[i][j-1], v + dp[temp][j-1]) # 
        return dp[m][k]    
        

if __name__ == "__main__":
    print(Solution().maxValue(events = [[1,2,4],[3,4,3],[2,3,1]], k = 2))
    print(Solution().maxValue(events = [[1,2,4],[3,4,3],[2,3,10]], k = 2))
    print(Solution().maxValue2(events = [[1,2,4],[3,4,3],[2,3,1]], k = 2))
    print(Solution().maxValue2(events = [[1,2,4],[3,4,3],[2,3,10]], k = 2))