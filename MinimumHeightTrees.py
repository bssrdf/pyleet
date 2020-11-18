'''
-Medium-

A tree is an undirected graph in which any two vertices are connected by 
exactly one path. In other words, any connected graph without simple cycles 
is a tree.

Given a tree of n nodes labelled from 0 to n - 1, and an array of n - 1 
edges where edges[i] = [ai, bi] indicates that there is an undirected edge 
between the two nodes ai and bi in the tree, you can choose any node of the 
tree as the root. When you select a node x as the root, the result tree 
has height h. Among all possible rooted trees, those with minimum height 
(i.e. min(h))  are called minimum height trees (MHTs).

Return a list of all MHTs' root labels. You can return the answer in any order.

The height of a rooted tree is the number of edges on the longest downward 
path between the root and a leaf.

 

Example 1:


Input: n = 4, edges = [[1,0],[1,2],[1,3]]
Output: [1]
Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
Example 2:


Input: n = 6, edges = [[3,0],[3,1],[3,2],[3,4],[5,4]]
Output: [3,4]
Example 3:

Input: n = 1, edges = []
Output: [0]
Example 4:

Input: n = 2, edges = [[0,1]]
Output: [0,1]
 

Constraints:

1 <= n <= 2 * 10^4
edges.length == n - 1
0 <= ai, bi < n
ai != bi
All the pairs (ai, bi) are distinct.
The given input is guaranteed to be a tree and there will be no repeated edges.


'''
from collections import defaultdict
from collections import deque

class Solution(object):

    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]        
        """
        if n == 1: return [0]
        graph = [set() for _ in range(n)]
        nodes = []
        def build_graph(edges):
            for e in edges:
            # two directions
                graph[e[0]].add(e[1])
                graph[e[1]].add(e[0])
        def init_nodes():
            for i in range(n):
                if len(graph[i])==1:
                    nodes.append(i)
        # BFS
        build_graph(edges)
        init_nodes()
        while True:
            next_nodes = []
            for node in nodes:
                children = graph[node]
                for child in children:                    
                    graph[child].remove(node)
                    if len(graph[child])==1:                       
                       next_nodes.append(child)                                   
            if len(next_nodes)==0:    
                return nodes
            nodes = next_nodes

    def findMinHeightTreeTLE(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]        
        """
        '''
        the naive approach of doing BFS for every node will result in TLE.

        '''
        if n == 1: return [0]
        res = []
        mh = n+1
        g = defaultdict(list)
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        for i in range(n):                
            visited = [False] * n
            visited[i] = True
            q = deque([i])
            cnt = 0
            while q:                
                for j in range(len(q)):
                    u = q.popleft()
                    for v in g[u]:
                        if not visited[v]:
                            visited[v] = True
                            q.append(v)
                cnt += 1
                if cnt-1 > mh: break
            if mh > cnt-1:
                mh = cnt-1
                res = [i] 
            elif mh == cnt-1:
                res.append(i)            
                
        return res
             

if __name__ == "__main__":
    print(Solution().findMinHeightTrees(4, [[1,0],[1,2],[1,3]]))
    print(Solution().findMinHeightTrees(6, [[3,0],[3,1],[3,2],[3,4],[5,4]]))
    print(Solution().findMinHeightTrees(2, [[1,0]]))
    print(Solution().findMinHeightTrees(3, [[0,1], [0,2]]))

