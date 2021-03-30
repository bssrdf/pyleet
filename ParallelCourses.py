'''
-Medium-

*Topological Sort*

There are N courses, labelled from 1 to N.

We are given relations[i] = [X, Y], representing a prerequisite relationship between 
course X and course Y: course X has to be studied before course Y.

In one semester you can study any number of courses as long as you have studied all the 
prerequisites for the course you are studying.

Return the minimum number of semesters needed to study all courses. If there is no way 
to study all the courses, return -1.

Example 1:

Input: N = 3, relations = [[1,3],[2,3]]
Output: 2
Explanation: 
In the first semester, courses 1 and 2 are studied. In the second semester, course 3 is studied.
Example 2:

Input: N = 3, relations = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: 
No course can be studied because they depend on each other.
Note:

1 <= N <= 5000
1 <= relations.length <= 5000
relations[i][0] != relations[i][1]
There are no repeated relations in the input.

'''
from collections import deque, defaultdict

class Solution(object):

    def minNumberOfSemesters(self, n, dependencies):
        indeg = [0] * (n+1)
        m = defaultdict(list)
        q = deque()
        for x,y in dependencies:
            indeg[y] += 1
            m[x].append(y)
        for i in range(1, n+1):
            if indeg[i] == 0:
                q.append(i)
        ans = 0
        while q:
            nxt = deque()
            while q:
                course = q.popleft()
                n -= 1
                for i in m[course]:
                    indeg[i] -= 1
                    if indeg[i] == 0:
                        nxt.append(i)
            q = nxt
            ans += 1
        return ans if n == 0 else -1

if __name__ == "__main__":
    print(Solution().minNumberOfSemesters(3, [[1,3],[2,3]]))
    print(Solution().minNumberOfSemesters(3, [[1,2],[2,3],[3,1]]))


