'''




'''

from typing import List
from collections import defaultdict, deque
class Solution:
    def magnificentSets2(self, n: int, edges: List[List[int]]) -> int:
        G = defaultdict(set)
        dist = [[10**4+1]*(n+1) for _ in range(n+1)]
        for u,v in edges:
            G[u].add(v)
            G[v].add(u)
        color = [0]*(n+1)
        def dfs(cur, col, nodes):
            if color[cur] != 0: 
                return color[cur] == col
            color[cur] = col
            nodes.append(cur)
            for i in G[cur]:
                if not dfs(i, -1*col, nodes):
                    return False
            return True
        def bfs(src):
            dist[src][src] = 1
            que = deque([src])
            while que:
                u = que.popleft()
                for v in G[u]:
                    if dist[src][v] > dist[src][u]+1:
                        dist[src][v] = dist[src][u]+1
                        que.append(v)
        for i in range(1, n+1):
            bfs(i)
        ans = 0
        for i in range(1, n+1):
            if color[i] == 0:
                kara = []
                mxdist = 0
                if not dfs(i, 1, kara):
                    return -1
                for u in kara:
                    for v in kara:
                        mxdist = max(mxdist, dist[u][v])
                ans += mxdist
        
        return ans
    
    def magnificentSets(self, n: int, edges: List[List[int]]) -> int:
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        components = []
        seen = set()
        for i in range(1, n + 1):
            if i in seen:
                continue
            queue = deque([i])
            visited = set([i])
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    for neighbor in graph[node]:
                        if neighbor in visited:
                            continue
                        visited.add(neighbor)
                        queue.append(neighbor)
            components.append(visited)
            seen = seen.union(visited)
        longest = [-1] * len(components)        
        for k in range(len(components)):
            for i in components[k]:
                longest[k] = max(longest[k], self.bfs(graph, i))
        if min(longest) < 0:
            return -1
        return sum(longest)
            
    def bfs(self, graph, i):
        queue = deque([i])
        seen = set([i])
        seenLevel = set()
        ans = 0
        while queue:
            ans += 1
            nextLevel = set()
            for _ in range(len(queue)):
                node = queue.popleft()
                for neighbor in graph[node]:
                    if neighbor in seenLevel:
                        return -1
                    if neighbor in seen:
                        continue
                    seen.add(neighbor)
                    nextLevel.add(neighbor)
                    queue.append(neighbor)
            seenLevel = nextLevel
        return ans


print(Solution().magnificentSets(n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))
print(Solution().magnificentSets(n = 6, edges = [[1,2],[1,4],[2,5],[5,4],[2,6],[2,3],[3,4],[4,6]]))
print(Solution().magnificentSets(n = 3, edges = [[1,2],[2,3],[3,1]]))


print(Solution().magnificentSets2(n = 6, edges = [[1,2],[1,4],[1,5],[2,6],[2,3],[4,6]]))
print(Solution().magnificentSets2(n = 6, edges = [[1,2],[1,4],[2,5],[5,4],[2,6],[2,3],[3,4],[4,6]]))
print(Solution().magnificentSets2(n = 3, edges = [[1,2],[2,3],[3,1]]))
        