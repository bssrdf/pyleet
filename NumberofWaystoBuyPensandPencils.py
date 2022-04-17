'''
-Medium-

You are given an integer total indicating the amount of money you have. You are 
also given two integers cost1 and cost2 indicating the price of a pen and pencil 
respectively. You can spend part or all of your money to buy multiple quantities 
(or none) of each kind of writing utensil.

Return the number of distinct ways you can buy some number of pens and pencils.

 

Example 1:

Input: total = 20, cost1 = 10, cost2 = 5
Output: 9
Explanation: The price of a pen is 10 and the price of a pencil is 5.
- If you buy 0 pens, you can buy 0, 1, 2, 3, or 4 pencils.
- If you buy 1 pen, you can buy 0, 1, or 2 pencils.
- If you buy 2 pens, you cannot buy any pencils.
The total number of ways to buy pens and pencils is 5 + 3 + 1 = 9.
Example 2:

Input: total = 5, cost1 = 10, cost2 = 10
Output: 1
Explanation: The price of both pens and pencils are 10, which cost more than total, so you cannot buy any writing utensils. Therefore, there is only 1 way: buy 0 pens and 0 pencils.
 

Constraints:

1 <= total, cost1, cost2 <= 106


'''

class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        # wrong way
        dp = [0]*(total+1)
        dp[0] = 1
        for i in range(1, total+1):
            if i < cost1 and i < cost2:
                dp[i] = 1
            elif i < cost1:    
                dp[i] = dp[i-cost2] + 1
            elif i < cost2:    
                dp[i] = dp[i-cost1] + 1
            else:  
                dp[i] = dp[i-cost1] + dp[i-cost2] 
        print(dp)
        return sum(dp)

    def waysToBuyPensPencils2(self, total: int, cost1: int, cost2: int) -> int:
        # wrong way
        ways = total//cost2
        dp = [0]*(ways+1)
        dp[0] = 1
        ans = 0
        for i in range(ways+1):           
            t  =  total - i*cost2
            ans += t // cost1 + 1
            print(i, t, t//cost1, ans)

        # print(dp)
        return ans

if __name__ == "__main__":
    print(Solution().waysToBuyPensPencils2(total = 20, cost1 = 10, cost2 = 5))     