'''
-Hard-
*DP*
*Digit DP*
Given a positive integer n, find the number of non-negative integers less than or 
equal to n, whose binary representations do NOT contain consecutive ones.

Example 1:
Input: 5
Output: 5
Explanation: 
Here are the non-negative integers <= 5 with their corresponding binary representations:
0 : 0
1 : 1
2 : 10
3 : 11
4 : 100
5 : 101
Among them, only integer 3 disobeys the rule (two consecutive ones) and the other 5 
satisfy the rule. 
Note: 1 <= n <= 10^9

'''

from functools import lru_cache

class Solution(object):
    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        dp = [0]*(num+1)
        dp[0] = 1
        def isConsecutive(n):            
            return (n & (n >> 1))        
        for i in range(1,num+1):                                             
                j = i-1
                while j >= 0 and isConsecutive(j):                    
                    j -= 1                 
                if isConsecutive(i):
                    dp[i] = dp[j]
                else:                      
                    dp[i] = dp[j]+1   
        return dp[num]

    def findIntegersFast(self, num):
        """
        :type num: int
        :rtype: int
        """                
        t = bin(num)[2:][::-1]
        cnt = len(t) 
        zero, one = [0]*(cnt), [0]*(cnt)
        zero[0] = 1 
        one[0] = 1
        for i in range(1,cnt):
            zero[i] = zero[i - 1] + one[i - 1]
            one[i] = zero[i - 1]
        res = zero[cnt - 1] + one[cnt - 1]
        print(t, res, one) 
        for i in range(cnt - 2, -1, -1):
            if t[i] == '1' and t[i + 1] == '1': break
            if t[i] == '0' and t[i + 1] == '0': res -= one[i]
        return res
    
    def findIntegersFibonacci(self, num):
        """
        :type num: int
        :rtype: int
        """         
        res, dp, k, pre = 0, [0]*32, 31, 0
        dp[0], dp[1] = 1, 2
        for i in range(2, 32):
            dp[i] = dp[i-1] + dp[i-2]
        while k>=0:
            if num & 1 << k:
                res += dp[k]
                if pre: return res
                pre = 1
            else:
                pre = 0
            k -= 1
        return res+1
    
    def findIntegers2(self, n):
        # digit DP solution
        s = bin(n)[2:]
        @lru_cache(None) 
        def dp(pos, last, tight):
            if pos == len(s):
                return 1
            ans = 0
            limit = ord(s[pos]) - ord('0') if tight else 1 
            for i in range(limit+1):                
                ntight = tight and i == limit
                if last == 1:
                    if i != 1:
                       ans += dp(pos+1, False, ntight)
                else:
                    ans += dp(pos+1, i == 1, ntight)
            return ans        
        return dp(0, 0, True) 
    
        



if __name__ == "__main__":
    #print(Solution().findIntegers(10000))
    #print(Solution().findIntegersFast(10000))
    # print(Solution().findIntegersFast(20))
    # print(Solution().findIntegersFibonacci(20))
    # print(Solution().findIntegersFast(5))
    print(Solution().findIntegersFibonacci(5))
    print(Solution().findIntegers2(5))
    print(Solution().findIntegers(10000))
    print(Solution().findIntegers2(10000))