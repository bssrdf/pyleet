'''
-Medium-

*Union Find*

Given n nodes labeled from 0 to n - 1 and a list of undirected edges 
(each edge is a pair of nodes), write a function to find the number of connected 
components in an undirected graph.

Sample I/O
Example 1
Input: n = 5 and edges = [[0, 1], [1, 2], [3, 4]]

     0          3
     |          |
     1 --- 2    4 

Output: 2
Example 2
Input: n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]]

     0           4
     |           |
     1 --- 2 --- 3

Output:  1
Note
You can assume that no duplicate edges will appear in edges. 
Since all edges are undirected, [0, 1] is the same as [1, 0] and 
thus will not appear together in edges.


'''

import collections

class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        pass

    def countComponentsBFS(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        dist = collections.defaultdict(list)
        for source, target in edges:
            dist[source].append(target)
            dist[target].append(source)
        count = 0
        visited=set()
        queue = collections.deque()
        for x in range(n):
            if x in visited:
                continue
            queue.append(x)
            while queue:
                source=queue.popleft()
                if source in visited:
                    continue
                visited.add(source)
                for target in dist[source]:
                    queue.append(target)
            count+=1
        return count

if __name__ == '__main__':
    print(Solution().countComponentsBFS(5, [[0, 1], [1, 2], [2, 3], [3, 4]]))