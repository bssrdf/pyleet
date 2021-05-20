'''
-Medium-
Given two non-negative integers num1 and num2 represented as strings, return 
the product of num1 and num2, also represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs 
to integer directly.

 

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
 

Constraints:

1 <= num1.length, num2.length <= 200
num1 and num2 consist of digits only.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.


'''

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = ""
        m, n = len(num1), len(num2)
        vals = [0]*(m + n)
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = (ord(num1[i]) - ord('0')) * (ord(num2[j]) - ord('0'))
                p1, p2 = i + j, i + j + 1 
                sm = mul + vals[p2]
                vals[p1] += sm // 10
                vals[p2] = sm % 10
        for val in vals:
            if not res and val == 0: continue
            res += str(val)
        return res if res else '0'
if __name__ == "__main__":
    print(Solution().multiply(num1 = "123", num2 = "456"))