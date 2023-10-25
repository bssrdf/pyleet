'''

-Medium-

$$$

*Sorting*
*Binary Search*
*Binary Index Tree*
*BIT*
*Fenwick Tree*


Given the 0-indexed arrays prices and profits of length n. There are n items in an store where the ith item has a price of prices[i] and a profit of profits[i].

We have to pick three items with the following condition:

prices[i] < prices[j] < prices[k] where i < j < k.
If we pick items with indices i, j and k satisfying the above condition, the profit would be profits[i] + profits[j] + profits[k].

Return the maximum profit we can get, and -1 if it's not possible to pick three items with the given condition.

 

Example 1:

Input: prices = [10,2,3,4], profits = [100,2,7,10]
Output: 19
Explanation: We can't pick the item with index i=0 since there are no indices j and k such that the condition holds.
So the only triplet we can pick, are the items with indices 1, 2 and 3 and it's a valid pick since prices[1] < prices[2] < prices[3].
The answer would be sum of their profits which is 2 + 7 + 10 = 19.
Example 2:

Input: prices = [1,2,3,4,5], profits = [1,5,3,4,6]
Output: 15
Explanation: We can select any triplet of items since for each triplet of indices i, j and k such that i < j < k, the condition holds.
Therefore the maximum profit we can get would be the 3 most profitable items which are indices 1, 3 and 4.
The answer would be sum of their profits which is 5 + 4 + 6 = 15.
Example 3:

Input: prices = [4,3,2,1], profits = [33,20,19,87]
Output: -1
Explanation: We can't select any triplet of indices such that the condition holds, so we return -1.
 

Constraints:

3 <= prices.length == profits.length <= 2000
1 <= prices[i] <= 106
1 <= profits[i] <= 106


'''

from typing import List
import bisect
class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        n = len(prices)
        ans = -1
        for j in range(1, n-1):
            for i in range(j):
                for k in range(j+1, n):
                    if prices[i] < prices[j] < prices[k]:
                        ans = max(ans, profits[i] + profits[j] + profits[k])
        return ans             

    def maxProfit2(self, prices: List[int], profits: List[int]) -> int:
        n = len(prices)
        ans = -1
        for j, x in enumerate(profits):
            left = right = 0
            for i in range(j):
                if prices[i] < prices[j] and left < profits[i]:
                    left = profits[i]
            for k in range(j + 1, n):
                if prices[j] < prices[k] and right < profits[k]:
                    right = profits[k]
            if left and right:
                ans = max(ans, left + x + right)
                # print(j, x, ans, left, right)
        return ans   
 
    def maxProfit3(self, prices: List[int], profits: List[int]) -> int:
        n = len(prices)
        ans = -1
        leftMax, rightMax = [-1]*n, [-1]*n

        bit = [0]*(n+1)
        def update(i, x):
            while i <= n:
                bit[i] = max(bit[i], x)
                i += i & (-i)
        def query(i):
            t = 0
            while i > 0:
                t = max(t, bit[i])
                i -= i & (-i)
            return t
        
        arr = sorted(prices)
        #print(arr)
        mp = {}
        for i,a in enumerate(arr):
           if a not in mp:
              mp[a] = i
        for j in range(n):
            #idx = bisect.bisect_left(arr, prices[j])
            idx = mp[prices[j]]
            #idx1 = idx
            # if mark[idx]:
            idx -= 1
            if idx == -1:
                leftMax[j] = 0
                #idx = 0
            else:
                leftMax[j] = query(idx+1)
         #   print(j, prices[j], idx, idx1, leftMax[j])
            update(idx+2, profits[j])
        #print(leftMax)

        
        bit = [0]*(n+1)
        arr = sorted([-p for p in prices])
        mp = {}
        for i,a in enumerate(arr):
           if a not in mp:
              mp[a] = i
        #print(arr)
        for j in range(n-1, -1, -1):
            #idx = bisect.bisect_left(arr, -prices[j])
            idx = mp[-prices[j]]
          #  idx1 = idx
            idx -= 1
            if idx == -1:
                rightMax[j] = 0
                #idx = 0
            else:
                rightMax[j] = query(idx+1)
         #   print(j, prices[j], idx, idx1, rightMax[j])
            update(idx+2, profits[j])

        #print(rightMax)

        for i in range(n):
            x = profits[i]
            left, right = leftMax[i], rightMax[i]
            if left != 0 and right != 0:
                ans = max(ans, left + x + right)
            # print(ans, x, left, right)    
        return ans   


from random import randint
if __name__ == "__main__":
    # print(Solution().maxProfit(prices = [10,2,3,4], profits = [100,2,7,10]))
    # print(Solution().maxProfit(prices = [1,2,3,4,5], profits = [1,5,3,4,6]))
    # print(Solution().maxProfit(prices = [4,3,2,1], profits = [33,20,19,87]))

    # print(Solution().maxProfit3(prices = [10,2,3,4], profits = [100,2,7,10]))
    # print(Solution().maxProfit3(prices = [1,2,3,4,5], profits = [1,5,3,4,6]))
    # print(Solution().maxProfit3(prices = [4,3,2,1], profits = [33,20,19,87]))
    # prices = [15, 18, 62, 49, 21, 100, 76, 62, 6, 92]
    # profits = [23, 98, 68, 16, 71, 82, 59, 64, 41, 9]
    # print(Solution().maxProfit2(prices=prices, profits=profits))
    # print(Solution().maxProfit3(prices=prices, profits=profits))
    # prices  =  [36, 74, 41, 39, 8, 84, 75, 75, 96, 28]
    # profits =  [61, 65, 76, 65, 71, 82, 85, 94, 84, 6]
    # print(Solution().maxProfit2(prices=prices, profits=profits))
    # print(Solution().maxProfit3(prices=prices, profits=profits))

    # prices  =  [8, 74, 41, 39, 8, 84, 75, 75, 96, 28]
    # profits =  [61, 65, 76, 65, 71, 82, 85, 94, 84, 6]
    # print(Solution().maxProfit2(prices=prices, profits=profits))
    # print(Solution().maxProfit3(prices=prices, profits=profits))

    prices  = [13, 9,   6, 2, 15, 5, 13, 4, 15, 17, 15, 11,  7, 13, 15, 17, 6, 1,  3, 1]
    profits = [19, 17, 17, 3, 20, 4, 19, 5, 11, 16, 19,  7, 14, 13,  3,  7, 9, 5, 19, 5]
    print(Solution().maxProfit2(prices=prices, profits=profits))
    print(Solution().maxProfit3(prices=prices, profits=profits))
    prices =  [13, 16, 10, 11,  1, 17, 17, 16, 3, 16, 10,  5, 13,  5, 5, 18, 9, 14,  6, 6]
    profits = [19, 13,  1,  1, 14,  9,  3,  3, 2,  9,  9, 18,  7, 12, 8,  3, 9, 15, 16, 5]
    print(Solution().maxProfit2(prices=prices, profits=profits))
    print(Solution().maxProfit3(prices=prices, profits=profits))
    prices = [8, 1, 6, 12, 15, 3, 15, 17, 16, 12, 7, 6, 10, 6, 7, 15, 8, 13, 8, 18]
    profits = [6, 4, 19, 14, 7, 8, 7, 19, 15, 3, 12, 6, 8, 19, 4, 16, 13, 13, 14, 19]
    print(Solution().maxProfit2(prices=prices, profits=profits))
    print(Solution().maxProfit3(prices=prices, profits=profits))

    for _ in range(100):
      N = 20000
      M = 20000
      prices, profits = [], []
      for _ in range(N):
        prices.append(randint(1, M))
        profits.append(randint(1, M))
      s1 = Solution().maxProfit3(prices=prices, profits=profits)
      print(s1)
    #   s2 = Solution().maxProfit2(prices=prices, profits=profits)
    #   print(s2)
    #   if s1 != s2:
    #     print(prices)
    #     print(profits)

   