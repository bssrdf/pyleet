'''
-Hard-
*Digit DP*
*DP*

You are given two numeric strings num1 and num2 and two integers max_sum and min_sum. We denote an integer x to be good if:

num1 <= x <= num2
min_sum <= digit_sum(x) <= max_sum.
Return the number of good integers. Since the answer may be large, return it modulo 109 + 7.

Note that digit_sum(x) denotes the sum of the digits of x.

 

Example 1:

Input: num1 = "1", num2 = "12", min_num = 1, max_num = 8
Output: 11
Explanation: There are 11 integers whose sum of digits lies between 1 and 8 are 1,2,3,4,5,6,7,8,10,11, and 12. Thus, we return 11.
Example 2:

Input: num1 = "1", num2 = "5", min_num = 1, max_num = 5
Output: 5
Explanation: The 5 integers whose sum of digits lies between 1 and 5 are 1,2,3,4, and 5. Thus, we return 5.
 

Constraints:

1 <= num1 <= num2 <= 1022
1 <= min_sum <= max_sum <= 400


'''

from functools import lru_cache
class Solution:
    def count(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        s = ""
        mod = 10**9 + 7

        @lru_cache(None)
        def dfs(idx, tight, sm):  
            # tight is 1/True means the digits chosen so far all matches s[:idx]
            # so next digit can not be bigger than s[idx]
            # otherwise if tight is 0/False, next digit can be free 0-9 
            nonlocal s,min_sum,max_sum,mod

            if idx == len(s):
                if sm >= min_sum and sm <= max_sum:
                    return 1
                return 0

            up = int(s[idx]) if tight else 9  
            res = 0
            for digit in range(up + 1):
                newSum = sm + digit
                if newSum > max_sum: # next digits are more greater than curr so newSum always greater
                    break
                res += dfs(idx + 1, tight and digit == up, newSum)
                res %= mod
            return res


        s = num2
        res = dfs(0,1,0)

        dfs.cache_clear()  # clear the dp states for new dfs

        s = str(int(num1)-1)
        res -= dfs(0,1,0)

        return res % mod
    
    def count2(self, num1: str, num2: str, min_sum: int, max_sum: int) -> int:
        # follows a Digit DP template
        s = ""
        mod = 10**9 + 7

        @lru_cache(None)
        def dp(i, isPrefix, isBigger, sm):
            if i == len(s):
                if not isBigger and sm >= min_sum and sm <= max_sum:
                    return 1
                return 0
            up = int(s[i]) if isPrefix else 9  
            res = 0
            for digit in range(up + 1):
                newSum = sm + digit
                if newSum > max_sum: # next digits are greater than curr so newSum always greater
                    break
                res += dp(i + 1, isPrefix and digit == up, isBigger or (isPrefix and digit > s[i]), newSum)
                res %= mod
            return res

        s = list(int(i) for i in num2)
        res = dp(0,True,False,0)

        dp.cache_clear()  # clear the dp states for new dfs

        s = list(int(i) for i in str(int(num1)-1))

        res -= dp(0,True,False,0)

        return res % mod
    
if __name__ == "__main__":
    print(Solution().count(num1 = "1", num2 = "5", min_sum = 1, max_sum = 5))
    print(Solution().count2(num1 = "1", num2 = "5", min_sum = 1, max_sum = 5))
    print(Solution().count(num1 = "18766", num2 = "987565966", min_sum = 10, max_sum = 255))
    print(Solution().count2(num1 = "18766", num2 = "987565966", min_sum = 10, max_sum = 255))