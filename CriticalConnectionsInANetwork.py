'''
There are n servers numbered from 0 to n-1 connected by undirected 
server-to-server connections forming a network where connections[i] 
= [a, b] represents a connection between servers a and b. Any server 
can reach any other server directly or indirectly through the network.

A critical connection is a connection that, if removed, will make 
some server unable to reach some other server.

Return all critical connections in the network in any order.

Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
 

Constraints:

1 <= n <= 10^5
n-1 <= connections.length <= 10^5
connections[i][0] != connections[i][1]
There are no repeated connections.

'''
from collections import defaultdict

class Solution(object):
    def criticalConnections(self, n, connections):
        """
        :type n: int
        :type connections: List[List[int]]
        :rtype: List[List[int]]
        """
        g = defaultdict(set)
        pre = [-1]*n
        low = [-1]*n
        cnt = [0]
        for c in connections:
            g[c[0]].add(c[1]) # undirected graph, connect 
            g[c[1]].add(c[0]) # in both directions
        ans = []
        def dfs(edge):            
            v, w = edge
            pre[w] = cnt[0]
            low[w] = pre[w]
            cnt[0] += 1
            for i in g[w]:
                if i == v: continue                    
                if pre[i] == -1:
                    dfs((w,i))          
                    # low[i] > pre[w] indicates no back edge to
                    # w's ancesters; otherwise, low[i] will be 
                    # < pre[w]+1 since back edge makes low[i] smaller           
                    if low[i] > pre[w]: 
                    #print(low[i], pre[w]+1, (w,i))                       
                        ans.append([w,i])                
                    low[w] = min(low[w], low[i]) # low[i] might be an ancestor of w
                else: # if i was already discovered means that we found an ancestor
                    low[w] = min(low[w], pre[i]) # finds the ancestor with the least 
                                                 # discovery time
               
                
        dfs((-1,0))
        #print(low)
        #print(pre)
        return ans
 


if __name__=="__main__":
    print(Solution().criticalConnections(4, [[0,1],[1,2],[2,0],[1,3]]))

    print(Solution().criticalConnections(7, [[0,1],[0,2],[1,3],[1,4],
                                              [2,5], [2,6]]))




