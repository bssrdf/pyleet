'''
-Hard-
*Backtracking*

You are given an integer array cards of length 4. You have four cards, each containing a number 
in the range [1, 9]. You should arrange the numbers on these cards in a mathematical expression 
using the operators ['+', '-', '*', '/'] and the parentheses '(' and ')' to get the value 24.

You are restricted with the following rules:

The division operator '/' represents real division, not integer division.
For example, 4 / (1 - 2 / 3) = 4 / (1 / 3) = 12.
Every operation done is between two numbers. In particular, we cannot use '-' as a unary operator.
For example, if cards = [1, 1, 1, 1], the expression "-1 - 1 - 1 - 1" is not allowed.
You cannot concatenate numbers together
For example, if cards = [1, 2, 1, 2], the expression "12 + 12" is not valid.
Return true if you can get such expression that evaluates to 24, and false otherwise.

 

Example 1:

Input: cards = [4,1,8,7]
Output: true
Explanation: (8-4) * (7-1) = 24
Example 2:

Input: cards = [1,2,1,2]
Output: false
 

Constraints:

cards.length == 4
1 <= cards[i] <= 9
'''

class Solution(object):
    def judgePoint24(self, cards):
        """
        :type cards: List[int]
        :rtype: bool
        """
        eps = 0.001
        def helper(nums, ops, eps):
            if len(nums) == 1: return abs(nums[0] - 24) < eps
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j: continue
                    t = []
                    for k in range(len(nums)):
                        if k != i and k != j: t.append(nums[k])
                    for op in ops:
                        #for '+' and '*', exchanging left and right operands gives 
                        # the same answer, so we skip i > j iterations
                        if (op == '+' or op == '*') and i > j: continue
                        if op == '/' and nums[j] < eps: continue # prevent divide by zero
                        t.append(ops[op](nums[i], nums[j]))
                        if helper(t, ops, eps): return True
                        t.pop()
            return False
        ops = {'+': lambda x,y: x+y, 
               '-': lambda x,y: x-y, 
               '*': lambda x,y: x*y, 
               '/': lambda x,y: x/y}
        return helper(cards, ops, eps)
    

    def judgePoint24Expression(self, cards):
        """
        :type cards: List[int]
        :rtype: bool
        """
        eps = 0.001
        self.ans = []
        def helper(nums, ops, eps, expr):
            if len(nums) == 1: 
                if abs(nums[0] - 24) < eps:
                    self.ans.append(expr[0])
                    return True
                return False
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j: continue
                    t, e = [], []
                    for k in range(len(nums)):
                        if k != i and k != j: 
                            t.append(nums[k])
                            e.append(expr[k])
                    for op in ops:
                        #for '+' and '*', exchanging left and right operands gives 
                        # the same answer, so we skip i > j iterations
                        if (op == '+' or op == '*') and i > j: continue
                        if op == '/' and nums[j] < eps: continue # prevent divide by zero
                        t.append(ops[op](nums[i], nums[j]))
                        e.append('('+(expr[i] if expr[i] else str(nums[i]))
                                 +op+(expr[j] if expr[j] else str(nums[j]))+')')
                        if helper(t, ops, eps, e): return True
                        t.pop()
                        e.pop()
            return False
        ops = {'+': lambda x,y: x+y, 
               '-': lambda x,y: x-y, 
               '*': lambda x,y: x*y, 
               '/': lambda x,y: x/y}
        if helper(cards, ops, eps, ['']*4):
            return self.ans

if __name__ == "__main__":  
    print(Solution().judgePoint24([4,1,8,7]))
    print(Solution().judgePoint24Expression([4,1,8,7]))
    print(Solution().judgePoint24Expression([1,3,4,6]))