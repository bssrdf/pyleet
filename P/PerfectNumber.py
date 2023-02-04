'''
-Math-

A perfect number is a positive integer that is equal to the sum of its 
positive divisors, excluding the number itself. A divisor of an integer x 
is an integer that can divide x evenly.

Given an integer n, return true if n is a perfect number, otherwise return 
false.

 

Example 1:

Input: num = 28
Output: true
Explanation: 28 = 1 + 2 + 4 + 7 + 14
1, 2, 4, 7, and 14 are all divisors of 28.
Example 2:

Input: num = 6
Output: true
Example 3:

Input: num = 496
Output: true
Example 4:

Input: num = 8128
Output: true
Example 5:

Input: num = 2
Output: false

'''

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        s = 1
        i = 2
        while i*i <= num:        
            if num % i == 0:
                s += i + (0 if num//i == i else num//i)
            i += 1
        return num != 1 and s==num

if __name__ == "__main__":
    print(Solution().checkPerfectNumber(28))