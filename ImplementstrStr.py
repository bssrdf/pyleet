'''
-Easy-
*Rolling Hash*
*Rabin Karp*
*KMP*
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
from collections import defaultdict

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
    
    def strStrSunday(self, haystack, needle):
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
        skip = defaultdict(int)
        for i,c in enumerate(needle):
            skip[c] = m-i
        idx = 0
        while idx < n-m+1:
            j = idx
            while j < idx+m:
                if needle[j-idx] != haystack[j]:
                    break
                j += 1
            if j != idx+m:
                #c = haystack[idx+m]
                k = idx+m
                if k < n and haystack[k] in skip:
                    idx += skip[haystack[k]]
                else:
                    idx += m
            else:
                return idx
        return -1

    def strStrKMP(self, haystack, needle):
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
        def partialMatchTable(P):
            pt = [0]*m
            k = 0
            for q in range(1,m):                
                while k > 0 and P[k] != P[q]:
                    k = pt[k-1] # note the difference from CLRS text which has k = pt[k]
                if P[k] == P[q]:
                    k += 1
                pt[q] = k
            return pt
        table = partialMatchTable(needle)
        j = 0        
        for i in range(n):            
            while j > 0 and needle[j] != haystack[i]:
                j = table[j-1] # note the difference from CLRS text which has k = pt[k]
            if needle[j] == haystack[i]:
                j += 1 
            if j == m:
                return i-m+1 # note the difference from CLRS text which has i-m
        return -1

    def strStrKMP2(self, haystack, needle):
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
        b = [0] * (m + 1)
        i, j = 0, -1
        b[i] = j
        # prepare roll-back table
        while i < m:
            # roll-back
            while j >= 0 and needle[i] != needle[j]:                 
                j = b[j]
            j += 1
            i += 1 
            b[i] = j
        
        i = j = 0
        while i < n:
        #for i in range(m):    
            # roll-back
            while j >= 0 and needle[j] != haystack[i]: 
                j = b[j]
            j += 1
            i += 1
            if j == m: 
                return i - m
        return -1    
        
        




if __name__ == "__main__":
    #assert Solution().strStr("abcdefg", "ab") == 0
    #assert Solution().strStr("abcdefg", "bc") == 1
    #assert Solution().strStr("abcdefg", "cd") == 2
    '''
    assert Solution().strStr("abcdefg", "fg") == 5
    #assert Solution().strStr("abcdefg", "bcf") == -1
    assert Solution().strStr("a", "a") == 0
    assert Solution().strStrRabinKarp("abcdefg", "fg") == 5
    assert Solution().strStrRabinKarp("a", "a") == 0
    assert Solution().strStrRabinKarp("aaaaa", "bba") == -1
    assert Solution().strStrSunday("aaaaa", "aab") == -1
    assert Solution().strStrSunday("hello", "ll") == 2
    assert Solution().strStrSunday("mississippi","a") == -1
    assert Solution().strStrSunday("mississippi","issi") == 1
    '''
    assert Solution().strStrKMP("aaaaa", "aab") == -1
    assert Solution().strStrKMP("hello", "ll") == 2
    assert Solution().strStrKMP("mississippi","a") == -1
    assert Solution().strStrKMP("mississippi","issi") == 1
    #'''
    
    # this test case will fail Sunday and Brute Force with TLE
    #  only Rabin-Karp and KMP can pass AC  
    source = "a"*99999+'b'+"a"*99999
    target = "a"*100000
   # from collections import Counter
   # cs = Counter(source)
   # ct = Counter(target)
    #print(cs, ct) 
    #print(Solution().strStrSunday(source, target))
    print(Solution().strStrRabinKarp(source, target))
    print(Solution().strStrKMP(source, target))
    #'''
    


            
