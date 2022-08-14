'''

-Hard-
*Couting*
*DP*
*Digit DP*

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
            
        
if __name__ == "__main__":
    print(Solution().countSpecialNumbers(135))