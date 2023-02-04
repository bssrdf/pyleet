'''
-Medium-
*Sorting*

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum 
number of intervals you need to remove to make the rest of the intervals non-overlapping.

 

Example 1:

Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
Example 2:

Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.
Example 3:

Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.
 

Constraints:

1 <= intervals.length <= 2 * 10^4
intervals[i].length == 2
-2 * 10^4 <= starti < endi <= 2 * 10^4


'''



class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        """
        sort by starting point: the minimum number of intervals to cover the whole range
        """
        intervals.sort()
        last = 0
        res = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[last][1]:
                res += 1
                if intervals[i][1] < intervals[last][1]:
                    last = i
            else: last = i
        return res
    
    def eraseOverlapIntervals2(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        """        
        sort by ending point: the maximum number of intervals that are non-overlapping
        为了保留更多的区间数目，在众多重合的区间里面，我们会优先选择右端点靠前的区间。
        因为它对后续的影响最小，有更大的概率让更多的区间出现。
        """
        intervals.sort(key=lambda x: x[1])
        i, cnt = 0, 0
        while i < len(intervals):
            cnt += 1
            j = i+1
            while j < len(intervals) and intervals[j][0] < intervals[i][1]:
                j += 1
            i = j
        return len(intervals) - cnt



    
if __name__ == "__main__":
    print(Solution().eraseOverlapIntervals([[1,2],[2,3],[3,4],[1,3]]))
    print(Solution().eraseOverlapIntervals2([[1,2],[2,3],[3,4],[1,3]]))