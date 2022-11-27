'''
-Hard-

Given a string of digits s, return the number of palindromic subsequences of s having length 5. Since the answer may be very large, return it modulo 109 + 7.

Note:

A string is palindromic if it reads the same forward and backward.
A subsequence is a string that can be derived from another string by deleting some or no characters without changing the order of the remaining characters.
 

Example 1:

Input: s = "103301"
Output: 2
Explanation: 
There are 6 possible subsequences of length 5: "10330","10331","10301","10301","13301","03301". 
Two of them (both equal to "10301") are palindromic.
Example 2:

Input: s = "0000000"
Output: 21
Explanation: All 21 subsequences are "00000", which is palindromic.
Example 3:

Input: s = "9999900000"
Output: 2
Explanation: The only two palindromic subsequences are "99999" and "00000".
 

Constraints:

1 <= s.length <= 104
s consists of digits.


'''

class Solution:
    def countPalindromes(self, s: str) -> int:
        mod, n, ans = 10 ** 9 + 7, len(s), 0
        pre, cnts = [[[0] * 10 for _ in range(10)] for _ in range(n)], [0] * 10
        for i in range(n):
            c = ord(s[i]) - ord('0')
            if i:
                for j in range(10):
                    for k in range(10):
                        pre[i][j][k] = pre[i - 1][j][k] 
                        if k == c: pre[i][j][k] += cnts[j]
            cnts[c] += 1
        suf, cnts = [[[0] * 10 for _ in range(10)] for _ in range(n)], [0] * 10
        for i in range(n - 1, -1, -1):
            c = ord(s[i]) - ord('0')
            if i < n - 1:
                for j in range(10):
                    for k in range(10):
                        suf[i][j][k] = suf[i + 1][j][k]
                        if k == c: suf[i][j][k] += cnts[j]
            cnts[c] += 1
        for i in range(2, n - 2):
            for j in range(10):
                for k in range(10):
                    ans += pre[i - 1][j][k] * suf[i + 1][j][k]
        return ans % mod


if __name__=="__main__":
    print(Solution().countPalindromes(s = "103301"))