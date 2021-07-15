'''
-Hard-

You are given a string s. You can convert s to a palindrome by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.

 

Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: s = "abcd"
Output: "dcbabcd"
 

Constraints:

0 <= s.length <= 5 * 10^4
s consists of lowercase English letters only.

'''

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i, n = 0, len(s)
        for j in range(n - 1, -1, -1):
            if s[i] == s[j]: i += 1
        if i == n: return s
        rem = s[i:]
        return rem[::-1] + self.shortestPalindrome(s[:i]) + s[i:]

if __name__ == "__main__":
    print(Solution().shortestPalindrome("aacecaaa"))