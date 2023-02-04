'''
-Medium-

*DFS*
*Backtracking*

Given two integers n and k, return all possible combinations of k numbers out 
of 1 ... n.

You may return the answer in any order.

 

Example 1:

Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
Example 2:

Input: n = 1, k = 1
Output: [[1]]
 

Constraints:

1 <= n <= 20
1 <= k <= n

'''

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        res = []
        def dfs(start, depth, cur):
            if depth == k:
                res.append(cur[:])
                return
            for i in range(start, n+1):
                cur.append(i)
                dfs(i+1, depth+1, cur)
                cur.pop() 
        dfs(1, 0, [])
        return res

if __name__ == "__main__":
    print(Solution().combine(4,2))