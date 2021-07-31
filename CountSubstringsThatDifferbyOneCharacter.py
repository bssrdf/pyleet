'''

-Medium-

Given two strings s and t, find the number of ways you can choose a non-empty substring of s and replace a single character by a different character such that the resulting substring is a substring of t. In other words, find the number of substrings in s that differ from some substring in t by exactly one character.

For example, the underlined substrings in "computer" and "computation" only differ by the 'e'/'a', so this is a valid way.

Return the number of substrings that satisfy the condition above.

A substring is a contiguous sequence of characters within a string.

 

Example 1:

Input: s = "aba", t = "baba"
Output: 6
Explanation: The following are the pairs of substrings from s and t that differ by exactly 1 character:
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
("aba", "baba")
The underlined portions are the substrings that are chosen from s and t.
​​Example 2:
Input: s = "ab", t = "bb"
Output: 3
Explanation: The following are the pairs of substrings from s and t that differ by 1 character:
("ab", "bb")
("ab", "bb")
("ab", "bb")
​​​​The underlined portions are the substrings that are chosen from s and t.
Example 3:
Input: s = "a", t = "a"
Output: 0
Example 4:

Input: s = "abe", t = "bbc"
Output: 10
 

Constraints:

1 <= s.length, t.length <= 100
s and t consist of lowercase English letters only.

'''

class Solution(object):
    def countSubstrings(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        def count(i,j):
            return 0 if s[i] == t[j] else nxt(i+1,j+1)*pre(i-1,j-1)
        def nxt(i,j):
            res = 1
            while i < m and j < n and s[i] == t[j]:
                i += 1
                j += 1
                res += 1
            return res
        def pre(i,j):
            res = 1
            while i >= 0 and j >= 0 and s[i] == t[j]:
                i -= 1
                j -= 1
                res += 1
            return res
        res = 0
        for i in range(m):
            for j in range(n):
                res += count(i,j)
        return res



if __name__ == "__main__":
    print(Solution().countSubstrings(s = "aba", t = "baba"))