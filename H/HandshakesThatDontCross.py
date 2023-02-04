'''
-Hard-
*DP*

You are given an even number of people numPeople that stand around a circle and each person shakes hands with someone else so that there are numPeople / 2 handshakes total.

Return the number of ways these handshakes could occur such that none of the handshakes cross.

Since the answer could be very large, return it modulo 109 + 7.

 

Example 1:



Input: numPeople = 4
Output: 2
Explanation: There are two ways to do it, the first way is [(1,2),(3,4)] and the second one is [(2,3),(4,1)].
Example 2:



Input: numPeople = 6
Output: 5
 

Constraints:

2 <= numPeople <= 1000
numPeople is even.

'''


class Solution:
    def numberOfWays(self, numPeople: int) -> int:
        # 设计dp[i]表示i个人互相握手有多少种符合题意的方法。

        # 我们考虑最后一个人（第i个人）的握手方案。注意i必须是偶数，否则整体就无解。
        # 第i个人的选择可以是他左手第1个、第3个、第5个...直至右手第1个。考虑到第i个人的配成功，
        # 会将整个圈划分成了独立的左右两部分，因此上面这些方案其实对应了将这个圈细分的每种可能：
        # (0,i-2),(2,i-4),(4,i-6)...(i-2,0)，其中每个括号内表示左右两部分的人数。

        # 因此我们可以得到递推关系式：dp[i] = sum(dp[j]+dp[i-2-j])， j=0,2,...i-2
        kMod = 1_000_000_007
        n = numPeople
        # dp[i] := # Of ways i handshakes pair w//o crossing
        dp = [0]*(n+1)
        dp[0] = 1
        dp[2] = 1
        for i in range(4, n + 1, 2):
            for j in range(0, i, 2):
                dp[i] += dp[j] * dp[i - 2 - j] % kMod
                dp[i] %= kMod
        return dp[n]
if __name__ == "__main__":
    print(Solution().numberOfWays(4))
    print(Solution().numberOfWays(6))
    print(Solution().numberOfWays(100))
