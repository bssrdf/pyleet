'''
-Medium-

Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter in pattern and 
a non-empty substring in str.(i.e if a corresponds to s, then b cannot correspond to s. For example, 
given pattern = "ab", str = "ss", return false.)

You may assume both pattern and str contains only lowercase letters.

样例
Example 1

Input:
pattern = "abab"
str = "redblueredblue"
Output: true
Explanation: "a"->"red","b"->"blue"
Example 2

Input:
pattern = "aaaa"
str = "asdasdasdasd"
Output: true
Explanation: "a"->"asd"
Example 3

Input:
pattern = "aabb"
str = "xyzabcxzyabc"
Output: false
'''


class Solution:
    """
    @param pattern: a string,denote pattern string
    @param str: a string, denote matching string
    @return: a boolean
    """
    def wordPatternMatch(self, pattern, str):
        # write your code here
        m = {}
        def helper(p, r):
            if p == len(pattern) and r == len(str): return True
            if p == len(pattern) or r == len(str): return False
            c = pattern[p]
            for i in range(r, len(str)):
                t = str[r:i+1]
                if c in m and m[c] == t:
                    if helper(p + 1, i + 1): return True
                elif c not in m:
                    b = False
                    for it in m:
                        if m[it] == t: b = True
                    if not b:
                        m[c] = t
                        if helper(p + 1, i + 1): return True
                        m.pop(c)
            return False
        return helper(0, 0)

if __name__ == "__main__":
    print(Solution().wordPatternMatch(pattern = "abab", str = "redblueredblue"))
    print(Solution().wordPatternMatch(pattern = "aabb", str = "xyzabcxzyabc"))