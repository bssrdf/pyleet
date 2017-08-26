# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 17:37:28 2017

@author: merli
"""

'''
A 2d grid map of m rows and n columns is initially filled with water. We may 
perform an addLand operation which turns the water at position (row, col) into 
a land. Given a list of positions to operate, count the number of islands 
after each addLand operation. An island is surrounded by water and is formed 
by connecting adjacent lands horizontally or vertically. You may assume all 
four edges of the grid are all surrounded by water.

Example:

Given m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]].
Initially, the 2d grid grid is filled with water. (Assume 0 represents water 
and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
We return the result as an array: [1, 1, 2, 3]

Challenge:

Can you do it in time complexity O(k log mn), where k is the length of the positions?


'''
from collections import deque

class Solution(object):
    
        
    def numIslands(self, m, n, positions):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        roots = [-1]*(m*n)
        cnt = 0
        dirs = [(-1,0), (0,-1), (1,0), (0,1)]
        for i,j in positions:                            
            idx = i*n+j
            roots[idx] = idx
            cnt += 1
            for r,c in dirs:
                i1,j1=i+r,j+c
                if i1<0 or i1>=n or j1<0 or j1>=m:
                    continue
                
                idx1 = n*i1+j1
                if roots[idx1] != -1:
                    x,y =self.find(roots, idx),self.find(roots, idx1) 
                    if x != y:
                        roots[x] = y
                        cnt -= 1
        return cnt
        
    def find(self, roots, i):
        # this while loop is called "qiuck union";
        # it "recursively" decends to the root node represented by the
        # node whose roots value is untouched 'i'
        while roots[i] != i:
            # path compression; set every other node in path point to its grandparent
            roots[i] = roots[roots[i]] 
            i = roots[i]
        return i

if __name__ == "__main__":
    positions = [[0,0],[0,1],[1,2],[2,1]]
    positions = [[0,0],[0,2],[0,1],[1,1]]
    print Solution().numIslands(3, 3, positions)