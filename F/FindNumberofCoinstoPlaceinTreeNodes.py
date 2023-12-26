'''

-Hard-
*DFS*

You are given an undirected tree with n nodes labeled from 0 to n - 1, and rooted at node 0. You are given a 2D integer array edges of length n - 1, where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the tree.

You are also given a 0-indexed integer array cost of length n, where cost[i] is the cost assigned to the ith node.

You need to place some coins on every node of the tree. The number of coins to be placed at node i can be calculated as:

If size of the subtree of node i is less than 3, place 1 coin.
Otherwise, place an amount of coins equal to the maximum product of cost values assigned to 3 distinct nodes in the subtree of node i. If this product is negative, place 0 coins.
Return an array coin of size n such that coin[i] is the number of coins placed at node i.

 

Example 1:


Input: edges = [[0,1],[0,2],[0,3],[0,4],[0,5]], cost = [1,2,3,4,5,6]
Output: [120,1,1,1,1,1]
Explanation: For node 0 place 6 * 5 * 4 = 120 coins. All other nodes are leaves with subtree of size 1, place 1 coin on each of them.
Example 2:


Input: edges = [[0,1],[0,2],[1,3],[1,4],[1,5],[2,6],[2,7],[2,8]], cost = [1,4,2,3,5,7,8,-4,2]
Output: [280,140,32,1,1,1,1,1,1]
Explanation: The coins placed on each node are:
- Place 8 * 7 * 5 = 280 coins on node 0.
- Place 7 * 5 * 4 = 140 coins on node 1.
- Place 8 * 2 * 2 = 32 coins on node 2.
- All other nodes are leaves with subtree of size 1, place 1 coin on each of them.
Example 3:


Input: edges = [[0,1],[0,2]], cost = [1,2,-2]
Output: [0,1,1]
Explanation: Node 1 and 2 are leaves with subtree of size 1, place 1 coin on each of them. For node 0 the only possible product of cost is 2 * 1 * -2 = -4. Hence place 0 coins on node 0.
 

Constraints:

2 <= n <= 2 * 104
edges.length == n - 1
edges[i].length == 2
0 <= ai, bi < n
cost.length == n
1 <= |cost[i]| <= 104
The input is generated such that edges represents a valid tree.



'''

from typing import List

class Solution:
    def placedCoins(self, edges: List[List[int]], cost: List[int]) -> List[int]:
        n = len(cost)
        G = [[] for _ in range(n)]
        for u,v in edges:
            G[u].append(v)
            G[v].append(u)
        ans = [0]*n 
        def dfs(u, par):
            cnt, p, q  = 0, [cost[u]] if cost[u] > 0 else [] , [cost[u]] if cost[u] < 0 else [] 
            for v in G[u]:
                if v == par: continue
                c, pos, neg = dfs(v, u)                
                p += pos
                p.sort(reverse=True)                    
                while len(p) > 3:
                    p.pop()
                q += neg
                q.sort()
                while len(q) > 3:
                    q.pop()
                cnt += c
            if cnt <= 1:
                ans[u] = 1 
            else:
                t = 0
                if len(p) == 3:
                    t = max(t, p[0]*p[1]*p[2])
                if len(p) >= 1 and len(q) >= 2:
                    t = max(t, p[0]*q[0]*q[1])
                ans[u] = t    
            return (cnt+1, p, q)        
        dfs(0, -1)
        return ans
        

if __name__ == "__main__":
    print(Solution().placedCoins(edges = [[0,1],[0,2],[0,3],[0,4],[0,5]], cost = [1,2,3,4,5,6]))
    print(Solution().placedCoins(edges = [[0,1],[0,2],[1,3],[1,4],[1,5],[2,6],[2,7],[2,8]], cost = [1,4,2,3,5,7,8,-4,2]))
    print(Solution().placedCoins(edges = [[0,1],[0,2]], cost = [1,2,-2]))
    edges = [[0,1],[0,2],[0,3],[0,4],[0,5],[0,6],[0,7],[0,8],[0,9],[0,10],[0,11],[0,12],[0,13],[0,14],[0,15],[0,16],[0,17],[0,18],[0,19],[0,20],[0,21],[0,22],[0,23],[0,24],[0,25],[0,26],[0,27],[0,28],[0,29],[0,30],[0,31],[0,32],[0,33],[0,34],[0,35],[0,36],[0,37],[0,38],[0,39],[0,40],[0,41],[0,42],[0,43],[0,44],[0,45],[0,46],[0,47],[0,48],[0,49],[0,50],[0,51],[0,52],[0,53],[0,54],[0,55],[0,56],[0,57],[0,58],[0,59],[0,60],[0,61],[0,62],[0,63],[0,64],[0,65],[0,66],[0,67],[0,68],[0,69],[0,70],[0,71],[0,72],[0,73],[0,74],[0,75],[0,76],[0,77],[0,78],[0,79],[0,80],[0,81],[0,82],[0,83],[0,84],[0,85],[0,86],[0,87],[0,88],[0,89],[0,90],[0,91],[0,92],[0,93],[0,94],[0,95],[0,96],[0,97],[0,98],[0,99]]
    cost = [-5959,602,-6457,7055,-1462,6347,7226,-8422,-6088,2997,-7909,6433,5217,3294,-3792,7463,8538,-3811,5009,151,5659,4458,-1702,-1877,2799,9861,-9668,-1765,2181,-8128,7046,9529,6202,-8026,6464,1345,121,1922,7274,-1227,-9914,3025,1046,-9368,-7368,6205,-6342,8091,-6732,-7620,3276,5136,6871,4823,-1885,-4005,-3974,-2725,-3845,-8508,7201,-9566,-7236,-3386,4021,6793,-8759,5066,5879,-5171,1011,1242,8536,-8405,-9646,-214,2251,-9934,-8820,6206,1006,1318,-9712,7230,5608,-4601,9185,346,3056,8913,-2454,-3445,-4295,4802,-8852,-6121,-4538,-5580,-9246,-6462]
    print(Solution().placedCoins(edges = edges, cost = cost))
