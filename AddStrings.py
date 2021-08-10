'''
-Easy-

Given two non-negative integers, num1 and num2 represented as string, return 
the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large 
integers (such as BigInteger). You must also not convert the inputs to integers directly.

 

Example 1:

Input: num1 = "11", num2 = "123"
Output: "134"
Example 2:

Input: num1 = "456", num2 = "77"
Output: "533"
Example 3:

Input: num1 = "0", num2 = "0"
Output: "0"
 

Constraints:

1 <= num1.length, num2.length <= 104
num1 and num2 consist of only digits.
num1 and num2 don't have any leading zeros except for the zero itself.

'''

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        i, j = len(num1)-1, len(num2)-1
        res = []
        t = 0
        while i >= 0 and j >= 0:
            k = int(num1[i])+int(num2[j])+t
            if k >= 10:
                k -= 10
                t = 1
            else:
                t = 0
            res.append(str(k))
            i -= 1
            j -= 1
        l = -1
        if i >= 0:
            num = num1
            l = i
        elif j >= 0:
            num = num2
            l = j
        while l >= 0:
            k = int(num[i])+t
            if k >= 10:
                k -= 10
                t = 1
            else:
                t = 0
            res.append(str(k))
            l -= 1
        return ''.join(res[::-1])
        
    def addStrings2(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if len(num1) > len(num2):
            num2 = '0'*(len(num1)-len(num2))+num2
        elif len(num2) > len(num1):
            num1 = '0'*(len(num2)-len(num1))+num1
        i, j = len(num1)-1, len(num2)-1
        res = []
        t = 0
        while i >= 0 and j >= 0:
            k = int(num1[i])+int(num2[j])+t
            if k >= 10:
                k -= 10
                t = 1
            else:
                t = 0
            res.append(str(k))
            i -= 1
            j -= 1
        if t == 1:
            res.append(str(t))
        return ''.join(res[::-1])
    
if __name__ == "__main__":
    print(Solution().addStrings(num1 = "456", num2 = "77"))
    print(Solution().addStrings(num1 = "0", num2 = "0"))
    print(Solution().addStrings2(num1 = "456", num2 = "77"))
    print(Solution().addStrings2(num1 = "0", num2 = "0"))