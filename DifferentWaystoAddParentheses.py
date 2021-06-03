'''
-Medium-
*Divide and Conquer*
*Hash Table*
*Memoization*


Given a string expression of numbers and operators, return all possible results from computing all 
the different possible ways to group numbers and operators. You may return the answer in any order.

 

Example 1:

Input: expression = "2-1-1"
Output: [0,2]
Explanation:
((2-1)-1) = 0 
(2-(1-1)) = 2
Example 2:

Input: expression = "2*3-4*5"
Output: [-34,-14,-10,-10,10]
Explanation:
(2*(3-(4*5))) = -34 
((2*3)-(4*5)) = -14 
((2*(3-4))*5) = -10 
(2*((3-4)*5)) = -10 
(((2*3)-4)*5) = 10
 

Constraints:

1 <= expression.length <= 20
expression consists of digits and the operator '+', '-', and '*'.


'''
from collections import defaultdict
class Solution(object):
    
    
    def diffWaysToCompute(self, expression):
        """
        :type expression: str
        :rtype: List[int]
        """
        memo = defaultdict(list)
        def helper(input):
            if input in memo: return memo[input]
            res = []
            for i in range(len(input)):
                if (input[i] == '+' or input[i] == '-' or input[i] == '*'):
                    left  = helper(input[:i])   # divide
                    right = helper(input[i+1:]) # divide
                    # merge the results
                    for j in range(len(left)):
                        for k in range(len(right)):
                            if input[i] == '+': res.append(left[j] + right[k])
                            elif input[i] == '-': res.append(left[j] - right[k])
                            else: res.append(left[j] * right[k])
            if not res: res.append(int(input)) # base case: down to a single number
            memo[input] = res
            return res
        return helper(expression)

if __name__ == "__main__":
    print(Solution().diffWaysToCompute("2*3-4*5"))