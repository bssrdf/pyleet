'''
-Hard-
*Stack*
*DP*

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
        res, start, n = 0, 0, len(s)        
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
            #print('start',start, 'res', res)
        return res
    
    def longestValidParenthesesDP(self, s):
        """
        :type s: str
        :rtype: int
        """
        """
        If s[i] is '(', set longest[i] to 0,because any string end with '(' cannot 
        be a valid one.

        Else if s[i] is ')'

            If s[i-1] is '(', longest[i] = longest[i-2] + 2

            Else if s[i-1] is ')' and s[i-longest[i-1]-1] == '(', 
                longest[i] = longest[i-1] + 2 + longest[i-longest[i-1]-2]

            For example, input "()(())", at i = 5, longest array is [0,2,0,0,2,0], 
            longest[5] = longest[4] + 2 + longest[1] = 6.

        """
        n = len(s)
        if len(s) == 1: return 0
        dp = [0]*n
        res = 0
        for i in range(1, n):
            if s[i] == '(': continue # cannot form the valid parentheses
            if s[i-1] == '(':
                dp[i] = dp[i-2]+2 if i >= 2 else 2
            else:
                if i-dp[i-1]-1 >= 0 and s[i-1-dp[i-1]] == '(':
                    dp[i] = dp[i-1] + 2 + (dp[i-dp[i-1]-2] if i-dp[i-1]-2>=0 else 0)
            res = max(res, dp[i])
        return res

                 


        
        

            
        
        

if __name__ == "__main__":
    '''
    print(Solution().longestValidParentheses("()())()"))
    print(Solution().longestValidParentheses("(()"))
    print(Solution().longestValidParentheses(")()())"))
    print(Solution().longestValidParentheses(""))
    '''
    print(Solution().longestValidParentheses("()(()"))
    print(Solution().longestValidParentheses("(((())"))
    print(Solution().longestValidParenthesesDP("(((())"))