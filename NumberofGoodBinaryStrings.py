'''

-Medium-
$$$
*DP*

You are given four integers minLenght, maxLength, oneGroup and zeroGroup.

A binary string is good if it satisfies the following conditions:

The length of the string is in the range [minLength, maxLength].
The size of each block of consecutive 1's is a multiple of oneGroup.
For example in a binary string 00110111100 sizes of each block of consecutive ones are [2,4].
The size of each block of consecutive 0's is a multiple of zeroGroup.
For example, in a binary string 00110111100 sizes of each block of consecutive ones are [2,1,2].
Return the number of good binary strings. Since the answer may be too large, return it modulo 109 + 7.

Note that 0 is considered a multiple of all the numbers.

 

Example 1:

Input: minLength = 2, maxLength = 3, oneGroup = 1, zeroGroup = 2
Output: 5
Explanation: There are 5 good binary strings in this example: "00", "11", "001", "100", and "111".
It can be proven that there are only 5 good strings satisfying all conditions.
Example 2:

Input: minLength = 4, maxLength = 4, oneGroup = 4, zeroGroup = 3
Output: 1
Explanation: There is only 1 good binary string in this example: "1111".
It can be proven that there is only 1 good string satisfying all conditions.
 

Constraints:

1 <= minLength <= maxLength <= 105
1 <= oneGroup, zeroGroup <= maxLength



'''


class Solution:
    def goodBinaryStrings(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
        n =  maxLength
        O, Z = oneGroup, zeroGroup
        dp =[[0]*(n+1) for _ in range(2)]
        dp[0][0] = dp[1][0] = 1
        for i in range(1, n+1):
            j = 1
            while i - j*Z >= 0:                 
                dp[0][i] += dp[1][i-j*Z]
                j += 1
            j = 1
            while i - j*O >= 0:                 
                dp[1][i] += dp[0][i-j*O]
                j += 1
        # print(dp[0])
        # print(dp[1])
        ans = 0
        for i in range(minLength, maxLength+1):
            ans += dp[0][i] + dp[1][i]
        return ans
    

    def goodBinaryStrings2(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
        n =  maxLength
        O, Z = oneGroup, zeroGroup
        dp =[[0]*(n+1) for _ in range(2)]
        dp[0][0] = dp[1][0] = 1
        dp0, dp1 = [0]*O, [0]*Z
        dp0[0] = dp1[0] = 1
        ans = 0
        for i in range(1, n+1):
            dp[0][i] += dp1[i%Z]
            dp[1][i] += dp0[i%O]
            dp1[i%Z] += dp[1][i]
            dp0[i%O] += dp[0][i]            
            if i >= minLength:
                ans += dp[0][i] + dp[1][i]
            # print(i, ans, dp[0][i] + dp[1][i] )
        # print(dp[0])
        # print(dp[1])
        return ans
    
    def goodBinaryStrings3(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
        MOD, n = 10**9 + 7, maxLength
        O, Z = oneGroup, zeroGroup
        dp = [0]*2
        dp0, dp1 = [0]*O, [0]*Z
        dp0[0] = dp1[0] = 1
        ans = 0
        for i in range(1, n+1):
            dp[0] = dp1[i%Z]
            dp[1] = dp0[i%O]
            dp1[i%Z] += dp[1]
            dp0[i%O] += dp[0]
            if i >= minLength:
                ans = (ans + sum(dp)) % MOD
        return ans
    
    def goodBinaryStrings4(self, minLength: int, maxLength: int, oneGroup: int, zeroGroup: int) -> int:
        mod = 10**9 + 7
        f = [1] + [0] * maxLength
        for i in range(1, len(f)):
            if i - oneGroup >= 0:
                f[i] += f[i - oneGroup]
            if i - zeroGroup >= 0:
                f[i] += f[i - zeroGroup]
            f[i] %= mod
        return sum(f[minLength:]) % mod



from random import randint
if __name__=="__main__":
    print(Solution().goodBinaryStrings(minLength = 2, maxLength = 3, oneGroup = 1, zeroGroup = 2))
    print(Solution().goodBinaryStrings2(minLength = 2, maxLength = 3, oneGroup = 1, zeroGroup = 2))
    print(Solution().goodBinaryStrings3(minLength = 2, maxLength = 3, oneGroup = 1, zeroGroup = 2))
    print(Solution().goodBinaryStrings(minLength = 4, maxLength = 4, oneGroup = 4, zeroGroup = 3))
    print(Solution().goodBinaryStrings2(minLength = 4, maxLength = 4, oneGroup = 4, zeroGroup = 3))
    print(Solution().goodBinaryStrings3(minLength = 4, maxLength = 4, oneGroup = 4, zeroGroup = 3))
    print(Solution().goodBinaryStrings3(minLength = 2546, maxLength = 49863, oneGroup = 1010, zeroGroup = 555))
    print(Solution().goodBinaryStrings4(minLength = 2546, maxLength = 49863, oneGroup = 1010, zeroGroup = 555))
    N = 10**5
    for i in range(50):
        minLength = randint(1, N)
        maxLength = randint(minLength, N)
        oneGroup = randint(1, maxLength)
        zeroGroup = randint(1, maxLength)
        sol1 = Solution().goodBinaryStrings3(minLength = minLength, maxLength = maxLength, oneGroup = oneGroup, zeroGroup = zeroGroup)
        sol2 = Solution().goodBinaryStrings4(minLength = minLength, maxLength = maxLength, oneGroup = oneGroup, zeroGroup = zeroGroup)
        print(minLength, maxLength, oneGroup, zeroGroup, sol1, sol2)

        
    
