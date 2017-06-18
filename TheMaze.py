# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 00:45:51 2017

@author: merli
"""

class Solution(object):
    def solve(self, maze, start, end):
        
    
    
if __name__=="__main__":
    maze=[ [0, 0, 1, 0, 0],
           [0, 0, 0, 0, 0],
           [0, 0, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 0, 0, 0],
          ]          
    if Solution().solve(maze, (0,4), (4,4)):
        print 'True'
    else:
        print 'False'