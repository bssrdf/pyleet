'''
-Easy-

Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 10^4
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.

'''

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        res = []

        i, j = len(a) - 1, len(b) - 1
        carry = 0

        while i >= 0 or j >= 0:
            total = carry
            if i >= 0: 
                total += int(a[i])
                i -= 1
            if j >= 0:
                total += int(b[j])
                j -= 1
            #print(total%2, carry)
            res.append(str(total % 2))
            carry = total // 2

        if carry:
            res.append(str(carry))

        return "".join(res)[::-1]

if __name__ == "__main__":
    print(Solution().addBinary("1010", "1011"))
    print(Solution().addBinary("1011", "1011"))