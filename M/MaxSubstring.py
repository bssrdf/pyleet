'''
-Hard-

Given a string s, return the last substring of s in lexicographical order.

1 <= s.length <= 4 * 10^4
s contains only lowercase English letters.

样例
Example 1:

Input: "abab"
Output: "bab"
Explanation: The substrings are ["a", "ab", "aba", "abab", "b", "ba", "bab"]. 
The lexicographically maximum substring is "bab".
Example 2:

Input: "baca"
Output: "ca"

'''

class Solution:
    """
    @param s: the matrix
    @return: the last substring of s in lexicographical order
    """
    def maxSubstring(self, s):
        # Write your code here.
        cm = 'a'
        for c in s:
            if cm < c: cm = c
        startWithLast = []
        for i in range(len(s)):
            if s[i] == cm:
                startWithLast.append(s[i:])
        startWithLast.sort()
        return startWithLast[-1]
            

if __name__ == "__main__":
    print(Solution().maxSubstring('abab'))
    print(Solution().maxSubstring('baca'))