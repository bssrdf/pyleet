'''
-Medium-

You are given a 0-indexed 2D integer array of events where 
events[i] = [startTimei, endTimei, valuei]. The ith event starts at 
startTimei and ends at endTimei, and if you attend this event, you will 
receive a value of valuei. You can choose at most two non-overlapping events 
to attend such that the sum of their values is maximized.

Return this maximum sum.

Note that the start time and end time is inclusive: that is, you cannot 
attend two events where one of them starts and the other ends at the same time. 
More specifically, if you attend an event with end time t, the next event 
must start at or after t + 1.

 

Example 1:


Input: events = [[1,3,2],[4,5,2],[2,4,3]]
Output: 4
Explanation: Choose the green events, 0 and 1 for a sum of 2 + 2 = 4.
Example 2:

Example 1 Diagram
Input: events = [[1,3,2],[4,5,2],[1,5,5]]
Output: 5
Explanation: Choose event 2 for a sum of 5.
Example 3:


Input: events = [[1,5,3],[1,5,1],[6,6,5]]
Output: 8
Explanation: Choose events 0 and 2 for a sum of 3 + 5 = 8.
 

Constraints:

2 <= events.length <= 10^5
events[i].length == 3
1 <= startTimei <= endTimei <= 10^9
1 <= valuei <= 10^6

'''

from typing import List
import bisect

class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        n, sortStart, sortEnd = len(events), [], []
        for i, (s, e, v) in enumerate(events):
            sortStart.append((s, i))
            sortEnd.append((e, i))
        sortStart.sort()
        sortEnd.sort()
        # Q: How can we quickly get the maximum score of an interval not intersecting 
        # with the interval we chose?
        # A: precompute the maximum score at the index binary search finds
        maxScoreSt, maxScoreEn = [0]*n, [0]*n
        maxScoreSt[-1] = events[sortStart[-1][1]][2]
        maxScoreEn[0] = events[sortEnd[0][1]][2]
        for i in range(1, n):
            maxScoreEn[i] = max(maxScoreEn[i-1], events[sortEnd[i][1]][2])  
        for i in range(n-2,-1,-1):
            maxScoreSt[i] = max(maxScoreSt[i+1], events[sortStart[i][1]][2])  
        ans = 0
        for i, (s, e, v) in enumerate(events):
            ans = max(ans, v)
            idx = bisect.bisect_left(sortEnd, (s,0)) - 1
            if idx >= 0:
                ans = max(ans, v+maxScoreEn[idx])
            idx = bisect.bisect_right(sortStart, (e,n)) + 1
            if idx < n:
                ans = max(ans, v+maxScoreSt[idx])
        return ans    

    def maxTwoEvents2(self, events: List[List[int]]) -> int:
        n, sortStart, sortEnd = len(events), [], []
        for i, (s, e, v) in enumerate(events):
            sortStart.append((s, i))
            sortEnd.append((e, i))
        sortStart.sort()
        sortEnd.sort()
        st = [s[0] for s in sortStart]
        se = [s[0] for s in sortEnd]
            
        # Q: How can we quickly get the maximum score of an interval not intersecting 
        # with the interval we chose?
        # A: precompute the maximum score at the index binary search finds
        maxScoreSt, maxScoreEn = [0]*n, [0]*n
        maxScoreSt[-1] = events[sortStart[-1][1]][2]
        maxScoreEn[0] = events[sortEnd[0][1]][2]
        for i in range(1, n):
            maxScoreEn[i] = max(maxScoreEn[i-1], events[sortEnd[i][1]][2])  
        for i in range(n-2,-1,-1):
            maxScoreSt[i] = max(maxScoreSt[i+1], events[sortStart[i][1]][2])  
        ans = 0
        for i, (s, e, v) in enumerate(events):
            ans = max(ans, v)
            idx = bisect.bisect_left(se, s) - 1
            if idx >= 0:
                ans = max(ans, v+maxScoreEn[idx])
            idx = bisect.bisect_right(st, e) + 1
            if idx < n:
                ans = max(ans, v+maxScoreSt[idx])
        return ans    
    

if __name__ == "__main__":
    print(Solution().maxTwoEvents([[1,3,2],[4,5,2],[2,4,3]]))
    print(Solution().maxTwoEvents([[1,3,2],[4,5,2],[1,5,5]]))
    print(Solution().maxTwoEvents([[1,5,3],[1,5,1],[6,6,5]]))
    print(Solution().maxTwoEvents([[1,1,1],[1,1,1]]))
    print(Solution().maxTwoEvents2([[1,3,2],[4,5,2],[2,4,3]]))
    print(Solution().maxTwoEvents2([[1,3,2],[4,5,2],[1,5,5]]))
    print(Solution().maxTwoEvents2([[1,5,3],[1,5,1],[6,6,5]]))
    print(Solution().maxTwoEvents2([[1,1,1],[1,1,1]]))