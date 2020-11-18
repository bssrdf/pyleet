'''
-Medium-
*Interval*

Given a sorted list of disjoint intervals, each interval intervals[i] = [a, b] 
represents the set of real numbers x such that a <= x < b.

We remove the intersections between any interval in intervals and the interval 
toBeRemoved.

Return a sorted list of intervals after all such removals.

 

Example 1:

Input: intervals = [[0,2],[3,4],[5,7]], toBeRemoved = [1,6]
Output: [[0,1],[6,7]]
Example 2:

Input: intervals = [[0,5]], toBeRemoved = [2,3]
Output: [[0,2],[3,5]]
 

Constraints:

1 <= intervals.length <= 10^4
-10^9 <= intervals[i][0] < intervals[i][1] <= 10^9

'''

class Solution(object):
    def removeIntervals(self, intervals, toBeRemoved):
        """        
        :type intervals: List[List[int]]
        :type toBeRemoved: List[int]
        :rtype: List[List[int]]
        """
        res = []
        for b,e in intervals:
            if e <= toBeRemoved[0] or b >= toBeRemoved[1]:
                res.append([b,e]) 
            else:
                if b < toBeRemoved[0]:
                    res.append([b, toBeRemoved[0]]) 
                if e > toBeRemoved[1]:
                    res.append([toBeRemoved[1], e]) 
        return res


if __name__ == "__main__":
    print(Solution().removeIntervals([[0,2],[3,4],[5,7]], [1,6]))
    print(Solution().removeIntervals([[0,5]], [2,3]))