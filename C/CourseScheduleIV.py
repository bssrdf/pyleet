'''

-Medium-

*Topological Sort*

There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course ai first if you want to take course bi.

For example, the pair [0, 1] indicates that you have to take course 0 before you can take course 1.
Prerequisites can also be indirect. If course a is a prerequisite of course b, and course b is a prerequisite of course c, then course a is a prerequisite of course c.

You are also given an array queries where queries[j] = [uj, vj]. For the jth query, you should answer whether course uj is a prerequisite of course vj or not.

Return a boolean array answer, where answer[j] is the answer to the jth query.

 

Example 1:


Input: numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]
Output: [false,true]
Explanation: The pair [1, 0] indicates that you have to take course 1 before you can take course 0.
Course 0 is not a prerequisite of course 1, but the opposite is true.
Example 2:

Input: numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]
Output: [false,false]
Explanation: There are no prerequisites, and each course is independent.
Example 3:


Input: numCourses = 3, prerequisites = [[1,2],[1,0],[2,0]], queries = [[1,0],[1,2]]
Output: [true,true]
 

Constraints:

2 <= numCourses <= 100
0 <= prerequisites.length <= (numCourses * (numCourses - 1) / 2)
prerequisites[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
All the pairs [ai, bi] are unique.
The prerequisites graph has no cycles.
1 <= queries.length <= 104
0 <= ui, vi <= n - 1
ui != vi



'''

from typing import List
from collections import defaultdict, deque
class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        n = numCourses
        graph = defaultdict(list)
        indeg = [0]*n
        for u,v in prerequisites:
            graph[u].append(v)        
            indeg[v] += 1
        deps = [set() for _ in range(n)]
        que = deque()
        for i in range(n):
            if indeg[i] == 0:
                que.append(i)
        while que:
            u = que.popleft()
            for v in graph[u]:
                deps[v].add(u)
                for w in deps[u]:
                   deps[v].add(w)
                indeg[v] -= 1
                if indeg[v] == 0:
                    que.append(v)
        ans = []
        for u,v in queries:
            if u in deps[v]:
                ans.append(True)
            else:
                ans.append(False)
        return ans

        


        
if __name__ == "__main__":
    print(Solution().checkIfPrerequisite(numCourses = 2, prerequisites = [[1,0]], queries = [[0,1],[1,0]]))
    print(Solution().checkIfPrerequisite(numCourses = 2, prerequisites = [], queries = [[1,0],[0,1]]))
    pre = [[6,3],[6,8],[6,5],[6,10],[6,0],[6,7],[6,4],[6,9],[6,1],[3,8],[3,10],[3,0],[3,7],[3,4],[3,2],[3,9],[3,1],[8,5],[8,10],[8,4],[8,2],[8,9],[5,10],[5,7],[5,4],[5,9],[5,1],[10,0],[10,7],[10,4],[10,2],[10,9],[0,7],[0,4],[0,2],[7,2],[7,9],[7,1],[4,2],[4,9],[4,1],[2,9],[2,1]]
    query = [[2,1],[8,9],[6,7],[3,8],[4,10],[9,6],[4,2],[5,10],[3,5],[5,9],[10,7],[7,6],[7,10],[0,5],[2,8],[6,2],[9,7],[9,4],[5,0],[9,5],[0,9],[6,10],[8,9],[5,8],[8,9],[4,5],[1,10],[6,5],[5,9],[0,9],[2,6],[4,5],[9,1],[8,1],[9,10],[4,6],[6,4],[5,9],[7,1],[10,1],[9,6],[1,3],[2,0],[9,10],[5,9],[7,5],[9,6],[1,4],[3,1],[10,4],[5,6],[1,4],[4,3],[9,5],[4,5],[5,8],[5,6],[9,10],[9,10],[7,8],[5,6],[4,6],[3,5],[7,10],[8,10],[7,8],[0,4],[7,0],[8,3],[8,10],[2,4],[6,10],[0,1],[10,6],[7,2],[4,3],[2,3],[3,1],[1,4],[5,7],[4,10],[7,2],[6,8],[0,8],[4,3],[8,7],[0,3],[10,9],[5,7],[6,8],[8,5],[3,5],[9,5],[7,9],[7,9],[3,4],[7,6],[3,9],[2,0],[10,6],[7,6],[10,6],[4,3],[9,10],[3,7],[7,10],[6,1]]
    print(Solution().checkIfPrerequisite(numCourses = 11, prerequisites = pre, queries= query))
