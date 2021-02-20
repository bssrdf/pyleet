'''

-Medium-

*Stack*

Given a string s of '(' , ')' and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( '(' or ')', in 
any positions ) so that the resulting parentheses string is valid and return 
any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, 
or
It can be written as (A), where A is a valid string.
 

Example 1:

Input: s = "lee(t(c)o)de)"
Output: "lee(t(c)o)de"
Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
Example 2:

Input: s = "a)b(c)d"
Output: "ab(c)d"
Example 3:

Input: s = "))(("
Output: ""
Explanation: An empty string is also valid.
Example 4:

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)"
 

Constraints:

1 <= s.length <= 10^5
s[i] is one of  '(' , ')' and lowercase English letters.

'''
from collections import deque

class Solution(object):
    def minRemoveToMakeValid(self, s):
        """
        :type s: str
        :rtype: str
        """
        """
        BFS works but TLE. The efficient solution is using the stack.
        """
        strs = list(s)
        stack = []
        for i in range(len(strs)):
            if strs[i] == '(':
                stack.append(i)
            elif strs[i] == ')':
                if stack: stack.pop()
                else: strs[i] = ''
        for i in stack: strs[i] = ''
        return ''.join(strs)

        
if __name__ == "__main__":
    print(Solution().minRemoveToMakeValid("lee(t(c)o)de)"))
    print(Solution().minRemoveToMakeValid("))(("))
    print(Solution().minRemoveToMakeValid("a)b(c)d"))
    print(Solution().minRemoveToMakeValid("(a(b(c)d)"))
