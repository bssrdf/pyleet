'''
-Hard-
*Dijkstra's Algorithm*

You are given an integer n denoting the number of nodes of a weighted directed graph. 
The nodes are numbered from 0 to n - 1.

You are also given a 2D integer array edges where edges[i] = [fromi, toi, weighti] denotes 
that there exists a directed edge from fromi to toi with weight weighti.

Lastly, you are given three distinct integers src1, src2, and dest denoting three distinct 
nodes of the graph.

Return the minimum weight of a subgraph of the graph such that it is possible to reach 
dest from both src1 and src2 via a set of edges of this subgraph. In case such a subgraph 
does not exist, return -1.

A subgraph is a graph whose vertices and edges are subsets of the original graph. The 
weight of a subgraph is the sum of weights of its constituent edges.

 

Example 1:


Input: n = 6, edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]], src1 = 0, src2 = 1, dest = 5
Output: 9
Explanation:
The above figure represents the input graph.
The blue edges represent one of the subgraphs that yield the optimal answer.
Note that the subgraph [[1,0,3],[0,5,6]] also yields the optimal answer. It is not possible to get a subgraph with less weight satisfying all the constraints.
Example 2:


Input: n = 3, edges = [[0,1,1],[2,1,1]], src1 = 0, src2 = 1, dest = 2
Output: -1
Explanation:
The above figure represents the input graph.
It can be seen that there does not exist any path from node 1 to node 2, hence there are no subgraphs satisfying all the constraints.
 

Constraints:

3 <= n <= 105
0 <= edges.length <= 105
edges[i].length == 3
0 <= fromi, toi, src1, src2, dest <= n - 1
fromi != toi
src1, src2, and dest are pairwise distinct.
1 <= weight[i] <= 105


'''
from typing import List
import heapq


from collections import defaultdict

class Solution:
    def minimumWeight(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        MAXD = float('inf')
        ans = MAXD
        g1, g2 = defaultdict(list), defaultdict(list)
        for u, v, w in edges:
            g1[u].append((v,w))  
            g2[v].append((u,w))              
        dist1, dist2, dist3 = [MAXD]*n, [MAXD]*n, [MAXD]*n
        def findDist(g, src, dist):                        
            dist[src] = 0
            pq = [(0, src)]
            while pq:
                d, u = heapq.heappop(pq)
                for v, w in g[u]:
                    if dist[v] > d + w:
                        dist[v] = d + w
                        heapq.heappush(pq, (dist[v], v))  
        findDist(g1, src1, dist1)
        findDist(g1, src2, dist2)
        findDist(g2, dest, dist3)
        for i in range(n):
            ans = min(ans, dist1[i]+dist2[i]+dist3[i])
        return -1 if ans == MAXD else ans
    
    def minimumWeight2(self, n: int, edges: List[List[int]], src1: int, src2: int, dest: int) -> int:
        G1 = defaultdict(list)
        G2 = defaultdict(list)
        for a, b, w in edges:
            G1[a].append((b, w))
            G2[b].append((a, w))

        def Dijkstra(graph, K):
            q, t = [(0, K)], {}
            while q:
                time, node = heapq.heappop(q)
                if node not in t:
                    t[node] = time
                    for v, w in graph[node]:
                        heapq.heappush(q, (time + w, v))
            return [t.get(i, float("inf")) for i in range(n)]
        
        arr1 = Dijkstra(G1, src1)
        arr2 = Dijkstra(G1, src2)
        arr3 = Dijkstra(G2, dest)
        
        ans = float("inf")
        for i in range(n):
            ans = min(ans, arr1[i] + arr2[i] + arr3[i])
        
        return ans if ans != float("inf") else -1
        



if __name__ == "__main__":
    print(Solution().minimumWeight(n = 6, edges = [[0,2,2],[0,5,6],[1,0,3],[1,4,5],[2,1,1],[2,3,3],[2,3,4],[3,4,2],[4,5,1]], src1 = 0, src2 = 1, dest = 5))
    print(Solution().minimumWeight(n = 3, edges = [[0,1,1],[2,1,1]], src1 = 0, src2 = 1, dest = 2))
    edges = [[29,3,67],[72,52,31],[72,55,72],[29,63,14],[72,71,34],[29,26,68],[29,33,34],[29,4,7],[72,42,78],[29,65,65],[29,78,42],[29,30,11],[72,7,59],[29,80,4],[72,11,77],[72,45,89],[72,61,10],[72,31,9],[72,8,54],[72,23,58],[72,37,53],[72,9,53],[72,41,39],[29,35,11],[72,49,82],[72,12,54],[29,25,4],[29,17,97],[29,40,45],[29,75,32],[72,15,97],[72,76,35],[29,74,76],[72,36,14],[29,6,19],[72,50,8],[29,34,26],[72,13,49],[72,46,56],[72,5,24],[29,43,62],[72,48,69],[72,66,48],[72,39,7],[72,54,30],[72,19,84],[72,57,90],[72,22,29],[72,53,2],[29,68,80],[72,44,16],[29,73,80],[72,27,2],[29,79,64],[72,60,82],[72,14,10],[29,77,89],[29,69,93],[72,47,33],[29,18,71],[29,58,87],[72,28,15],[72,70,41],[72,24,59],[72,21,95],[29,59,8],[29,62,63],[72,81,10],[72,10,45],[29,1,54],[29,67,4],[72,32,29],[72,56,1],[29,16,99],[29,20,70],[29,38,80],[29,2,93],[29,0,25],[72,64,80],[29,51,84],[17,51,44],[81,51,2],[41,51,39],[71,51,41]]
    print(Solution().minimumWeight(82, edges, 29, 72, 51))    
    