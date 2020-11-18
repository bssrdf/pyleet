'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
 

Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
Example 4:

Input: s = "([)]"
Output: false
Example 5:

Input: s = "{[]}"
Output: true
 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

'''

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {')':'(', ']':'[', '}':'{'}
        def match(c1, c2):
            return c1 == mapping[c2]
        for c in s:
            if c in '([{':
                stack.append(c)
            if c in ')]}':
                if not stack or not match(stack[-1], c):
                   return False
                stack.pop()
        return len(stack) == 0


if __name__ == "__main__":
    print(Solution().isValid("()[]{}"))
    print(Solution().isValid("([)]"))
    print(Solution().isValid("{[]}"))
    print(Solution().isValid("{"))