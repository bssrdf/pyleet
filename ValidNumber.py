'''

-Hard-

A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
At least one digit, followed by a dot '.'.
At least one digit, followed by a dot '.', followed by at least one digit.
A dot '.', followed by at least one digit.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
At least one digit.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

 

Example 1:

Input: s = "0"
Output: true
Example 2:

Input: s = "e"
Output: false
Example 3:

Input: s = "."
Output: false
Example 4:

Input: s = ".1"
Output: true
 

Constraints:

1 <= s.length <= 20
s consists of only English letters (both uppercase and lowercase), digits (0-9), 
plus '+', minus '-', or dot '.'.

'''
from enum import Enum

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        n = len(s)
        left, right = 0, n - 1
        eExisted = False
        dotExisted = False
        digitExisited = False
        # Delete spaces in the front and end of string
        while s[left] == ' ': left += 1
        while s[right] == ' ': right -= 1
        # If only have one char and not digit, return false
        if left >= right and (s[left] < '0' or s[left] > '9'): return False
        # Process the first char
        if s[left] == '.': dotExisted = True
        elif s[left] >= '0' and s[left] <= '9': digitExisited = True
        elif s[left] != '+' and s[left] != '-': return False
        # Process the middle chars
        for i in range(left + 1, right):
            if s[i] >= '0' and s[i] <= '9': 
                digitExisited = True
            elif (s[i] == 'e' or s[i] == 'E'): # e/E cannot follow +/-, must follow a digit
                if not eExisted and s[i - 1] != '+' and s[i - 1] != '-' and digitExisited: 
                    eExisted = True
                else: return False
            elif s[i] == '+' or s[i] == '-':  #// +/- can only follow e/E
                if s[i - 1] != 'e' and s[i - 1] != 'E': return False                
            elif s[i] == '.': # dot can only occur once and cannot occur after e/E
                if not dotExisted and not eExisted: dotExisted = True
                else: return False
            else: return False
        # Process the last char, it can only be digit or dot, when is dot, 
        # there should be no dot and e/E before and must follow a digit
        if s[right] >= '0' and s[right] <= '9': return True
        elif s[right] == '.' and not dotExisted and not eExisted and digitExisited:
            return True
        else: return False

    def isNumberFSM(self, s):
        """
        :type s: str
        :rtype: bool
        """
        class InputType(Enum): 
            INVALID = 0		# 0 Include: Alphas, '(', '&' ans so on
            SPACE = 1		# 1
            SIGN = 2		# 2 '+','-'
            DIGIT = 3		# 3 numbers
            DOT = 4			# 4 '.'
            EXPONENT = 5	# 5 'e' 'E'
        transTable = [
		#0INVA,1SPA,2SIG,3DI,4DO,5E
			[-1,  0,  3,  1,  2, -1], #0初始无输入或者只有space的状态
			[-1,  8, -1,  1,  4,  5], #1输入了数字之后的状态
			[-1, -1, -1,  4, -1, -1], #2前面无数字，只输入了Dot的状态
			[-1, -1, -1,  1,  2, -1], #3输入了符号状态
			[-1,  8, -1,  4, -1,  5], #4前面有数字和有dot的状态
			[-1, -1,  6,  7, -1, -1], #5'e' or 'E'输入后的状态
			[-1, -1, -1,  7, -1, -1], #6输入e之后输入Sign的状态
			[-1,  8, -1,  7, -1, -1], #7输入e后输入数字的状态
			[-1,  8, -1, -1, -1, -1]  #8前面有有效数输入之后，输入space的状态
		]
        state = 0
        for c in s:
            input = InputType.INVALID.value
            if c == ' ': input = InputType.SPACE.value
            elif c == '+' or c == '-': input = InputType.SIGN.value
            elif c.isdigit(): input = InputType.DIGIT.value
            elif c == '.': input = InputType.DOT.value
            elif c == 'e' or c == 'E': input = InputType.EXPONENT.value
            state = transTable[state][input]
            if state == -1: return False
        return state == 1 or state == 4 or state == 7 or state == 8



if __name__ == "__main__":
    print(Solution().isNumber(" 2e-9 "))
    print(Solution().isNumberFSM(" 2e-9 "))