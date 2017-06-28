# -*- coding: utf-8 -*-
"""
Created on Wed Jun 28 00:55:07 2017

@author: merli
"""

class Solution(object):
    def TestRecursion(self, mL):
        #mL = 0
        def dfs(s):
            #if mL < s:
            mL = s
            if s>10:
                return
            else:
                s+=1
                dfs(s)
        dfs(0)
        print mL
            
if __name__ == "__main__":
    #print Solution().TestRecursion()
    Solution().TestRecursion(0)