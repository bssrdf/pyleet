'''
-Medium-

Given a balanced parentheses string S, compute the score of the string based 
on the following rule:

() has score 1
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

Input: "()"
Output: 1
Example 2:

Input: "(())"
Output: 2
Example 3:

Input: "()()"
Output: 2
Example 4:

Input: "(()(()))"
Output: 6
 

Note:

S is a balanced parentheses string, containing only ( and ).
2 <= S.length <= 50


'''

class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """"
        """
        Our goal is to maintain the score at the current depth we are on. When we 
        see an opening bracket, we increase our depth, and our score at the new 
        depth is 0. When we see a closing bracket, we add twice the score of the 
        previous deeper part - except when counting (), which has a score of 1.

        """
        stack = [0] #The score of the current frame

        for x in S:
            if x == '(':
                #see a (：stack.push(0)increase our depth
                stack.append(0)
            else:
                """                
                see a )：we need to decrease our depth
                v = stack.pop(); score of the ith depth
                """
                v = stack.pop()
                """
                w = stack.pop(); score of the（i-1)th depth
                stack.push(w + Math.max(2 * v, 1)); 
                collect a new score for the（i-1)th depth
                """
                stack[-1] += max(2 * v, 1)

        return stack.pop()
        


if __name__ == "__main__":
    print(Solution().scoreOfParentheses("(()(()))"))
