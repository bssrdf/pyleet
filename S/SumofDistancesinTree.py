'''

-Hard-

There is an undirected connected tree with n nodes labeled from 0 to n - 1 and n - 1 edges.

You are given the integer n and the array edges where edges[i] = [ai, bi] indicates that there 
is an edge between nodes ai and bi in the tree.

Return an array answer of length n where answer[i] is the sum of the distances between the ith node 
in the tree and all other nodes.

 

Example 1:


Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
Output: [8,12,6,10,10,10]
Explanation: The tree is shown above.
We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
equals 1 + 1 + 2 + 2 + 2 = 8.
Hence, answer[0] = 8, and so on.
Example 2:


Input: n = 1, edges = []
Output: [0]
Example 3:


Input: n = 2, edges = [[1,0]]
Output: [1,1]
 

Constraints:

1 <= n <= 3 * 10^4
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
The given input represents a valid tree.

'''

import collections
from functools import lru_cache

class Solution:
    def sumOfDistancesInTree(self, N, edges):
        dic1 = collections.defaultdict(list)
        for e in edges:
            dic1[e[0]].append(e[1])
            dic1[e[1]].append(e[0])
        
        # eachItem subtreeDist[n]=[a, b] means subtree rooted at n has totally a nodes, 
        # and sum of distance in the subtree for n is b
        subtreeDist = [[0, 0] for _ in range(N)]
        
        ans = [0]*N
        
        def sumSubtreeDist(n, exclude):
            cnt, ret = 0, 0
            exclude.add(n)
            for x in dic1[n]:
                if x in exclude:
                    continue
                res = sumSubtreeDist(x, exclude)
                cnt += res[0]
                ret += (res[0]+res[1])
            subtreeDist[n][0] = cnt+1
            subtreeDist[n][1] = ret
            return cnt+1, ret
            
        # recursively calculate the sumDist for all subtrees 
        # 0 can be replaced with any other number in [0, N-1]
        # and the chosen root has its correct sum distance in the whole tree
        sumSubtreeDist(0, set())
        
        # visit and calculates the sum distance in the whole tree
        def visit(n, pre, exclude):
            if pre==-1:
                ans[n] = subtreeDist[n][1]
            else:
                ans[n] = ans[pre]-2*subtreeDist[n][0]+N
            exclude.add(n)
            for x in dic1[n]:
                if x not in exclude:
                    visit(x, n, exclude)
                
        visit(0, -1, set())
        return ans
    
    def sumOfDistancesInTree2(self, N, edges):
        dic1 = collections.defaultdict(list)
        for e in edges:
            dic1[e[0]].append(e[1])
            dic1[e[1]].append(e[0])
        
        # eachItem subtreeDist[n]=[a, b] means subtree rooted at n has totally a nodes, 
        # and sum of distance in the subtree for n is b
        subtreeDist = [[0, 0] for _ in range(N)]
        
        ans = [0]*N
        visited = [False]*N
        
        def sumSubtreeDist(n):
            cnt, ret = 0, 0
            visited[n] = True
            for x in dic1[n]:
                if visited[x]: continue
                res = sumSubtreeDist(x)
                cnt += res[0]
                ret += (res[0]+res[1])
            subtreeDist[n][0] = cnt+1
            subtreeDist[n][1] = ret
            return cnt+1, ret
            
        # recursively calculate the sumDist for all subtrees 
        # 0 can be replaced with any other number in [0, N-1]
        # and the chosen root has its correct sum distance in the whole tree
        sumSubtreeDist(0)

        visited = [False]*N        
        # visit and calculates the sum distance in the whole tree
        def visit(n, pre):
            if pre==-1:
                ans[n] = subtreeDist[n][1]
            else:
                ans[n] = ans[pre]-2*subtreeDist[n][0]+N
            visited[n] = True
            for x in dic1[n]:
                if not visited[x]:
                    visit(x, n)
                
        visit(0, -1)
        return ans

    def sumOfDistancesInTreeFast(self, N, edges):
        sumDist = [0] * N
        downNodes = [0] * N
        
        nbors = collections.defaultdict(list)
        for start, j in edges:
            nbors[start].append(j)
            nbors[j].append(start)

        def downDFS(prev, now):
            dSum = nSum = 0
            for nei in nbors[now]:
                if nei == prev: continue
                n, d = downDFS(now, nei)
                dSum += d + n
                nSum += n
            downNodes[now] = nSum + 1
            sumDist[now] = dSum
            return downNodes[now], sumDist[now]

        downDFS(-1, 0)

        def moveRoot(prev, now):
            if now != 0:
                sumDist[now] = sumDist[prev] - 2 * downNodes[now] + N
            for nei in nbors[now]:
                if nei == prev: continue
                moveRoot(now, nei)

        moveRoot(0, 0)

        return sumDist
    

    def sumOfDistancesInTree3(self, n, edges):
        # TLE, but very close
        tree = collections.defaultdict(list)
        for e in edges:
            tree[e[0]].append(e[1])
            tree[e[1]].append(e[0])
        ans = [0]*n
        # visit and calculates the sum distance in the whole tree
        @lru_cache(None)
        def dfs(i, pre):
            ret, nNode = 0, 1            
            for j in tree[i]:
                if j == pre: continue
                t = dfs(j, i) 
                nNode += t[1]
                ret += t[0] + t[1]
            return (ret, nNode)  
        for i in range(n):
            ans[i] = dfs(i, -1)[0]           
        return ans
    

    def sumOfDistancesInTree4(self, n, edges):
        # TLE, but very close with 73/74 testcases passed
        tree = collections.defaultdict(list)
        for e in edges:
            tree[e[0]].append(e[1])
            tree[e[1]].append(e[0])
        ans = [0]*n
        # visit and calculates the sum distance in the whole tree
        cache = {}
        def dfs(i, pre):
            ret, nNode = 0, 1            
            if (i, pre) in cache:
                return cache[(i, pre)] 
            for j in tree[i]:
                if j == pre: continue
                if (j, i) in cache:
                    t = cache[(j,i)]
                else:
                    t = dfs(j, i) 
                nNode += t[1]
                ret += t[0] + t[1]
            cache[(i, pre)] = (ret, nNode)      
            return cache[(i,pre)]
        for i in range(n):
            ans[i] = dfs(i, -1)[0]           
        return ans

    

if __name__ == "__main__": 
    print(Solution().sumOfDistancesInTree(N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]))
    print(Solution().sumOfDistancesInTree2(N = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]))
    print(Solution().sumOfDistancesInTree3(n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]))
    print(Solution().sumOfDistancesInTree4(n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]))