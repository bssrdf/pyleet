'''
Given a string s and an integer k, find out if the given string is a K-Palindrome or not.

A string is K-Palindrome if it can be transformed into a palindrome by removing at most 
k characters from it.

 

Example 1:

Input: s = "abcdeca", k = 2
Output: true
Explanation: Remove 'b' and 'e' characters.
 

Constraints:

1 <= s.length <= 1000
s has only lowercase English letters.
1 <= k <= s.length
Hints
Can you reduce this problem to a classic problem?
The problem is equivalent to finding any palindromic subsequence of length at least N-K where N is the length of the string.
Try to find the longest palindromic subsequence.
Use DP to do that.

'''

class Solution(object):
    def isValidPalindrome(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
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
            if dp1[0] >= (n-k): return True
        return False

    
if __name__ == "__main__":
    print(Solution().isValidPalindrome(s = "abcdeca", k = 2))