'''
-Easy-

*Binary Search*

Given a non-negative integer x, compute and return the square root of x.

Since the return type is an integer, the decimal digits are truncated, and 
only the integer part of the result is returned.

 

Example 1:

Input: x = 4
Output: 2
Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since the decimal 
part is truncated, 2 is returned.
 

Constraints:

0 <= x <= 2^31 - 1

'''

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 2: return x
        left, right = 0, x
        while left < right:
            mid = left + (right - left)//2
            mid2 = mid * mid
            if mid2 == x: return mid
            elif mid2 > x: right = mid
            else: left = mid+1
        return left-1




if __name__ == "__main__":
    print(Solution().mySqrt(20))
