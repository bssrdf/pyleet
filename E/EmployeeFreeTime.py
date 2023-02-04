'''
-Hard-

We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for 
all employees, also in sorted order.

The Intervals is an 1d-array. Each two numbers shows an interval. For example, [1,2,8,10] 
represents that the employee works in [1,2] and [8,10].

Also, we wouldn't include intervals like [5, 5] in our answer, as they have zero length.

1.schedule and schedule[i] are lists with lengths in range [1, 100].
2.0 <= schedule[i].start < schedule[i].end <= 10^8.


样例
Example 1:

Input：schedule = [[1,2,5,6],[1,3],[4,10]]
Output：[(3,4)]
Explanation:
There are a total of three employees, and all common
free time intervals would be [-inf, 1], [3, 4], [10, inf].
We discard any intervals that contain inf as they aren't finite.
Example 2:

Input：schedule = [[1,3,6,7],[2,4],[2,5,9,12]]
Output：[(5,6),(7,9)]
Explanation：
There are a total of three employees, and all common
free time intervals would be [-inf, 1], [5, 6], [7, 9],[12,inf].
We discard any intervals that contain inf as they aren't finite.

'''

"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

from collections import defaultdict, namedtuple
import heapq
import sys

class Job:
    def __init__(self, id):
        self.id = id        


Event = namedtuple('Event', 'starts ends')

class Solution:
    """
    @param schedule: a list schedule of employees
    @return: Return a list of finite intervals 
    """
    def employeeFreeTime(self, schedule):
        # Write your code here
        events = defaultdict(lambda: Event(starts=[], ends=[]))
        counter = 0 
        for iv in schedule:
            for i in range(0,len(iv)-1,2):            
                left, right = iv[i], iv[i+1]
                job = Job(counter)
                counter += 1
                events[left].starts.append(job)  # possible multiple building at the same x-coordinate.
                events[right].ends.append(job)
        res = []
        ret = set()
        start = -float('inf')
        # Process events in order by x-coordinate.
        for x, event in sorted(events.items(), key=lambda x: x[0]):  # sort the dictionary by key
            #print('key = ', x, start, len(ret), ret) 
            if len(ret) == 0: 
                res.append((start, x))
                start = x

            for job in event.starts:
               # print 'starts ', x, building
                ret.add(job.id)
                
            for job in event.ends:
               # print 'ends ',  x, building
               # mark the building to be deleted
                ret.remove(job.id)

            if len(ret) == 0:                 
                start = x


            
        return res[1:]
    

    def employeeFreeTimeCleanCode(self, schedule):
        # Write your code here
        meetings = []
        for iv in schedule:
            for i in range(0,len(iv)-1,2):            
                meetings.append([iv[i], iv[i+1]])
        res = []
        meets = sorted(meetings, key=lambda x: x[0])
        e = -sys.maxsize-1
        for m in meets:
            if m[0] > e:
                res.append((e, m[0]))
            e = max(m[1], e)
        return res[1:]

if __name__ == "__main__":
    print(Solution().employeeFreeTime([[1,3,6,7],[2,4],[2,5,9,12]]))
    print(Solution().employeeFreeTime([[1,2,5,6],[1,3],[4,10]]))
    print(Solution().employeeFreeTimeCleanCode([[1,3,6,7],[2,4],[2,5,9,12]]))
    print(Solution().employeeFreeTimeCleanCode([[1,2,5,6],[1,3],[4,10]]))
