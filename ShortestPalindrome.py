'''
-Hard-
*KMP*

You are given a string s. You can convert s to a palindrome by adding characters in front of it.

Return the shortest palindrome you can find by performing this transformation.

 

Example 1:

Input: s = "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: s = "abcd"
Output: "dcbabcd"
 

Constraints:

0 <= s.length <= 5 * 10^4
s consists of lowercase English letters only.

'''

class Solution(object):
    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        i, n = 0, len(s)
        for j in range(n - 1, -1, -1):
            if s[i] == s[j]: 
                i += 1
                print(i,j)
        if i == n: return s
        rem = s[i:]
        print(i,rem)
        return rem[::-1] + self.shortestPalindrome(s[:i]) + s[i:]
    
    def shortestPalindromeKMP(self, s):
        """
        :type s: str
        :rtype: str
        """
        snew = s + "#" + s[::-1] 
        print(snew)
        def partialMatchTable(P):
            m = len(P)
            pt = [0]*m
            k = 0
            for q in range(1,m):                
                while k > 0 and P[k] != P[q]:
                    k = pt[k-1] # note the difference from CLRS text which has k = pt[k]
                if P[k] == P[q]:
                    k += 1
                pt[q] = k
            return pt
        table = partialMatchTable(snew)
        print(table)
        t = s[table[-1]:]
        return t[::-1]+s 
if __name__ == "__main__":
    #print(Solution().shortestPalindrome("aacecaaa"))
    #print(Solution().shortestPalindrome("adcababa"))
    #print(Solution().shortestPalindromeKMP("adcababa"))
    print(Solution().shortestPalindromeKMP("adcaadcbaba"))
    #print(Solution().shortestPalindromeKMP("acababa"))
    #print(Solution().shortestPalindromeKMP("aacecaaa"))