'''

-Hard-
*DP*


Given a single positive integer x, we will write an expression of the form x (op1) x (op2) x (op3) x ... where each operator op1, op2, etc. is either addition, subtraction, multiplication, or division (+, -, *, or /). For example, with x = 3, we might write 3 * 3 / 3 + 3 - 3 which is a value of 3.

When writing such an expression, we adhere to the following conventions:

The division operator (/) returns rational numbers.
There are no parentheses placed anywhere.
We use the usual order of operations: multiplication and division happen before addition and subtraction.
It is not allowed to use the unary negation operator (-). For example, "x - x" is a valid expression as it only uses subtraction, but "-x + x" is not because it uses negation.
We would like to write an expression with the least number of operators such that the expression equals the given target. Return the least number of operators used.

 

Example 1:

Input: x = 3, target = 19
Output: 5
Explanation: 3 * 3 + 3 * 3 + 3 / 3.
The expression contains 5 operations.
Example 2:

Input: x = 5, target = 501
Output: 8
Explanation: 5 * 5 * 5 * 5 - 5 * 5 * 5 + 5 / 5.
The expression contains 8 operations.
Example 3:

Input: x = 100, target = 100000000
Output: 3
Explanation: 100 * 100 * 100 * 100.
The expression contains 3 operations.
 

Constraints:

2 <= x <= 100
1 <= target <= 2 * 108


'''
from math import log, ceil

from functools import lru_cache

class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        T = int(log(target)/log(x)) + 1
        f, g, a  = [0]*(T+1), [0]*(T+1),  [0]*(T+1)
        i = 0
        while target > 0:
            a[i] = target % x
            target //= x   
            i += 1
        print(a) 
        for i in range(T, -1, -1):
            if i == T:
                f[i] = a[i] * i
                g[i] = (a[i]+1)*i                
            else:
                s = 2 if i==0 else i
                f[i] = min(f[i+1]+a[i]*s,  g[i+1]+abs(a[i]-x)*s)
                g[i] = min(f[i+1]+(a[i]+1)*s, g[i+1]+abs(a[i]+1-x)*s)
            # print(f[i])
        return f[0]-1
    
    def leastOpsExpressTarget2(self, x: int, target: int) -> int:
        # T = int(log(target, 10)/log(x,10)) + 1 
        T = ceil(log(target, x))
        @lru_cache(None)
        def dfs(t, k):
            if k == 0 or t == 1: return t * 2
            pk = x**k
            a = t // pk
            if t % pk == 0:
                return k * a  
            # print(t, pk, a, k, a*pk)
            ans1 = a * k + dfs(t - a*pk, k-1)
            ans2 = (a+1) * k + dfs((a+1)*pk-t, k-1)
            return min(ans1, ans2) 
        return dfs(target, T) - 1



if __name__ == "__main__":
    print(Solution().leastOpsExpressTarget(x = 5, target = 501))
    print(Solution().leastOpsExpressTarget2(x = 5, target = 501))
        