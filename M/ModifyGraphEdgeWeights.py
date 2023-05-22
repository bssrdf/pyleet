'''

-Hard-

*Dijkstra's Algorithm*


You are given an undirected weighted connected graph containing n nodes labeled from 0 to n - 1, and an integer array edges where edges[i] = [ai, bi, wi] indicates that there is an edge between nodes ai and bi with weight wi.

Some edges have a weight of -1 (wi = -1), while others have a positive weight (wi > 0).

Your task is to modify all edges with a weight of -1 by assigning them positive integer values in the range [1, 2 * 109] so that the shortest distance between the nodes source and destination becomes equal to an integer target. If there are multiple modifications that make the shortest distance between source and destination equal to target, any of them will be considered correct.

Return an array containing all edges (even unmodified ones) in any order if it is possible to make the shortest distance from source to destination equal to target, or an empty array if it's impossible.

Note: You are not allowed to modify the weights of edges with initial positive weights.

 

Example 1:



Input: n = 5, edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], source = 0, destination = 1, target = 5
Output: [[4,1,1],[2,0,1],[0,3,3],[4,3,1]]
Explanation: The graph above shows a possible modification to the edges, making the distance from 0 to 1 equal to 5.
Example 2:



Input: n = 3, edges = [[0,1,-1],[0,2,5]], source = 0, destination = 2, target = 6
Output: []
Explanation: The graph above contains the initial edges. It is not possible to make the distance from 0 to 2 equal to 6 by modifying the edge with weight -1. So, an empty array is returned.
Example 3:



Input: n = 4, edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], source = 0, destination = 2, target = 6
Output: [[1,0,4],[1,2,3],[2,3,5],[0,3,1]]
Explanation: The graph above shows a modified graph having the shortest distance from 0 to 2 as 6.
 

Constraints:

1 <= n <= 100
1 <= edges.length <= n * (n - 1) / 2
edges[i].length == 3
0 <= ai, bi < n
wi = -1 or 1 <= wi <= 107
ai != bi
0 <= source, destination < n
source != destination
1 <= target <= 109
The graph is connected, and there are no self-loops or repeated edges


'''

from typing import List
from collections import defaultdict
from math import inf
from heapq import heappop, heappush
class Solution:
    def modifiedGraphEdges(self, n: int, edges: List[List[int]], source: int, destination: int, target: int) -> List[List[int]]:
        G = [[] for _  in range(n)]
        for u, v, w in edges:
            G[u].append([v, w])
            G[v].append([u, w])

        def dijkstra(source, adj, skip_negative):
            pq = [[0, source]]
            dist = [inf]*n
            dist[source] = 0
            parent = {}
            while pq:
                d, node = heappop(pq)
                if d > dist[node]:
                    continue
                for nei, w in adj[node]:
                    if w == -1:
                        if skip_negative:
                            continue
                        w = 1
                    d2 = d + w
                    if d2 < dist[nei]:
                        dist[nei] = d2
                        parent[nei] = node
                        heappush(pq, [d2, nei])

            return dist, parent
        
        distR, parentR = dijkstra(destination, G, skip_negative=True)
        # if distR.get(source, inf) < target:
        if distR[source] < target: # here is the shortest distance from destination to source without
                                   # using any -1 edge; can not make target as shortest dist if an even
                                   # shorter one exists.
            return []
        dist, parent = dijkstra(source, G, skip_negative=False)
        if dist[destination] > target: # even setting all modfieable edge weight to 1 can still make
                                       # the shortest distance > target; impossible    
            return []
        
        path = [destination]
        while path[-1] != source:
            path.append(parent[path[-1]])
        path = path[::-1]
        
        edges = {(min(u,v), max(u,v)) : w for u, v, w in edges}
        
        walked = 0
        for i in range(len(path) - 1):
            u, v = path[i], path[i+1]
            e = (min(u, v), max(u, v))
            if edges[e] == -1:
                # edges[e] = max(target - distR.get(v, inf) - walked, 1)
                edges[e] = max(target - distR[v] - walked, 1)
            walked += edges[e]
        
        for e, w in edges.items():
            if w == -1:
                edges[e] = 2 * (10 ** 9)
        
        return [[u,v,w] for (u,v), w in edges.items()]
        







if __name__ == "__main__":
    print(Solution().modifiedGraphEdges(n = 5, edges = [[4,1,-1],[2,0,-1],[0,3,-1],[4,3,-1]], source = 0, destination = 1, target = 5))
    print(Solution().modifiedGraphEdges(n = 4, edges = [[1,0,4],[1,2,3],[2,3,5],[0,3,-1]], source = 0, destination = 2, target = 6))
    print(Solution().modifiedGraphEdges(n = 3, edges = [[0,1,-1],[0,2,5]], source = 0, destination = 2, target = 6))
