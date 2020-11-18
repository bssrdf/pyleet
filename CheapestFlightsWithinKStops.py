'''
-Medium-

*DFS*
*BFS*
*Bellman-Ford*
*DP*

There are n cities connected by m flights. Each flight starts from city u and 
arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the 
destination dst, your task is to find the cheapest price from src to dst 
with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as 
marked red in the picture.

Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as 
marked blue in the picture.
 

Constraints:

The number of nodes n will be in range [1, 100], with nodes labeled from 
0 to n - 1.
The size of flights will be in range [0, n * (n - 1) / 2].
The format of each flight will be (src, dst, price).
The price of each flight will be in the range [1, 10000].
k is in the range of [0, n - 1].
There will not be any duplicated flights or self cycles.

'''
import heapq

from collections import defaultdict
from collections import deque

class Solution(object):

    def findCheapestPriceDijkstra(self, n, flights, src, dst, k):
        '''
        The key difference with the classic Dijkstra algo is, we don't 
        maintain the global optimal distance to each node, i.e. ignore 
        below optimization:
          alt ← dist[u] + length(u, v) if alt < dist[v]:
        Because there could be routes which their length is shorter but 
        pass more stops, and those routes don't necessarily constitute the 
        best route in the end. To deal with this, rather than maintain the 
        optimal routes with 0..K stops for each node, the solution simply 
        put all possible routes into the priority queue, so that all of 
        them has a chance to be processed. IMO, this is the most brilliant part.
        And the solution simply returns the first qualified route, it's easy 
        to prove this must be the best route.
        '''
        f = defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p
        heap = [(0, src, k + 1)]
        while heap:
            cost, city, stops = heapq.heappop(heap)
            print(cost, city, stops)
            if city == dst:
                return p
            if stops > 0:
                for j in f[city]:
                    heapq.heappush(heap, (cost + f[city][j], j, stops - 1))
        return -1

    def findCheapestPriceBellmanFord(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
                
        dp = [[10**10 for _ in range(n)] for _ in range(K+2)]
        g = defaultdict(dict)        
        for f in flights:
            g[f[0]][f[1]] = f[2]        
        dp[0][src] = 0        
        for k in range(1,K+2):
            dp[k][src] = 0
            for f in flights:
                dp[k][f[1]] = min(dp[k][f[1]], dp[k-1][f[0]]+f[2])
        return -1 if dp[K+1][dst] == 10**10 else dp[K+1][dst]       
        

    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """
        dq = deque()
        cnt = 0
        res = 10**10        
        g = defaultdict(dict)        
        for f in flights:
            g[f[0]][f[1]] = f[2]        
        dq.append((src,0))        
        while dq:
            for i in range(len(dq)):
                city, cost = dq.popleft()                        
                if city == dst: 
                    res = min(res, cost)
                for d in g[city]:
                    # branch prune
                    if cost+g[city][d] > res: continue                    
                    dq.append((d, cost+g[city][d]))
            if cnt > K: break
            cnt += 1
        return -1 if res == 10**10 else res     

if __name__ == "__main__":
    #'''
    print(Solution().findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]],
                                      0, 2, 1))
    print(Solution().findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]],
                                       0, 2, 0))
    print(Solution().findCheapestPrice(4, [[0,3,59],[2,0,83],[2,3,32],
                                           [0,2,97],[3,1,16],[1,3,16]]
                                       , 3, 0, 3))
    
    tickets = [[3,15,7066],[2,7,9254],[15,12,54],[6,8,8137],[7,12,9819],[5,2,7956],[14,3,6675],[8,14,4543],[5,13,1689],[2,12,1220],[9,15,5710],[11,13,5799],[16,3,154],[4,6,5499],[13,2,1143],[0,6,485],[16,2,5211],[9,7,4453],[0,8,8798],[4,9,4760],[16,6,9182],[6,18,3774],[17,3,630],[0,2,5689],[18,1,4688],[4,11,4044],[14,0,4253],[2,18,3697],[16,18,7525],[15,14,1480],[2,10,4931],[10,8,1741],[3,10,7964],[7,15,7880],[17,2,9694],[6,14,9167],[10,1,6844],[13,3,4742],[16,15,6428],[0,1,5819],[13,17,2815],[14,17,5654],[5,3,8906],[9,14,9342],[7,17,3559],[16,12,2633],[17,9,331],[10,4,3234],[2,17,9607],[12,5,2003],[5,9,6784],[15,0,175],[10,11,6834],[2,9,6348],[18,13,7372],[15,7,3535],[1,14,7877],[1,4,8036],[7,16,7089],[1,12,6523],[4,14,3668],[1,10,8785],[1,13,1219],[13,11,8834],[18,11,2920],[12,2,531],[4,17,8509],[2,11,3368],[16,5,5302],[14,5,6143],[10,14,1639],[10,16,7114],[10,13,9941],[13,18,1779],[9,5,5628],[12,14,2892],[11,17,1064],[1,17,8652],[15,16,8192],[9,10,260],[7,1,6405],[16,7,3532],[3,0,9842],[12,16,3233],[13,1,8375],[10,7,6730],[18,4,6232],[17,5,7097],[14,13,7290],[10,2,4442],[13,5,8228],[14,6,4709],[6,11,4636],[14,8,10000],[8,9,9133],[5,18,6091],[10,3,6397],[4,3,8425],[14,12,7883],[4,16,901],[16,4,4051],[1,0,7827],[5,11,8596],[18,9,4058],[18,6,5500],[16,9,2414],[12,11,4230],[1,6,3821],[18,0,1299],[11,5,4232],[15,2,5251],[12,13,1716],[17,15,3],[0,16,1708],[3,11,661],[17,16,9213],[8,0,2913],[2,6,556],[5,1,9106],[16,10,7006],[2,13,3038]]
    print(Solution().findCheapestPrice(19, tickets, 12, 10, 0))

    print(Solution().findCheapestPrice(4, [[0,1,1],[0,2,5],[1,2,1],[2,3,1]],
                                       0, 3, 1))
    #'''
    print(Solution().findCheapestPrice(5, [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]],
                                       0, 2, 2))

    print(Solution().findCheapestPriceBellmanFord(3, [[0,1,100],[1,2,100],[0,2,500]],
                                      0, 2, 1))
    print(Solution().findCheapestPriceBellmanFord(3, [[0,1,100],[1,2,100],[0,2,500]],
                                       0, 2, 0))
    print(Solution().findCheapestPriceBellmanFord(4, [[0,3,59],[2,0,83],[2,3,32],
                                           [0,2,97],[3,1,16],[1,3,16]]
                                       , 3, 0, 3))
    
    tickets = [[3,15,7066],[2,7,9254],[15,12,54],[6,8,8137],[7,12,9819],[5,2,7956],[14,3,6675],[8,14,4543],[5,13,1689],[2,12,1220],[9,15,5710],[11,13,5799],[16,3,154],[4,6,5499],[13,2,1143],[0,6,485],[16,2,5211],[9,7,4453],[0,8,8798],[4,9,4760],[16,6,9182],[6,18,3774],[17,3,630],[0,2,5689],[18,1,4688],[4,11,4044],[14,0,4253],[2,18,3697],[16,18,7525],[15,14,1480],[2,10,4931],[10,8,1741],[3,10,7964],[7,15,7880],[17,2,9694],[6,14,9167],[10,1,6844],[13,3,4742],[16,15,6428],[0,1,5819],[13,17,2815],[14,17,5654],[5,3,8906],[9,14,9342],[7,17,3559],[16,12,2633],[17,9,331],[10,4,3234],[2,17,9607],[12,5,2003],[5,9,6784],[15,0,175],[10,11,6834],[2,9,6348],[18,13,7372],[15,7,3535],[1,14,7877],[1,4,8036],[7,16,7089],[1,12,6523],[4,14,3668],[1,10,8785],[1,13,1219],[13,11,8834],[18,11,2920],[12,2,531],[4,17,8509],[2,11,3368],[16,5,5302],[14,5,6143],[10,14,1639],[10,16,7114],[10,13,9941],[13,18,1779],[9,5,5628],[12,14,2892],[11,17,1064],[1,17,8652],[15,16,8192],[9,10,260],[7,1,6405],[16,7,3532],[3,0,9842],[12,16,3233],[13,1,8375],[10,7,6730],[18,4,6232],[17,5,7097],[14,13,7290],[10,2,4442],[13,5,8228],[14,6,4709],[6,11,4636],[14,8,10000],[8,9,9133],[5,18,6091],[10,3,6397],[4,3,8425],[14,12,7883],[4,16,901],[16,4,4051],[1,0,7827],[5,11,8596],[18,9,4058],[18,6,5500],[16,9,2414],[12,11,4230],[1,6,3821],[18,0,1299],[11,5,4232],[15,2,5251],[12,13,1716],[17,15,3],[0,16,1708],[3,11,661],[17,16,9213],[8,0,2913],[2,6,556],[5,1,9106],[16,10,7006],[2,13,3038]]
    print(Solution().findCheapestPriceBellmanFord(19, tickets, 12, 10, 0))

    print(Solution().findCheapestPriceBellmanFord(4, [[0,1,1],[0,2,5],[1,2,1],[2,3,1]],
                                       0, 3, 1))
    #'''
    print(Solution().findCheapestPriceBellmanFord(5, [[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]],
                                       0, 2, 2))

    print(Solution().findCheapestPriceDijkstra(4, [[0,1,1],[0,2,5],[1,2,1],[2,3,1]],
                                       0, 3, 1))                         