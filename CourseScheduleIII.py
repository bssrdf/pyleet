'''
-Hard-

*Greedy*

There are n different online courses numbered from 1 to n. Each course has some 
duration(course length) t and closed on dth day. A course should be taken 
continuously for t days and must be finished before or on the dth day. You will 
start at the 1st day.

Given n online courses represented by pairs (t,d), your task is to find the 
maximal number of courses that can be taken.

Example:

Input: [[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]
Output: 3
Explanation: 
There're totally 4 courses, but you can take 3 courses at most:
First, take the 1st course, it costs 100 days so you will finish it on the 100th day, and ready to take the next course on the 101st day.
Second, take the 3rd course, it costs 1000 days so you will finish it on the 1100th day, and ready to take the next course on the 1101st day. 
Third, take the 2nd course, it costs 200 days so you will finish it on the 1300th day. 
The 4th course cannot be taken now, since you will finish it on the 3300th day, which exceeds the closed date.
 

Note:

The integer 1 <= d, t, n <= 10,000.
You can't take two courses simultaneously.

'''

import heapq
class Solution(object):
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        courses.sort(key = lambda x: x[1])
        f = 0 # currentTotalTime
        q = []
        for t, d in courses:
            # During iteration, say I want to add the current course, 
            # currentTotalTime being total time of all courses taken till now, 
            # but adding the current course might exceed my deadline or it doesn’t.
            if f+t <= d:
                # If it doesn’t, then I have added one new course. 
                heapq.heappush(q, -t)
                # Increment the currentTotalTime with duration of current course.
                f += t
            elif q:
                # if it exceeds deadline, I can swap current course with current 
                # courses that has biggest duration.
                # * What preprocessing do I need to do on my course processing 
                # order so that this swap is always legal?
                tmax = -q[0]
                if tmax > t: # greedily evict the largest t from the pq
                    heapq.heappop(q) 
                    heapq.heappush(q, -t)    
                    # * No harm done and I might have just reduced the 
                    # currentTotalTime, right?
                    f = f + t - tmax
        return len(q)

if __name__ == "__main__":
    print(Solution().scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]))
    print(Solution().scheduleCourse([[2,5],[2,19],[1,8],[1,3]]))