'''
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a val (int) and a list (List[Node]) 
of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}

'''

"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""

from collections import deque

class Solution(object):
    def cloneGraphDFS(self, node):

        if not node:
           return
        mark = {}
        clone = Node(node.val, [])
        mark[node] = clone

        def dfs(node):           
            for n in node.neighbors:
                if not n in mark:
                    mark[n] = Node(n.val, [])
                    dfs(n)
                mark[node].neighbors.append(mark[n])

        dfs(node)
        return clone






    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        q = deque()
        q.append(node)
        mark = {}
        clone = Node(node.val, [])
        mark[node] = clone
        while q:
            p = q.popleft()                     
            
            for n in p.neighbors:
                if not n in mark: 
                     mark[n] = Node(n.val, [])
                     q.append(n)                
                
                mark[p].neighbors.append(mark[n])
        return clone