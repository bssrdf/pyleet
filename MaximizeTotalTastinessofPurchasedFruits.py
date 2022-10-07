'''

-Medium-
$$$

*DP*


ou are given two non-negative integer arrays price and tastiness, both arrays have the same length n. You are also given two non-negative integers maxAmount and maxCoupons.

For every integer i in range [0, n - 1]:

price[i] describes the price of ith fruit.
tastiness[i] describes the tastiness of ith fruit.
You want to purchase some fruits such that total tastiness is maximized and the total price does not exceed maxAmount.

Additionally, you can use a coupon to purchase fruit for half of its price (rounded down to the closest integer). You can use at most maxCoupons of such coupons.

Return the maximum total tastiness that can be purchased.

Note that:

You can purchase each fruit at most once.
You can use coupons on some fruit at most once.
 

Example 1:

Input: price = [10,20,20], tastiness = [5,8,8], maxAmount = 20, maxCoupons = 1
Output: 13
Explanation: It is possible to make total tastiness 13 in following way:
- Buy first fruit without coupon, so that total price = 0 + 10 and total tastiness = 0 + 5.
- Buy second fruit with coupon, so that total price = 10 + 10 and total tastiness = 5 + 8.
- Do not buy third fruit, so that total price = 20 and total tastiness = 13.
It can be proven that 13 is the maximum total tastiness that can be obtained.
Example 2:

Input: price = [10,15,7], tastiness = [5,8,20], maxAmount = 10, maxCoupons = 2
Output: 28
Explanation: It is possible to make total tastiness 20 in following way:
- Do not buy first fruit, so that total price = 0 and total tastiness = 0.
- Buy second fruit with coupon, so that total price = 0 + 7 and total tastiness = 0 + 8.
- Buy third fruit with coupon, so that total price = 7 + 3 and total tastiness = 8 + 20.
It can be proven that 28 is the maximum total tastiness that can be obtained.
 

Constraints:

n == price.length == tastiness.length
1 <= n <= 100
0 <= price[i], tastiness[i], maxAmount <= 1000
0 <= maxCoupons <= 5

'''
from functools import lru_cache
from typing import List
from random import randint

class Solution(object):
    def maxTastiness(self, price: List[int], tastiness: List[int], maxAmount: int, maxCoupons: int) -> int:
        n = len(price)
        @lru_cache(None) 
        def dfs(i, cost, coup):
            if i == n:
                return 0            
            ret = dfs(i+1, cost, coup)  # do not buy i-th fruit      
            if cost+price[i] <= maxAmount: # buy i-th fruit with full price     
                ret = max(ret, tastiness[i]+dfs(i+1, cost+price[i], coup))
            if cost+price[i]//2 <= maxAmount and coup > 0: # buy i-th fruit with coupon
                ret = max(ret, tastiness[i]+dfs(i+1, cost+price[i]//2, coup-1))
            return ret
        return dfs(0, 0, maxCoupons)
    
    def maxTastiness2(self, price: List[int], tastiness: List[int], maxAmount: int, maxCoupons: int) -> int:
        @lru_cache(None)
        def dfs(i, j, k):
            if i == len(price):
                return 0
            ans = dfs(i + 1, j, k)
            if j >= price[i]:
                ans = max(ans, dfs(i + 1, j - price[i], k) + tastiness[i])
            if j >= price[i] // 2 and k:
                ans = max(
                    ans, dfs(i + 1, j - price[i] // 2, k - 1) + tastiness[i])
            return ans

        return dfs(0, maxAmount, maxCoupons)

if __name__ == "__main__":  
    print(Solution().maxTastiness(price = [10,20,20], tastiness = [5,8,8], maxAmount = 20, maxCoupons = 1))         
    print(Solution().maxTastiness(price = [10,15,7], tastiness = [5,8,20], maxAmount = 10, maxCoupons = 2))         
    N = 100
    maxP, maxT = 100, 100
    price = [randint(0, maxP) for _ in range(N)]
    tastiness = [randint(0, maxT) for _ in range(N)]
    print(Solution().maxTastiness(price = price, tastiness = tastiness, maxAmount = 650, maxCoupons = 3))         
    print(Solution().maxTastiness2(price = price, tastiness = tastiness, maxAmount = 650, maxCoupons = 3))         



