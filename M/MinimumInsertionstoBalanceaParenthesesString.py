'''
-Medium-

Given a parentheses string s containing only the characters '(' and ')'. A 
parentheses string is balanced if:

Any left parenthesis '(' must have a corresponding two consecutive right parenthesis '))'.
Left parenthesis '(' must go before the corresponding two consecutive right parenthesis '))'.
In other words, we treat '(' as an opening parenthesis and '))' as a closing parenthesis.

For example, "())", "())(())))" and "(())())))" are balanced, ")()", "()))" and "(()))" 
are not balanced.
You can insert the characters '(' and ')' at any position of the string to balance 
it if needed.

Return the minimum number of insertions needed to make s balanced.

 

Example 1:

Input: s = "(()))"
Output: 1
Explanation: The second '(' has two matching '))', but the first '(' has only ')' matching. We need to to add one more ')' at the end of the string to be "(())))" which is balanced.
Example 2:

Input: s = "())"
Output: 0
Explanation: The string is already balanced.
Example 3:

Input: s = "))())("
Output: 3
Explanation: Add '(' to match the first '))', Add '))' to match the last '('.
 

Constraints:

1 <= s.length <= 105
s consists of '(' and ')' only.


'''

class Solution:
    def minInsertions(self, s: str) -> int:
        stack, ans = [], 0
        i = 0
        while i < len(s) - 1:
            if s[i] == '(':
                stack.append(s[i])
                i += 1
            else:
                if stack and stack[-1] == '(':
                    if s[i+1] == ')':
                        i = i+2
                    else:
                        ans += 1
                        i += 1
                    stack.pop()
                else:
                    if s[i+1] == ')':
                        i = i+2
                        ans += 1
                    else:
                        ans += 2
                        i += 1
        if i == len(s) - 1:
            if s[-1] == '(':
                stack.append(s[-1])
            else:
                if stack and stack[-1] == '(':                    
                    ans += 1
                    stack.pop()
                else:
                    ans += 2
        while stack:
            ans += 2
            stack.pop()
        return ans        
    
    def minInsertions2(self, s: str) -> int:
        i, stack, ans, n = 0, [], 0, len(s)
        while i < len(s):
            if s[i] == '(':
                stack.append(s[i])
                i += 1
            else:
                if stack and stack[-1] == '(':
                    if i+1 < n and s[i+1] == ')':
                        i = i+2
                    else:
                        ans += 1
                        i += 1
                    stack.pop()
                else:
                    if i+1 < n and s[i+1] == ')':
                        i += 2
                        ans += 1
                    else:
                        ans += 2
                        i += 1
        while stack:
            ans += 2
            stack.pop()
        return ans        




if __name__ == "__main__":
    print(Solution().minInsertions("(()))"))
    print(Solution().minInsertions("())"))
    print(Solution().minInsertions("))())("))