'''

-Hard-
*Recursion*

Return the result of evaluating a given boolean expression, represented as a string.

An expression can either be:

"t", evaluating to True;
"f", evaluating to False;
"!(expr)", evaluating to the logical NOT of the inner expression expr;
"&(expr1,expr2,...)", evaluating to the logical AND of 2 or more inner expressions expr1, expr2, ...;
"|(expr1,expr2,...)", evaluating to the logical OR of 2 or more inner expressions expr1, expr2, ...
 

Example 1:

Input: expression = "!(f)"
Output: true
Example 2:

Input: expression = "|(f,t)"
Output: true
Example 3:

Input: expression = "&(t,f)"
Output: false
 

Constraints:

1 <= expression.length <= 2 * 104
expression[i] consists of characters in {'(', ')', '&', '|', '!', 't', 'f', ','}.
expression is a valid expression representing a boolean, as given in the description.


'''
from operator import  and_, or_
from functools import reduce
class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        def helper(s):
            if s[0] == 't': return True
            if s[0] == 'f': return False 
            sub = s[2:-1]
            if s[0] == '!':
                return not helper(sub)            
            i, cnt, subexps = 0, 0, []         
            n = len(sub)  
            # if '(' in sub: 
            while i < n:                
                if sub[i] == '(':
                    j, cnt = i, 0
                    while i < n:
                        if sub[i] == '(': cnt += 1
                        if sub[i] == ')': cnt -= 1
                        if cnt == 0: break
                        i += 1
                    subexps.append(sub[j-1:i+1])                    
                elif sub[i] in 'tf':    
                    subexps.append(sub[i])                
                i += 1
            ret = helper(subexps[0])              
            for se in subexps[1:]:
                if s[0] == '&':
                    ret = ret and helper(se)
                else:
                    ret = ret or helper(se)
            return ret
            # using reduce seems slower
            fun = and_ if s[0] == '&' else or_
            return reduce(fun, (helper(se) for se in subexps))

        return helper(expression)    

        

if __name__ == "__main__":
    print(Solution().parseBoolExpr(expression = "!(f)"))
    print(Solution().parseBoolExpr(expression = "|(f,t)"))
    print(Solution().parseBoolExpr(expression = "&(t,f)"))
    print(Solution().parseBoolExpr(expression = "|(&(t,f,t),!(t))"))
    print(Solution().parseBoolExpr(expression = "|(&(t,f,t),t)"))