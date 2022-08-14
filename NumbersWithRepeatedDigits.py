'''
-Hard-
*Counting*
*DP*
*Digit DP*


Given an integer n, return the number of positive integers in the range [1, n] that have at least one repeated digit.

 

Example 1:

Input: n = 20
Output: 1
Explanation: The only positive number (<= 20) with at least 1 repeated digit is 11.
Example 2:

Input: n = 100
Output: 10
Explanation: The positive numbers (<= 100) with atleast 1 repeated digit are 11, 22, 33, 44, 55, 66, 77, 88, 99, and 100.
Example 3:

Input: n = 1000
Output: 262
 

Constraints:

1 <= n <= 109

'''

class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
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
                return n - ans
        return n - (ans + 1)
        