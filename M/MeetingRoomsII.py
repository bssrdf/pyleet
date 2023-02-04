'''
Given an array of meeting time intervals consisting of start and 
end times [[s1,e1],[s2,e2],...] (si < ei), find the minimum number 
of conference rooms required.

Example 1:

Input: [[0, 30],[5, 10],[15, 20]]
Output: 2
Example 2:

Input: [[7,10],[2,4]]
Output: 1

'''

import sys
import heapq
class Solution(object):

    def rooms(self, meetings):    
        capacity = ans = 0
        for _, v in sorted(x for i, j in meetings for x in [[i, 1], [j, -1]]):
            capacity += v
            ans = max(ans, capacity)
        return ans    
        
    def roomsUsingHeap(self, meetings):
        meets = sorted(meetings, key=lambda x: x[0])
        pq = [] 
        cnt = 0      
        for m in meets:
            if not pq:
                heapq.heappush(pq, m[1])
                cnt += 1
            else:
                if m[0] >= pq[0]:
                    heapq.heappop(pq)
                else:
                    cnt += 1
                heapq.heappush(pq, m[1])
        return cnt


print(Solution().rooms([[0,30],[5,10],[15,20]]))
print(Solution().rooms([[7,10],[2,4]]))
print(Solution().roomsUsingHeap([[0,30],[5,10],[15,20]]))
print(Solution().roomsUsingHeap([[7,10],[2,4]]))

meetings = [(65,424),(351,507),(314,807),(387,722),(19,797),(259,722),(165,221),(136,897)]
print(Solution().rooms(meetings))