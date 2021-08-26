'''
-Medium-

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

 

Example 1:

Input: x = 2.00000, n = 10
Output: 1024.00000
Example 2:

Input: x = 2.10000, n = 3
Output: 9.26100
Example 3:

Input: x = 2.00000, n = -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
 

Constraints:

-100.0 < x < 100.0
-2^31 <= n <= 2^31-1
-10^4 <= xn <= 10^4


'''

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        m = n
        n = abs(n)
        res = 1.0
        while n > 0:                                       
            if n % 2 == 1: res *= x
            x = x * x                          
            n //= 2      
        return res if m > 0 else 1.0/res

    def myPowAC(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        #  16 ms, faster than 78.05% 
        m = n
        n = abs(n)
        if n == 0: return 1.0
        res = x
        b = bin(n)[2:]
        #print(b)
        #n //= 2
        for i in b[1:]:
            res = res * res
            if i == '1': res *= x                                      
        #    print(i, res)
        return res if m > 0 else 1.0/res

    
if __name__ == "__main__":
    print(Solution().myPow(x = 2.00000, n = 4))
    print(Solution().myPowAC(x = 2.00000, n = 4))
    print(Solution().myPow(x = 2.00000, n = 10))
    print(Solution().myPowAC(x = 2.00000, n = 10))
    print(Solution().myPow(x = 2.00000, n = 1))
    print(Solution().myPowAC(x = 2.00000, n = 1))
    print(Solution().myPow(x = 2.00000, n = -2))
    print(Solution().myPowAC(x = 2.00000, n = -2))
    