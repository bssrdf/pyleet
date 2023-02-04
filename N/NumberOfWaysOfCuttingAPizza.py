'''
-Hard-

Given a rectangular pizza represented as a rows x cols matrix containing the 
following characters: 'A' (an apple) and '.' (empty cell) and given the integer k. 
You have to cut the pizza into k pieces using k-1 cuts. 

For each cut you choose the direction: vertical or horizontal, then you choose 
a cut position at the cell boundary and cut the pizza into two pieces. If you 
cut the pizza vertically, give the left part of the pizza to a person. If you 
cut the pizza horizontally, give the upper part of the pizza to a person. Give 
the last piece of pizza to the last person.

Return the number of ways of cutting the pizza such that each piece contains at 
least one apple. Since the answer can be a huge number, return this modulo 
10^9 + 7.

 

Example 1:



Input: pizza = ["A..","AAA","..."], k = 3
Output: 3 
Explanation: The figure above shows the three ways to cut the pizza. Note 
that pieces must contain at least one apple.
Example 2:

Input: pizza = ["A..","AA.","..."], k = 3
Output: 1
Example 3:

Input: pizza = ["A..","A..","..."], k = 1
Output: 1
 

Constraints:

1 <= rows, cols <= 50
rows == pizza.length
cols == pizza[i].length
1 <= k <= 10
pizza consists of characters 'A' and '.' only.

'''

from functools import lru_cache
class Solution(object):

    def waysAC(self, pizza, K):
        m, n, MOD = len(pizza), len(pizza[0]), 10 ** 9 + 7
        preSum = [[0] * (n + 1) for _ in range(m + 1)]
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                preSum[r][c] = preSum[r][c + 1] + preSum[r + 1][c] - preSum[r + 1][c + 1] + (pizza[r][c] == 'A')

        @lru_cache(None)
        def dp(k, r, c):
            if preSum[r][c] == 0: return 0
            if k == 0: return 1
            ans = 0
            # cut horizontally
            for nr in range(r + 1, m):
                if preSum[r][c] - preSum[nr][c] > 0:
                    ans = (ans + dp(k - 1, nr, c)) % MOD
            # cut vertically                    
            for nc in range(c + 1, n):
                if preSum[r][c] - preSum[r][nc] > 0:
                    ans = (ans + dp(k - 1, r, nc)) % MOD
            return ans

        return dp(K - 1, 0, 0)

    def ways(self, pizza, k):
        """
        :type pizza: List[str]
        :type k: int
        :rtype: int
        """
        m = len(pizza)
        n = len(pizza[0])
        MOD = 10 ** 9 + 7        
        apples = [[0 for _ in range(n+1)] for _ in range(m+1)]        
        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                apples[r][c] = apples[r][c + 1] + apples[r + 1][c] - \
                               apples[r + 1][c + 1] + (pizza[r][c] == 'A')               
        for i in range(m+1):
            print(apples[i])                        
        @lru_cache(None)    
        def helper(row, col, cuts):
            if apples[row][col] == 0: return 0
            if cuts == 0: return 1                        
            res = 0
            for i in range(row+1, m):    
                # check if there are apples on row            
                if apples[row][col]-apples[i][col] > 0:
                    res = (res + helper(i, col, cuts-1)) % MOD
            for j in range(col+1, n):               
                # check if there are apples on col            
                if apples[row][col]-apples[row][j] > 0:                 
                    res = (res +helper(row, j, cuts-1) ) % MOD
            return res  
        return helper(0, 0, k-1)                          


if __name__ == "__main__":
    print(Solution().ways(["A..","AAA","..."], 3))
    print(Solution().ways(["..A","AAA","..."], 3))
    print(Solution().waysAC(["A..","AAA","..."], 3))
    print(Solution().waysAC(["..A","AAA","..."], 3))
    #print(Solution().ways([".A..A","A.A..","A.AA.","AAAA.","A.AA."], 5))
    #print(Solution().waysAC([".A..A","A.A..","A.AA.","AAAA.","A.AA."], 5))