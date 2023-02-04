'''
-Medium-


Solve a given equation and return the value of 'x' in the form of a string "x=#value". The equation contains only '+', '-' operation, the variable 'x' and its coefficient. You should return "No solution" if there is no solution for the equation, or "Infinite solutions" if there are infinite solutions for the equation.

If there is exactly one solution for the equation, we ensure that the value of 'x' is an integer.

 

Example 1:

Input: equation = "x+5-3+x=6+x-2"
Output: "x=2"
Example 2:

Input: equation = "x=x"
Output: "Infinite solutions"
Example 3:

Input: equation = "2x=x"
Output: "x=0"
 

Constraints:

3 <= equation.length <= 1000
equation has exactly one '='.
equation consists of integers with an absolute value in the range [0, 100] without any leading zeros, and the variable 'x'.


'''


class Solution:
    def solveEquation(self, equation: str) -> str:
        left, right = equation.split('=')
        def tokenize(s):
            tokens = []        
            for t1 in s.split('+'):
                if '-' in t1: 
                    for t2 in t1.split('-'):
                        tokens.append(t2)
                        tokens.append('-')
                    tokens.pop()    
                else:
                    tokens.append(t1)
                tokens.append('+')
            tokens.pop()        
            return tokens
        def parse(tokens):
            cnt, sign, sm = 0, 1, 0
            for t in tokens:
                if not t: continue
                if 'x' in t:
                    cnt += sign*(int(t[:-1]) if t[:-1] else 1)
                elif t == '+':
                    sign = 1
                elif t == '-':
                    sign = -1
                else:
                    sm += sign*int(t)
            return cnt, sm     
        left = tokenize(left)
        right = tokenize(right)
        l, numL = parse(left)
        r, numR = parse(right)
        if l != r:
            return 'x='+str((numR-numL)//(l-r))
        elif numR == numL:
            return "Infinite solutions"   
        return "No solution"

    
if __name__ == "__main__":
    print(Solution().solveEquation(equation = "x+5-3+x=6+x-2"))
    print(Solution().solveEquation(equation = "x=x"))
    print(Solution().solveEquation(equation = "2x=x"))
    print(Solution().solveEquation(equation ="2x+3x-6x=x+2"))
    print(Solution().solveEquation(equation ="-x=-1"))
    print(Solution().solveEquation(equation = "2+2-x+x+3x=x+2x-x+x+4"))
    print(Solution().solveEquation(equation ="1-x+x-x+x=99"))