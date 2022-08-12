'''
-Medium-

Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 

Example 1:

Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")
Example 2:

Input: s = "adc"
Output: 0
Explanation: There are no palindromic subsequences of length 3 in "adc".
Example 3:

Input: s = "bbcbaba"
Output: 4
Explanation: The 4 palindromic subsequences of length 3 are:
- "bbb" (subsequence of "bbcbaba")
- "bcb" (subsequence of "bbcbaba")
- "bab" (subsequence of "bbcbaba")
- "aba" (subsequence of "bbcbaba")
 

Constraints:

3 <= s.length <= 105
s consists of only lowercase English letters.



'''

from collections import Counter
from string import  ascii_lowercase
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        #TLE
        # cnt = Counter(s)
        res = set()
        for c in s:
            tmp = set()
            for d in res:
                if len(d) == 1:
                    tmp.add(d+c)
                elif len(d) == 2 and d[0] == c:
                    tmp.add(d+c)
            res |= tmp
            if c not in res:
                res.add(c)    
        # print(res)
        return sum(1 for r in res if len(r) == 3)
    

    def countPalindromicSubsequence2(self, s: str) -> int:
        cnt = [0]*26
        for c in s:
            cnt[ord(c)-ord('a')] += 1 
        res = [[0]*26 for _ in range(26)]
        cnt1 = [0]*26
        for c in s:
            idx1 = ord(c)-ord('a')
            for idx in range(26):
                if res[idx1][idx] > 0: continue 
                if cnt1[idx] > 0 and cnt[idx] - (cnt1[idx] + (1 if idx==idx1 else 0)) > 0:
                    res[idx1][idx] = 1 
            cnt1[idx1] += 1

        return sum(sum(r) for r in res)
    
    def countPalindromicSubsequence3(self, s: str) -> int:
        first, last = [len(s)]*26, [0]*26
        for i,c in enumerate(s):
            first[ord(c)-ord('a')] = min(first[ord(c)-ord('a')], i)  
            last[ord(c)-ord('a')] = i  
        res = 0
         
        for i in range(26):
            if first[i] < last[i]:
                res += len(set(s[first[i]+1:last[i]])) 
        return res

    def countPalindromicSubsequence4(self, s):
        res = 0
        for c in ascii_lowercase:
            i, j = s.find(c), s.rfind(c)
            if i > -1:
                res += len(set(s[i + 1: j]))
        return res





if __name__ == "__main__":
    print(Solution().countPalindromicSubsequence(s = "aabca"))
    print(Solution().countPalindromicSubsequence(s = "adc"))
    print(Solution().countPalindromicSubsequence(s = "bbcbaba"))
    print(Solution().countPalindromicSubsequence2(s = "aabca"))
    print(Solution().countPalindromicSubsequence2(s = "adc"))
    print(Solution().countPalindromicSubsequence2(s = "bbcbaba"))
    print(Solution().countPalindromicSubsequence3(s = "aabca"))
    s = "tlpjzdmtwderpkpmgoyrcxttiheassztncqvnfjeyxxp" 
    print(Solution().countPalindromicSubsequence4(s = s))
    print(Solution().countPalindromicSubsequence3(s = s))
    print(Solution().countPalindromicSubsequence2(s = s))


