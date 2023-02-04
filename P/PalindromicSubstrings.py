'''
-Medium-

*Brute Force*

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as 
different substrings even they consist of same characters.

Example 1:

Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
 

Example 2:

Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
 

Note:

The input string length won't exceed 1000.


'''

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        ans = 0
        n = len(s)
        def count(l, r):
            cnt = 0
            while l >= 0 and r < n and s[l] == s[r]:
                cnt += 1
                l -= 1
                r += 1
            return cnt
        for i in range(n):
            ans += count(i,i) # odd length
            ans += count(i-1,i) # even length
        return ans

    def countSubstringsDP(self, s):
        """
        :type s: str
        :rtype: int
        """
        n, res = len(s), 0
        # dp[i][j] is true of s[i:j] is a palindrom
        dp = [[False for _ in range(n)] for _ in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i, n):
                dp[i][j] = (s[i] == s[j]) and (j - i <= 2 or dp[i + 1][j - 1])
                if dp[i][j]: res += 1
        return res

        
if __name__ == "__main__":
    print(Solution().countSubstrings("aaa"))
    print(Solution().countSubstringsDP("aaa"))