'''
-Hard-


You are given a 0-indexed string s and are tasked with finding two non-intersecting palindromic substrings of odd length such that the product of their lengths is maximized.

More formally, you want to choose four integers i, j, k, l such that 0 <= i <= j < k <= l < s.length and both the substrings s[i...j] and s[k...l] are palindromes and have odd lengths. s[i...j] denotes a substring from index i to index j inclusive.

Return the maximum possible product of the lengths of the two non-intersecting palindromic substrings.

A palindrome is a string that is the same forward and backward. A substring is a contiguous sequence of characters in a string.

 

Example 1:

Input: s = "ababbb"
Output: 9
Explanation: Substrings "aba" and "bbb" are palindromes with odd length. product = 3 * 3 = 9.
Example 2:

Input: s = "zaaaxbbby"
Output: 9
Explanation: Substrings "aaa" and "bbb" are palindromes with odd length. product = 3 * 3 = 9.
 

Constraints:

2 <= s.length <= 105
s consists of lowercase English letters.



'''

from collections import defaultdict
class Solution:
    def maxProduct(self, s: str) -> int:
        magic_prime = 32416189573
        def maxLengthPalin(t):
            print('t:', t)
            if not t: return -1, 0
            res, l, r = -1, 0, len(t)
            def findPalin(m):
                print('m = ', m)
                curHash = 0
                Pm = pow(26, m-1, magic_prime)
                pos = defaultdict(set)
                for i in range(len(t)):
                    idx = ord(t[i]) - 97
                    if i >= m:
                        curHash = 26*(curHash-Pm*(ord(t[i-m]) - 97)) + idx 
                    else: 
                        curHash = curHash*26 + idx
                    curHash %= magic_prime    
                    pos[curHash].add(i)
                curHash = 0
                for i in range(len(t)-1, -1, -1):
                    idx = ord(t[i]) - 97
                    if i <= len(t)-m-1:
                        curHash = 26*(curHash-Pm*(ord(t[i+m]) - 97)) + idx 
                    else: 
                        curHash = curHash*26 + idx
                    curHash %= magic_prime
                    if curHash in pos:
                        return pos[curHash].pop()
                return -1
            while l < r:
                mid = l + (r-l)//2
                k = findPalin(mid)
                if k == -1:
                    r = mid 
                else:
                    l = mid + 1
                    res = k
            return res, l  
        idx, lth1 = maxLengthPalin(s)
        l, r = idx-lth1, idx
        idx, lth2 = maxLengthPalin(s[:l])
        idx, lth3 = maxLengthPalin(s[r:])
        return lth1 * max(lth2, lth3)



        

if __name__ == "__main__":
    print(Solution().maxProduct(s = "ababbb"))