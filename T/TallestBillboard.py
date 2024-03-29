'''
-Hard-

You are installing a billboard and want it to have the largest height. The 
billboard will have two steel supports, one on each side. Each steel support 
must be an equal height.

You are given a collection of rods that can be welded together. For example, 
if you have rods of lengths 1, 2, and 3, you can weld them together to make 
a support of length 6.

Return the largest possible height of your billboard installation. If you 
cannot support the billboard, return 0.

 

Example 1:

Input: rods = [1,2,3,6]
Output: 6
Explanation: We have two disjoint subsets {1,2,3} and {6}, which have the same sum = 6.
Example 2:

Input: rods = [1,2,3,4,5,6]
Output: 10
Explanation: We have two disjoint subsets {2,3,5} and {4,6}, which have the same sum = 10.
Example 3:

Input: rods = [1,2]
Output: 0
Explanation: The billboard cannot be supported, so we return 0.
 

Constraints:

1 <= rods.length <= 20
1 <= rods[i] <= 1000
sum(rods[i]) <= 5000


'''

from typing import List
import collections 

class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        n = len(rods)
        sum_ = sum(rods)
        dp = [[0]*(sum_+1) for _ in range(n+1)]
        for i in range(sum_+1): dp[0][i] = -10**9
        dp[0][0] = 0
        for i in range(1, n+1):
        	for j in range(sum_):
        		dp[i][j] = dp[i - 1][j]
        		if j >= rods[i - 1]:
        			dp[i][j] = max(dp[i][j], dp[i - 1][j - rods[i - 1]] + rods[i - 1])
        		else: 
        			dp[i][j] = max(dp[i][j], dp[i - 1][rods[i - 1] - j] + j)
        		if j + rods[i - 1] <= sum_:
        			dp[i][j] = max(dp[i][j], dp[i - 1][j + rods[i - 1]])
        return dp[n][0]

    def tallestBillboard2(self, rods: List[int]) -> int:
        sum_ = sum(rods)
        dp = [-10**9]*(sum_+1)
        dp[0] = 0
        for x in rods:
            cur = dp[:]
            for d in range(sum_-x+1):
                dp[d + x] = max(dp[d + x], cur[d])
                dp[abs(d - x)] = max(dp[abs(d - x)], cur[d] + min(d, x))
        return dp[0]
    
    def tallestBillboard3(self, rods):
        #Consider this problem as:
        #Given a list of numbers, multiply each number with 1 or 0 or -1, make the 
        # sum of all numbers to 0. Find a combination which has the largest sum 
        # of all positive numbers.
        #e.g. Given [1,2,3,4,5,6], we have 1*0 + 2 + 3 - 4 + 5 - 6 = 0, the sum 
        # of all positive numbers is 2 + 3 + 5 = 10. The answer is 10.

        # This is a knapsack problem.
        # dp[i][j] represents whether the sum of first i numbers can be j - 5000. 
        # dp[0][5000] = true.
        # Then dp[i + 1][j] = dp[i][j - rods[i]] | dp[i][j + rods[i]] | dp[i][j].
        # max[i][j] represents the largest sum of all positive numbers when the 
        # sum of first i numbers is j - 5000.

        # Time complexity: O(N*sum)

        # It is like a knapsack problem.
        # Consider this problem as:
        # Given a list of numbers, multiply each number with 1 or 0 or -1, make the 
        # sum of all numbers to 0. Find a combination which has the largest sum of 
        # all positive numbers.

        # We can consider the sum as the key and positive number sum as the value.
        # We initally have dp[0] = 0

        # We iterate through the numbers and calculate the pairs that we got. In 
        # the case that we have same sum but different postive number sum, we only 
        # keep the largest postive number sum.

        # Let's run through a example, [1,2,3]
        # First we have {0:0}.
        # After 1, we have {0: 0, 1: 1, -1: 0}
        # After 2, we have {0:0, 2:2, -2:0, 1:1, 3:3,-1:1, -1:0,1:2,-3:0}
        # we will drop 1:1 and -1:0 since they have smaller value with the same key[1]and [-1]. 
        # That left us with {0:0, 2:2, -2:0, 3:3,-1:1,1:2,-3:0}
        # Number 3 is doing pretty much the same.
        # Then we will get the final result with dp[0]
        dp = dict()
        dp[0] = 0
        
        for i in rods:
            cur = collections.defaultdict(int)
            for s in dp:
                cur[s+i] = max(dp[s] + i, cur[s+i])
                cur[s] = max(dp[s], cur[s])
                cur[s-i] = max(dp[s], cur[s-i])
            dp = cur
        return dp[0]
       
       

if __name__ == "__main__":
    print(Solution().tallestBillboard([1,2,3,6]))
    print(Solution().tallestBillboard2([1,2,3,6]))
    print(Solution().tallestBillboard3([1,2,3,6]))