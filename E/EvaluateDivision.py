'''

You are given equations in the format A / B = k, where A and B are 
variables represented as strings, and k is a real number 
(floating-point number). Given some queries, return the answers. 
If the answer does not exist, return -1.0.

The input is always valid. You may assume that evaluating the queries 
will result in no division by zero and there is no contradiction.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], 
queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = 
[1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],
["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]
 

Constraints:

1 <= equations.length <= 20
equations[i].length == 2
1 <= equations[i][0], equations[i][1] <= 5
values.length == equations.length
0.0 < values[i] <= 20.0
1 <= queries.length <= 20
queries[i].length == 2
1 <= queries[i][0], queries[i][1] <= 5
equations[i][0], equations[i][1], queries[i][0], queries[i][1] consist of lower case English letters and digits.

'''

from collections import defaultdict
import itertools

class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        g = defaultdict(set)
        for e,v in zip(equations, values):
            g[e[0]].add((e[1], v))
            g[e[1]].add((e[0], 1.0/v))
        ans = []
        def find(start, target):
            def dfs(n, mul, pathset):
                if n == target:
                    return True
                pathset.add(n)
                for (node, val) in g[n]: 
                    if node not in pathset:                   
                        mul[0] *= val                 
                        if dfs(node, mul, pathset):
                            return True
                        mul[0] /= val
                pathset.remove(n)
                return False
            res = [1.0]            
            return res[0] if dfs(start, res, set()) else -1.0
               
        for q in queries:            
            if q[0] in g:
                if q[0] == q[1]:
                    ans.append(1.0)
                else:
                    ans.append(find(q[0],q[1]))
            else:
                ans.append(-1.0)           

        return ans

    def calcEquationFloydWarshall(self, equations, values, queries):    
        quot = defaultdict(dict)
        for (num, den), val in zip(equations, values):
            quot[num][num] = quot[den][den] = 1.0
            quot[num][den] = val
            quot[den][num] = 1 / val
        for k, i, j in itertools.permutations(quot, 3):
            if k in quot[i] and j in quot[k]:
               quot[i][j] = quot[i][k] * quot[k][j]
        return [quot[num].get(den, -1.0) for num, den in queries]
 

if __name__ == "__main__":
    equations = [["a","b"],["b","c"]]
    values = [2.0,3.0]
    queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
    print(Solution().calcEquation(equations, values, queries))
