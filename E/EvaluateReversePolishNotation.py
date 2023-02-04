'''
-Medium-

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another 
expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means 
the expression would always evaluate to a result, and there will not be any 
division by zero operation.

 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 

Constraints:

1 <= tokens.length <= 10^4
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].


'''
import math
import operator
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        ops = {'+' : operator.add, '-' : operator.sub, '*' : operator.mul, 
               '/' : lambda a,b : a//b if a*b > 0 else int(math.ceil(a/b)) }
        stack = []
        def func(op):
            b = stack.pop()
            a = stack.pop()
            stack.append(ops[op](a,b))
        for t in tokens:
            if t not in ops:
                stack.append(int(t))
            else:
                func(t)
        return stack.pop()




if __name__ == "__main__":
    print(Solution().evalRPN(["2","1","+","3","*"]))
    print(Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
    print(Solution().evalRPN(["4","-2","/","2","-3","-","-"]))
