
from typing import List
from collections import defaultdict, deque, Counter

class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        n = len(vals)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        ans = 0 
        def bfs(target):
            ret = 0
            que = deque()
            visited = [False]*n
            srcs = [0]*n
            for i in range(n):
                if vals[i] == target:
                    que.append(i)
                    visited[i] = True
                    srcs[i] = 1
            while que:
                u = que.popleft()                
                if target == 3:
                    print('X',target, u, ret, visited)
                for v in graph[u]:
                    if not visited and vals[v] <= target:
                        que.append(v)
                        if visited[v] == 0:
                            
                            visited[v] = visited[u]
                        else:
                            ret += visited[v]
                            visited[v] += visited[u]
            print(target, 'ret=', ret)
            return ret
        counter = Counter(vals)              
        for c in counter:
            if counter[c] > 1: ans += bfs(c)
            ans += counter[c]
            print(c, counter[c], ans)
        return ans
    
    def numberOfGoodPaths2(self, vals: List[int], edges: List[List[int]]) -> int:
        # // key concept
        # // gradually build up the graph from the nodes with small value
        # // so that whenever nodes with larger value are connected with other existing nodes (with smaller values)
        # // it ensures that any connection of the nodes (i.e., path) with larger value would be valid!
        res = n = len(vals)
        f = list(range(n))
        count = [Counter({vals[i]: 1}) for i in range(n)]
        print(count)
        edges = sorted([max(vals[i], vals[j]),i,j] for i,j in edges)

        def find(x):
            if f[x] != x:
                f[x] = find(f[x])
            return f[x]

        for v,i,j in edges:
            fi, fj = find(i), find(j)
            cj, ci = count[fi][v], count[fj][v]
            res += ci * cj
            print(v, i, j, fi, fj, ci, cj, count)
            f[fj] = fi
            count[fi] = Counter({v: ci + cj})
        return res


          

if __name__ == "__main__":
    # print(Solution().numberOfGoodPaths(vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]))
    print(Solution().numberOfGoodPaths2(vals = [1,3,2,1,3], edges = [[0,1],[0,2],[2,3],[2,4]]))
        