'''
-Hard-
*DFS*
*BFS*

There is an undirected tree with n nodes labeled from 0 to n - 1.

You are given a 0-indexed integer array nums of length n where nums[i] represents the value of the ith node. You are also given a 2D integer array edges of length n - 1 where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

You are allowed to delete some edges, splitting the tree into multiple connected components. Let the value of a component be the sum of all nums[i] for which node i is in the component.

Return the maximum number of edges you can delete, such that every connected component in the tree has the same value.

 

Example 1:


Input: nums = [6,2,2,2,6], edges = [[0,1],[1,2],[1,3],[3,4]] 
Output: 2 
Explanation: The above figure shows how we can delete the edges [0,1] and [3,4]. The created components are nodes [0], [1,2,3] and [4]. The sum of the values in each component equals 6. It can be proven that no better deletion exists, so the answer is 2.
Example 2:

Input: nums = [2], edges = []
Output: 0
Explanation: There are no edges to be deleted.
 

Constraints:

1 <= n <= 2 * 104
nums.length == n
1 <= nums[i] <= 50
edges.length == n - 1
edges[i].length == 2
0 <= edges[i][0], edges[i][1] <= n - 1
edges represents a valid tree.


'''

from typing import List
from collections import defaultdict, deque

class Solution:
    def componentValue(self, nums: List[int], edges: List[List[int]]) -> int:
        # Wrong 
        n = len(nums)
        t = sum(nums)
        mx = max(nums)
        degs = [0]*n
        for u,v in edges:
            degs[u] += 1
            degs[v] += 1
        edges.sort(key = lambda x: (min(degs[x[0]], degs[x[1]]), -max(nums[x[0]], nums[x[1]])))
        # for e in edges:
        print([max(nums[e[0]], nums[e[1]]) for e in edges])
        l, r = 0, n
        def valid(m):
            nc = n
            roots = [i for i in range(n)]
            ranks = [nums[i] for i in range(n)]
            nc = n
            def find(x):
                while x != roots[x]:
                    roots[x] = roots[roots[x]]
                    x = roots[x]
                return x
            def union(x, y):
                nonlocal nc
                fx, fy = find(x), find(y)
                if fx != fy:
                    nc -= 1
                    roots[fx] = fy
                    ranks[fy] += ranks[fx]
                    ranks[fx] = 0
            if t % (m+1) != 0: return False
            if mx > t //(m+1): return False
            for u,v in edges:
                if nc == m+1: break
                union(u, v)
            st = set()    
            for i in range(n):
                if ranks[i] > 0: st.add(ranks[i])
                if len(st) > 1:
                    return False
            return True
                
            
            
        while l < r:
            mid = l + (r-l)//2
            if valid(mid):
                l = mid + 1
            else:
                r = mid
        return l-1
    
    def componentValue2(self, nums: List[int], edges: List[List[int]]) -> int:
        # DFS 
        tree = defaultdict(set)
        for i,j in edges:
            tree[i].add(j)
            tree[j].add(i)

        def check(cur, prev, target, ncomp):
            # very simple yet subtle DFS traversal to detect whether the graph
            # can be decomposed to separate components with each sum equal to target
            val = nums[cur]
            for kid in tree[cur]-{prev}:
                val += check(kid, cur, target, ncomp)
            if val == target: # if the subcomponent with cur as root has sum equal to target
                ncomp[0] -= 1 # this subcomponent can be detached and form its own tree   
                return 0 # return 0 to parent since this subcompnent is detached.
            return val # otherwise, hopefully its parent can form such a subcomponent

        tot = sum(nums)
        for n in range(min(tot//max(nums), len(nums)), 0, -1):  # for simplicity, i do not use O(n^1/2) approach to find all factors here
            if tot % n == 0:
                ncomp = [n]
                check(0, -1, tot//n, ncomp)
                if ncomp[0] == 0: 
                    return n-1 # to form n components, need to remove n-1 edges
        
    def componentValue3(self, nums: List[int], edges: List[List[int]]) -> int:
        # BFS
        n = len(nums)
        tree = defaultdict(set)
        deg = [0]*n
        for u,v in edges:
            deg[u] += 1
            deg[v] += 1
            tree[u].add(v)
            tree[v].add(u)
        def check(target):
            que = deque()
            vals = list(nums)
            degs = deg[:]
            for i in range(n):
                if degs[i] == 1:
                    que.append(i)
            while que:
                u = que.popleft()
                if vals[u] > target: return False
                if degs[u] == 0: continue
                degs[u] = 0
                for v in tree[u]:                    
                    if vals[u] == target or degs[v] > 0:
                        degs[v] -= 1
                        vals[v] += vals[u] if vals[u] != target else 0
                        if degs[v] == 0:
                            return vals[v] == target
                        elif degs[v] == 1:
                            que.append(v)

                    # elif degs[v] > 0:
                    #     vals[v] += vals[u]
                    #     degs[v] -= 1
                    #     if degs[v] == 0:
                    #         return vals[v] == target
                    #     elif degs[v] == 1:
                    #         que.append(v)
            return True
            

        tot = sum(nums)
        for i in range(min(tot//max(nums), len(nums)), 0, -1):  # for simplicity, i do not use O(n^1/2) approach to find all factors here
            if tot % i == 0:
                if check(tot//i):             
                    return i-1 # to form n components, need to remove n-1 edges


if __name__ == "__main__":
    nums = [1,1,1,2,2,1,1,1,2,1,1,1,1,2,2,1,1,1,1,2]
    edges = [[12,14],[14,8],[8,4],[4,16],[16,1],[1,15],[15,5],[5,6],[6,9],[9,10],[10,17],[17,19],[19,13],[13,0],[0,2],[2,3],[3,18],[18,7],[7,11]]
    print(Solution().componentValue(nums, edges))
    print(Solution().componentValue2(nums, edges))
    print(Solution().componentValue3(nums, edges))