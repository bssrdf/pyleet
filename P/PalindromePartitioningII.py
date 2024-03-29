'''
-Hard-
*DP*

Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

 

Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
Example 2:

Input: s = "a"
Output: 0
Example 3:

Input: s = "ab"
Output: 1
 

Constraints:

1 <= s.length <= 2000
s consists of lower-case English letters only.

'''


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        n = len(s)
        dp = [float('inf')]*(n + 1)
        dp[0] = -1
        for i in range(n):
            lth = 0
            while i - lth >= 0 and i + lth < n and s[i - lth] == s[i + lth]:
                dp[i + lth + 1] = min(dp[i + lth + 1], 1 + dp[i - lth])
                lth += 1
            lth = 0
            while i - lth >= 0 and i + lth +1 < n and s[i - lth] == s[i + lth + 1]:
                dp[i + lth + 2] = min(dp[i + lth + 2], 1 + dp[i - lth])
                lth += 1
        return dp[n]     

    def minCutDP(self, s):
        """
        :type s: str
        :rtype: int
        """
        # suppose we know the answer dp[j-1] to the problem s[:j] 
        # if s[j:i] is a palindrom, we know dp[i] = 1+dp[j-1]   
        # conversely, we can construct the solution dp[i] by
        # iterating j from 0 to i and find all palindroms s[j:i]
        # and update dp[i] as min(dp[i], 1+dp[j-1])
        if not s: return 0
        n = len(s)
        dp = [float('inf')] * n   
        pal = [[False for _ in range(n)] for _ in range(n)]     
        for i in range(n):
            dp[i] = i
            for j in range(i+1):
                if s[j] == s[i] and (i-j<=2 or pal[j+1][i-1]):
                    pal[j][i] = True
                    dp[i] = 0 if j == 0 else min(dp[i], 1+dp[j-1])                
            for p in pal:
               print(p)
            print("===========")
        return dp[n-1] 

    def __init__(self, s=None):
        """
        :type s: str
        :rtype: int
        """             
        if s:
            n = len(s)
            self.pal = [[False for _ in range(n)] for _ in range(n)]     
            for i in range(n):
                for j in range(i+1):
                    if s[j] == s[i] and (i-j<=2 or self.pal[j+1][i-1]):
                        self.pal[j][i] = True

    def isPalindrome(self,i,j):    
        return self.pal[i][j]
 
        
if __name__ == "__main__":
    #print(Solution().minCut("aab"))
    #print(Solution().minCutDP("aab"))
    #print(Solution().minCutDP("cabac"))
    s = Solution("cababa")
    print(s.isPalindrome(0,5))