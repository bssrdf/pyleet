'''

-Medium-
*Sweep Line*



You are given a 2D integer array ranges where ranges[i] = [starti, endi] denotes that all integers between starti and endi (both inclusive) are contained in the ith range.

You are to split ranges into two (possibly empty) groups such that:

Each range belongs to exactly one group.
Any two overlapping ranges must belong to the same group.
Two ranges are said to be overlapping if there exists at least one integer that is present in both ranges.

For example, [1, 3] and [2, 5] are overlapping because 2 and 3 occur in both ranges.
Return the total number of ways to split ranges into two groups. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: ranges = [[6,10],[5,15]]
Output: 2
Explanation: 
The two ranges are overlapping, so they must be in the same group.
Thus, there are two possible ways:
- Put both the ranges together in group 1.
- Put both the ranges together in group 2.
Example 2:

Input: ranges = [[1,3],[10,20],[2,5],[4,8]]
Output: 4
Explanation: 
Ranges [1,3], and [2,5] are overlapping. So, they must be in the same group.
Again, ranges [2,5] and [4,8] are also overlapping. So, they must also be in the same group. 
Thus, there are four possible ways to group them:
- All the ranges in group 1.
- All the ranges in group 2.
- Ranges [1,3], [2,5], and [4,8] in group 1 and [10,20] in group 2.
- Ranges [1,3], [2,5], and [4,8] in group 2 and [10,20] in group 1.
 

Constraints:

1 <= ranges.length <= 105
ranges[i].length == 2
0 <= starti <= endi <= 109


'''

from typing import List
from collections import Counter
import math

class Solution:
    def countWays(self, ranges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        events = []
        for l,r in ranges:
            events.append((l, 1))
            events.append((r, -1))
        events.sort(key=lambda x: (x[0], -x[1]))
        cnt, sm, groups = 0, 0, []
        for i in range(len(events)):
            _, y = events[i]             
            if y == 1:
                cnt += 1
            sm += y 
            if sm == 0:
                groups.append(cnt)
                cnt = 0
        # print(groups)
        # return (2*math.comb(len(groups), 2) + 2)%MOD
        return pow(2, len(groups), MOD)
    
    def countWays2(self, ranges: List[List[int]]) -> int:
        MOD = 10**9 + 7
        events = []
        for l,r in ranges:
            events.append((l, 1))
            events.append((r, -1))
        events.sort(key=lambda x: (x[0], -x[1]))
        cnt, sm = 0, 0
        for i in range(len(events)):
            _, y = events[i]             
            sm += y 
            if sm == 0:               
                cnt += 1
        return pow(2, cnt, MOD)




if __name__ == '__main__':
    print(Solution().countWays( ranges = [[0,2],[2,3]]))
    print(Solution().countWays( ranges = [[6,10],[5,15]]))
    print(Solution().countWays( ranges = [[1,3],[10,20],[2,5],[4,8]]))
    print(Solution().countWays( ranges = [[1,2],[1,1],[0,4]]))
    print(Solution().countWays( ranges = [[0,0],[8,9],[12,13],[1,3]]))