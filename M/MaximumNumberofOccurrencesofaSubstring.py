'''
-Medium-

Given a string s, return the maximum number of ocurrences of any 
substring under the following rules:

The number of unique characters in the substring must be less 
than or equal to maxLetters.

The substring size must be between minSize and maxSize inclusive.
 

Example 1:

Input: s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4
Output: 2
Explanation: Substring "aab" has 2 ocurrences in the original string.
It satisfies the conditions, 2 unique letters and size 3 (between minSize and maxSize).
Example 2:

Input: s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3
Output: 2
Explanation: Substring "aaa" occur 2 times in the string. It can overlap.
Example 3:

Input: s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3
Output: 3
Example 4:

Input: s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3
Output: 0
 

Constraints:

1 <= s.length <= 10^5
1 <= maxLetters <= 26
1 <= minSize <= maxSize <= min(26, s.length)
s only contains lowercase English letters.



'''

from collections import Counter

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        n, m = len(s), Counter()
        left, right = 0, 0
        oc = Counter()
        while right < n:
            c = s[right]
            m[c] += 1
            right += 1
            while len(m) > maxLetters:                
                m[s[left]] -= 1
                if m[s[left]] == 0:
                    m.pop(s[left])
                left += 1
            while minSize <= right-left <= maxSize:
                oc[s[left:right]] += 1  
                m[s[left]] -= 1
                if m[s[left]] == 0:
                    m.pop(s[left])
                left += 1            
        #print(oc)
        return max(oc.values()) if oc else 0


        
if __name__ == "__main__":
    print(Solution().maxFreq(s = "aababcaab", maxLetters = 2, minSize = 3, maxSize = 4))
    print(Solution().maxFreq(s = "aaaa", maxLetters = 1, minSize = 3, maxSize = 3))
    print(Solution().maxFreq(s = "aabcabcab", maxLetters = 2, minSize = 2, maxSize = 3))
    print(Solution().maxFreq(s = "abcde", maxLetters = 2, minSize = 3, maxSize = 3))