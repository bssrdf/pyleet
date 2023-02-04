# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 00:45:51 2017

@author: merli
"""
import sys
from queue import Queue

class Solution(object):    
    
    def solve(self, board, start, end):
        row = [ -1,  0, 0,  1 ]
        col = [  0, -1, 1,  0 ]    
        m,n = len(board),len(board[0])
        visi = [[False for _ in xrange(n)] for _ in xrange(m)]
        def go(di, dj, i, j):
            while 0 <= (i+di) < m and 0 <= (j+dj) < n and board[i+di][j+dj] == 0:
                i += di
                j += dj
            return (i,j)
        def DFS(x, y, target, replacement):
            board[x][y] = replacement                        
            for r,c in zip(row, col):
                i,j = go(r,c,x,y)
                if i==end[0] and j==end[1]:
                    return True                    
                #if i>=0 and i<len(board) and j>=0 and j<len(board[0]) and board[i][j] == target:                                                
                return DFS(i, j, target, replacement)                 
            return False        
            
        return DFS(start[0], start[1], 0, -1)
        
    def hasPath(self, maze, start, destination):
        return self.helper(maze, destination, start[0], start[1])
        
    
    def helper(self, maze, dest, i, j):
        if (i, j) == dest:
            return True
        if maze[i][j] == 2:
            return False
        up, down, left, right = i, i, j, j
        while up > 0 and maze[up-1][j] != 1:
            up -= 1
        while down < len(maze)-1 and maze[down+1][j] != 1:
            down += 1
        while left > 0 and maze[i][left-1] != 1:
            left -= 1
        while right < len(maze[0])-1 and maze[i][right+1] != 1:
            right += 1
        maze[i][j] = 2
        return self.helper(maze, dest, up, j) or self.helper(maze, dest, down, j) or self.helper(maze, dest, i, left) or self.helper(maze, dest, i, right)
        
    def PathBFS(self, maze, start, destination):
        m,n = len(maze),len(maze[0])
        visited = [[False for _ in xrange(n)] for _ in xrange(m)]
        q = Queue(m*n) 
        q.enqueue((start, 0))
        visited[start[0]][start[1]] = True
        min_dis = sys.maxint
        while not q.isEmpty():
            (i,j),dist = q.dequeue()
            if i==destination[0] and j==destination[1]:
                min_dist = dist
                break
            up, down, left, right = i, i, j, j
            if up >= 1 and maze[up-1][j] == 1:
                up -= 1
            if down <= len(maze)-2 and maze[down+1][j] == 1:
                down += 1
            if left >=1 and maze[i][left-1] == 1:
                left -= 1
            if right <= len(maze[0])-2 and maze[i][right+1] == 1:
                right += 1
            if not visited[up][j]:
                q.enqueue(((up,j),dist+1))
                visited[up][j] = True                
            if not visited[down][j]:
                q.enqueue(((down,j),dist+1))
                visited[down][j] = True
            if not visited[i][left]:
                q.enqueue(((i,left),dist+1))
                visited[i][left] = True
            if not visited[i][right]:
                q.enqueue(((i,right),dist+1))
                visited[i][right] = True
        if min_dist == sys.maxint:
            print 'destination not reached'
        else:
            print 'min path is ', min_dist

    
if __name__=="__main__":
    maze=[ [0, 0, 1, 1, 1, 1],
           [0, 0, 1, 0, 0, 1],
           [0, 0, 1, 1, 1, 1],
           [1, 1, 1, 1, 1, 0],
           [0, 0, 0, 0, 1, 0],
           [0, 0, 0, 0, 1, 0],
          ]          
    Solution().PathBFS(maze, (5,4), (0,2))
