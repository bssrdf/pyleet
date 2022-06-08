'''
-Medium-
*DP*
*Knapsack Problem*

You are given two 0-indexed integer arrays of the same length present and future where present[i] is the current price of the ith stock and future[i] is the price of the ith stock a year in the future. You may buy each stock at most once. You are also given an integer budget representing the amount of money you currently have.

Return the maximum amount of profit you can make.

 

Example 1:

Input: present = [5,4,6,2,3], future = [8,5,4,3,5], budget = 10
Output: 6
Explanation: One possible way to maximize your profit is to:
Buy the 0th, 3rd, and 4th stocks for a total of 5 + 2 + 3 = 10.
Next year, sell all three stocks for a total of 8 + 3 + 5 = 16.
The profit you made is 16 - 10 = 6.
It can be shown that the maximum profit you can make is 6.
Example 2:

Input: present = [2,2,5], future = [3,4,10], budget = 6
Output: 5
Explanation: The only possible way to maximize your profit is to:
Buy the 2nd stock, and make a profit of 10 - 5 = 5.
It can be shown that the maximum profit you can make is 5.
Example 3:

Input: present = [3,3,12], future = [0,3,15], budget = 10
Output: 0
Explanation: One possible way to maximize your profit is to:
Buy the 1st stock, and make a profit of 3 - 3 = 0.
It can be shown that the maximum profit you can make is 0.
 

Constraints:

n == present.length == future.length
1 <= n <= 1000
0 <= present[i], future[i] <= 100
0 <= budget <= 1000

'''
from functools import lru_cache

class Solution(object):
    def maxProfits(self, present, future, budget):
        P, F, B = present, future, budget
        n = len(P)
        # pos = [(v,i) for i,v in enumerate(P)]
        # pos.sort(key = lambda x: x[0])
        # P1, F1 = [], []
        # for v,i in pos:
        #     P1.append(P[i])
        #     F1.append(F[i])        
        # P, F = P1, F1
        dp = [[0]*(B+1) for _ in range (n+1)]
        for i in range(1, n+1):
            for j in range(1, B+1):
                if j - P[i-1] >= 0:                 
                    dp[i][j] = max(dp[i-1][j-P[i-1]]+(F[i-1]-P[i-1]), dp[i-1][j])
                else:
                    dp[i][j] = dp[i-1][j]
        return max(dp[n])
    
    def maxProfits2(self, present, future, budget):
        # stack overflow
        P, F, B = present, future, budget
        pos = [(v,i) for i,v in enumerate(P)]
        pos.sort(key = lambda x: x[0])
        P1, F1 = [], []
        for v,i in pos:
            P1.append(P[i])
            F1.append(F[i])        
        P, F = P1, F1
        n = len(P)
        @lru_cache(None)
        def dp(i, m):
            if i == n: return 0
            if P[i] > m: return 0
            if m <= 0: return 0
            ans = dp(i+1, m) 
            x = F[i]-P[i]
            ans = max(ans, x + dp(i+1, m-P[i]))            
            return ans 
        return dp(0, B)

    def maxProfits3(self, present, future, budget):
        arr = [(a, b - a) for a, b in zip(present, future) if b > a]
        dp = [0] * (budget + 1)
        for v, w in arr:
            for j in range(budget, v - 1, -1):
                dp[j] = max(dp[j], dp[j - v] + w)
        return dp[-1]






if __name__ == "__main__":   
    from random import randint
    print(Solution().maxProfits(present = [5,4,6,2,3], future = [8,5,4,3,5], budget = 10))
    print(Solution().maxProfits(present = [2,2,5], future = [3,4,10], budget = 6))
    print(Solution().maxProfits(present = [3,3,12], future = [0,3,15], budget = 10))
    print(Solution().maxProfits(present = [3, 6, 10, 7, 18, 25, 3, 12], 
                                 future =  [0, 10, 6, 5, 27, 14, 13, 15], budget = 20))
    
    print(Solution().maxProfits2(present = [5,4,6,2,3], future = [8,5,4,3,5], budget = 10))
    print(Solution().maxProfits2(present = [2,2,5], future = [3,4,10], budget = 6))
    print(Solution().maxProfits2(present = [3,3,12], future = [0,3,15], budget = 10))
    print(Solution().maxProfits2(present = [3, 6, 10, 7, 18, 25, 3, 12], 
                                 future =  [0, 10, 6, 5, 27, 14, 13, 15], budget = 21))
    
    n = 1000
    present, future = [], []
    for i in range(n):
        p, f = randint(0, 100), randint(0, 100)
        present.append(p)
        future.append(f)
    print(Solution().maxProfits2(present = present,
                                 future =  future, budget = 887))
    print(Solution().maxProfits3(present = present,
                            future =  future, budget = 887))
    


    
