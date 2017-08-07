"""
Write a function that takes a string as input and returns the string reversed.
"""
__author__ = 'Daniel'

import string

class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = 0
        r = len(s)-1
        ss = list(s)
        while l <= r:
            if  s[l] in string.ascii_letters and s[r] in string.ascii_letters:
                t = ss[l]
                ss[l] = ss[r]
                ss[r] = t
                l += 1
                r -= 1
            elif s[l] in string.ascii_letters:
                r -= 1
            elif s[r] in string.ascii_letters:
                l += 1
            else:
                l += 1
                r -= 1
        return ''.join(ss)


if __name__ == "__main__":
    print Solution().reverseString('he!ll%o')

