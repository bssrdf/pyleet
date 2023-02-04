'''
-Hard-
*KMP*

A string is called a happy prefix if is a non-empty prefix which is also a 
suffix (excluding itself).

Given a string s, return the longest happy prefix of s. Return an empty 
string "" if no such prefix exists.

 

Example 1:

Input: s = "level"
Output: "l"
Explanation: s contains 4 prefix excluding itself ("l", "le", "lev", "leve"), and suffix ("l", "el", "vel", "evel"). The largest prefix which is also suffix is given by "l".
Example 2:

Input: s = "ababab"
Output: "abab"
Explanation: "abab" is the largest prefix which is also suffix. They can overlap in the original string.
Example 3:

Input: s = "leetcodeleet"
Output: "leet"
Example 4:

Input: s = "a"
Output: ""
 

Constraints:

1 <= s.length <= 10^5
s contains only lowercase English letters.

'''

class Solution(object):
    def longestPrefix(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        lps = [0]*n
        k = 0
        for q in range(1,n):
            while k > 0 and s[k] != s[q]:
                k = lps[k-1]
            if s[k] == s[q]:
                k += 1
            lps[q] = k
        print(lps)
        return "" if lps[-1] == 0 else s[n-lps[-1]:n]





if __name__ == "__main__":   
    print(Solution().longestPrefix("level"))
    print(Solution().longestPrefix("ababab"))
    print(Solution().longestPrefix("leetcodeleet"))
    print(Solution().longestPrefix("a"))
    print(Solution().longestPrefix("bba"))