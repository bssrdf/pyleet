'''
-Medium-

Given an integer n, return the count of all numbers with unique digits, x, where 0 <= x < 10n.

 

Example 1:

Input: n = 2
Output: 91
Explanation: The answer should be the total numbers in the range of 0 ≤ x < 100, excluding 11,22,33,44,55,66,77,88,99
Example 2:

Input: n = 0
Output: 1
 

Constraints:

0 <= n <= 8

'''

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        ans = 0
        for i in range(1, n+1):
            x, k = 1, 9
            for _ in range(i-1):
                x *= k
                k -= 1
            ans += 9 * x # ways to get special integers with digits less than that in n
        
        return ans+1