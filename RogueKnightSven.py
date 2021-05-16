'''
-Medium-
*DP*
In material plane "reality", there are n + 1 planets, namely planet 0, 
planet 1, ..., planet n.
Each planet has a portal through which we can reach the target planet directly 
without passing through other planets.
But portal has two shortcomings.
First, planet i can only reach the planet whose number is greater than i, and 
the difference between i can not exceed the limit.
Second, it takes cost[j] gold coins to reach the planet j through the portal.
Now, Rogue Knight Sven arrives at the planet 0 with m gold coins, how many 
ways does he reach the planet n through the portal?

1 <= n <= 50, 0 <= m <= 100, 1 <= limit <= 50, 0 <= cost[i] <= 100。
The problem guarantees cost [0] = 0, cause cost[0] does not make sense
样例
Example 1:

Input:
n = 1
m = 1
limit = 1
cost = [0, 1]
Output:
1
Explanation:
Plan 1: planet 0 → planet 1
Example 2:

Input:
n = 1
m = 1
limit = 1
cost = [0,2]
Output:
0
Explanation:
He can not reach the target planet.

'''

class Solution:
    """
    @param n: the max identifier of planet.
    @param m: gold coins that Sven has.
    @param limit: the max difference.
    @param cost: the number of gold coins that reaching the planet j through the portal costs.
    @return: return the number of ways he can reach the planet n through the portal.
    """
    def getNumberOfWays(self, n, m, limit, cost):
        # dp[i][j]表示到达星球i时剩余金币为j的方式数
        dp = [ [0]*(m+1) for _ in range(n+1)]
        # 初始化,在星球0金币数为m
        dp[0][m] = 1
        # 对于星球i,i-1到i-limit可以直接到达
        # dp[i][k]表示剩余金币为k的方式数,由于花销为cost[i],
        # 则在前一个到达的星球其对应的方式数为dp[pos][k+cost[i]](i-limit <= pos <= i-1)
        for i in range(1, n+1):
            for j in range(1, min(limit+1,i+1)):
                for k in range(m-cost[i]+1):
                    dp[i][k] += dp[i - j][k + cost[i]]
        # 将剩余钱数的各种方式数相加得到结果
        return sum([dp[n][i] for i in range(m+1)])
