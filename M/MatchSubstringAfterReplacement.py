'''

-Hard-
*KMP*

You are given two strings s and sub. You are also given a 2D character array mappings where mappings[i] = [oldi, newi] indicates that you may replace any number of oldi characters of sub with newi. Each character in sub cannot be replaced more than once.

Return true if it is possible to make sub a substring of s by replacing zero or more characters according to mappings. Otherwise, return false.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: s = "fool3e7bar", sub = "leet", mappings = [["e","3"],["t","7"],["t","8"]]
Output: true
Explanation: Replace the first 'e' in sub with '3' and 't' in sub with '7'.
Now sub = "l3e7" is a substring of s, so we return true.
Example 2:

Input: s = "fooleetbar", sub = "f00l", mappings = [["o","0"]]
Output: false
Explanation: The string "f00l" is not a substring of s and no replacements can be made.
Note that we cannot replace '0' with 'o'.
Example 3:

Input: s = "Fool33tbaR", sub = "leetd", mappings = [["e","3"],["t","7"],["t","8"],["d","b"],["p","b"]]
Output: true
Explanation: Replace the first and second 'e' in sub with '3' and 'd' in sub with 'b'.
Now sub = "l33tb" is a substring of s, so we return true.

 

Constraints:

1 <= sub.length <= s.length <= 5000
0 <= mappings.length <= 1000
mappings[i].length == 2
oldi != newi
s and sub consist of uppercase and lowercase English letters and digits.
oldi and newi are either uppercase or lowercase English letters or digits.

'''

from typing import List

class Solution:
    def matchReplacement(self, s: str, sub: str, mappings: List[List[str]]) -> bool:
        table = [[False]*128 for _ in range(128)]
        for x in mappings:
            table[ord(x[0])][ord(x[1])] = True
        def match(s, t):
            return s == t or table[ord(t)][ord(s)]
        def strStr(haystack, needle):        
            if not needle:
                return 0
            if not haystack:
                return -1
            if len(needle) > len(haystack):
                return -1
            m, n = len(needle), len(haystack)    
            def partialMatchTable(P):
                pt = [0]*m
                k = 0
                for q in range(1,m): # start matching at index 1, no need to match itself                
                    while k > 0 and not match(P[k], P[q]): 
                        k = pt[k-1] # note the difference from CLRS text which has k = pt[k]
                    if match(P[k], P[q]):
                        k += 1
                    pt[q] = k
                return pt
            suffix = partialMatchTable(needle)
            j = 0        
            for i in range(n):            
                while j > 0 and not match(haystack[i], needle[j]):
                    j = suffix[j-1] # note the difference from CLRS text which has k = pt[k]
                if match(haystack[i], needle[j]):
                    j += 1 
                if j == m:
                    return i-m+1 # note the difference from CLRS text which has i-m
            return -1
        return strStr(s, sub) != -1


if __name__ == "__main__":
    print(Solution().matchReplacement(s = "fool3e7bar", sub = "leet", mappings = [["e","3"],["t","7"],["t","8"]]))