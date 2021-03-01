'''
-Hard-
*DP*

Given two strings s and t, return the number of distinct subsequences of s which 
equals t.

A string's subsequence is a new string formed from the original string by 
deleting some (can be none) of the characters without disturbing the 
remaining characters' relative positions. (i.e., "ACE" is a subsequence of 
"ABCDE" while "AEC" is not).

It is guaranteed the answer fits on a 32-bit signed integer.

 

Example 1:

Input: s = "rabbbit", t = "rabbit"
Output: 3
Explanation:
As shown below, there are 3 ways you can generate "rabbit" from S.
rabbbit
rabbbit
rabbbit
Example 2:

Input: s = "babgbag", t = "bag"
Output: 5
Explanation:
As shown below, there are 5 ways you can generate "bag" from S.
babgbag
babgbag
babgbag
babgbag
babgbag
 

Constraints:

0 <= s.length, t.length <= 1000
s and t consist of English letters.

'''


class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
        for j in range(m+1): 
            #若原字符串不为空，而子序列为空，也返回1，因为空串也是任意字符串的一个子序列。
            dp[0][j] = 1
        for i in range(1, n+1): 
            for j in range(1, m+1):
                """
                The first case is easy to catch. When the new character in s, s[j-1], 
                is not equal with the head char in t, t[i-1], we can no longer increment 
                the number of distinct subsequences, it is the same as the situation 
                before incrementing the s, so dp[i][j] = dp[i][j-1].

                However, when the new incrementing character in s, s[j-1] is equal 
                with t[j-1], which contains two case:

                We don't match those two characters, which means that it still has 
                original number of distinct subsequences, so dp[i][j] = dp[i][j-1].

                We match those two characters, in this way. dp[i][j] = dp[i-1][j-1];
                Thus, including both two case, dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
                """
                dp[i][j] = dp[i][j - 1] + (dp[i - 1][j - 1] if t[i - 1] == s[j - 1] else 0)
        return dp[n][m]

if __name__ == '__main__':   
    """
      Ø r a b b b i t
    Ø 1 1 1 1 1 1 1 1
    r 0 1 1 1 1 1 1 1
    a 0 0 1 1 1 1 1 1
    b 0 0 0 1 2 3 3 3
    b 0 0 0 0 1 3 3 3
    i 0 0 0 0 0 0 3 3
    t 0 0 0 0 0 0 0 3 

    """
    print(Solution().numDistinct("rabbbit", "rabbit"))
    """
      Ø b a b g b a g
    Ø 1 1 1 1 1 1 1 1
    b 0 1 1 2 2 3 3 3
    a 0 0 1 1 1 1 4 4
    g 0 0 0 0 1 1 1 5

    """
    print(Solution().numDistinct("babgbag", "bag"))