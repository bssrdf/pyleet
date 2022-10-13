'''

-Easy-

A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

 

Example 1:

Input: s = "YazaAay"
Output: "aAa"
Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.
Example 2:

Input: s = "Bb"
Output: "Bb"
Explanation: "Bb" is a nice string because both 'B' and 'b' appear. The whole string is a substring.
Example 3:

Input: s = "c"
Output: ""
Explanation: There are no nice substrings.
 

Constraints:

1 <= s.length <= 100
s consists of uppercase and lowercase English letters.


'''

from collections import Counter
from re import T

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        n = len(s)
        ans = ''
        for i in range(n):
            for j in range(i, n):
               t = s[i:j+1] 
               cnt = Counter(t)            
               flag = True
               for c in cnt:
                   if c.islower() and cnt[c.upper()] == 0:  
                       flag = False
                   if c.isupper() and cnt[c.lower()] == 0:  
                       flag = False
               if flag and j-i+1 > len(ans):
                    ans = t
        return ans 
    
    def longestNiceSubstring2(self, s: str) -> str:
        if len(s) < 2: return ""
        st = set(s)
        for i in range(len(s)):
            c = s[i]
            if c.upper() in st and c.lower() in st:
                continue 
            sub1 = self.longestNiceSubstring(s[:i+1])
            sub2 = self.longestNiceSubstring(s[i+1:])
            return sub1 if len(sub1) >= len(sub2) else sub2
        return s    




        
if __name__ == "__main__":   
    print(Solution().longestNiceSubstring(s = "YazaAay"))
    print(Solution().longestNiceSubstring(s = "Bb"))
    print(Solution().longestNiceSubstring2(s = "YazaAay"))
    print(Solution().longestNiceSubstring2(s = "Bb"))
