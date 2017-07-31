# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 20:14:31 2017

Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.



@author: merli
"""
import string

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        charPos = {}        
        sb = 0
        maxl = 0        
        for i,c in enumerate(s):
            if c in charPos:
                sb = max(sb, charPos[c]+1)               
            charPos[c] = i
            maxl = max(maxl, i-sb+1)            
        return maxl
        
if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring("bbbbbb") == 1
    