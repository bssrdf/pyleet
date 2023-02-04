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
from itertools import accumulate

class Solution:
    def maxProduct(self, s: str) -> int:
        #Wrong
        print("s length", len(s))
        magic_prime = 32416189573
        def maxLengthPalin(t):
            # print('t:', t)
            if not t: return -1, 0
            if len(t) == 1: return 0, 1
            if len(t) == 2: return (1, 2) if t[0] == t[1] else (-1, 0)            
            res, l, r = -1, 0, len(t)+1
            def findPalin(m):
                # print('m = ', m)
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
                    # if i>=m-1:
                        # print('i, t, curHash', i, t[i-m+1:i+1], curHash)
                    if i >= m-1:
                        pos[curHash].add(i)
                # print('m, pos', m, pos)
                curHash = 0
                for i in range(len(t)-1, -1, -1):
                    idx = ord(t[i]) - 97
                    if i <= len(t)-m-1:
                        curHash = 26*(curHash-Pm*(ord(t[i+m]) - 97)) + idx 
                    else: 
                        curHash = curHash*26 + idx
                    curHash %= magic_prime
                    # print('i, t, curHash', i, t[i], curHash)
                    if i <= len(t)-m and curHash in pos:
                        return pos[curHash].pop()
                return -1
            while l < r:
                mid = l + (r-l)//2
                k = findPalin(mid)
                # print("mid, k", mid, k)
                if k == -1:
                    r = mid 
                else:
                    l = mid + 1
                    res = k
            return res, l-1  
        idx, lth1 = maxLengthPalin(s)
        print('idx,lth1', idx, lth1)
        # if lth1 == len(s): return 1
        l, r = idx-lth1, idx
        idx, lth2 = maxLengthPalin(s[:l+1])
        print('idx,lth2', idx, lth2)
        idx, lth3 = maxLengthPalin(s[r+1:])
        print('idx,lth3', idx, lth3)
        return lth1 * max(lth2, lth3)
    

    def maxProduct2(self, s: str) -> int:
        def manachers(S):
            # Manacher's Algorithm - Finding all sub-palindromes in O(N)
            # https://cp-algorithms.com/string/manacher.html
            n = len(S)
            #l2r[i] the maximum length of palindrom in S[:i]
            m, l2r = [0]*n, [1]*n # m is d1 array
            l, r = 0, 1 # Initially we set l=0, r=1, which corresponds to the empty string.
            for i in range(n):
                m[i] = 0 if i >= r else min(m[l+r-i], r-i)
                # run trivial algorithm to expand the range(palindrom)
                while i-m[i] >= 0 and i + m[i] < n and S[i - m[i]] == S[i + m[i]]:
                    l2r[i + m[i]] = 2 * m[i] + 1
                    m[i] += 1
                if i + m[i] > r: # update left/right border
                    l = i - m[i]
                    r = i + m[i]
            for i in range(1,n):
                l2r[i] = max(l2r[i], l2r[i-1])
            return l2r
        n = len(s)
        res = 1
        l2r = manachers(s)
        r2l = manachers(s[::-1])
        for i,j  in zip(range(n-1), range(n-2,0,-1)):
            res = max(res, l2r[i]*r2l[j])
        return res
                
    def maxProduct3(self, s: str) -> int:
        mod = 10**9 + 7
        base = 27
        n = len(s)
        forward_hash = [0] * (len(s) + 1)
        backward_hash = [0] * (len(s) + 1)
        for i in range(1, n+1):
            forward_hash[i] = (forward_hash[i-1] * base + (ord(s[i-1]) - ord('a'))) % mod
        for i in range(n-1, -1, -1):
            backward_hash[i] = (backward_hash[i+1] * base + (ord(s[i]) - ord('a'))) % mod
            
        def is_parlin(s, center, l):
            # check if it is a palin, with l being the radius
            # [left, center-1] vs [center+1, right]
            p = pow(base, l, mod)
            left_hash = (forward_hash[center] - forward_hash[center-l] * p) % mod
            right_hash = (backward_hash[center+1] - backward_hash[center+l+1] * p) % mod
            return left_hash == right_hash
        
        # inclusive
        before_idx_max_len = [1] * n
        after_idx_max_len = [1] * n
        
        # for each center, expand
        for i in range(1, n-1):
            max_radius = 1
            if s[i-1] != s[i+1]: # radius = 1 fails
                continue
            # find the largest extention so that [center+1, right] is the same as [left, center-1]
            start, end = 1, min(i, n-i)
            while start + 1 < end:
                mid = (start + end) // 2
                if is_parlin(s, i, mid):
                    start = mid
                else:
                    end = mid
            if i + end < n and is_parlin(s, i, end):
                max_radius = end
            else:
                max_radius = start
                
            left = i - max_radius
            right = i + max_radius
            before_idx_max_len[right] = max(before_idx_max_len[right], 2*max_radius+1)
            after_idx_max_len[left] = max(after_idx_max_len[left], 2*max_radius+1)
        
        # handle trick case1: if ending with i is palin with len, then end with i-1 should be parlin with at least len-2!
        for i in range(n-2, -1, -1):
            before_idx_max_len[i] = max(before_idx_max_len[i], before_idx_max_len[i+1]-2)
        for i in range(1, n):
            after_idx_max_len[i] = max(after_idx_max_len[i], after_idx_max_len[i-1]-2)
        
        # case2: find max till now using next array
        for i in range(n-1, 0, -1):
            before_idx_max_len[i] = max(before_idx_max_len[i-1], before_idx_max_len[i])
        for i in range(n-2, -1, -1):
            after_idx_max_len[i] = max(after_idx_max_len[i+1], after_idx_max_len[i])
        
        # print(before_idx_max_len, after_idx_max_len)
        # find the best possible
        res = 1
        for i in range(n-1):
            res = max(res, before_idx_max_len[i] * after_idx_max_len[i+1])
            
        return res



        

if __name__ == "__main__":
    # print(Solution().maxProduct(s = "ababbb"))
    # print(Solution().maxProduct(s = "zaaaxbbby"))
    # print(Solution().maxProduct(s ="wtbptdhbjqsrwkxccxkwrsqjbhdtpbtw"))
    s = "ggbswiymmlevedhkbdhntnhdbkhdevelmmyiwsbgg"
    print(Solution().maxProduct(s = s))
    print(Solution().maxProduct2(s = s))
    print(Solution().maxProduct3(s = s))
