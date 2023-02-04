'''
-Hard-

You are given a string s (0-indexed)​​​​​​. You are asked to perform the following operation on s​​​​​​ until you get a sorted string:

Find the largest index i such that 1 <= i < s.length and s[i] < s[i - 1].
Find the largest index j such that i <= j < s.length and s[k] < s[i - 1] for all the possible values of k in the range [i, j] inclusive.
Swap the two characters at indices i - 1​​​​ and j​​​​​.
Reverse the suffix starting at index i​​​​​​.
Return the number of operations needed to make the string sorted. Since the answer can be too large, return it modulo 109 + 7.

 

Example 1:

Input: s = "cba"
Output: 5
Explanation: The simulation goes as follows:
Operation 1: i=2, j=2. Swap s[1] and s[2] to get s="cab", then reverse the suffix starting at 2. Now, s="cab".
Operation 2: i=1, j=2. Swap s[0] and s[2] to get s="bac", then reverse the suffix starting at 1. Now, s="bca".
Operation 3: i=2, j=2. Swap s[1] and s[2] to get s="bac", then reverse the suffix starting at 2. Now, s="bac".
Operation 4: i=1, j=1. Swap s[0] and s[1] to get s="abc", then reverse the suffix starting at 1. Now, s="acb".
Operation 5: i=2, j=2. Swap s[1] and s[2] to get s="abc", then reverse the suffix starting at 2. Now, s="abc".
Example 2:

Input: s = "aabaa"
Output: 2
Explanation: The simulation goes as follows:
Operation 1: i=3, j=4. Swap s[2] and s[4] to get s="aaaab", then reverse the substring starting at 3. Now, s="aaaba".
Operation 2: i=4, j=4. Swap s[3] and s[4] to get s="aaaab", then reverse the substring starting at 4. Now, s="aaaab".
 

Constraints:

1 <= s.length <= 3000
s​​​​​​ consists only of lowercase English letters.


'''

from functools import lru_cache

class Solution:
    def makeStringSorted(self, s: str) -> int:
        @lru_cache(None)
        def f(i):
            return 1 if i <= 1 else (f(i-1)*i) % (10**9+7)
        
        @lru_cache(None)
        def inv(i):
            N = 10**9 + 7
            return pow(i, N-2, N)

        N, n, out = 10**9 + 7, len(s), 0
        cnt = [0]*26
        for i in range(n-1, -1, -1):
            ind = ord(s[i]) - ord("a")
            cnt[ind] += 1
            ans = sum(cnt[:ind]) * f(n-i-1)
            for j in range(26):
                ans = ans * inv(f(cnt[j])) % N
            out += ans
        return out % N
        