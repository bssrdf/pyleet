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
        indeg = [0 for _ in xrange(numCourses)]
        for a, b in prerequisites:
            courses[b].append(a)
            indeg[b] += 1
#        print courses
        seq = []
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
            seq.append(c)
            return True
        for x in xrange(numCourses):
            if not dfs(x):
                return []
        return seq[::-1]
        
    def canFinishUsingQueue(self, numCourses, prerequisites):      
        courses = collections.defaultdict(list)
        visited = [0 for _ in xrange(numCourses)]
        indeg = [0 for _ in xrange(numCourses)]
        for a, b in prerequisites:
            courses[b].append(a)
            indeg[a] += 1
        print indeg
        seq = []
        for i in xrange(numCourses):
            if indeg[i] == 0:
                seq.append(i)
        i = 0
        print 'seq = ', len(seq)
        while i<len(seq):
            for c in courses[i]:
                indeg[c] -= 1
                if indeg[c] == 0:
                    seq.append(c)
            print i, 'seq = ', len(seq)
            i += 1              
        return seq

if __name__ == "__main__":
    #assert Solution().canFinish(2, [[1, 0], [0, 1]]) is False
#    print Solution().canFinish(4, [[1,0],[2,0],[3,1],[3,2]])
    print Solution().canFinishUsingQueue(4, [[1,0],[2,0],[3,1],[3,2]])
    #print Solution().canFinishUsingQueue(2, [[1, 0], [0, 1]])
