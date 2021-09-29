'''
-Easy-

Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by 
deleting some (can be none) of the characters without disturbing the relative positions 
of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

 

Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false
 

Constraints:

0 <= s.length <= 100
0 <= t.length <= 10^4
s and t consist only of lowercase English letters.
 

Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, 
and you want to check one by one to see if t has its subsequence. In this scenario, 
how would you change your code?

'''
import bisect as bi
from collections import defaultdict

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = j = 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1; j += 1
            else:
                j += 1
        return i == len(s)  
    def isSubsequence2(self, s: str, t: str) -> bool:    
        # for followup, preprocess t
        # binary search the succesive position of s's character 
        # in the index arrays of each t's character
        idx = defaultdict(list)
        for i, c in enumerate(t):
            idx[c].append(i)
        print(idx)
        prev = 0
        for i, c in enumerate(s):            
            j = bi.bisect_left(idx[c], prev)
            if j == len(idx[c]): return False
            prev = idx[c][j] + 1
            print('prev:', prev)
        return True        


        

if __name__ == "__main__": 
    print(Solution().isSubsequence(s = "abc", t = "ahbgdc"))
    print(Solution().isSubsequence(s = "axc", t = "ahbgdc"))
    print(Solution().isSubsequence2(s = "abc", t = "ahbgdc"))
    print(Solution().isSubsequence2(s = "axc", t = "ahbgdc"))