'''

-Hard-
*BFS*

There exists an undirected and unrooted tree with n nodes indexed from 0 to n - 1. You are given an integer n and a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree. You are also given an array coins of size n where coins[i] can be either 0 or 1, where 1 indicates the presence of a coin in the vertex i.

Initially, you choose to start at any vertex in the tree. Then, you can perform the following operations any number of times: 

Collect all the coins that are at a distance of at most 2 from the current vertex, or
Move to any adjacent vertex in the tree.
Find the minimum number of edges you need to go through to collect all the coins and go back to the initial vertex.

Note that if you pass an edge several times, you need to count it into the answer several times.

 

Example 1:


Input: coins = [1,0,0,0,0,1], edges = [[0,1],[1,2],[2,3],[3,4],[4,5]]
Output: 2
Explanation: Start at vertex 2, collect the coin at vertex 0, move to vertex 3, collect the coin at vertex 5 then move back to vertex 2.
Example 2:


Input: coins = [0,0,0,1,1,0,0,1], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[5,6],[5,7]]
Output: 2
Explanation: Start at vertex 0, collect the coins at vertices 4 and 3, move to vertex 2,  collect the coin at vertex 7, then move back to vertex 0.
 

Constraints:

n == coins.length
1 <= n <= 3 * 104
0 <= coins[i] <= 1
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
ai != bi
edges represents a valid tree.



'''

from typing import List
from collections import deque, defaultdict

class Solution:
    def collectTheCoins(self, coins: List[int], edges: List[List[int]]) -> int:
        # wrong
        n = len(coins)
        if n == 1: return 0
        G = defaultdict(list)
        que = deque()
        degs = [0]*n
        for u,v in edges:
            G[u].append(v)
            G[v].append(u)
            degs[u] += 1
            degs[v] += 1            
        for i in range(n):
            if degs[i] == 1: 
                if coins[i] == 1:            
                    que.append(i) 
                else: 
                    degs[i] = 0
                    for v in G[i]:
                        if degs[v] > 0:
                            degs[v] -= 1
                            if degs[v] == 1:
                                que.append(v) 
                # que.append(i) 
        # col = [0]*n
        print(degs)
        print(que)
        for _ in range(len(que)):
            u = que.popleft()
            degs[u] -= 1
            for v in G[u]:
                if degs[v] > 0:
                    degs[v] = 0
        # print(degs)
        cnt = sum([1 for d in degs if d > 0])                           
        return  (cnt - 1)*2 if cnt >= 1 else 0
    
    def collectTheCoins2(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        if n == 1: return 0
        G = defaultdict(list)
        que = deque()
        degs = [0]*n
        for u,v in edges:
            G[u].append(v)
            G[v].append(u)
            degs[u] += 1
            degs[v] += 1    
        for i in range(n):
            if degs[i] == 1 and coins[i] == 0: 
                que.append(i)        
        while que:
            u = que.popleft()
            degs[u] -= 1 # remove the node with coins = 0
            for v in G[u]:
                if degs[v] > 1:
                    degs[v] -= 1
                    if (not coins[v]) and degs[v] == 1:
                        que.append(v)
        for i in range(n):
            if degs[i] == 1: 
                que.append(i)  
        for _ in range(2):
            for _ in range(len(que)):
                u = que.popleft()
                degs[u] = 0
                for v in G[u]:
                    if degs[v] > 1:
                        degs[v] -= 1
                        if degs[v] == 1:
                            que.append(v)
        cnt = sum([1 for d in degs if d > 0])                           
        return  (cnt - 1)*2 if cnt >= 1 else 0
    
    def collectTheCoins3(self, coins: List[int], edges: List[List[int]]) -> int:
        n = len(coins)
        tree = [set() for _ in range(n)]
        for u, v in edges: 
            tree[u].add(v)
            tree[v].add(u)
        leaf = deque()
        for u in range(n):
            while len(tree[u]) == 1 and not coins[u]: 
                v = tree[u].pop()
                tree[v].remove(u)
                u = v 
            if len(tree[u]) == 1: leaf.append(u)
        for _ in range(2): 
            for _ in range(len(leaf)): 
                u = leaf.popleft()
                if tree[u]: 
                    v = tree[u].pop()
                    tree[v].remove(u)
                    if len(tree[v]) == 1: leaf.append(v)
        return sum(len(tree[u]) for u in range(n))

 
if __name__ == '__main__':
    print(Solution().collectTheCoins2(coins = [1,0,0,0,0,1], edges = [[0,1],[1,2],[2,3],[3,4],[4,5]]))
    print(Solution().collectTheCoins2(coins = [0,0,0,1,1,0,0,1], edges = [[0,1],[0,2],[1,3],[1,4],[2,5],[5,6],[5,7]]))
    print(Solution().collectTheCoins2(coins = [0], edges = []))
    coins = [1,0,0,1,1,0,0,0,0,1,0,0]
    edges = [[0,1],[1,2],[1,3],[2,4],[4,5],[5,6],[5,7],[4,8],[7,9],[7,10],[10,11]]
    print(Solution().collectTheCoins2(coins = coins, edges = edges))
    print(Solution().collectTheCoins2(coins = [0, 0], edges = [[0,1]]))
    coins = [1,1,1,0,0,0,0,0,1,0,0,1,1,0,1,1,0,0,1]
    edges = [[0,1],[1,2],[2,3],[1,4],[4,5],[5,6],[6,7],[3,8],[6,9],[7,10],[10,11],[10,12],[7,13],[12,14],[13,15],[14,16],[15,17],[10,18]]
    print(Solution().collectTheCoins2(coins = coins, edges = edges))
    print(Solution().collectTheCoins3(coins = coins, edges = edges))
