'''
-Medium-
*Dijkstra's Algorithm*
*Shortest Path*

You are given an array start where start = [startX, startY] represents your initial position (startX, startY) in a 2D space. You are also given the array target where target = [targetX, targetY] represents your target position (targetX, targetY).

The cost of going from a position (x1, y1) to any other position in the space (x2, y2) is |x2 - x1| + |y2 - y1|.

There are also some special roads. You are given a 2D array specialRoads where specialRoads[i] = [x1i, y1i, x2i, y2i, costi] indicates that the ith special road can take you from (x1i, y1i) to (x2i, y2i) with a cost equal to costi. You can use each special road any number of times.

Return the minimum cost required to go from (startX, startY) to (targetX, targetY).

 

Example 1:

Input: start = [1,1], target = [4,5], specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]
Output: 5
Explanation: The optimal path from (1,1) to (4,5) is the following:
- (1,1) -> (1,2). This move has a cost of |1 - 1| + |2 - 1| = 1.
- (1,2) -> (3,3). This move uses the first special edge, the cost is 2.
- (3,3) -> (3,4). This move has a cost of |3 - 3| + |4 - 3| = 1.
- (3,4) -> (4,5). This move uses the second special edge, the cost is 1.
So the total cost is 1 + 2 + 1 + 1 = 5.
It can be shown that we cannot achieve a smaller total cost than 5.
Example 2:

Input: start = [3,2], target = [5,7], specialRoads = [[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]
Output: 7
Explanation: It is optimal to not use any special edges and go directly from the starting to the ending position with a cost |5 - 3| + |7 - 2| = 7.
 

Constraints:

start.length == target.length == 2
1 <= startX <= targetX <= 105
1 <= startY <= targetY <= 105
1 <= specialRoads.length <= 200
specialRoads[i].length == 5
startX <= x1i, x2i <= targetX
startY <= y1i, y2i <= targetY
1 <= costi <= 105


'''
from typing import List
from collections import defaultdict
import heapq
from math import inf
class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        R = specialRoads
        m = len(R)
        n = 2*m+2
        G = defaultdict(list)
        T = n-1
        def dist (x1, y1, x2, y2):
            return abs(x2-x1) + abs(y2-y1)
        for i, (sx,sy,tx,ty,c) in enumerate(R):
            G[0].append([i+1, dist(start[0], start[1], sx, sy)]) 
        for i, (sx,sy,tx,ty,c) in enumerate(R):
            G[i+1].append([i+m+1,min(dist(sx,sy,tx,ty),c)]) 
        for i, (sx,sy,tx,ty,c) in enumerate(R):
            if tx == target[0] and ty == target[1]:
               T = i+1+m
               break 
        for i, (sx,sy,tx,ty,c) in enumerate(R):
            if T != i+1+m:
                G[i+1+m].append([T,dist(tx, ty, target[0], target[1])]) 
        for i in range(m):
            for j in range(m):
                if i != j:
                    G[i+1+m].append([j+1, dist(R[i][2],R[i][3],R[j][0],R[j][1])])
        G[0].append([T, dist(start[0], start[1], target[0], target[1])])
        pq = [(0, 0)]
        dis = [inf]*n
        while pq:
            d, cur = heapq.heappop(pq) 
            if cur == T: return d
            dis[cur] = d
            for nxt, cost in G[cur]:
                if dis[nxt] > dis[cur] + cost:
                    dis[nxt] = dis[cur] + cost
                    heapq.heappush(pq, (dis[nxt], nxt))
        return -1

if __name__ == '__main__':
    print(Solution().minimumCost(start = [1,1], target = [4,5], specialRoads = [[1,2,3,3,2],[3,4,4,5,1]]))
    print(Solution().minimumCost(start = [3,2], target = [5,7], specialRoads = [[3,2,3,4,4],[3,3,5,5,5],[3,4,5,6,6]]))
    print(Solution().minimumCost([1,1], [9,9], [[2,4,9,2,1],[4,8,4,4,4],[5,9,9,9,1],[3,9,7,9,3]]))