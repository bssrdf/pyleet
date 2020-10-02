'''
Given a directed acyclic graph of N nodes. Find all possible paths from 
node 0 to node N-1, and return them in any order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  
graph[i] is a list of all nodes j for which the edge (i, j) exists.

Example:
Input: [[1,2],[3],[3],[]]
Output: [[0,1,3],[0,2,3]]
Explanation: The graph looks like this:
0--->1
|    |
v    v
2--->3
There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.


'''
from collections import defaultdict

class Solution(object):
    def allPathsSourceTarget(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[List[int]]
        """

        """
        Since the input graph is a DAG, there is no need for visited array 

        """


        
        N = len(graph)        
        ans = []
  
        def dfs(node, path):          
            
            #path.append(node)
            if node == N-1:
                ans.append(path[:])     
            #    path.pop()
                return            
            for n in graph[node]:     
                   dfs(n, path+[node])           
            #path.pop()                
        dfs(0, [])
        return ans




if __name__ == "__main__":
    print(Solution().allPathsSourceTarget([[1,2],[3],[3],[]]))
    print(Solution().allPathsSourceTarget([[4,3,1],[3,2,4],[3],[4],[]]))
