'''
-Hard-
*DFS*

You are given an array pairs, where pairs[i] = [xi, yi], and:

There are no duplicates.
xi < yi
Let ways be the number of rooted trees that satisfy the following conditions:

The tree consists of nodes whose values appeared in pairs.
A pair [xi, yi] exists in pairs if and only if xi is an ancestor of yi or yi is 
an ancestor of xi.
Note: the tree does not have to be a binary tree.
Two ways are considered to be different if there is at least one node that has 
different parents in both ways.

Return:

0 if ways == 0
1 if ways == 1
2 if ways > 1
A rooted tree is a tree that has a single root node, and all edges are oriented to be outgoing from the root.

An ancestor of a node is any node on the path from the root to that node (excluding the node itself). The root has no ancestors.

 

Example 1:


Input: pairs = [[1,2],[2,3]]
Output: 1
Explanation: There is exactly one valid rooted tree, which is shown in the above figure.
Example 2:


Input: pairs = [[1,2],[2,3],[1,3]]
Output: 2
Explanation: There are multiple valid rooted trees. Three of them are shown in the above figures.
Example 3:

Input: pairs = [[1,2],[2,3],[2,4],[1,5]]
Output: 0
Explanation: There are no valid rooted trees.
 

Constraints:

1 <= pairs.length <= 10^5
1 <= xi < yi <= 500
The elements in pairs are unique.


'''
from typing import List
from collections import defaultdict

class Solution:
    def checkWays(self, pairs: List[List[int]]) -> int:
        g = defaultdict(set)
        P = pairs
        for u, v in P:
            g[u].add(v)
            g[v].add(u)

        def helper(nodes):
            d, m = defaultdict(list), len(nodes) - 1
            for node in nodes:
                d[len(g[node])].append(node)

            if len(d[m]) == 0: return 0 # we need to find node which is connected with all other nodes,
                                        # that is its degree should be equal to m = len(nodes) - 1.
                                        # If we did not found such a node, we can immedietly return 0: 
                                        # it is not possible to recunstruct a tree.
            root = d[m][0]
            
            for node in g[root]: g[node].remove(root)
            
            comps, seen, i = defaultdict(set), set(), 0
            def dfs(node, i):
                comps[i].add(node)
                seen.add(node)
                for neib in g[node]:
                    if neib not in seen: dfs(neib, i)
                        
            for node in nodes:
                if node != root and node not in seen:
                    dfs(node, i)
                    i += 1
                    
            cands = [helper(comps[i]) for i in comps]
            if 0 in cands: return 0
            if 2 in cands: return 2 # it means, that we found 2 or more solutions for some 
                                    # subproblems and 1 for others, like cands = [1, 2, 1, 1, 2]. 
                                    # In this case, we can be sure, that we have more than 2 solutions 
                                    # (in fact we have 1*2*1*1*2). 
            if len(d[m]) >= 2: return 2
            return 1
            
        return helper(set(g.keys()))

if __name__ == "__main__":
    print(Solution().checkWays([[1,2],[2,3]]))