'''
-Medium-
*DP*
*Binary Search*

You are given an integer n representing the number of houses on a number line, numbered from 0 to n - 1.

Additionally, you are given a 2D integer array offers where offers[i] = [starti, endi, goldi], indicating that ith buyer wants to buy all the houses from starti to endi for goldi amount of gold.

As a salesman, your goal is to maximize your earnings by strategically selecting and selling houses to buyers.

Return the maximum amount of gold you can earn.

Note that different buyers can't buy the same house, and some houses may remain unsold.

 

Example 1:

Input: n = 5, offers = [[0,0,1],[0,2,2],[1,3,2]]
Output: 3
Explanation: There are 5 houses numbered from 0 to 4 and there are 3 purchase offers.
We sell houses in the range [0,0] to 1st buyer for 1 gold and houses in the range [1,3] to 3rd buyer for 2 golds.
It can be proven that 3 is the maximum amount of gold we can achieve.
Example 2:

Input: n = 5, offers = [[0,0,1],[0,2,10],[1,3,2]]
Output: 10
Explanation: There are 5 houses numbered from 0 to 4 and there are 3 purchase offers.
We sell houses in the range [0,2] to 2nd buyer for 10 golds.
It can be proven that 10 is the maximum amount of gold we can achieve.
 

Constraints:

1 <= n <= 105
1 <= offers.length <= 105
offers[i].length == 3
0 <= starti <= endi <= n - 1
1 <= goldi <= 103


'''

from typing import List
import bisect
class Solution:
    def maximizeTheProfit(self, n: int, offers: List[List[int]]) -> int:
        dp = [0] * (n + 1)
        m = [[] for _ in range(n)]
        for s,e,g in offers:
            m[e].append([s,g])
        for e in range(1, n + 1):
            dp[e] = dp[e - 1]
            for s, g in m[e - 1]:
                dp[e] = max(dp[e], dp[s] + g)
        return dp[-1]
    
    def maximizeTheProfit2(self, n: int, offers: List[List[int]]) -> int:
        offers.sort(key=lambda v: v[1])
        m = len(offers)
        dp = [0] * m
        dp[0] = offers[0][2]
        def search(index):
            left, right = 0, index-1
            while left <= right:
                mid = left + (right-left)//2
                if offers[mid][1] < offers[index][0]:
                    if offers[mid + 1][1] < offers[index][0]:
                        left = mid + 1
                    else:
                        return mid
                else:
                    right = mid - 1
            return -1
        for i in range(1, m):
            #print(i, jobs[i])
            l = search(i)
            profit = offers[i][2]
            if l != -1:
                profit += dp[l]
            dp[i] = max(dp[i-1], profit)
        return dp[-1]



    
if __name__ == "__main__":
    # print(Solution().maximizeTheProfit(n = 5, offers = [[0,0,1],[0,2,2],[1,3,2]]))
    print(Solution().maximizeTheProfit2(n = 5, offers = [[0,0,1],[0,2,2],[1,3,2]]))
    # print(Solution().maximizeTheProfit(n = 5, offers = [[0,0,1],[0,2,10],[1,3,2]]))
    # print(Solution().maximizeTheProfit(n = 4, offers = [[1,3,9],[0,2,10],[1,3,3],[0,1,3],[2,2,1],[3,3,7],[2,2,1],[1,2,9],[1,2,8]]))
    print(Solution().maximizeTheProfit(n = 4, offers = [[1,3,9],[0,2,10],[0,1,3],[2,2,1],[3,3,7],[1,2,9]]))
    print(Solution().maximizeTheProfit2(n = 4, offers = [[1,3,9],[0,2,10],[0,1,3],[2,2,1],[3,3,7],[1,2,9]]))
    print(Solution().maximizeTheProfit(n = 10, offers=[[0,6,5],[2,9,4],[0,9,2],[3,9,3],[1,6,10],[0,1,3],[3,8,9],[4,8,3],[2,6,5],[0,4,6]]))
    print(Solution().maximizeTheProfit2(n = 10, offers=[[0,6,5],[2,9,4],[0,9,2],[3,9,3],[1,6,10],[0,1,3],[3,8,9],[4,8,3],[2,6,5],[0,4,6]]))
    print(Solution().maximizeTheProfit(n = 7, offers=[[1,2,5],[4,6,7],[0,2,4],[4,4,1],[2,4,7],[0,5,4],[2,3,7],[3,4,6],[1,2,9],[2,5,8]]))
    print(Solution().maximizeTheProfit2(n = 7, offers=[[1,2,5],[4,6,7],[0,2,4],[4,4,1],[2,4,7],[0,5,4],[2,3,7],[3,4,6],[1,2,9],[2,5,8]]))