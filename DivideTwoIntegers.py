'''

-Medium-

Given two integers dividend and divisor, divide two integers without using 
multiplication, division, and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero, which means losing its 
fractional part. For example, truncate(8.345) = 8 and truncate(-2.7335) = -2.

Note:

Assume we are dealing with an environment that could only store integers 
within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For this problem, 
assume that your function returns 231 − 1 when the division result overflows.
 

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Explanation: 10/3 = truncate(3.33333..) = 3.
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Explanation: 7/-3 = truncate(-2.33333..) = -2.
Example 3:

Input: dividend = 0, divisor = 1
Output: 0
Example 4:

Input: dividend = 1, divisor = 1
Output: 1
 

Constraints:

-2^31 <= dividend, divisor <= 2^31 - 1
divisor != 0

'''

class Solution(object):

    def divideFast(self, dividend, divisor):
        m, n, res = abs(dividend), abs(divisor), 0
        if m < n: return 0
        t, p = n, 1
        while m > (t << 1):
            t <<= 1
            p <<= 1
        res += p + self.divideFast(m - t, n)
        if (dividend < 0) ^ (divisor < 0): res = -res
        return 2**31-1 if res > 2**31-1 else res


    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        def bitMultiply(multiplicand, multiplier):
            res = 0
            while multiplier:
                if multiplier & 1: res += multiplicand
                multiplicand <<= 1
                multiplier >>= 1
            return res
        minus = (dividend >= 0) ^ (divisor >= 0)
        dd, dr = abs(dividend), abs(divisor)
        left, right = 0, dd+1
         
        while left < right :
            mid = left + ((right-left) >> 1)
            res = bitMultiply(mid, dr)
            if res > dd: right = mid
            else: left = mid+1
        ans = left-1
        if (minus): ans = 0-ans
        return 2**31-1 if ans > 2**31-1 or ans < -2**31 else ans
        


if __name__ == "__main__":
    print(Solution().divide(10,3))
    print(Solution().divideFast(10,3))