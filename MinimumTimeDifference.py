'''
-Medium-
Given a list of 24-hour clock time points in "HH:MM" format, 
return the minimum minutes difference between any two time-points in the list.
 

Example 1:

Input: timePoints = ["23:59","00:00"]
Output: 1
Example 2:

Input: timePoints = ["00:00","23:59","00:00"]
Output: 0
 

Constraints:

2 <= timePoints <= 2 * 104
timePoints[i] is in the format "HH:MM".



'''



from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        timePoints.sort()
        t1 = timePoints[0].split(':')
        A = timePoints + [str(int(t1[0])+24)+':'+t1[1]]
        def diff(t1, t2):
            s1, s2 = t1.split(":"), t2.split(":")
            return 60*(int(s2[0]) -int(s1[0])) + (int(s2[1]) -int(s1[1])) 
        res = 24*60
        for i in range(len(A)-1):
            res = min(res, diff(A[i], A[i+1]))
        return res
        