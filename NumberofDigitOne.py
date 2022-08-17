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

from functools import lru_cache

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
    

    def countDigitOne2(self, n):
        s = str(n)
        @lru_cache(None) 
        # def dp(pos, count, flag):
        def dp(pos, count, tight):
            if pos == len(s):
                return count
            ans = 0
            limit = ord(s[pos])-ord('0') if tight == 1 else 9 
            # limit = ord(s[pos])-ord('0') if flag == 0 else 9 
            for i in range(limit+1):
                ncount = count+1 if i == 1 else count
                ntight = tight and i == limit
                # nflag =  flag or (i != limit)
                # ans += dp(pos+1, ncount, nflag)
                ans += dp(pos+1, ncount, ntight)
            return ans        
        # return dp(0, 0, 0) 
        return dp(0, 0, 1) 
    
    def countDigitOne3(self, n: int) -> int:
        if n <= 0: 
            return 0
        N = list(map(int, str(n)))

        @lru_cache(None)
        def dp(pos, isPrefix, isBigger, ones):
            if pos == len(N):
                return 0
            result = 0
            for i in range(0 if pos > 0 else 1, 10):
                _isPrefix = isPrefix and i == N[pos]
                _isBigger = isBigger or (isPrefix and i > N[pos])
                _ones = ones + (1 if i == 1 else 0)
                if not (pos == len(N) - 1 and _isBigger):
                    result += ones
                if i == 1 and not (pos == len(N) - 1 and _isBigger):
                    result += 1
                result += dp(pos + 1, _isPrefix, _isBigger, _ones)
            return result

        return dp(0, True, False, 0)



if __name__ == "__main__":
    print(Solution().countDigitOne(13))
    print(Solution().countDigitOne(135))
    print(Solution().countDigitOne2(13))
    print(Solution().countDigitOne2(135))
    print(Solution().countDigitOne3(135))