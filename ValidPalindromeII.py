'''

-Easy-

Given a non-empty string s, you may delete at most one character. Judge whether you can 
make it a palindrome.

Example 1:
Input: "aba"
Output: True
Example 2:
Input: "abca"
Output: True
Explanation: You could delete the character 'c'.
Note:
The string will only contain lowercase characters a-z. The maximum length of the string is 50000.

'''

class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        left, right = 0, n-1
        def isValid(s, l, r):
            i, j = l, r
            while i <= j:
                if s[i] != s[j]: return False
                i += 1
                j -= 1
            return True
        while left <= right:
            if s[left] != s[right]:
                return isValid(s, left, right-1) or isValid(s, left+1, right)
            left += 1
            right -= 1
        return True



if __name__ == "__main__":
    print(Solution().validPalindrome("abca"))
    print(Solution().validPalindrome("aba"))
    print(Solution().validPalindrome("abvea"))
