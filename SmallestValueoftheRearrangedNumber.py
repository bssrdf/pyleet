'''

-Medium-
*Sorting*


You are given an integer num. Rearrange the digits of num such that its value is minimized and it does not contain any leading zeros.

Return the rearranged number with minimal value.

Note that the sign of the number does not change after rearranging the digits.

 

Example 1:

Input: num = 310
Output: 103
Explanation: The possible arrangements for the digits of 310 are 013, 031, 103, 130, 301, 310. 
The arrangement with the smallest value that does not contain any leading zeros is 103.
Example 2:

Input: num = -7605
Output: -7650
Explanation: Some possible arrangements for the digits of -7605 are -7650, -6705, -5076, -0567.
The arrangement with the smallest value that does not contain any leading zeros is -7650.
 

Constraints:

-1015 <= num <= 1015


'''

class Solution:
    def smallestNumber(self, num: int) -> int:
        if num == 0: return 0
        dig = []
        k = abs(num)
        while k > 0:
            j = k % 10
            dig.append(j)
            k //= 10
        if num > 0:
            dig.sort()
            if dig[0] == 0:
                i = 0
                while i < len(dig) and dig[i] == 0:
                    i += 1
                dig[0], dig[i] = dig[i], dig[0]
            ans = 0
            for d in dig:
                ans = ans*10+d
            return ans        
        else:
            dig.sort(reverse=True)
            ans = 0
            for d in dig:
                ans = ans*10+d
            return -ans    