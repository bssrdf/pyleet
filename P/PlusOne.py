# -*- coding: utf-8 -*-
"""
Created on Sat Aug 12 19:31:59 2017

@author: merli
"""

class Solution(object):
     def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        l = len(digits)-1
        plus = False
        while l >= 0:
            if l == len(digits)-1 or plus:
                digits[l] += 1
                if digits[l] <= 9 and plus:
                    plus = False
                if digits[l] > 9:
                    if not plus:                        
                        plus = True
                    digits[l] = 0
            l -= 1
        if plus:
            return [1]+digits
        else:
            return digits
        
        
if __name__ == "__main__":
    #dg = [9,9,9]
    #dg = [7,8,6,0]
    dg = [9]
    print Solution().plusOne(dg)