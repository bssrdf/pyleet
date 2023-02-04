'''
Given a triangle, find the minimum path sum from top to bottom. Each step you may 
move to adjacent numbers on the row below.

For example, given the following triangle

[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the 
total number of rows in the triangle.

'''

from functools import lru_cache

class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n  = len(triangle)
        dp = triangle[n-1][:]
        for layer in range(n-2,-1,-1):
            for i in range(layer+1):
                dp[i] = min(dp[i], dp[i+1]) + triangle[layer][i]
       
        return dp[0]


    def minimumTotalLRUCache(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        n  = len(triangle)
        @lru_cache(None)
        def dfs(i,j):
            if i == n: return 0            
            return triangle[i][j] + min(dfs(i+1,j), dfs(i+1,j+1))
        return dfs(0,0)


if __name__ == "__main__": 
    tri = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
      ] 
    print(Solution().minimumTotal(tri))