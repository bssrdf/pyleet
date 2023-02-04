'''
-Hard-

You are an ant tasked with adding n new rooms numbered 0 to n-1 to your colony. You are 
given the expansion plan as a 0-indexed integer array of length n, prevRoom, where 
prevRoom[i] indicates that you must build room prevRoom[i] before building room i, and 
these two rooms must be connected directly. Room 0 is already built, so prevRoom[0] = -1. 
The expansion plan is given such that once all the rooms are built, every room will be 
reachable from room 0.

You can only build one room at a time, and you can travel freely between rooms you have 
already built only if they are connected. You can choose to build any room as long as its 
previous room is already built.

Return the number of different orders you can build all the rooms in. Since the answer 
may be large, return it modulo 10^9 + 7.

 

Example 1:


Input: prevRoom = [-1,0,1]
Output: 1
Explanation: There is only one way to build the additional rooms: 0 → 1 → 2
Example 2:


Input: prevRoom = [-1,0,0,1,2]
Output: 6
Explanation:
The 6 ways are:
0 → 1 → 3 → 2 → 4
0 → 2 → 4 → 1 → 3
0 → 1 → 2 → 3 → 4
0 → 1 → 2 → 4 → 3
0 → 2 → 1 → 3 → 4
0 → 2 → 1 → 4 → 3
 

Constraints:

n == prevRoom.length
2 <= n <= 10^5
prevRoom[0] == -1
0 <= prevRoom[i] < n for all 1 <= i < n
Every room is reachable from room 0 once all the rooms are built.


'''
import collections
import math
import sys
#print(sys.getrecursionlimit())
#sys.setrecursionlimit(100000)
#import resource
#resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))

class Solution(object):
    def waysToBuildRooms(self, prevRoom):
        """
        :type prevRoom: List[int]
        :rtype: int
        """
        MOD = 10**9 + 7
        g = collections.defaultdict(list)
        for cur, pre in enumerate(prevRoom):
            g[pre].append(cur)
        #print(g)    
        def dfs(cur):
            if not g[cur]:
                return 1, 1
            ans, l = 1, 0
            for nxt in g[cur]:
                tmp, r = dfs(nxt)
                ans = (ans * tmp * math.comb(l+r, r)) % MOD
                l += r
            return ans, l + 1
            
        return dfs(0)[0]

    def waysToBuildRoomsModuloInverse(self, prevRoom):
        """
        :type prevRoom: List[int]
        :rtype: int
        """
        def dfs(tree, size, root):
            ans = 1
            for nxt in tree[root]:
                ans += dfs(tree, size, nxt)
            size[root] = ans
            return ans
        def power(x, y, m):
            if y == 0:
                return 1
            p = power(x, y // 2, m) % m
            p = (p * p) % m
            if y % 2 == 0:
                return p
            else:
                return (x * p) % m
        def modInverse(a, m):
            return power(a, m - 2, m)
        n = len(prevRoom)
        MOD = 10**9 + 7
        g = collections.defaultdict(list)
        for cur, pre in enumerate(prevRoom):
            g[pre].append(cur)
        size = [0] * n
        dfs(g, size, 0)
        nFac = 1
        for i in range(1, n+1):
            nFac *= i
        denorm = 1
        for i in range(n):
            denorm *= size[i]
        inverse = modInverse(denorm, MOD)
        res = (nFac*inverse)%MOD
        return res
        
    def waysToBuildRoomsDP(self, prevRoom):
        """
        :type prevRoom: List[int]
        :rtype: int
        """
        MOD, M = 10**9 + 7, 10**5
        facts = [1]*(M+1)
        for i in range(1, M+1):
            facts[i] = (facts[i-1] * i) % MOD
            
        facts_inv = [1]*M + [pow(facts[M], MOD - 2, MOD)]
        for i in range(M-1, 0, -1):
            facts_inv[i] = facts_inv[i+1]*(i+1) % MOD
        
        graph = collections.defaultdict(list)
        for i, num in enumerate(prevRoom):
            graph[num].append(i)

        def dp(node):
            ans, sm = 1, 1
            for neib in graph[node]:
                ans2, sm2 = dp(neib)
                ans = (ans * self.facts_inv[sm2] * ans2) % self.MOD
                sm += sm2
            return ((ans * self.facts[sm-1]) % self.MOD, sm)

        return dp(0)[0]

    def waysToBuildRoomsTopo(self, prevRoom):
        """
        :type prevRoom: List[int]
        :rtype: int
        """
        mod=10**9+ 7
        N=len(prevRoom)
        Adj=[[] for _ in range(N)]
        Indegree=[0]*N
        Fac=[1]*(N+1)
        Inv=[1]*(N+1)
        for n in range(1,N+1):
            Fac[n]=n*Fac[n-1]%mod
            Inv[n]=pow(Fac[n],mod-2,mod)
        
        for i in range(1,len(prevRoom)):
            Adj[prevRoom[i]].append(i)
        
        children=[0]*N
        
        def findChildren(node):
            nonlocal children
            ans=1
            for child in Adj[node]:
                ans+=findChildren(child)
            
            children[node]=ans
            return ans
        
        findChildren(0)
        
        def find(node):
            val=1
            for child in Adj[node]:
                val*=find(child)
                val%=mod
                
            total=0
            childcnt=[]
            for child in Adj[node]:
                total+=children[child]
                childcnt.append(children[child])
            
            
            val*=Fac[total]
            val%=mod
            
            for cnt in childcnt:
                val*=Inv[cnt]
                val%=mod
            return val
        
        return find(0)
        



if __name__ == "__main__":
    #print(Solution().waysToBuildRooms([-1,0,0,1,2]))
    #print(Solution().waysToBuildRoomsModuloInverse([-1,0,0,1,2]))
    rooms = list(range(-1, 2500))
    #print(rooms[0])
    #print(rooms[-1])
    #print(Solution().waysToBuildRooms(rooms))
    #print(Solution().waysToBuildRoomsDP(rooms))
    #print(Solution().waysToBuildRoomsTopo(rooms))
    #print(Solution().waysToBuildRoomsModuloInverse(rooms) == 1)
    assert Solution().waysToBuildRoomsModuloInverse(rooms) == 2