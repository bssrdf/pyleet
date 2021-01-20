'''
-Medium-

Given a string s, find the longest palindromic subsequence's length in s. You 
may assume that the maximum length of s is 1000.

Example 1:
Input:

"bbbab"
Output:
4
One possible longest palindromic subsequence is "bbbb".
 

Example 2:
Input:

"cbbd"
Output:
2
One possible longest palindromic subsequence is "bb".
 

Constraints:

1 <= s.length <= 1000
s consists only of lowercase English letters.


'''

class Solution(object):
    def longestPalindromeSubseq(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)        
        if n <= 1: return n
        # dp[i][j]: max length of palindrom in substring s[i..j]
        dp = [[0 for _ in range(n)] for _ in range(n)]        
        for l in range(1, n+1): # the order of iteration is 1) length of substring            
            for i in range(0, n-l+1): # 2) index of the start of substring 
                j = i+l-1
                if i == j:
                    dp[i][j] = 1 #base case: length 1 substring is a palindrom               
                    continue         
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])                 
        return dp[0][n-1]

    def longestPalindromeSubseqO1Space(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)        
        if n <= 1: return n
        # dp0: sol. of length l
        # dp1: sol. of length l-1
        # dp2: sol. of length l-2
        dp0, dp1, dp2 = [0]*n, [0]*n, [0]*n
        for l in range(1, n+1):            
            for i in range(0, n-l+1):
                j = i+l-1
                if i == j:
                    dp0[i] = 1                
                    continue
                if s[i] == s[j]:
                    dp0[i] = dp2[i+1] + 2                
                else:
                    dp0[i] = max(dp1[i+1], dp1[i])                 
            dp0, dp1, dp2 = dp2, dp0, dp1             
        return dp1[0]

    def longestPalindromeSubseqMemo(self, s):
        """
        :type s: str
        :rtype: int
        """

        n = len(s)        
        if n <= 1: return n        
        memo = [[-1 for _ in range(n)] for _ in range(n)]        
        def helper(i,j):
            if memo[i][j] != -1: return memo[i][j]
            if i > j:  return 0
            if i == j: return 1
            if s[i] == s[j]:
                memo[i][j] = helper(i+1, j-1)+2
            else:
                memo[i][j] = max(helper(i+1,j), helper(i,j-1))
            return memo[i][j]
        return helper(0, n-1)



if __name__ == "__main__":
    print(Solution().longestPalindromeSubseq("bbbab"))
    print(Solution().longestPalindromeSubseqO1Space("bbbab"))
    print(Solution().longestPalindromeSubseqMemo("bbbab"))