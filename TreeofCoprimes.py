'''
-Hard-

There is a tree (i.e., a connected, undirected graph that has no cycles) consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges. Each node has a value associated with it, and the root of the tree is node 0.

To represent this tree, you are given an integer array nums and a 2D array edges. Each nums[i] represents the ith node's value, and each edges[j] = [uj, vj] represents an edge between nodes uj and vj in the tree.

Two values x and y are coprime if gcd(x, y) == 1 where gcd(x, y) is the greatest common divisor of x and y.

An ancestor of a node i is any other node on the shortest path from node i to the root. A node is not considered an ancestor of itself.

Return an array ans of size n, where ans[i] is the closest ancestor to node i such that nums[i] and nums[ans[i]] are coprime, or -1 if there is no such ancestor.

 

Example 1:



Input: nums = [2,3,3,2], edges = [[0,1],[1,2],[1,3]]
Output: [-1,0,0,1]
Explanation: In the above figure, each node's value is in parentheses.
- Node 0 has no coprime ancestors.
- Node 1 has only one ancestor, node 0. Their values are coprime (gcd(2,3) == 1).
- Node 2 has two ancestors, nodes 1 and 0. Node 1's value is not coprime (gcd(3,3) == 3), but node 0's
  value is (gcd(2,3) == 1), so node 0 is the closest valid ancestor.
- Node 3 has two ancestors, nodes 1 and 0. It is coprime with node 1 (gcd(3,2) == 1), so node 1 is its
  closest valid ancestor.
Example 2:



Input: nums = [5,6,10,2,3,6,15], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]
Output: [-1,0,-1,0,0,0,-1]
 

Constraints:

nums.length == n
1 <= nums[i] <= 50
1 <= n <= 105
edges.length == n - 1
edges[j].length == 2
0 <= uj, vj < n
uj != vj


'''

from typing import List

from collections import defaultdict
class Solution:
    def getCoprimes(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        n = len(nums)
        def gcd(a, b):
            while b != 0:
                r = a % b
                a, b  = b, r
            return a
        gcds = [set() for _ in range(51)]
        for i in range(1, 51):
            for j in range(1, 51):
                if gcd(i, j) == 1:            
                    gcds[i].add(j)
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        ans = [-1]*n        
        visited = [False]*n
        def dfs(u, dic, d):
            # if not dic:
            #     ans[u] = -1
            visited[u] = True
            arr = [(d,k,v)  for k, (v, d) in dic.items()]
            arr.sort(reverse = True)
            # print(u, arr, gcds[nums[u]], ans[u])
            # print(u, arr, dic, ans[u])
            for _, k, v in arr:
                if k in gcds[nums[u]]:
                   ans[u] = v
                   break
            # print(ans[u])
            if nums[u] in dic:
                pre, depth = dic[nums[u]]  
            else: pre, depth = -1,-1 
            # print('X', pre, depth, u, dic)
            # if pre != -1:
            #     dic.pop(nums[u])
            dic[nums[u]] = (u, d+1)
            # print('A', pre, u, dic)
            for v in graph[u]:
                if not visited[v]:
                    dfs(v, dic, d+1)
            if pre == -1:
                dic.pop(nums[u])
            else:
                dic[nums[u]] = (pre, depth) 
            # print('B',pre, u, dic)
        dfs(0, {}, 0)
        return ans

    def getCoprimes2(self, nums: List[int], edges: List[List[int]]) -> List[int]:
        n = len(nums)
        def gcd(a, b):
            while b != 0:
                r = a % b
                a, b  = b, r
            return a
        gcds = [set() for _ in range(51)]
        for i in range(1, 51):
            for j in range(1, 51):
                if gcd(i, j) == 1:            
                    gcds[i].add(j)
        graph = defaultdict(list)
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        ans = [-1]*n        
        visited = [False]*n
        def dfs(u, dic, d):
            visited[u] = True
            maxDep = -1
            for k, (v, dep) in dic.items():
                if k in gcds[nums[u]]:
                    if dep > maxDep: 
                       maxDep = dep
                       ans[u] = v            
            if nums[u] in dic:
                pre, depth = dic[nums[u]]  
            else: pre, depth = -1,-1 
            dic[nums[u]] = (u, d+1)
            for v in graph[u]:
                if not visited[v]:
                    dfs(v, dic, d+1)
            if pre == -1:
                dic.pop(nums[u])
            else:
                dic[nums[u]] = (pre, depth) 
        dfs(0, {}, 0)
        return ans


            
            
            






        




if __name__ == "__main__":
    print(Solution().getCoprimes(nums = [2,3,3,2], edges = [[0,1],[1,2],[1,3]]))
    print(Solution().getCoprimes(nums = [5,6,10,2,3,6,15], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]))
    print(Solution().getCoprimes2(nums = [2,3,3,2], edges = [[0,1],[1,2],[1,3]]))
    print(Solution().getCoprimes2(nums = [5,6,10,2,3,6,15], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[2,6]]))
    nums = [9,16,30,23,33,35,9,47,39,46,16,38,5,49,21,44,17,1,6,37,49,15,23,46,38,9,27,3,24,1,14,17,12,23,43,38,12,4,8,17,11,18,26,22,49,14,9]
    edges =  [[17,0],[30,17],[41,30],[10,30],[13,10],[7,13],[6,7],[45,10],[2,10],[14,2],[40,14],[28,40],[29,40],[8,29],[15,29],[26,15],[23,40],[19,23],[34,19],[18,23],[42,18],[5,42],[32,5],[16,32],[35,14],[25,35],[43,25],[3,43],[36,25],[38,36],[27,38],[24,36],[31,24],[11,31],[39,24],[12,39],[20,12],[22,12],[21,39],[1,21],[33,1],[37,1],[44,37],[9,44],[46,2],[4,46]]
    print(Solution().getCoprimes(nums, edges))
    print(Solution().getCoprimes2(nums, edges))