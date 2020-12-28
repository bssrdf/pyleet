'''
-Medium-
*Sort*
*Interval*

Given an array of intervals where intervals[i] = [starti, endi], merge all 
overlapping intervals, and return an array of the non-overlapping intervals 
that cover all the intervals in the input.

 

Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.
 

Constraints:

1 <= intervals.length <= 10^4
intervals[i].length == 2
0 <= starti <= endi <= 10^4
'''

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        candidate = intervals[0]
        res = []
        for iv in intervals[1:]:
            if candidate[1] < iv[0]:
                res.append(candidate)
                candidate = iv
            elif candidate[1] < iv[1]:
                candidate = [candidate[0], iv[1]]                
        res.append(candidate)
        return res


if __name__ == "__main__":
    print(Solution().merge([[1,3],[2,6],[8,10],[15,18]]))
    print(Solution().merge([[1,4],[4,5]]))
    print(Solution().merge([[1,4],[0,4]]))
    print(Solution().merge([[1,4],[2,3]]))
    print(Solution().merge([[2,3],[4,5],[6,7],[8,9],[1,10]]))


'''
# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

    # To print the result
    def __str__(self):
        return "[" + str(self.start) + "," + str(self.end) + "]"
    

import sys

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        result = []
        if not intervals:
            return result
        intervals.sort(key=lambda x: x.start)
        intervals.append(Interval(sys.maxint, sys.maxint))
        newInv = intervals[0]
        for iv in intervals[1:]:
            if iv.start <= newInv.end:
                newInv.end = max(iv.end, newInv.end)
            else:
                result.append(Interval(newInv.start, newInv.end))
                newInv = Interval(iv.start, iv.end)
        return result


if __name__ == "__main__":
    intervals = Solution().merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)])
    #intervals = Solution().merge([Interval(1, 3), Interval(5, 9), Interval(2, 6), Interval(8, 10), Interval(15, 18)])
    for interval in intervals:
        print(interval)
'''
