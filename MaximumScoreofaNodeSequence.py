'''

-Hard-


There is an undirected graph with n nodes, numbered from 0 to n - 1.

You are given a 0-indexed integer array scores of length n where scores[i] denotes 
the score of node i. You are also given a 2D integer array edges 
where edges[i] = [ai, bi] denotes that there exists an undirected edge 
connecting nodes ai and bi.

A node sequence is valid if it meets the following conditions:

There is an edge connecting every pair of adjacent nodes in the sequence.
No node appears more than once in the sequence.
The score of a node sequence is defined as the sum of the scores of the nodes in the sequence.

Return the maximum score of a valid node sequence with a length of 4. If no such 
sequence exists, return -1.

 

Example 1:


Input: scores = [5,2,9,8,4], edges = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
Output: 24
Explanation: The figure above shows the graph and the chosen node sequence [0,1,2,3].
The score of the node sequence is 5 + 2 + 9 + 8 = 24.
It can be shown that no other node sequence has a score of more than 24.
Note that the sequences [3,1,2,0] and [1,0,2,3] are also valid and have a score of 24.
The sequence [0,3,2,4] is not valid since no edge connects nodes 0 and 3.
Example 2:


Input: scores = [9,20,6,4,11,12], edges = [[0,3],[5,3],[2,4],[1,3]]
Output: -1
Explanation: The figure above shows the graph.
There are no valid node sequences of length 4, so we return -1.
 

Constraints:

n == scores.length
4 <= n <= 5 * 104
1 <= scores[i] <= 108
0 <= edges.length <= 5 * 104
edges[i].length == 2
0 <= ai, bi <= n - 1
ai != bi
There are no duplicate edges.
'''

from typing import List
from collections import defaultdict, deque
import heapq
import bisect

class Solution:
    def maximumScore2(self, scores: List[int], edges: List[List[int]]) -> int:
        # wrong solution
        n = len(scores)
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u) 
        visited = [False]*n
        ans = [-1]
        def dfs(u, path, sums):
            if len(path) == 4:
                # print(path)
                ans[0] = max(ans[0], sums)
                sums -= scores[path.popleft()]  
            visited[u] = True
            path.append(u)
            for v in g[u]:
                if v not in path:
                    dfs(v, path, sums)
            # path.pop()
            #visited[u] = False 
        for u in range(n):
            if not visited[u]:
                dfs(u, deque(), 0)
        return ans[0]
    
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        n = len(scores)
        S = scores
        ans = -1
        '''
        neibor = [[[0, -1] for _ in range(2)] for _ in range(n)]
        for u, v in edges:
            e = neibor[u]
            if S[v] >= e[0][0]:
                e[1][0], e[1][1] = e[0][0], e[0][1]
                e[0][0], e[0][1] = S[v], v 
            elif S[v] >= e[1][0]:
                e[1][0], e[1][1] = S[v], v 
            e = neibor[v]
            if S[u] >= e[0][0]:
                e[1][0], e[1][1] = e[0][0], e[0][1]
                e[0][0], e[0][1] = S[u], u 
            elif S[u] >= e[1][0]:
                e[1][0], e[1][1] = S[u], u 
        
        for u, v in edges:
            eu, ev = neibor[u], neibor[v]
            c = S[u]+S[v]
            if eu[0][1] == ev[0][1]:
                if eu[1][1] == -1 and ev[1][1] == -1:
                    continue 
                elif eu[1][1] == -1:
                    ans = max(ans, c+eu[0][0]+ev[1][0])
                elif ev[1][1] == -1:
                    ans = max(ans, c+eu[1][0]+ev[0][0])
                else:
                    ans = max(ans, c+eu[1][0]+ev[0][0], c+eu[0][0]+ev[1][0])
            else:
                ans = max(ans, c+S[eu[0][1]]+S[ev[0][1]])
            print(u,v,c,ans,eu,ev)
        return ans
        '''
        neibor = [[] for _ in range(n)]
        for u, v in edges:
            heapq.heappush(neibor[u], (scores[v], v))
            if len(neibor[u]) > 3:
                heapq.heappop(neibor[u])
            heapq.heappush(neibor[v], (scores[u], u))
            if len(neibor[v]) > 3:
                heapq.heappop(neibor[v])
        # for i in range(n):    
        #     print(i, neibor[i])
        for u, v in edges:
            eu, ev = [], []
            # while neibor[u]:
            for i in range(len(neibor[u])):
                if neibor[u][i][1] != v:
                    heapq.heappush(eu, (-neibor[u][i][0], neibor[u][i][1]))
            for i in range(len(neibor[v])):
                if neibor[v][i][1] != u: 
                    heapq.heappush(ev, (-neibor[v][i][0], neibor[v][i][1]))               
            if eu and ev:
                c = S[u]+S[v]
                if eu[0][1] == ev[0][1]:
                    if len(eu) == 1 and len(ev) == 1:
                        continue 
                    elif len(eu) == 1:
                        ans = max(ans, c-eu[0][0]-ev[1][0])
                    elif len(ev) == 1:
                        ans = max(ans, c-eu[1][0]-ev[0][0])
                    else:
                        ans = max(ans, c-eu[1][0]-ev[0][0], c-eu[0][0]-ev[1][0])
                else:
                    ans = max(ans, c-eu[0][0]-ev[0][0])
            # print(u,v,S[u]+S[v],ans,eu,ev)    
        return ans 
    
    def maximumScore3(self, scores: List[int], edges: List[List[int]]) -> int:
        A, E = scores, edges
        n = len(A)
        
        # Store the top 3 neighbors of a node.
        top3 = defaultdict(list)
        
        def func(a, b, e):
            bisect.insort_left(top3[a], [e, b])
            if len(top3[a]) > 3:
                top3[a].pop(0)
        
        # Update the information of top 3 neighbors of each node
        for a, b in E:
            func(a, b, A[b])
            func(b, a, A[a])
        
        ans = -1
        for a, b in E:
            # If there is less than 2 neighbors of a node, skip this pair.
            if len(top3[a]) < 2 or len(top3[b]) < 2:
                continue
            for c in top3[a]:
                for d in top3[b]:
                    # Find the maximum score of two non-duplicated neighbors of a and b.
                    if c[1] not in [a, b] and d[1] not in [a, b] and c[1] != d[1]:
                        ans = max(ans, A[a] + A[b] + c[0] + d[0])
        return ans
    
    def maximumScore4(self, scores: List[int], edges: List[List[int]]) -> int:
        g = defaultdict(list)
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        for node in g:
            g[node].sort(key=lambda idx: scores[idx])    
        ans = -1
        for x, y in edges:
            if not g[x] or not g[y]:
                continue
            i, j = len(g[x])-1, len(g[y])-1
            if g[x][i] == y:
                i -= 1
            if g[y][j] == x:
                j -= 1
            if i < 0 or j < 0:
                continue    
            if g[x][i] == g[y][j]:
                # print(x, y, i, j, g[x][i], g[y][j], g[x], g[y])
                if i and j:
                    if scores[g[x][i-1]] > scores[g[y][j-1]] or g[y][j-1] == x:
                        i -= 1
                    else:
                        j -= 1
                    if g[x][i] == y:
                        i -= 1
                    if g[y][j] == x:
                        j -= 1    
                else:
                    continue        
            if i < 0 or j < 0:
                continue    
            
            nei_x = g[x][i]
            nei_y = g[y][j]
            ans = max(ans, scores[x] + scores[y] + scores[nei_x] + scores[nei_y])
            # print(x, y, nei_x, nei_y)
        return ans           
        
 




if __name__ == "__main__":
    #'''
    scores = [5,2,9,8,4]
    edges = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]
    print(Solution().maximumScore(scores, edges))
    scores = [9,20,6,4,11,12]
    edges = [[0,3],[5,3],[2,4],[1,3]]
    print(Solution().maximumScore(scores, edges))
    scores = [18,6,4,9,8,2]
    edges = [[0,1],[0,2],[0,3],[0,4],[0,5],[1,2],[1,3],[1,4],[1,5],[2,3],[2,4],[2,5],[3,4],[3,5],[4,5]]
    print(Solution().maximumScore(scores, edges))
    #'''
    scores = [6,17,3,22,27,18,10,26,30,22,16,18]
    edges = [[0,1],[6,7],[0,2],[6,8],[0,3],[6,9],[0,4],[6,10],[0,5],[6,11],[1,2],[7,8],[1,3],[7,9],[1,4],[7,10],[1,5],[7,11],[2,3],[8,9],[2,4],[8,10],[2,5],[8,11],[3,4],[9,10],[3,5],[9,11],[4,5],[10,11]]
    print(Solution().maximumScore(scores, edges))
    
        