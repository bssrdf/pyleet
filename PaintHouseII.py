'''
-Hard-

*DP*

There are a row of n houses, each house can be painted with one of the k colors. 
The cost of painting each house with a certain color is different. You have to 
paint all the houses such that no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by a n x k 
cost matrix. For example, costs[0][0] is the cost of painting house 0 with 
color 0; costs[1][2] is the cost of painting house 1 with color 2, and so on... 
Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[1,5,3],[2,9,4]]
Output: 5
Explanation: Paint house 0 into color 0, paint house 1 into color 2. Minimum 
cost: 1 + 4 = 5; 
             Or paint house 0 into color 2, paint house 1 into color 0. 
             Minimum cost: 3 + 2 = 5. 
Follow up:
Could you solve it in O(nk) runtime?

'''

class Solution(object):
    def minCost(self, costs):
        n = len(costs)
        m = len(costs[0])
        dp = [[0 for _ in range(m)] for _ in range(n+1)]        
        s1, s2 = 0, 0
        for i in range(1, n+1):            
            t1, t2 = float('inf'), float('inf')
            for k in range(m):
                if dp[i-1][k] == s1:
                    dp[i][k] = s2 + costs[i-1][k]
                else:
                    dp[i][k] = s1 + costs[i-1][k]
                if dp[i][k] < t1: 
                    t2 = t1 
                    t1 = dp[i][k] 
                elif dp[i][k] < t2 and dp[i][k] != t1: 
                    t2 = dp[i][k]
            s1,s2 = t1, t2
        return s1




if __name__ == "__main__":
    print(Solution().minCost([[1,5,3],[2,9,4]]))
    print(Solution().minCost([[17,2,17],[16,16,5],[14,3,19]]))