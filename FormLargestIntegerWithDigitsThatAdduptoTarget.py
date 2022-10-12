'''

-Hard-
*DP*


Given an array of integers cost and an integer target, return the maximum integer you 
can paint under the following rules:

The cost of painting a digit (i + 1) is given by cost[i] (0-indexed).
The total cost used must be equal to target.
The integer does not have 0 digits.
Since the answer may be very large, return it as a string. If there is no way to paint any integer given the condition, return "0".

 

Example 1:

Input: cost = [4,3,2,5,6,7,2,5,5], target = 9
Output: "7772"
Explanation: The cost to paint the digit '7' is 2, and the digit '2' is 3. Then cost("7772") = 2*3+ 3*1 = 9. You could also paint "977", but "7772" is the largest number.
Digit    cost
  1  ->   4
  2  ->   3
  3  ->   2
  4  ->   5
  5  ->   6
  6  ->   7
  7  ->   2
  8  ->   5
  9  ->   5
Example 2:

Input: cost = [7,6,5,5,5,6,8,7,8], target = 12
Output: "85"
Explanation: The cost to paint the digit '8' is 7, and the digit '5' is 5. Then cost("85") = 7 + 5 = 12.
Example 3:

Input: cost = [2,4,6,2,4,6,4,4,4], target = 5
Output: "0"
Explanation: It is impossible to paint any integer with total cost equal to target.
 

Constraints:

cost.length == 9
1 <= cost[i], target <= 5000


'''

from typing import List

class Solution:
    def largestNumber(self, cost: List[int], target: int) -> str:
        mi = min(cost)
        n = target // mi
        print('n=', n)
        dp = [['0']*(target+1) for _ in range(n+1)]
        res = '0'
        for j in range(1, target+1):
            for k in range(9):
               dp[1][j] = max(dp[1][j], str(k+1) if j == cost[k] else '')
        # print('x', 1, dp[1])
        for i in range(2, n+1):
            for j in range(1, target+1):
                for k in range(9):
                    if j - cost[k] >= 0: 
                        dp[i][j] = max(dp[i][j], str(k+1)+dp[i-1][j-cost[k]] if dp[i-1][j-cost[k]] else '', key=len)

                        # dp[i][j] = max(dp[i][j], str(k+1)+dp[i-1][j-cost[k]] if dp[i-1][j-cost[k]] else '', key=int)
            # print('x', dp[i][target])
            # print('x',i, dp[i])
            res = max(res, dp[i][target],key=len)
            # res = max(res, dp[i][target],key=int)
        return res
    

    def largestNumber2(self, cost: List[int], target: int) -> str:
        dp = ['0' for _ in range(target+1)]
        dp[target] = ""        
        for i in range(target-1, -1, -1):
            for k in range(9):
                val = i + cost[k]
                if val <= target and dp[val] != "0": 
                    if len(dp[val])+1 >= len(dp[i]):
                        dp[i] = str(k+1) + dp[val]

        return dp[0]
    

    def largestNumber3(self, cost: List[int], target: int) -> str:
        dp = ['0' for _ in range(target+1)]
        dp[0] = ""        
        for i in range(1, target+1):
            for k in range(9):
                val = i - cost[k]
                if val >= 0 and dp[val] != "0": 
                    if len(dp[val])+1 >= len(dp[i]): # >= is required here as k goes from 1 to 9
                                                     # if a k gives the same length, it replaces
                                                     # the previous smaller k 
                        dp[i] = str(k+1) + dp[val]

        return dp[target]

if __name__ == "__main__":
    # print(Solution().largestNumber(cost = [4,3,2,5,6,7,2,5,5], target = 9))
    # print(Solution().largestNumber(cost = [7,6,5,5,5,6,8,7,8], target = 12))
    # print(Solution().largestNumber(cost = [2,4,6,2,4,6,4,4,4], target = 5))
    # print(Solution().largestNumber(cost = [4,2,3,3,4,5,5,2,2],  target = 795))
    print(Solution().largestNumber2(cost = [4,2,3,3,4,5,5,2,2],  target = 795))
    print(Solution().largestNumber3(cost = [4,2,3,3,4,5,5,2,2],  target = 795))
        