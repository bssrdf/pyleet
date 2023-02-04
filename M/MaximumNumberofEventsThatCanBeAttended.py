'''
-Medium-

*Greedy*

Given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at 
startDayi and ends at endDayi.

You can attend an event i at any day d where startTimei <= d <= endTimei. Notice that you 
can only attend one event at any time d.

Return the maximum number of events you can attend.

 

Example 1:


Input: events = [[1,2],[2,3],[3,4]]
Output: 3
Explanation: You can attend all the three events.
One way to attend them all is as shown.
Attend the first event on day 1.
Attend the second event on day 2.
Attend the third event on day 3.
Example 2:

Input: events= [[1,2],[2,3],[3,4],[1,2]]
Output: 4
Example 3:

Input: events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
Output: 4
Example 4:

Input: events = [[1,100000]]
Output: 1
Example 5:

Input: events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
Output: 7
 

Constraints:

1 <= events.length <= 10^5
events[i].length == 2
1 <= startDayi <= endDayi <= 10^5
'''

from typing import List
import heapq
class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        pq = []
        events.sort()
        res, i, n = 0, 0, len(events)
        total_days = max(event[1] for event in events)
        for day in range(1, total_days+1):
            while pq and pq[0] < day:
                heapq.heappop(pq)
            while i < n and events[i][0] == day:
                heapq.heappush(pq, events[i][1])
                i += 1
            if pq:
                heapq.heappop(pq)
                res += 1
        return res
    
    def maxEvents2(self, events: List[List[int]]) -> int:
        A = events
        A.sort(reverse=1)
        h = []
        res = d = 0
        while A or h:
            if not h: d = A[-1][0]
            while A and A[-1][0] <= d:
                heapq.heappush(h, A.pop()[1])
            heapq.heappop(h)
            res += 1
            d += 1
            while h and h[0] < d:
                heapq.heappop(h)
        return res


if __name__ == "__main__":
    print(Solution().maxEvents([[1,2],[2,3],[3,4]]))
    print(Solution().maxEvents2([[1,2],[2,3],[3,4]]))
        