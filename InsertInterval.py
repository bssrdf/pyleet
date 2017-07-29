'''
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10]
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
    def insert(self, intervals, newInterval):
        """
            :type intervals: List[Interval]
            :type newInterval: Interval
           :rtype: List[Interval]
        """
        res = []
        i = 0
        while i < len(intervals):
            iv = intervals[i]
            if iv.start > newInterval.end:
                break
            elif iv.end < newInterval.start:
                res.append(iv)
            else:
                newInterval.start = min(newInterval.start, iv.start)
                newInterval.end = max(newInterval.end, iv.end)
            i += 1

        if i <= len(intervals):
            res.append(newInterval)
            while i < len(intervals):
                res.append(intervals[i])
                i += 1

        return res


if __name__ == "__main__":
    intervals = Solution().insert([Interval(2, 6), Interval(8, 10), Interval(15, 18)], Interval(0, 1))
    #intervals = Solution().insert([Interval(1, 3), Interval(8, 10), Interval(15, 18)], Interval(7, 9))
    for interval in intervals:
        print(interval)
