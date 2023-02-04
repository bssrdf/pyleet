'''

-Hard-
*Couting*
*DP*
*Digit DP*
*Bitmask*

We call a positive integer special if all of its digits are distinct.

Given a positive integer n, return the number of special integers that belong to the interval [1, n].

 

Example 1:

Input: n = 20
Output: 19
Explanation: All the integers from 1 to 20, except 11, are special. Thus, there are 19 special integers.
Example 2:

Input: n = 5
Output: 5
Explanation: All the integers from 1 to 5 are special.
Example 3:

Input: n = 135
Output: 110
Explanation: There are 110 integers from 1 to 135 that are special.
Some of the integers that are not special are: 22, 114, and 131.
 

Constraints:

1 <= n <= 2 * 109


'''

from functools import lru_cache

class Solution:
    def countSpecialNumbers(self, n: int) -> int:
        s, ans = str(n), 0
        digits = len(s)
        for i in range(1, digits):
            x, k = 1, 9
            for _ in range(i-1):
                x *= k
                k -= 1
            ans += 9 * x # ways to get special integers with digits less than that in n
        done = [0]*10
        for i in range(digits):
            smaller, idx = 0, ord(s[i])-ord('0') 
            for j in range(idx):
                if done[j] == 0:
                    smaller += 1
            if i == 0 and s[i] > '0':
                smaller -= 1
            aage, rem = 1, 10-i-1
            for _ in range(i+1, digits):
                aage *= rem
                rem -= 1
            ans += smaller * aage
            if done[idx] == 0:
                done[idx] = 1
            else:
                return ans
        return ans + 1
    

    def countSpecialNumbers2(self, n: int) -> int:
        # Digit DP solution
        s = str(n)
        @lru_cache(None)
        def dp(pos, tight, mask):
            # state:
            # pos: the position where a digit can be put, [1, len(s)]
            # tight: whether there is constraint on which digit can be picked: 0/1
            # mask: indicate which digit has been picked [0, 2^10] 
            if pos == len(s): return int(mask != 0)
            ans = 0
            if tight == 1:
                for i in range(ord(s[pos]) - ord('0')+1):
                    if mask & (1 << i) > 0: continue
                    newmask = mask if mask == 0 and i == 0 else (mask | (1<<i))
                    if i == ord(s[pos]) - ord('0'):
                        ans += dp(pos+1, 1, newmask)
                    else:
                        ans += dp(pos+1, 0, newmask)
            else:
                for i in range(10):
                    if mask & (1 << i) > 0: continue
                    newmask = mask if mask == 0 and i == 0 else (mask | (1<<i))
                    ans += dp(pos+1, 0, newmask)
            return ans
        return dp(0, 1, 0)


        
if __name__ == "__main__":
    print(Solution().countSpecialNumbers(135))
    print(Solution().countSpecialNumbers2(135))