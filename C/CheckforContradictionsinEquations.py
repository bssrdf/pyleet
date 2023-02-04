'''
-Hard-
*DFS*

You are given a 2D array of strings equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] means that Ai / Bi = values[i].

Determine if there exists a contradiction in the equations. Return true if there is a contradiction, or false otherwise.

Note: Two floating point numbers are considered equal if their absolute difference is less than 10-5.

 

Example 1:

Input: equations = [["a","b"],["b","c"],["a","c"]], values = [3,0.5,1.5]
Output: false
Explanation:
The given equations are: a / b = 3, b / c = 0.5, a / c = 1.5
There are no contradictions in the equations. One possible assignment to satisfy all equations is:
a = 3, b = 1 and c = 2.
Example 2:

Input: equations = [["le","et"],["le","code"],["code","et"]], values = [2,5,0.5]
Output: true
Explanation:
The given equations are: le / et = 2, le / code = 5, code / et = 0.5
Based on the first two equations, we get code / et = 0.4.
Since the third equation is code / et = 0.5, we get a contradiction.
 

Constraints:

1 <= equations.length <= 500
equations[i].length == 2
1 <= Ai.length, Bi.length <= 5
Ai, Bi consist of lower case English letters.
equations.length == values.length
0.0 < values[i] <= 20.0

'''
from typing import List
from collections import defaultdict


class Solution:
    def checkContradictions(self, equations: List[List[str]], values: List[float]) -> bool:
        def check_equal(a, b):
            return abs(a-b) < 1e-5
        graph = defaultdict(set)
        for (a,b), r in zip(equations, values):
            if a == b:
                if check_equal(r, 1): continue
                else: return True
            else:
                graph[a].add((b, r))
                graph[b].add((a, 1/r))
        vals = {}
        def dfs(cur):
            for nb, ratio in graph[cur]:
                if nb in vals:
                    if not check_equal(vals[cur]/vals[nb], ratio):
                        return True
                else:
                    vals[nb] = vals[cur] / ratio
                    if dfs(nb): return True
            return False
        for u in graph:
            if u not in vals:
                vals[u] = 1 # seed value
            if dfs(u): return True
        return False

        



if __name__ == "__main__":
    print(Solution().checkContradictions(equations = [["a","b"],["b","c"],["a","c"]], values = [3,0.5,1.5]))
    print(Solution().checkContradictions(equations = [["le","et"],["le","code"],["code","et"]], values = [2,5,0.5]))
