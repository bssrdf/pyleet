# -*- coding: utf-8 -*-
"""
Created on Sun Jun 25 14:20:26 2017

@author: merli
"""



class Solution(object):
    def insertAtBottom(self, s, ele):
        if s:
            tmp = s.pop()
            self.insertAtBottom(s, ele)
            s.append(tmp)
        else:
            s.append(ele)
    
    def reverseStack(self, s, level):
        level += 1
        if s:
            top = s.pop()
            #print level, s
            self.reverseStack(s, level)
            print level, top, s
            self.insertAtBottom(s, top)
            #print level, s
        
        
        
if __name__ == "__main__":
    s = [x for x in range(10)]
    Solution().reverseStack(s, 0)
    print s
