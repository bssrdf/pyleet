'''

-Medium-

You have d dice and each die has f faces numbered 1, 2, ..., f. You are given three 
integers d, f, and target.

Return the number of possible ways (out of fd total ways) modulo 10**9 + 7 to roll the 
dice so the sum of the face-up numbers equals target.

 

Example 1:

Input: d = 1, f = 6, target = 3
Output: 1
Explanation: 
You throw one die with 6 faces.  There is only one way to get a sum of 3.
Example 2:

Input: d = 2, f = 6, target = 7
Output: 6
Explanation: 
You throw two dice, each with 6 faces.  There are 6 ways to get a sum of 7:
1+6, 2+5, 3+4, 4+3, 5+2, 6+1.
Example 3:

Input: d = 2, f = 5, target = 10
Output: 1
Explanation: 
You throw two dice, each with 5 faces.  There is only one way to get a sum of 10: 5+5.
Example 4:

Input: d = 1, f = 2, target = 3
Output: 0
Explanation: 
You throw one die with 2 faces.  There is no way to get a sum of 3.
Example 5:

Input: d = 30, f = 30, target = 500
Output: 222616187
Explanation: 
The answer must be returned modulo 10^9 + 7.
 

Constraints:

1 <= d, f <= 30
1 <= target <= 1000

'''

class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:        
        MOD = 10**9+7
        dp = [[0]*(target+1) for _ in range(d+1)]
        dp[0][0] = 1
        for i in range(1, d+1):
            for t in range(1, target+1):
                for j in range(1, min(f,t)+1):
                    dp[i][t] = (dp[i][t] + dp[i-1][t-j]) % MOD
        return dp[d][target]

    def numRollsToTarget2(self, d: int, f: int, target: int) -> int:        
        MOD = 10**9+7
        dp1 = [0]*(target+1)
        dp = [0]*(target+1)
        dp1[0] = 1
        for i in range(1, d+1):
            for t in range(1, target+1):
                for j in range(1, min(f,t)+1):
                    dp[t] = (dp[t] + dp1[t-j]) % MOD
            dp1 = dp[:]
            dp = [0]*(target+1)
        return dp1[target]

    def numRollsToTarget3(self, d: int, f: int, target: int) -> int:        
        MOD = 10**9+7
        dp1 = [0]*(target+1)
        dp = [0]*(target+1)
        dp1[0] = 1
        for i in range(1, d+1):
            for t in range(1, target+1):
                if t > i * f: break # optimization: no way to form t using i dices 
                for j in range(1, min(f,t)+1):
                    dp[t] = (dp[t] + dp1[t-j]) % MOD
            dp1 = dp[:]
            dp = [0]*(target+1)
        return dp1[target]




        
if __name__=="__main__":
    print(Solution().numRollsToTarget(2,6,7))
    print(Solution().numRollsToTarget(2,5,10))
    print(Solution().numRollsToTarget(1,2,3))
    #print(Solution().numRollsToTarget(30,30,500))
    print(Solution().numRollsToTarget2(2,6,7))
    print(Solution().numRollsToTarget2(2,5,10))
    print(Solution().numRollsToTarget2(1,2,3))
    #print(Solution().numRollsToTarget2(30,30,500))
    print(Solution().numRollsToTarget3(2,6,7))
    print(Solution().numRollsToTarget3(2,5,10))
    print(Solution().numRollsToTarget3(1,2,3))
    print(Solution().numRollsToTarget3(30,30,500))