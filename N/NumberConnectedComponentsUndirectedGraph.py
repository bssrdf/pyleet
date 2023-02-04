# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 19:35:52 2017

Given n nodes labeled from 0 to n - 1 and a list of undirected edges (each
 edge is a pair of nodes), write a function to find the number of connected 
 components in an undirected graph.

Example 1:

     0          3

     |          |

     1 --- 2    4

Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:

     0           4

     |           |

     1 --- 2 --- 3

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.

 Note:

You can assume that no duplicate edges will appear in edges. Since all edges 
are undirected, [0, 1] is the same as [1, 0] and thus will not appear together
 in edges.
@author: merli

"""

class Solution(object):
    def countComponentsDFS(self, n, edges):
        def dfs(n, g, visited):
            if visited[n]:
                return
            visited[n] = 1
            for x in g[n]:
                dfs(x, g, visited)
                
        visited = [0] * n
        g = {x:[] for x in xrange(n)}
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            
        ret = 0
        for i in xrange(n):
            if not visited[i]:
                dfs(i, g, visited)
                ret += 1
                
        return ret    
        
    def countComponentsBFS(self, n, edges):
        g = {x:[] for x in xrange(n)}
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
            
        ret = 0
        for i in xrange(n):
            queue = [i]
            ret += 1 if i in g else 0
            for j in queue:
                if j in g:
                    queue += g[j]
                    del g[j]

        return ret
    
    def numberOfConnComps(self, n, edges):
        res = n
        roots = range(n)
        
        for e in edges:
            x = self.find(roots, e[0])
            y = self.find(roots, e[1])
            if x != y:            
                res -= 1
                roots[x] = y  # unionize the two subsets that contain two vertices             
        #print roots
        return res
        
    
        
    def find(self, roots, i):
        # this while loop is called "path compression";
        # it "recursively" decends to the root node represented by the
        # node whose roots value is untouched 'i'
        while roots[i] != i:
            i = roots[i]
        return i
        
if __name__ == "__main__":
    #edges = [[0, 1], [1, 2], [3, 4]]
    edges = [[1, 0], [1, 2], [3, 4]]
    #edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    print Solution().numberOfConnComps(5, edges)
    print Solution().countComponentsDFS(5, edges)
    print Solution().countComponentsBFS(5, edges)