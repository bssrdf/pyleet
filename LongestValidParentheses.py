'''
Given a string containing just the characters '(' and ')', find the length 
of the longest valid (well-formed) parentheses substring.

 

Example 1:

Input: s = "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()".
Example 2:

Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
Example 3:

Input: s = ""
Output: 0
 

Constraints:

0 <= s.length <= 3 * 104
s[i] is '(', or ')'.

'''

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        st = []
        n = len(s)        
        res = 0
        start = 0
        for i in range(n):
            if s[i] == '(': st.append(i)
            if s[i] == ')':
                if not st:
                    start = i+1
                else:
                    st.pop()
                    if not st:
                        res = max(res, i-start+1)
                    else:
                        res = max(res, i-st[-1])
        return res


        
        

            
        
        

if __name__ == "__main__":
    #'''
    print(Solution().longestValidParentheses("()())()"))
    print(Solution().longestValidParentheses("(()"))
    print(Solution().longestValidParentheses(")()())"))
    print(Solution().longestValidParentheses(""))
    #'''
    print(Solution().longestValidParentheses("()(()"))