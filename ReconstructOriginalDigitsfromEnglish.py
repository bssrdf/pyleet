'''
-Medium-

Given a non-empty string containing an out-of-order English representation of digits 0-9, 
output the digits in ascending order.

Note:
Input contains only lowercase English letters.
Input is guaranteed to be valid and can be transformed to its original digits. That means 
invalid inputs such as "abc" or "zerone" are not permitted.
Input length is less than 50,000.
Example 1:
Input: "owoztneoer"

Output: "012"
Example 2:
Input: "fviefuro"

Output: "45"


'''
import string 
from collections import defaultdict
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        m, digits = {}, [0]*10
        for c in s:
            m[c] = m.setdefault(c, 0)+1
        digits[0] = m.setdefault('z',0)
        digits[6] = m.setdefault('x',0)
        digits[2] = m.setdefault('w',0)
        digits[8] = m.setdefault('g',0)
        digits[7] = m.setdefault('s',0)-digits[6]
        digits[5] = m.setdefault('v',0)-digits[7]
        digits[4] = m.setdefault('f',0)-digits[5]
        digits[3] = m.setdefault('r',0)-digits[0]-digits[4]  
        digits[1] = m.setdefault('o',0)-digits[0]-digits[2]-digits[4]  
        digits[9] = m.setdefault('i',0)-digits[5]-digits[6]-digits[8]  
        res = ''
        for i in range(10):
            if digits[i] > 0: res += str(i)*digits[i]
        return res

            

if __name__ == "__main__":
    print(Solution().originalDigits("owoztneoer"))
