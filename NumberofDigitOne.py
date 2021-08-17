'''
-Hard-
Given an integer n, count the total number of digit 1 appearing in 
all non-negative integers less than or equal to n.

 

Example 1:

Input: n = 13
Output: 6
Example 2:

Input: n = 0
Output: 0
 

Constraints:

0 <= n <= 109

'''

class Solution(object):
    def countDigitOne(self, n):
        """
        :type n: int
        :rtype: int
        """
        # The idea is to calculate occurrence of 1 on every digit. 
        # There are 3 scenarios, for example

        # if n = xyzdabc
        # and we are considering the occurrence of one on thousand, it should be:

        #(1) xyz * 1000 + 0            if d == 0, means there is no 1 because of  this digit(none)
        #(2) xyz * 1000 + abc + 1      if d == 1, means there is abc of  1 because  of this digit(patrial)
        #(3) xyz * 1000 + 1000         if d > 1,  means there  is fully 1000 of  1 because of  this digit(fully)
        if n <= 0:
            return 0
        q, x, ans = n, 1, 0
        while q > 0:
            digit = q % 10
            q //= 10
            ans += q * x
            if digit == 1:
                ans += n % x + 1
            elif digit > 1:
                ans += x
            x *= 10
        return ans

if __name__ == "__main__":
    print(Solution().countDigitOne(13))