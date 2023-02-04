'''
-Hard-
*Stack*
*DP*

You are given a valid boolean expression as a string expression consisting of the characters '1','0','&' (bitwise AND operator),'|' (bitwise OR operator),'(', and ')'.

For example, "()1|1" and "(1)&()" are not valid while "1", "(((1))|(0))", and "1|(0&(1))" are valid expressions.
Return the minimum cost to change the final value of the expression.

For example, if expression = "1|1|(0&0)&1", its value is 1|1|(0&0)&1 = 1|1|0&1 = 1|0&1 = 1&1 = 1. We want to apply operations so that the new expression evaluates to 0.
The cost of changing the final value of an expression is the number of operations performed on the expression. The types of operations are described as follows:

Turn a '1' into a '0'.
Turn a '0' into a '1'.
Turn a '&' into a '|'.
Turn a '|' into a '&'.
Note: '&' does not take precedence over '|' in the order of calculation. Evaluate parentheses first, then in left-to-right order.

 

Example 1:

Input: expression = "1&(0|1)"
Output: 1
Explanation: We can turn "1&(0|1)" into "1&(0&1)" by changing the '|' to a '&' using 1 operation.
The new expression evaluates to 0. 
Example 2:

Input: expression = "(0&0)&(0&0&0)"
Output: 3
Explanation: We can turn "(0&0)&(0&0&0)" into "(0|1)|(0&0&0)" using 3 operations.
The new expression evaluates to 1.
Example 3:

Input: expression = "(0|(1|0&1))"
Output: 1
Explanation: We can turn "(0|(1|0&1))" into "(0|(0|0&1))" using 1 operation.
The new expression evaluates to 0.
 

Constraints:

1 <= expression.length <= 105
expression only contains '1','0','&','|','(', and ')'
All parentheses are properly matched.
There will be no empty parentheses (i.e: "()" is not a substring of expression).




'''

class Solution:
    def minOperationsToFlip(self, expression: str) -> int:
        # stack[i] = [dp0, dp1, operation], where dp0 and dp1 are the nuber 
        # operations needed to get 0 and 1 result. operation is the last 
        # operation encountered in the expression.
        stack = [[0, 0, None]]
        for e in expression:                                                    
            if e == "(":                                                        
                stack.append([0, 0, None])                                      # new nested bracket, add empty stack element
            elif e in { ")", "0", "1" }:                                        # if we have two expressions to combine
    
                if e == ")":                                                    # if ")", we can combine child with parent
                    dp0, dp1 = stack[-1][0], stack[-1][1]                       # remember nested bracket result as dp0 and dp1
                    stack.pop()                                                 # and pop it
                else:                                                           # if e is "0" or "1", consider it as nested expression
                    dp0, dp1 = int(e != "0"), int(e != "1")                     # and find dp0 and dp1

                if stack[-1][2] == "&":                                         # now combine results, look at point 3 in the list above
                    stack[-1] = [
                        min(stack[-1][0], dp0),                                 # dp0
                        min(stack[-1][1] + dp1, min(stack[-1][1], dp1) + 1),    # dp1
                        None                                                    # reset operation
                    ]
                elif stack[-1][2] == "|":
                    stack[-1] = [
                        min(stack[-1][0] + dp0, min(stack[-1][0], dp0) + 1),    # dp0
                        min(stack[-1][1], dp1),                                 # dp1
                        None                                                    # reset operation
                    ]
                else:                                                           # if operation is not set, then it's the first expression in nested brackets
                    stack[-1] = [dp0, dp1, None]                                # so just set dp0 and dp1 as last element of stack
            elif e in { "&", "|" }:                                             # if e is some of operations
                stack[-1][2] = e                                                # set the operation in the last element of stack
        return max(stack[0][0], stack[0][1])    

    def minOperationsToFlip2(self, expression: str) -> int:
        E = expression
        def corr(s):
            # for each closing bracket,  find corresponding open bracket save in d
            stack, d = [], {}
            for i, elem in enumerate(s):
                if elem == "(":
                    stack.append(i)
                elif elem == ")":
                    last = stack.pop()
                    d[i] = last
            return d

        def dfs(beg, end):
            # dfs returns a tuple (val, changes), where val is value before changing 
            # and changes is minumum number of changes we need to make to change val
            if beg == end: return (int(E[beg]) , 1) # case with just one number: 1 or 0
            beg2 = d.get(end, end)
            if beg2 == beg: return dfs(beg + 1, end - 1)
            # p1, c1 and p2, c2 are the values, costs of the 2 expressions before and after & or |
            p1, c1 = dfs(beg, beg2 - 2) # the expression before the operator (eg. before & or |), "beg2 - 2" to move from position from 2nd expression '(' to 1st expression ')'
            p2, c2 = dfs(beg2, end) # the expression after the operator (eg. after & or |)
            op = E[beg2 - 1]  # the operator, eg. & or |
            
            t = {"|": lambda x, y:x|y, "&": lambda x, y:x&y}
            c3 = 1 if p1 + p2 == 1 else min(c1, c2) + (p1^(op == "&"))
            # if p1+p2=1 (4 cases):
            # if p1 == 1 and p2 == 0 and op == "|": return (1, 1)
            # if p1 == 0 and p2 == 1 and op == "|": return (1, 1)
            # if p1 == 1 and p2 == 0 and op == "&": return (0, 1)
            # if p1 == 0 and p2 == 1 and op == "&": return (0, 1)
            # we can change the op (eg. &->| or |->&) with cost=1

            # else:
            # if we have 0|0, then what we can do is to change either left or right part to 1, 
            # so minimum number of changes is min(c1, c2). 
            # if p1 == 0 and p2 == 0 and op == "|": return (0, min(c1, c2))            
            # if p1 == 1 and p2 == 1 and op == "&": return (1, min(c1, c2))
            # if p1 == 1 and p2 == 1 and op == "|": return (1, 1 + min(c1, c2))
            # if p1 == 0 and p2 == 0 and op == "&": return (0, 1 + min(c1, c2))
            return (t[op](p1, p2), c3) # t[op](p1,p2)=p1 op p2 (eg. op is & or |), c3 is the final costs
            
        d = corr(E)
        return dfs(0, len(E) - 1)[1]         


if __name__ == "__main__":
    print(Solution().minOperationsToFlip(expression = "(0&0)&(0&0&0)"))
    print(Solution().minOperationsToFlip2(expression = "(0&0)&(0&0&0)"))