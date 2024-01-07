'''
-Medium-

You are given a string s that consists of lowercase English letters.

A string is called special if it is made up of only a single character. For example, the string "abc" is not special, whereas the strings "ddd", "zz", and "f" are special.

Return the length of the longest special substring of s which occurs at least thrice, or -1 if no special substring occurs at least thrice.

A substring is a contiguous non-empty sequence of characters within a string.

 

Example 1:

Input: s = "aaaa"
Output: 2
Explanation: The longest special substring which occurs thrice is "aa": substrings "aaaa", "aaaa", and "aaaa".
It can be shown that the maximum length achievable is 2.
Example 2:

Input: s = "abcdef"
Output: -1
Explanation: There exists no special substring which occurs at least thrice. Hence return -1.
Example 3:

Input: s = "abcaba"
Output: 1
Explanation: The longest special substring which occurs thrice is "a": substrings "abcaba", "abcaba", and "abcaba".
It can be shown that the maximum length achievable is 1.
 

Constraints:

3 <= s.length <= 5 * 105
s consists of only lowercase English letters.


'''

from collections import defaultdict

class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        length = [[0]*(n+1) for _ in range(26)]
        i = 0
        while i < n:
            j = i
            while j+1 < n and s[j+1] == s[j]:
                j += 1
            k, c = j-i+1, ord(s[i])-ord('a')
            length[c][k] += 1   
            if k > 1:
                length[c][k-1] += 2   
            if k > 2:
                length[c][k-2] = 3 
            i = j+1
        ans = -1
        for i in range(26):
            for j in range(n, 0, -1):            
                if length[i][j] >= 3:
                    ans = max(ans, j)
        # for r in length:
        #     print(r)   
        return ans   
    
    def maximumLength2(self, s: str) -> int:
        n = len(s)
        st = set(s)
        length = { c:[0]*(n+1) for c in st}
        i = 0
        while i < n:
            j = i
            while j+1 < n and s[j+1] == s[j]:
                j += 1
            k = j-i+1
            length[s[i]][k] += 1   
            if k > 1:
                length[s[i]][k-1] += 2   
            if k > 2:
                length[s[i]][k-2] = 3 
            i = j+1
        ans = -1
        for c in length:
            for j in range(n, 0, -1):            
                if length[c][j] >= 3:
                    ans = max(ans, j)
        # for r in length:
        #     print(r)   
        return ans   
    
    def maximumLength3(self, s: str) -> int:
        n = len(s)
        st = set(s)
        length = { c:defaultdict(int) for c in st}
        i = 0
        while i < n:
            j = i
            while j+1 < n and s[j+1] == s[j]:
                j += 1
            k = j-i+1
            length[s[i]][k] += 1   
            if k > 1:
                length[s[i]][k-1] += 2   
            if k > 2:
                length[s[i]][k-2] = 3 
            i = j+1
        ans = -1
        for c in length:
            for j in length[c]:
                if length[c][j] >= 3:
                    ans = max(ans, j)
        # for r in length:
        #     print(r)   
        return ans   



if __name__ == "__main__":
    print(Solution().maximumLength(s = "aaaa"))
    print(Solution().maximumLength(s = "abcdef"))
    print(Solution().maximumLength(s = "abcaba"))
    print(Solution().maximumLength(s = "aeeeerrree"))
    print(Solution().maximumLength2(s = "aaaa"))
    print(Solution().maximumLength2(s = "abcdef"))
    print(Solution().maximumLength2(s = "abcaba"))
    print(Solution().maximumLength2(s = "aeeeerrree"))
    print(Solution().maximumLength3(s = "aeeeerrree"))