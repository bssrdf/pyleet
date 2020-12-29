"""
-Medium-

*Topological Sort*

There are a total of n courses you have to take labelled from 0 to n - 1.

Some courses may have prerequisites, for example, if prerequisites[i] = 
[ai, bi] this means you must take the course bi before the course ai.

Given the total number of courses numCourses and a list of the prerequisite 
pairs, return the ordering of courses you should take to finish all courses.

If there are many valid answers, return any of them. If it is impossible to 
finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you 
should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you 
should have finished both courses 1 and 2. Both courses 1 and 2 should be 
taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is 
[0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.

"""
__author__ = 'Daniel'

import collections

class Solution:
    def findOrderDFS(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]

        Determine whether the graph is cyclic
        Marked twice -> cycle
        """
        courses = collections.defaultdict(list)
        visited = [0]*numCourses
        for a, b in prerequisites:
            courses[b].append(a)
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
        for x in range(numCourses):
            if not dfs(x):
                return []
        return seq[::-1]

        
    
    def findOrderSourceRemoval(self, numCourses, prerequisites):
        courses = collections.defaultdict(list)        
        indeg = [0] * numCourses
        for a, b in prerequisites:
            courses[b].append(a)
            indeg[a] += 1
        print(indeg)
        seq = []
        for i in range(numCourses):
            if indeg[i] == 0:
                seq.append(i)
        i = 0
        print('seq = ', len(seq), seq)
        while i<len(seq):
            for c in courses[seq[i]]:
                print(c, indeg[c])
                indeg[c] -= 1
                if indeg[c] == 0:
                    seq.append(c)
            print(i, 'seq = ', len(seq))
            i += 1              
        return seq

if __name__ == "__main__":
    #assert Solution().canFinish(2, [[1, 0], [0, 1]]) is False
#    print Solution().canFinish(4, [[1,0],[2,0],[3,1],[3,2]])
    #print(Solution().findOrderDFS(4, [[1,0],[2,0],[3,1],[3,2]]))
    #print(Solution().findOrderSourceRemoval(4, [[1,0],[2,0],[3,1],[3,2]]))
    #print(Solution().findOrderSourceRemoval(2, [[0,1]]))
    print(Solution().findOrderSourceRemoval(3, [[1,0],[1,2],[0,1]]))
    #print Solution().canFinishUsingQueue(2, [[1, 0], [0, 1]])
    
