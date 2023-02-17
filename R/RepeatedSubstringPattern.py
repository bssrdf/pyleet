'''
-Easy-

Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.


'''

def zarray(s):
    n = len(s)
    z = [0]*n
    # [L,R] make a window which matches
    # with prefix of s
    left, right, k = 0, 0, 0
    for i in range(1, n):
        # if i>R nothing matches so we will calculate.
        # Z[i] using naive way.
        if i > right:
            left, right = i, i
            # R-L = 0 in starting, so it will start
            # checking from 0'th index.
            while right < n and s[right - left] == s[right]:
                right += 1
            z[i] = right - left
            right -= 1
        else:
            # k = i-L so k corresponds to number which
            # matches in [L,R] interval.
            k = i - left
            # if Z[k] is less than remaining interval
            if z[k] < right - i + 1:
                z[i] = z[k]
            else:
                # else start from R and check manually
                left = i
                while right < n and s[right - left] == s[right]:
                    right += 1
                z[i] = right - left
                right -= 1
    return z


class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(n//2, 0, -1):
            if n % i == 0:
                c = n // i
                t = s[0:i]*c
                if t == s:
                    return True
        return False
    
    def repeatedSubstringPattern2(self, s: str) -> bool:
        n = len(s)
        Z = zarray(s)
        print(Z)
        for i,z in enumerate(Z):
            if z == (n-i) and n % (i) == 0:
                return True
                        
        return False
    
if __name__ == '__main__':
   print(Solution().repeatedSubstringPattern(s = "abcabcabcabc"))
   print(Solution().repeatedSubstringPattern2(s = "abcabcabcabc"))
   print(Solution().repeatedSubstringPattern2(s = "abab"))
   print(Solution().repeatedSubstringPattern2(s = "aba"))