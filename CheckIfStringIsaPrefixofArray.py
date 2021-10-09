'''
-Easy-

Given a string s and an array of strings words, determine whether s is a prefix string of words.

A string s is a prefix string of words if s can be made by concatenating the first k strings in words for some positive k no larger than words.length.

Return true if s is a prefix string of words, or false otherwise.

 

Example 1:

Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
Output: true
Explanation:
s can be made by concatenating "i", "love", and "leetcode" together.
Example 2:

Input: s = "iloveleetcode", words = ["apples","i","love","leetcode"]
Output: false
Explanation:
It is impossible to make s using a prefix of arr.
 

Constraints:

1 <= words.length <= 100
1 <= words[i].length <= 20
1 <= s.length <= 1000
words[i] and s consist of only lowercase English letters.

'''
from typing import List

class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        i, j, k = 0, 0, 0
        while i < len(s) and j < len(words):
            k = 0
            while i < len(s) and k < len(words[j]):
                if s[i] != words[j][k]: return False
                k += 1
                i += 1
            if k != len(words[j]): return False
            j += 1    
        if j == len(words) and i < len(s): return False
        return True