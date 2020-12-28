'''
-Medium-

Given a positive integer n, find the smallest integer which has exactly the same 
digits existing in the integer n and is greater in value than n. If no such 
positive integer exists, return -1.

Note that the returned integer should fit in 32-bit integer, if there is a valid 
answer but it does not fit in 32-bit integer, return -1.

 

Example 1:

Input: n = 12
Output: 21
Example 2:

Input: n = 21
Output: -1
 

Constraints:

1 <= n <= 2^31 - 1

'''

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = []
        dec = 10
        while n > 0:
            d = n % dec
            digits.append(d)
            n = (n-d)//dec
        m = len(digits)        
        i = 1
        while i < m:            
            if digits[i] < digits[i-1]: break
            i += 1
        if i == m: return -1
        j = 0
        while j <= i:
            if digits[j] > digits[i]: break
            j += 1
        digits[i], digits[j] = digits[j], digits[i]                            
        nums = sorted(digits[:i], reverse=True)+digits[i:]
        res, dec = 0, 1
        for d in nums:
            res += d*dec
            dec *= 10
        return res if res <= 2**31-1 else -1                    

    def nextGreaterElementStr(self, n):
        """
        :type n: int
        :rtype: int
        """
        digits = str(n)
        m = len(digits)
        i = m-1
        while i > 0:            
            if digits[i] > digits[i-1]: break
            i -= 1
        if i == 0: return -1
        j = m-1
        while j >= i:
            if digits[j] > digits[i-1]: break
            j -= 1
        digits = list(digits)    
        digits[i-1], digits[j] = digits[j], digits[i-1]                                    
        res = int(''.join(digits[:i]+sorted(digits[i:])))        
        return res if res <= 2**31-1 else -1                    
            


        
if __name__ == "__main__":
    print(Solution().nextGreaterElement(12))
    print(Solution().nextGreaterElement(123))
    print(Solution().nextGreaterElement(21))
    print(Solution().nextGreaterElement(11))
    print(Solution().nextGreaterElement(230241))
    print(Solution().nextGreaterElement(12222333))
    print(Solution().nextGreaterElementStr(12222333))