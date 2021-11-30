'''
-Medium-

We are given hours, a list of the number of hours worked per day for a given employee.

A day is considered to be a tiring day if and only if the number of hours worked 
is (strictly) greater than 8.

A well-performing interval is an interval of days for which the number of tiring days 
is strictly larger than the number of non-tiring days.

Return the length of the longest well-performing interval.

 

Example 1:

Input: hours = [9,9,6,0,6,6,9]
Output: 3
Explanation: The longest well-performing interval is [9,9,6].
Example 2:

Input: hours = [6,6,6]
Output: 0
 

Constraints:

1 <= hours.length <= 10^4
0 <= hours[i] <= 16

'''

from typing import List

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        res = score = 0
        seen = {}
        for i, h in enumerate(hours):
            score = score + 1 if h > 8 else score - 1
            if score > 0:
                res = i + 1
            seen.setdefault(score, i)
            if score - 1 in seen:
                # Here is my understanding of why we don't have to check all other score - x
                # The point is, seen stores the FIRST (very important) appearance of each score. 
                # If we think the initial score is 0, the accumulative logic will then expand 
                # the scores to the two opposite directions on the number line. Given that 
                # knowledge, you can imagine compared with other score - x, score - 1 is 
                # closest to the origin (or say, 0) on the number line. This means if you 
                # want to arrive score - x, you must have already arrived score - 1 before, 
                # because we start from 0.
                res = max(res, i - seen[score - 1])
        return res
        
        
if __name__ == '__main__':
    print(Solution().longestWPI([9,9,6,0,6,6,9]))
    print(Solution().longestWPI([6,6,6]))
    print(Solution().longestWPI([6,6,9]))
    print(Solution().longestWPI([9,9,9]))
    print(Solution().longestWPI([9,9,6,0,6,6,9,9,9]))

