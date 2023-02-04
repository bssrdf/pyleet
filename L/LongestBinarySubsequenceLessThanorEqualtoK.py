'''

-Medium-
*Greedy*
*DP*

You are given a binary string s and a positive integer k.

Return the length of the longest subsequence of s that makes up a binary number less than or equal to k.

Note:

The subsequence can contain leading zeroes.
The empty string is considered to be equal to 0.
A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
 

Example 1:

Input: s = "1001010", k = 5
Output: 5
Explanation: The longest subsequence of s that makes up a binary number less than or equal to 5 is "00010", as this number is equal to 2 in decimal.
Note that "00100" and "00101" are also possible, which are equal to 4 and 5 in decimal, respectively.
The length of this subsequence is 5, so 5 is returned.
Example 2:

Input: s = "00101001", k = 1
Output: 6
Explanation: "000001" is the longest subsequence of s that makes up a binary number less than or equal to 1, as this number is equal to 1 in decimal.
The length of this subsequence is 6, so 6 is returned.
 

Constraints:

1 <= s.length <= 1000
s[i] is either '0' or '1'.
1 <= k <= 109

'''

class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        val, cnt, pow = 0, 0, 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '1':
                cnt += 1
                val += pow
            pow <<= 1
            if val + pow > k: break
        return s.count('0') + cnt

    
    def longestSubsequence2(self, s: str, k: int) -> int:
        n = len(s)
        # dp[i] denotes the minimum binary value of a subsequence of length i
        dp = [0x3f3f3f3f]*(n+1)         
        dp[0] = 0
        dp[1] = int(s[0] == '1')
        for i in range(1, n):
            for j in range(i, -1, -1):
                cur = (dp[j] << 1) + int(s[i] == '1')
                if cur < dp[j+1]:
                    dp[j+1] = cur
        print(dp)
        ret = 1
        for i in range(2, n+1):
            if dp[i] <= k: ret = i
        return ret

    def longestSubsequence3(self, s: str, k: int) -> int:
        # TLE
        # dp[i][j] denotes the minimum value of a subsequence of j length 
        # using values upto 0 to i index of array.
        # i -> index of array
        # j -> len of subsequence
        n, INT_MAX = len(s), 0x3f3f3f3f
        dp = [[INT_MAX]*(n+1)  for _ in range(n+1)]
        for i in range(n+1):
            dp[i][0] = 0
        for i in range(1, n+1):
            for j in range(1, i+1):
                dp[i][j] = min(dp[i-1][j],dp[i][j])
                if dp[i-1][j-1] != INT_MAX:
                    dp[i][j] = min(dp[i][j],dp[i-1][j-1]*2+int(s[i-1]=='1'))
        ret = 1
        for i in range(1, n+1):
            for j in range(n+1):
                if dp[i][j] <= k: 
                    ret = max(ret, j)
        return ret            
        



if __name__ == "__main__":
    print(Solution().longestSubsequence(s = "1001010", k = 5))
    print(Solution().longestSubsequence(s = "00101001", k = 1))
    print(Solution().longestSubsequence2(s = "1001010", k = 5))
    print(Solution().longestSubsequence2(s = "00101001", k = 1))