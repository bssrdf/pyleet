'''
-Medium-
*Greedy*
*Sorting*


You have an inventory of different colored balls, and there is a customer that wants 
orders balls of any color.

The customer weirdly values the colored balls. Each colored ball's value is the number 
of balls of that color you currently have in your inventory. For example, if you own 6 
yellow balls, the customer would pay 6 for the first yellow ball. After the transaction, 
there are only 5 yellow balls left, so the next yellow ball is then valued at 5 (i.e., 
the value of the balls decreases as you sell more to the customer).

You are given an integer array, inventory, where inventory[i] represents the number of 
balls of the ith color that you initially own. You are also given an integer orders, 
which represents the total number of balls that the customer wants. You can sell the 
balls in any order.

Return the maximum total value that you can attain after selling orders colored balls. 
As the answer may be too large, return it modulo 109 + 7.

 

Example 1:


Input: inventory = [2,5], orders = 4
Output: 14
Explanation: Sell the 1st color 1 time (2) and the 2nd color 3 times (5 + 4 + 3).
The maximum total value is 2 + 5 + 4 + 3 = 14.
Example 2:

Input: inventory = [3,5], orders = 6
Output: 19
Explanation: Sell the 1st color 2 times (3 + 2) and the 2nd color 4 times (5 + 4 + 3 + 2).
The maximum total value is 3 + 2 + 5 + 4 + 3 + 2 = 19.
 

Constraints:

1 <= inventory.length <= 105
1 <= inventory[i] <= 109
1 <= orders <= min(sum(inventory[i]), 109)


'''

from typing import List

import heapq

class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        pq = [-i for i in inventory]
        heapq.heapify(pq)
        ans, MOD = 0, 10**9+7
        while pq and orders > 0:
            i = -heapq.heappop(pq)
            j = -pq[0] if pq else 0            
            if i > j:
                j = max(j, i-orders)                 
                profits = i*(i+1)//2 - j*(j+1)//2
                d = i-j
            else:
                profits = i
                d = 1

            ans = (ans + profits) % MOD            
            orders -= d
            print(i, j, d, orders, profits)
            i -= d  
            if i > 0:
                heapq.heappush(pq, -i)
        return ans
    
    def maxProfit2(self, inventory: List[int], orders: int) -> int:

        fn = lambda x: sum(max(0, xx - x) for xx in inventory) # balls sold 
    
        # last true binary search 
        lo, hi = 0, 10**9
        while lo < hi: 
            mid = lo + hi + 1 >> 1
            if fn(mid) >= orders: lo = mid
            else: hi = mid - 1
        
        ans = sum((x + lo + 1)*(x - lo)//2 for x in inventory if x > lo)
        return (ans - (fn(lo) - orders) * (lo + 1)) % 1_000_000_007

    def maxProfit3(self, inventory: List[int], orders: int) -> int:
        A, T = inventory, orders
        A.sort(reverse=True)
        n, ans, cur, MOD, i = len(A), 0, A[0], 10**9+7, 0
        while T: 
            while i < n and A[i] == cur: # handle those same numbers together
                i += 1
            next = 0 if i == n else A[i]
            h, r = cur - next, 0
            cnt = min(T, i*h)
            if T < i * h: # the i * h balls are more than what we need.
                h = T // i # we just reduce the height by `T / i` instead
                r = T % i
            val = cur - h # each of the remainder `r` balls has value `cur - h`.
            ans = (ans + (cur + val + 1) * h // 2 * i + val * r) % MOD
            T -= cnt
            cur = next
        return ans










        

if __name__ == "__main__":   
    print(Solution().maxProfit(inventory = [2,5], orders = 4))
    print(Solution().maxProfit(inventory = [3,5], orders = 6))
    print(Solution().maxProfit(inventory = [1000000000], orders = 1000000000))
    print(Solution().maxProfit(inventory = [76], orders = 22))
    print(Solution().maxProfit([497978859,167261111,483575207,591815159], 836556809))