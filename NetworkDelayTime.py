'''

*Dijkstra's algorithm*

There are N network nodes, labelled 1 to N.

Given times, a list of travel times as directed edges times[i] = (u, v, w), where 
u is the source node, v is the target node, and w is the time it takes for a signal 
to travel from source to target.

Now, we send a signal from a certain node K. How long will it take for all nodes to 
receive the signal? If it is impossible, return -1.

Input: times = [[2,1,1],[2,3,1],[3,4,1]], N = 4, K = 2
Output: 2
 

Note:

N will be in the range [1, 100].
K will be in the range [1, N].
The length of times will be in the range [1, 6000].
All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.
'''
from collections import defaultdict
import sys
import heapq
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        g = defaultdict(set)
        pq = []
        book = {}
        mx = sys.maxsize
        dist = [mx]*N
        def update(v, d):         
            if v in book:
                remove(v)    
            entry = [d, v]
            book[v] = entry
            heapq.heappush(pq, entry)

        def remove(v):    
            entry = book.pop(v)
            entry[-1] = -1
 
        for i in range(1, N+1):
            vert = [mx, i]
            book[i] = vert
            heapq.heappush(pq, vert)            
        for t in times:
            g[t[0]].add((t[1], t[2]))
        update(K, 0) 
        dist[K-1] = 0        
        while pq:
            (d, u) = heapq.heappop(pq)            
            if u != -1:                              
                del book[u]
                for v, w in g[u]:
                    if v in book and book[v][0] > d + w:                      
                        dist[v-1] = d+w                        
                        update(v, d+w)                 
        res = 0        
        for v in dist:
            if v == mx:
                return -1        
            res = max(res, v)
        return res       


if __name__ == "__main__":
    #print(Solution().networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2))
    #print(Solution().networkDelayTime([[1,2,1]], 2, 2))
    times = [[1,5,66],[3,5,55],[4,3,29],[1,2,9],[3,4,10],[3,1,3],[2,3,78],
             [1,4,98],[4,5,21],[5,2,19],[5,1,76],[4,1,65],[3,2,27],[5,3,23],
             [5,4,12],[2,1,36],[4,2,75],[2,4,11],[1,3,30],[2,5,8]]
    print(Solution().networkDelayTime(times, 5, 1))