'''

-Hard-

*DP*


You are given a string s of length n where s[i] is either:

'D' means decreasing, or
'I' means increasing.
A permutation perm of n + 1 integers of all the integers in the range [0, n] is called a valid permutation if for all valid i:

If s[i] == 'D', then perm[i] > perm[i + 1], and
If s[i] == 'I', then perm[i] < perm[i + 1].
Return the number of valid permutations perm. Since the answer may be large, return it modulo 109 + 7.

 

Example 1:

Input: s = "DID"
Output: 5
Explanation: The 5 valid permutations of (0, 1, 2, 3) are:
(1, 0, 3, 2)
(2, 0, 3, 1)
(2, 1, 3, 0)
(3, 0, 2, 1)
(3, 1, 2, 0)
Example 2:

Input: s = "D"
Output: 1
 

Constraints:

n == s.length
1 <= n <= 200
s[i] is either 'I' or 'D'.

'''

from functools import reduce


class Solution:
    def numPermsDISequence(self, s: str) -> int:
        n, MOD = len(s), 10**9 +7
        s = "#"+s
        # 这里dp[i][j]表示第i位上（以0为起点）的数值为j的方案数目。这里，j的取值范围是0~i。
        # 相当于0~i的一个permuatation。
        # dp = [[0]*205 for _ in range(205)]
        dp = [[0]*(n+1) for _ in range(n+1)]
        dp[0][0] = 1
        for i in range(1, n+1):
            for j in range(i+1):
                if s[i] == 'I':
                    for k in range(j):
                        dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD
                else:
                    for k in range(j, i):
                        dp[i][j] = (dp[i][j] + dp[i-1][k]) % MOD
        return reduce(lambda x, y: (x+y)%MOD, dp[n])
    

    def numPermsDISequence2(self, s: str) -> int:
        n, MOD = len(s), 10**9 +7
        s = "#"+s
        # 这里dp[i][j]表示第i位上（以0为起点）的数值为j的方案数目。这里，j的取值范围是0~i。
        # 相当于0~i的一个permuatation。
        # dp = [[0]*205 for _ in range(205)]
        dp = [[0]*(n+1) for _ in range(n+1)]
        dp[0][0] = 1 # base case
        for i in range(1, n+1):
            sm = 0
            if s[i] == 'I':
                for j in range(1, i+1):      
                    sm = (sm + dp[i-1][j-1]) % MOD          
                    dp[i][j] = sm
            else:
                for j in range(i, -1, -1):                
                    sm = (sm + dp[i-1][j]) % MOD          
                    dp[i][j] = sm
        return reduce(lambda x, y: (x+y)%MOD, dp[n])


if __name__ == "__main__":
    print(Solution().numPermsDISequence(s = "DID"))        
    print(Solution().numPermsDISequence2(s = "DID"))        