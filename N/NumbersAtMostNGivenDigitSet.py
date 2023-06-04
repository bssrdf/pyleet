'''
-Hard-

Given an array of digits, you can write numbers using each digits[i] as many 
times as we want.  For example, if digits = ['1','3','5'], we may write 
numbers such as '13', '551', and '1351315'.

Return the number of positive integers that can be generated that are less 
than or equal to a given integer n.

 

Example 1:

Input: digits = ["1","3","5","7"], n = 100
Output: 20
Explanation: 
The 20 numbers that can be written are:
1, 3, 5, 7, 11, 13, 15, 17, 31, 33, 35, 37, 51, 53, 55, 57, 71, 73, 75, 77.
Example 2:

Input: digits = ["1","4","9"], n = 1000000000
Output: 29523
Explanation: 
We can write 3 one digit numbers, 9 two digit numbers, 27 three digit numbers,
81 four digit numbers, 243 five digit numbers, 729 six digit numbers,
2187 seven digit numbers, 6561 eight digit numbers, and 19683 nine digit numbers.
In total, this is 29523 integers that can be written using the digits array.
Example 3:

Input: digits = ["7"], n = 8
Output: 1
 

Constraints:

1 <= digits.length <= 9
digits[i].length == 1
digits[i] is a digit from '1' to '9'.
All the values in digits are unique.
1 <= n <= 109


'''


from typing import List
from functools import lru_cache


class Solution(object):

    def atMostNGivenDigitSetDP(self, digits, n):
        """
        :type digits: List[str]
        :type n: int
        :rtype: int
        """        
        num = str(n)
        m = len(digits)
        N = len(num)
        res = 0
        '''
        先来分析例子1，当n为 100 时，所有的一位数和两位数都是可以的，既然可以重复使用数字，
        假设总共有m个数字，那么对于两位数来说，十位上和个位上分别都有m种可能，总共就是m^2 
        种可能，对于一位数来说，总共m种可能。那么看到这里就可以归纳出当n总共有N位的话，
        我们就可以快速的求出不超过 N-1 位的所有情况综合，用个 for 循环，累加m的指数即可。
        '''
        for i in range(1,N):
            res += m ** i
        # compare each bit (left to right) of n to d in digits
        # only if i-th bit equals one of d, loop continues      
        for i in range(N):
            hasSameNum = False
            for d in digits:
                if d < num[i]: # the i-th bit can use d, the rest can use all
                               # digits so total # = m^(N-1-i) 
                    res += m**(N - 1 - i)
                elif d == num[i]: # no need to consider digits after d for i-th bit 
                    hasSameNum = True
            # if no d = i-th bit of n, we can return result        
            if not hasSameNum:
                return res
        return res+1    
         

        


    def atMostNGivenDigitSet(self, digits, n):
        """
        :type digits: List[str]
        :type n: int
        :rtype: int
        """
        self.res = 0  
        digits.sort()      
        def dfs(start, path):
            if path:
                if int(''.join(path)) <= n:
                   # print(int(''.join(path)))
                    self.res += 1
                else:
                    return            
            for i in range(len(digits)):       
            # We set the start to `i` because one element could
            # be used more than once
                path.append(digits[i])
                dfs(i, path)
                path.pop()
        dfs(0, [])
        return self.res
    

    def atMostNGivenDigitSet2(self, digits: List[str], n: int) -> int:
        N = str(n)         
        @lru_cache(None) 
        def dfs(i, comp): # comp ----(-1 -> current number is bigger, 0 -> same, 1 smaller)
            if i == len(N):
                return comp > -1
            if comp != 0:
                return 1 + len(digits) * dfs(i + 1, comp)
            ans = 1
            for d in digits:
                if d == N[i]:
                    ans += dfs(i + 1, 0)
                elif int(d) > int(N[i]):
                    ans += dfs(i + 1, -1)
                else:
                    ans += dfs(i + 1, 1)
            return ans
        return dfs(0, 0) - 1
    
    def atMostNGivenDigitSet3(self, digits: List[str], n: int) -> int:
        D = list(int(d) for d in digits)
        N = list(int(i) for i in str(n))

        @lru_cache(None)
        def dp(i, isPrefix, isBigger):
            if i == len(N):
                return not isBigger
            if not isPrefix and not isBigger:
                return 1 + len(D) * dp(i + 1, False, False)
            return 1 + sum(dp(i + 1, isPrefix and d == N[i], isBigger or (isPrefix and d > N[i])) for d in D)

        return dp(0, True, False) - 1
        


if __name__ == "__main__":
    print(Solution().atMostNGivenDigitSet(["1","3","5","7"], 100))
    print(Solution().atMostNGivenDigitSetDP(["1","3","5","7"], 300))
    #print(Solution().atMostNGivenDigitSet(["7"], 8))
    print(Solution().atMostNGivenDigitSet2(["1","3","5","7"], 100))
    # print(Solution().atMostNGivenDigitSet2(["1","3","5","7"], 300))
    print(Solution().atMostNGivenDigitSet3(["1","3","5","7"], 100))