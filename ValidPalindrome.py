'''
-Easy-

*Two Pointers*

Given a string s, determine if it is a palindrome, considering only alphanumeric 
characters and ignoring cases.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
 

Constraints:

1 <= s.length <= 2 * 10^5
s consists only of printable ASCII characters.

'''

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        '''
        t = ''
        for c in s:
            if c.isalpha() or c.isdigit():
                t += c if c.isdigit() else c.lower()
        return t == t[::-1]
        '''
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[l].isalnum():
                l += 1
            while l <r and not s[r].isalnum():
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l +=1; r -= 1
        return True

if __name__ == "__main__":
    print(Solution().isPalindrome( "A man, a plan, a canal: Panama"))