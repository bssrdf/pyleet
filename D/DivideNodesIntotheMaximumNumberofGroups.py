'''
-Hard-

*DFS*
*BFS*
*Connected Components*
*Bipartite Graph*

You are given a positive integer n representing the number of nodes in an undirected graph. The nodes are labeled from 1 to n.

You are also given a 2D integer array edges, where edges[i] = [ai, bi] indicates that there is a bidirectional edge between nodes ai and bi. Notice that the given graph may be disconnected.

Divide the nodes of the graph into m groups (1-indexed) such that:

Each node in the graph belongs to exactly one group.
For every pair of nodes in the graph that are connected by an edge [ai, bi], if ai belongs to the group with index x, and bi belongs to the group with index y, then |y - x| = 1.
Return the maximum number of groups (i.e., maximum m) into which you can divide the nodes. Return -1 if it is impossible to group the nodes with the given conditions.

 

Example 1:


Input: n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]
Output: 4
Explanation: As shown in the image we:
- Add node 5 to the first group.
- Add node 1 to the second group.
- Add nodes 2 and 4 to the third group.
- Add nodes 3 and 6 to the fourth group.
We can see that every edge is satisfied.
It can be shown that that if we create a fifth group and move any node from the third or fourth group to it, at least on of the edges will not be satisfied.
Example 2:

Input: n = 3, edges = [[1,2],[2,3],[3,1]]
Output: -1
Explanation: If we add node 1 to the first group, node 2 to the second group, and node 3 to the third group to satisfy the first two edges, we can see that the third edge will not be satisfied.
It can be shown that no grouping is possible.
 

Constraints:

1 <= n <= 500
1 <= edges.length <= 104
edges[i].length == 2
1 <= ai, bi <= n
ai != bi
There is at most one edge between any pair of vertices.



'''

from typing import List
from collections import defaultdict, deque
class Solution:
    def magnificentSets2(self, n: int, edges: List[List[int]]) -> int:
        '''
        The number of group we can create for a connected graph is the maximum 
        of minimum distances between all nodes in that graph. Here distance 
        equals to number of nodes in the path.
        '''
        G = defaultdict(set)
        dist = [[10**4+1]*(n+1) for _ in range(n+1)]
        for u,v in edges:
            G[u].add(v)
            G[v].add(u)
        color = [0]*(n+1)
        def dfs(cur, col, nodes):
            if color[cur] != 0: 
                return color[cur] == col
            color[cur] = col
            nodes.append(cur) # save nodes in connected components
            for i in G[cur]:
                if not dfs(i, -1*col, nodes):
                    return False
            return True
        def bfs(src):
            # compute minimum distance of src to all other nodes
            # in the connected components
            dist[src][src] = 1
            que = deque([src])
            while que:
                u = que.popleft()
                for v in G[u]:
                    if dist[src][v] > dist[src][u]+1:
                        dist[src][v] = dist[src][u]+1
                        que.append(v)
        for i in range(1, n+1):
            bfs(i)
        ans = 0
        for i in range(1, n+1):
            if color[i] == 0:
                kara = []
                mxdist = 0
                if not dfs(i, 1, kara):
                    return -1
                #kara has nodes of one connected components which is 
                # also bipartite
                for u in kara:
                    for v in kara:
                        mxdist = max(mxdist, dist[u][v])
                ans += mxdist
        
        return ans
    
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        components = []
        seen = set()
        for i in range(1, n + 1):
            if i in seen:
                continue
            queue = deque([i])
            visited = set([i])
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if neighbor in visited:
                            continue
                        visited.add(neighbor)
                        queue.append(neighbor)
            components.append(visited)
            seen = seen.union(visited)
        longest = [-1] * len(components)        
        for k in range(len(components)):
            for i in components[k]:
                longest[k] = max(longest[k], self.bfs(graph, i))
        if min(longest) < 0:
            return -1
        return sum(longest)
            
    def bfs(self, graph, i):
        queue = deque([i])
        seen = set([i])
        seenLevel = set()
        ans = 0
        while queue:
            ans += 1
            nextLevel = set()
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor in seenLevel:
                        return -1
                    if neighbor in seen:
                        continue
                    seen.add(neighbor)
                    nextLevel.add(neighbor)
                    queue.append(neighbor)
            seenLevel = nextLevel
        return ans

if __name__ == "__main__":
    print(Solution().magnificentSets(n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))
    print(Solution().magnificentSets(n = 6, edges = [[1,2],[1,4],[2,5],[5,4],[2,6],[2,3],[3,4],[4,6]]))
    print(Solution().magnificentSets(n = 3, edges = [[1,2],[2,3],[3,1]]))


    print(Solution().magnificentSets2(n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))
    print(Solution().magnificentSets2(n = 6, edges = [[1,2],[1,4],[2,5],[5,4],[2,6],[2,3],[3,4],[4,6]]))
    print(Solution().magnificentSets2(n = 3, edges = [[1,2],[2,3],[3,1]]))
        