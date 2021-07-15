'''
-Easy-
*Rolling Hash*
*Rabin Karp*
Implement strStr().

Returns the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Subscribe to see which companies asked this question

Clarification:

What should we return when needle is an empty string? This is a great question to ask during an interview.

For the purpose of this problem, we will return 0 when needle is an empty string. This is 
consistent to C's strstr() and Java's indexOf().

 

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
Example 3:

Input: haystack = "", needle = ""
Output: 0
 

Constraints:

0 <= haystack.length, needle.length <= 5 * 10^4
haystack and needle consist of only lower-case English characters.

'''

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack:
            return -1
        if len(needle) > len(haystack):
            return -1
        for i in range(len(haystack)-len(needle)+1):
            find = True
            for j in range(len(needle)):
                #print i, j, haystack[i+j], needle[j]
                if haystack[i+j] != needle[j]:
                    find = False
                    break
            if find:
                return i
        return -1
    
    def strStrRabinKarp(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0
        if not haystack:
            return -1
        if len(needle) > len(haystack):
            return -1
        m, n = len(needle), len(haystack)
        q = 10**9+7
        d = 26
        h = pow(d, m-1, q)  
        p, t = 0, 0
        for i in range(m):
            p = (d*p+ord(needle[i]))%q
            t = (d*t+ord(haystack[i]))%q        
        for i in range(n-m+1):
            if p == t:
                find = True
                for j in range(m):
                    if haystack[i+j] != needle[j]:
                        find = False
                        break
                if find:
                    return i
            if i < n-m:
                t = (d*(t - ord(haystack[i])*h) + ord(haystack[i+m]))%q
        return -1




if __name__ == "__main__":
    #assert Solution().strStr("abcdefg", "ab") == 0
    #assert Solution().strStr("abcdefg", "bc") == 1
    #assert Solution().strStr("abcdefg", "cd") == 2
    assert Solution().strStr("abcdefg", "fg") == 5
    #assert Solution().strStr("abcdefg", "bcf") == -1
    assert Solution().strStr("a", "a") == 0
    assert Solution().strStrRabinKarp("abcdefg", "fg") == 5
    assert Solution().strStrRabinKarp("a", "a") == 0
    assert Solution().strStrRabinKarp("aaaaa", "bba") == -1
