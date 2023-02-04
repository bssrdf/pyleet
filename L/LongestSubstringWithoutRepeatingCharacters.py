# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 20:14:31 2017
-Medium-

*Sliding Window*


Given a string, find the length of the longest substring without repeating 
characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the 
answer must be a substring, "pwke" is a subsequence and not a substring.

The naive approach is very straightforward. But it is too slow. So how can we optimize it?

In the naive approaches, we repeatedly check a substring to see if it has 
duplicate character. But it is unnecessary. If a substring s​_{ij}
from index i to j - 1 is already checked to have no duplicate characters. 
We only need to check if s[j] is already in the substring s_{ij}.

To check if a character is already in the substring, we can scan the substring, 
which leads to an O(n^2) algorithm. But we can do better.

By using HashSet as a sliding window, checking if a character in the current 
can be done in O(1).

A sliding window is an abstract concept commonly used in array/string problems. 
A window is a range of elements in the array/string which usually defined by 
the start and end indices, i.e. [i, j)(left-closed, right-open). A sliding 
window is a window "slides" its two boundaries to the certain direction. For 
example, if we slide [i, j) to the right by 11 element, then it becomes [i+1, j+1)
(left-closed, right-open).

Back to our problem. We use HashSet to store the characters in current 
window [i, j) (j = i initially). Then we slide the index j to the right. 
If it is not in the HashSet, we slide j further. Doing so until s[j] is already 
in the HashSet. At this point, we found the maximum size of substrings without 
duplicate characters start with index i. If we do this for all i, we get our answer.

@author: merli
"""
import string
from collections import defaultdict

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


    def lengthOfLongestSubstringTemplate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        charPos = defaultdict(int)
        n, left, right = len(s), 0, 0
        maxl = 0
        while right < n:
            c = s[right]                    
            right += 1
            charPos[c] += 1
            while charPos[c] > 1: # found a repeated character in the window
                d = s[left]
                left += 1        # shrink the left 
                charPos[d] -= 1  # until repeated character becomes unique again   
            # [left, right) is the window without repeated characters.    
            # we can update result now
            maxl = max(maxl, right-left)            
        return maxl
        
if __name__ == "__main__":
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring("bbbbbb") == 1
    assert Solution().lengthOfLongestSubstringTemplate("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstringTemplate("bbbbbb") == 1