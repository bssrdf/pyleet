'''
-Hard-
*Union Find*
*Greedy*
*Minimum Spanning Tree*
*Kruskal's Algorithm*

There are n houses in a village. We want to supply water for all the houses by building 
wells and laying pipes.

For each house i, we can either build a well inside it directly with cost wells[i - 1] 
(note the -1 due to 0-indexing), or pipe in water from another well to it. The costs 
to lay pipes between houses are given by the array pipes, where each 
pipes[j] = [house1j, house2j, costj] represents the cost to connect house1j and house2j 
together using a pipe. Connections are bidirectional.

Return the minimum total cost to supply water to all houses.

 

Example 1:



Input: n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]
Output: 3
Explanation: 
The image shows the costs of connecting houses using pipes.
The best strategy is to build a well in the first house with cost 1 and connect the other houses to it with cost 2 so the total cost is 3.
 

Constraints:

1 <= n <= 10^4
wells.length == n
0 <= wells[i] <= 10^5
1 <= pipes.length <= 10^4
pipes[j].length == 3
1 <= house1j, house2j <= n
0 <= costj <= 10^5
house1j != house2j


Hints
What if we model this problem as a graph problem?
A house is a node and a pipe is a weighted edge.
How to represent building wells in the graph model?
Add a virtual node, connect it to houses with edges weighted by the costs to build wells in these houses.
The problem is now reduced to a Minimum Spanning Tree problem.

'''

class Solution(object):
    def minCostToSupplyWater(self, n,  wells, pipes):
        roots = [i for i in range(n+1)]# 并查集数组
        def find(i): # 查找根节点
            while roots[i] != i: 
                roots[i] = roots[roots[i]]
                i = roots[i]
            return i
        # 存储所有的边
        allPipes = []
        # 将每户与水源的连线加入allPipes数组
        for i in range(n):
            allPipes.append([0, i+1, wells[i]])
        # 将每户间的连线加入allPipes数组
        allPipes += pipes        
        # 按照cost升序排序
        allPipes.sort(key=lambda x: x[2])
        res = 0  # 返回结果
        for p in allPipes:
            r0 = find(p[0]) # 连线上第一个节点的根节点
            r1 = find(p[1]) # 连线上第二个节点的根节点
            if r0 == r1: continue # 根节点相同，不需此连线
            # 以下均为不在同一根节点下的情况

            # 某一个点的根节点为水源
            if r0 == 0 or r1 == 0:
                # 将另一节点也加到根节点下（Union合并操作）
                roots[r0] = 0
                roots[r1] = 0
            else:
                # 将一个根节点加入到另一个根节点下（Union合并操作）
                roots[r1] = r0
            res += p[2]  # 将当前连线cost加入返回结果
        return res
    
if __name__ == "__main__":
    print(Solution().minCostToSupplyWater(n = 3, wells = [1,2,2], pipes = [[1,2,1],[2,3,1]]))