'''

Hard
*BFS*
*Dynamic Programming*

An undirected, connected graph of N nodes (labeled 0, 1, 2, ..., N-1) is given as graph.

graph.length = N, and j != i is in the list graph[i] exactly once, if and only if nodes i 
and j are connected.

Return the length of the shortest path that visits every node. You may start and stop at 
any node, you may revisit nodes multiple times, and you may reuse edges.

 

Example 1:

Input: [[1,2,3],[0],[0],[0]]
Output: 4
Explanation: One possible path is [1,0,2,0,3]
Example 2:

Input: [[1],[0,2,4],[1,3,4],[2],[1,2]]
Output: 4
Explanation: One possible path is [0,1,4,2,3]
 

Note:

1 <= graph.length <= 12
0 <= graph[i].length < graph.length

'''

from collections import deque

class Solution(object):
    def shortestPathLength(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: int
        """
        n, target, res = len(graph), 0, 0
        visited = set()
        q = deque()
        for i in range(n):
            mask = 1 << i
            target |= mask 
            visited.add(str(mask)+'-'+str(i))
            q.append((mask, i)) 
        while q:
            for i in range(len(q)):
                m,v = q.popleft()
                if m == target: return res
                for nb in graph[v]:
                    mask = m | 1 << nb
                    path = str(mask) + '-'+str(nb)
                    if path in visited: continue
                    visited.add(path)
                    q.append((mask, nb))
            res += 1    
        return -1

if __name__ == "__main__":
    print(Solution().shortestPathLength([[1,2,3],[0],[0],[0]]))
    print(Solution().shortestPathLength([[1],[0,2,4],[1,3,4],[2],[1,2]]))