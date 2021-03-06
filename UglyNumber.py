# -*- coding: utf-8 -*-
"""
Created on Sun Jul 23 14:50:09 2017

@author: merli
"""

"""
Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not
ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.
"""
__author__ = 'Daniel'


class Solution(object):
    def isUglySimple(self, num):    
        for p in 2, 3, 5:
            #while num % p == 0 < num:
            while num % p == 0:
                num /= p
               # print num, p
        return num == 1
    
    def isUgly(self, num):
        """
        Prime factors: 2, 3, 5

        :type num: int
        :rtype: bool
        """
        if num < 1:
            return False
        if num == 1:
            return True

        ugly = {2, 3, 5}

        prime = 2
        while prime*prime <= num and num > 1:
            if num % prime != 0:
                prime += 1
            else:
                num /= prime
                if prime not in ugly:
                    return False

        if num not in ugly:
            return False

        return True
        
if __name__ == "__main__":
    for n in range(2,10000):
    #n= 71
        assert Solution().isUgly(n) == Solution().isUglySimple(n)