'''
-Medium-

On a campus represented as a 2D grid, there are N workers and M bikes, with N <= M. 
Each worker and bike is a 2D coordinate on this grid.

Our goal is to assign a bike to each worker. Among the available bikes and workers, we 
choose the (worker, bike) pair with the shortest Manhattan distance between each other, 
and assign the bike to that worker. (If there are multiple (worker, bike) pairs with the 
same shortest Manhattan distance, we choose the pair with the smallest worker index; 
if there are multiple ways to do that, we choose the pair with the smallest bike index). 
We repeat this process until there are no available workers.

The Manhattan distance between two points p1 and p2 is 
Manhattan(p1, p2) = |p1.x - p2.x| + |p1.y - p2.y|. 

Return a vector ansof length N, where ans[i] is the index (0-indexed) of the bike 
that the i-th worker is assigned to.

Example 1:



Input: 
workers = [[0,0],[2,1]], 
bikes = [[1,2],[3,3]]
Output: 
[1,0]
Explanation: 

Worker 1 grabs Bike 0 as they are closest (without ties), and Worker 0 is assigned Bike 1. So the output is [1, 0].
Example 2:



Input: 
workers = [[0,0],[1,1],[2,0]], 
bikes = [[1,0],[2,2],[2,1]]
Output: 
[0,2,1]
Explanation: 

Worker 0 grabs Bike 0 at first. Worker 1 and Worker 2 share the same distance to Bike 2, thus Worker 1 is a

Note:

0 <= workers[i][j], bikes[i][j] < 1000
All worker and bike locations are distinct.
1 <= workers.length <= bikes.length <= 1000

'''

import heapq

class Solution:
    """
    @param workers: workers' location
    @param bikes: bikes' location
    @return: assign bikes
    """
    def assignBikesTLE(self, workers, bikes):
        # write your code here
        n, m = len(workers), len(bikes)
        pq, res = [], [-1]*n
        assigned, taken = set(), set()
        for i in range(n):
            for j in range(m):
                md = abs(workers[i][0]-bikes[j][0]) + abs(workers[i][1]-bikes[j][1])
                heapq.heappush(pq, (md, i, j))
        while pq:
            _, w, b = heapq.heappop(pq)
            if w not in assigned:                
                assigned.add(w)
                if b not in taken:
                    taken.add(b)
                    res[w] = b
                else:
                    assigned.remove(w)
        return res
    
    def assignBikes(self, workers, bikes):
        distances = []     
        # distances[worker] is tuple of (distance, worker, bike) for each bike 
        for i, (x, y) in enumerate(workers):
            distances.append([])
            for j, (x_b, y_b) in enumerate(bikes):
                distance = abs(x - x_b) + abs(y - y_b)
                distances[-1].append((distance, i, j))
            distances[-1].sort(reverse = True)  # reverse so we can pop the smallest distance

        result = [None] * len(workers)
        used_bikes = set()
        queue = [distances[i].pop() for i in range(len(workers))]   # smallest distance for each worker
        heapq.heapify(queue)

        while len(used_bikes) < len(workers):
            _, worker, bike = heapq.heappop(queue)
            if bike not in used_bikes:
                result[worker] = bike
                used_bikes.add(bike)
            else:
                heapq.heappush(queue, distances[worker].pop()) # bike used, add next closest bike
        return result



if __name__ == "__main__":
    print(Solution().assignBikes([[0,0],[2,1]], [[1,2],[3,3]]))
    print(Solution().assignBikes([[0,0],[1,1],[2,0]], [[1,0],[2,2],[2,1]]))