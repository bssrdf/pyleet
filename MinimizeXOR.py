'''

-Medium-

Given two positive integers num1 and num2, find the integer x such that:

x has the same number of set bits as num2, and
The value x XOR num1 is minimal.
Note that XOR is the bitwise XOR operation.

Return the integer x. The test cases are generated such that x is uniquely determined.

The number of set bits of an integer is the number of 1's in its binary representation.

 

Example 1:

Input: num1 = 3, num2 = 5
Output: 3
Explanation:
The binary representations of num1 and num2 are 0011 and 0101, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 3 = 0 is minimal.
Example 2:

Input: num1 = 1, num2 = 12
Output: 3
Explanation:
The binary representations of num1 and num2 are 0001 and 1100, respectively.
The integer 3 has the same number of set bits as num2, and the value 3 XOR 1 = 2 is minimal.
 

Constraints:

1 <= num1, num2 <= 109

'''

class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        cnt2 = bin(num2).count('1')
        cnt1 = bin(num1).count('1')
        if cnt1 == cnt2: return num1
        elif cnt1 < cnt2:
            ans, d = num1, cnt2 - cnt1
            for i in range(31):
                if ans & (1<<i) == 0 and d > 0:
                    ans |= (1 << i)
                    d -= 1
            return ans
        else:
            ans, d  = 0, cnt2
            for i in range(31, -1, -1):
                if num1 & (1<<i) > 0 and d > 0:
                    ans |= (1 << i)
                    d -= 1
            return ans
        