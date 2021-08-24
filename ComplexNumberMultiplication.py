'''
-Medium-

A complex number can be represented as a string on the form "real+imaginaryi" 
where:

real is the real part and is an integer in the range [-100, 100].
imaginary is the imaginary part and is an integer in the range [-100, 100].
i2 == -1.
Given two complex numbers num1 and num2 as strings, return a string of the 
complex number that represents their multiplications.

 

Example 1:

Input: num1 = "1+1i", num2 = "1+1i"
Output: "0+2i"
Explanation: (1 + i) * (1 + i) = 1 + i2 + 2 * i = 2i, and you need convert it to the form of 0+2i.
Example 2:

Input: num1 = "1+-1i", num2 = "1+-1i"
Output: "0+-2i"
Explanation: (1 - i) * (1 - i) = 1 + i2 - 2 * i = -2i, and you need convert it to the form of 0+-2i.
 

Constraints:

num1 and num2 are valid complex numbers.

'''
class Solution(object):
    def complexNumberMultiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        def decompose(num):
            real,img = num.split('+')
            return int(real), int(img[:-1])
        r1,i1 = decompose(num1)
        r2,i2 = decompose(num2)
        a = r1*r2
        b = -i1*i2
        c = r1*i2 + r2*i1
        return str(a+b)+'+'+str(c)+'i'