'''

-Hard-
*DP*


Given a string s, return true if it is possible to split the string s into three non-empty palindromic substrings. Otherwise, return false.​​​​​

A string is said to be palindrome if it the same string when reversed.

 

Example 1:

Input: s = "abcbdd"
Output: true
Explanation: "abcbdd" = "a" + "bcb" + "dd", and all three substrings are palindromes.
Example 2:

Input: s = "bcbddxy"
Output: false
Explanation: s cannot be split into 3 palindromes.
 

Constraints:

3 <= s.length <= 2000
s​​​​​​ consists only of lowercase English letters.

'''

class Solution:
    def checkPartitioning(self, s: str) -> bool:
        n = len(s)
        dp = [[False]*n for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(i, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] if i+1 <= j-1 else True 
                else:
                    dp[i][j] = False
        for i in range(1, n-1):
            for j in range(i, n-1):
                if dp[0][i-1] and dp[i][j] and dp[j+1][n-1]:
                    return True
        return False

        