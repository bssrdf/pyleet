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

if __name__ == "__main__":
    print(Solution().wordPatternMatch(pattern = "abab", str = "redblueredblue"))
