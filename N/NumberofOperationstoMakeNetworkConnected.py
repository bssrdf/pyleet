'''
-Medium-


There are n computers numbered from 0 to n-1 connected by ethernet cables 
connections forming a network where connections[i] = [a, b] represents a 
connection between computers a and b. Any computer can reach any other 
computer directly or indirectly through the network.

Given an initial computer network connections. You can extract certain cables 
between two directly connected computers, and place them between any pair 
of disconnected computers to make them directly connected. Return the 
minimum number of times you need to do this in order to make all the computers 
connected. If it's not possible, return -1. 

 

Example 1:



Input: n = 4, connections = [[0,1],[0,2],[1,2]]
Output: 1
Explanation: Remove cable between computer 1 and 2 and place between 
computers 1 and 3.
Example 2:



Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2],[1,3]]
Output: 2
Example 3:

Input: n = 6, connections = [[0,1],[0,2],[0,3],[1,2]]
Output: -1
Explanation: There are not enough cables.
Example 4:

Input: n = 5, connections = [[0,1],[0,2],[3,4],[2,3]]
Output: 0
 

Constraints:

1 <= n <= 10^5
1 <= connections.length <= min(n*(n-1)/2, 10^5)
connections[i].length == 2
0 <= connections[i][0], connections[i][1] < n
connections[i][0] != connections[i][1]
There are no repeated connections.
No two computers are connected by more than one cable.


'''

from collections import defaultdict

class Solution(object):
    def makeConnected(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(connections) < n-1: return -1
        g = defaultdict(set)
        for u,v in connections:
            g[u].add(v)
            g[v].add(u)
        visited = [False]*n
        def dfs(node):
            visited[node] = True
            for nxt in g[node]:
                if not visited[nxt]:
                    visited[nxt] = True
                    dfs(nxt)
        islands = 0
        for i in range(n):
            if not visited[i]:
                dfs(i)
                islands += 1
        return islands-1 
        
    def makeConnectedUF(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: int
        """
        if len(connections) < n-1: return -1
        roots = [i for i in range(n)]                
        islands = n
        for u,v in connections:
            x = self.find(roots, u)
            y = self.find(roots, v)
            if x != y:
                islands -= 1
                roots[x] = y
        return islands-1 

    def find(self, roots, i):
        # this while loop is called "qiuck union";
        # it "recursively" decends to the root node represented by the
        # node whose roots value is untouched 'i'
        while roots[i] != i:
            # path compression; set every other node in path point to its grandparent
            roots[i] = roots[roots[i]] 
            i = roots[i]
        return i


if __name__ == "__main__":
    print(Solution().makeConnected(4, [[0,1],[0,2],[1,2]]))
    print(Solution().makeConnected(6, [[0,1],[0,2],[0,3],[1,2],[1,3]]))
    print(Solution().makeConnected(6, [[0,1],[0,2],[0,3],[1,2]]))
    print(Solution().makeConnected(5, [[0,1],[0,2],[3,4],[2,3]]))

    print(Solution().makeConnectedUF(4, [[0,1],[0,2],[1,2]]))
    print(Solution().makeConnectedUF(6, [[0,1],[0,2],[0,3],[1,2],[1,3]]))
    print(Solution().makeConnectedUF(6, [[0,1],[0,2],[0,3],[1,2]]))
    print(Solution().makeConnectedUF(5, [[0,1],[0,2],[3,4],[2,3]]))