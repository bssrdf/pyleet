'''

-Hard-
*DP*

You are given a string s and a positive integer k.

Select a set of non-overlapping substrings from the string s that satisfy the following conditions:

The length of each substring is at least k.
Each substring is a palindrome.
Return the maximum number of substrings in an optimal selection.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "abaccdbbd", k = 3
Output: 2
Explanation: We can select the substrings underlined in s = "abaccdbbd". Both "aba" and "dbbd" are palindromes and have a length of at least k = 3.
It can be shown that we cannot find a selection with more than two valid substrings.
Example 2:

Input: s = "adbcda", k = 2
Output: 0
Explanation: There is no palindrome substring of length at least 2 in the string.
 

Constraints:

1 <= k <= s.length <= 2000
s consists of lowercase English letters.

'''

class Solution:
    def maxPalindromes(self, s: str, k: int) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        for i in range(k, n + 1):
            dp[i] = dp[i - 1]
            for length in range(k, k + 2):
                j = i - length
                if j < 0:
                    break
                if self.isPalindrome(s, j, i):
                    dp[i] = max(dp[i], 1 + dp[j])
        return dp[-1]
    
    
    def isPalindrome(self, s, j, i):
        left, right = j, i - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True

if __name__ == "__main__":
    print(Solution().maxPalindromes(s = "abaccdbbd", k = 3))
