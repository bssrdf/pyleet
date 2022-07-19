'''

-Medium-
*Stack*

You are given a string s that consists of lower case English letters and brackets.

Reverse the strings in each pair of matching parentheses, starting from the innermost one.

Your result should not contain any brackets.

 

Example 1:

Input: s = "(abcd)"
Output: "dcba"
Example 2:

Input: s = "(u(love)i)"
Output: "iloveu"
Explanation: The substring "love" is reversed first, then the whole string is reversed.
Example 3:

Input: s = "(ed(et(oc))el)"
Output: "leetcode"
Explanation: First, we reverse the substring "oc", then "etco", and finally, the whole string.
 

Constraints:

1 <= s.length <= 2000
s only contains lower case English characters and parentheses.
It is guaranteed that all parentheses are balanced.




'''


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack  = []
        t = ''
        for i,c in enumerate(s):            
            if c == '(':
                stack.append(t)                
                t = ''
            elif c == ')':
                s1 = stack.pop()
                # stack.append(t[::-1]) 
                t = s1 + t[::-1] 
                stack.append(t) 
                t= ''
            else:
                t += c
        print(stack)
        return ''   
    
    def reverseParentheses4(self, s: str) -> str:
        stack = ['']
        for c in s:
            if c == '(':
                stack.append('')
            elif c == ')':
                add = stack.pop()[::-1]
                stack[-1] += add
            else:
                stack[-1] += c
        return stack.pop()
    
    def reverseParentheses2(self, s: str) -> str:
        res = ['']
        for c in s:
            if c == '(':
                res.append('')
            elif c == ')':
                res[len(res) - 2] += res.pop()[::-1]
            else:
                res[-1] += c
        return "".join(res)

    def reverseParentheses3(self, s: str) -> str:
        opened = []
        pair = {}
        for i, c in enumerate(s):
            if c == '(':
                opened.append(i)
            if c == ')':
                j = opened.pop()
                pair[i], pair[j] = j, i
        res = []
        i, d = 0, 1
        while i < len(s):
            if s[i] in '()':
                i = pair[i]
                d = -d
            else:
                res.append(s[i])
            i += d
        return ''.join(res)

                 
                        




if __name__ == "__main__":
    print(Solution().reverseParentheses(s = "(u(love)i)"))
    print(Solution().reverseParentheses(s = "(ed(et(oc))el)"))
        