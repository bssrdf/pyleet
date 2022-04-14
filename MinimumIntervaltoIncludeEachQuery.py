'''

-Hard-
*Line Sweep*
*Priority Queue*

You are given a 2D integer array intervals, where 
intervals[i] = [lefti, righti] describes the ith interval 
starting at lefti and ending at righti (inclusive). The size of 
an interval is defined as the number of integers it contains, or more 
formally righti - lefti + 1.

You are also given an integer array queries. The answer to the jth 
query is the size of the smallest interval i such 
that lefti <= queries[j] <= righti. If no such interval exists, 
the answer is -1.

Return an array containing the answers to the queries.

 

Example 1:

Input: intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]
Output: [3,3,1,4]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,4] is the smallest interval containing 2. The answer is 4 - 2 + 1 = 3.
- Query = 3: The interval [2,4] is the smallest interval containing 3. The answer is 4 - 2 + 1 = 3.
- Query = 4: The interval [4,4] is the smallest interval containing 4. The answer is 4 - 4 + 1 = 1.
- Query = 5: The interval [3,6] is the smallest interval containing 5. The answer is 6 - 3 + 1 = 4.
Example 2:

Input: intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]
Output: [2,-1,4,6]
Explanation: The queries are processed as follows:
- Query = 2: The interval [2,3] is the smallest interval containing 2. The answer is 3 - 2 + 1 = 2.
- Query = 19: None of the intervals contain 19. The answer is -1.
- Query = 5: The interval [2,5] is the smallest interval containing 5. The answer is 5 - 2 + 1 = 4.
- Query = 22: The interval [20,25] is the smallest interval containing 22. The answer is 25 - 20 + 1 = 6.
 

Constraints:

1 <= intervals.length <= 105
1 <= queries.length <= 105
intervals[i].length == 2
1 <= lefti <= righti <= 107
1 <= queries[j] <= 107
'''

from typing import List
import bisect
import heapq
class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        I = intervals
        pq = []
        for i,v in enumerate(intervals):
            heapq.heappush(pq, (I[i][1]-I[i][0]+1,i))
        n = len(queries)
        ans = [-1]*len(queries)
        qi = [(v,i) for i,v in enumerate(queries)]
        qi.sort()
        while pq:
            lth, i = heapq.heappop(pq)
            idx1 = bisect.bisect_left(qi, (I[i][0],0))
            idx2 = bisect.bisect_left(qi, (I[i][1],n))
            for j in range(idx1, idx2):
                if ans[qi[j][1]] == -1: 
                    ans[qi[j][1]] = lth
             
        return ans

    def minInterval2(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        I = intervals
        events = []
        pq = []
        for i,v in enumerate(intervals):
            events.append((v[0], -1, i))
            events.append((v[1], 1, i))
        for i,v in enumerate(queries):
            events.append((v, 0, i))
        n = len(queries)
        events.sort()
        ans = [-1]*len(queries)
        m = {}
        for e in events: 
            p, t, i = e
            if t == -1:
                m[i] = [I[i][1]-I[i][0]+1, False]
                heapq.heappush(pq, m[i])
            elif t == 1:
                m[i][1] = True
            else:
                while pq and pq[0][1]:
                    heapq.heappop(pq)
                if pq:
                    ans[i] = pq[0][0]
        return ans






    
if __name__ == "__main__":
    print(Solution().minInterval(intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]))
    print(Solution().minInterval(intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]))
    print(Solution().minInterval2(intervals = [[1,4],[2,4],[3,6],[4,4]], queries = [2,3,4,5]))
    print(Solution().minInterval2(intervals = [[2,3],[2,5],[1,8],[20,25]], queries = [2,19,5,22]))