from collections import defaultdict
from typing import List
class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        cnt = defaultdict(list)
        graph = defaultdict(list)

        count = [0]*n
        for u, v in roads:
            count[u] += 1
            count[v] += 1
            graph[u].append(v)
            graph[v].append(u)

        for i in range(n):
            cnt[count[i]].append(i)
        last = set()
        weight = [0]*n
        w = n
        for c in sorted(cnt.keys(), reverse=True):
            g1, g2 = set(), set()
            if len(cnt[c]) == 1:
                weight[cnt[c][0]] = w
                w -= 1
            elif last:
                for u in cnt[c]:
                   for v in graph[u]:
                       if v in last:
                           g1.add(u)
                           break
                g2 = set(cnt[c]) - g1
                for u in g1:
                    weight[u] = w
                    w -= 1
                for u in g2:
                    weight[u] = w
                    w -= 1
            else:
                for u in cnt[c]:
                    weight[u] = w
                    w -= 1
            last = set(cnt[c])
        ans = 0
        for i in range(n):
            ans += count[i]*weight[i]
        return ans
        
print(Solution().maximumImportance(n = 5, roads = [[0,1],[1,2],[2,3],[0,2],[1,3],[2,4]]))
print(Solution().maximumImportance(n = 5, roads = [[0,3],[2,4],[1,3]]))



                

                





            
         
        
        


