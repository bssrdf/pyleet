'''
-Medium-

*Bit Manipulation*

Given two integers a and b, return the sum of the two integers without using the 

operators + and -.

 

Example 1:

Input: a = 1, b = 2
Output: 3
Example 2:

Input: a = 2, b = 3
Output: 5
 

Constraints:

-1000 <= a, b <= 1000


'''
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # 32 bits integer max
        MAX = 0x7FFFFFFF
        # 32 bits interger min
        MIN = 0x80000000
        # mask to get last 32 bits
        mask = 0xFFFFFFFF
        print(MIN, MAX)
        while b != 0:
            # ^ get different bits and & gets double 1s, << moves carry
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        # if a is negative, get a's 32 bits complement positive first
        # then get 32-bit positive's Python complement negative
        return a if a <= MAX else ~(a ^ mask)


    def getSumTLE(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # TLE for python but works in c, c++, java
        print('a: {:08b}'.format(a))
        print('b: {:08b}'.format(b))
        print('14: {:08b}'.format(14))
        print('-14: {:08b}'.format(-14))
        while b != 0 :
            c = a & b 
            a = a ^ b
            b = c << 1
            print('a: {:08b}'.format(a))
            print('b: {:08b}'.format(b))
            print('c: {:08b}'.format(c))
        #print('a: {:8b}'.format(a))    
        return a

if __name__ == "__main__":
    #print(Solution().getSum(3,2))
    #print(Solution().getSum(7,5))
    print(Solution().getSum(-1,1))
    print(Solution().getSumTLE(7,5))


    
