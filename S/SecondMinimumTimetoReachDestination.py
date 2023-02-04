'''
-Hard-

A city is represented as a bi-directional connected graph with n vertices where each 
vertex is labeled from 1 to n (inclusive). The edges in the graph are represented as 
a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional 
edge between vertex ui and vertex vi. Every vertex pair is connected by at most 
one edge, and no vertex has an edge to itself. The time taken to traverse any edge 
is time minutes.

Each vertex has a traffic signal which changes its color from green to red and 
vice versa every change minutes. All signals change at the same time. You can 
enter a vertex at any time, but can leave a vertex only when the signal is green. 
You cannot wait at a vertex if the signal is green.

The second minimum value is defined as the smallest value strictly larger than 
the minimum value.

For example the second minimum value of [2, 3, 4] is 3, and the second minimum 
value of [2, 2, 4] is 4.

Given n, edges, time, and change, return the second minimum time it will take to 
go from vertex 1 to vertex n.

Notes:

You can go through any vertex any number of times, including 1 and n.
You can assume that when the journey starts, all signals have just turned green.
 

Example 1:

        
Input: n = 5, edges = [[1,2],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5
Output: 13
Explanation:
The figure on the left shows the given graph.
The blue path in the figure on the right is the minimum time path.
The time taken is:
- Start at 1, time elapsed=0
- 1 -> 4: 3 minutes, time elapsed=3
- 4 -> 5: 3 minutes, time elapsed=6
Hence the minimum time needed is 6 minutes.

The red path shows the path to get the second minimum time.
- Start at 1, time elapsed=0
- 1 -> 3: 3 minutes, time elapsed=3
- 3 -> 4: 3 minutes, time elapsed=6
- Wait at 4 for 4 minutes, time elapsed=10
- 4 -> 5: 3 minutes, time elapsed=13
Hence the second minimum time is 13 minutes.      
Example 2:


Input: n = 2, edges = [[1,2]], time = 3, change = 2
Output: 11
Explanation:
The minimum time path is 1 -> 2 with time = 3 minutes.
The second minimum time path is 1 -> 2 -> 1 -> 2 with time = 11 minutes.
 

Constraints:

2 <= n <= 10^4
n - 1 <= edges.length <= min(2 * 10^4, n * (n - 1) / 2)
edges[i].length == 2
1 <= ui, vi <= n
ui != vi
There are no duplicate edges.
Each vertex can be reached directly or indirectly from every other vertex.
1 <= time, change <= 10^3


'''

from typing import List

from collections import deque, defaultdict

class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        que, graph = deque(), defaultdict(list)
        visited = [[False]*2 for _ in range(n+1)]
        curTime, firstArrive = 0, -1
        visTime = [-1]*(n+1)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u) 
        que.append((1, curTime))
        visited[1][0] = True
        while que:
            u, cur = que.popleft()
            if u == n:
                if firstArrive == -1:
                    firstArrive = cur
                #elif cur > firstArrive: 
                else: return cur
            for v in graph[u]:                
                redLight = (cur // change) % 2 
                arrivalTime = cur + time
                if redLight: arrivalTime += change - (cur % change) 
                if visTime[v] != arrivalTime and not visited[v][0]:
                    visTime[v] = arrivalTime
                    visited[v][0] = True
                    que.append((v, arrivalTime))
                elif visTime[v] != arrivalTime and not visited[v][1]:
                    visTime[v] = arrivalTime
                    visited[v][1] = True
                    que.append((v, arrivalTime))
        return -1 

    def secondMinimum2(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        que, graph = deque(), defaultdict(list)
        visited = [[False]*2 for _ in range(n+1)]
        curTime, firstArrive = 0, -1
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u) 
        que.append((1, curTime))
        visited[1][0] = True
        while que:
            u, cur = que.popleft()
            if u == n:
                if firstArrive == -1:
                    firstArrive = cur
                elif cur > firstArrive: 
                    return cur
                #else: return cur
            for v in graph[u]:                
                redLight = (cur // change) % 2 
                arrivalTime = cur + time
                if redLight: arrivalTime += change - (cur % change) 
                if not visited[v][0]:
                    visited[v][0] = True
                    que.append((v, arrivalTime))
                elif not visited[v][1]:
                    visited[v][1] = True
                    que.append((v, arrivalTime))
        return -1 

    

    def secondMinimum3(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        que, graph = deque(), defaultdict(list)
        INT_MAX = float('inf')
        firstArrivedTime = INT_MAX
        visTime = [INT_MAX]*(n+1)
        visCount = [0]*(n+1)        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u) 
        que.append((1, 0))
        while que:
            u, cur = que.popleft()
            if v == n and firstArrivedTime == INT_MAX:
                firstArrivedTime = cur
            if v == n and cur > firstArrivedTime:
                return cur
            for v in graph[u]:                
                redLight = (cur // change) % 2 
                arrivalTime = cur + time
                if redLight: arrivalTime += change - (cur % change) 
                # visTime[next] != arrivalTime to avoid the same arrival time, think about this graph, 
                # 0->1->3 0->2->3, so 0 can reach 1 and 2 and then reach 3, there are 2 times 
                # that can reach to point 3 and we will use the 2nd time(it is the same as the 
                # 1st reach time) as our answer but we know that it is not right, so we need 
                # this condition.
                if visTime[v] != arrivalTime and visCount[v] <= 1:
                    visTime[v] = arrivalTime
                    visCount[v] += 1                
                    que.append((v, arrivalTime))
        return -1 
    
    





if __name__ == "__main__":
    print(Solution().secondMinimum(n = 5, edges = [[1,2],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5))
    print(Solution().secondMinimum(n = 2, edges = [[1,2]], time = 3, change = 2))
    print(Solution().secondMinimum(n = 5, edges = [[1,2],[2,5],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5))
    print(Solution().secondMinimum2(n = 5, edges = [[1,2],[2,5],[1,3],[1,4],[3,4],[4,5]], time = 3, change = 5))
        