"""
There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as
a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

For example:

2, [[1,0]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take. To take course 1 you should have finished course 0, and to take course 0 you
should also have finished course 1. So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph
is represented.
"""
__author__ = 'Daniel'

import collections

class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        Determine whether the graph is cyclic
        Marked twice -> cycle

        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        courses = collections.defaultdict(list)
        visited = [0 for _ in xrange(numCourses)]
        for a, b in sorted(prerequisites):
            courses[a].append(b)
        print courses
        def dfs(c):
            if visited[c] == -1:
                return False
            if visited[c] == 1:
                return True
            if visited[c] == 0:
                visited[c] = -1
                for l in courses[c]:
                    if not dfs(l):
                        return False
            visited[c] = 1
            return True
        for x in xrange(numCourses):
            if not dfs(x):
                return False
        return True




if __name__ == "__main__":
    assert Solution().canFinish(2, [[1, 0], [0, 1]]) is False
    #Solution().canFinish(2, [[1, 0], [0, 1]])
