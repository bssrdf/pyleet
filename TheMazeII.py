# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 17:15:28 2017

@author: merli
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Jun 18 00:45:51 2017

@author: merli
"""
from queue import Queue
import sys

class Solution(object):               
    
    def findShortestWay(self, maze, ball, hole):             
        m,n = len(maze),len(maze[0])
        visited = [[False for _ in xrange(n)] for _ in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if maze[i][j] == 0:
                    xy={}
                    up, down, left, right = i, i, j, j
                    while up > 0 and maze[up-1][j] != 1:
                        up -= 1
                    while down < len(maze)-1 and maze[down+1][j] != 1:
                        down += 1
                    while left > 0 and maze[i][left-1] != 1:
                        left -= 1
                    while right < len(maze[0])-1 and maze[i][right+1] != 1:
                        right += 1
                    xy['u'] = (up, j)
                    xy['d'] = (down, j)        
                    xy['l'] = (i, left)
                    xy['r'] = (i, right)
                    dmap[(i,j)] = xy
        q = Queue(m*n) 
        q.enqueue((ball,0,''))
        #while not q.isEmpty():
         #   p=q.dequeue()
            
        return ' '
        
    def findShortestWayDFS(self, maze, ball, hole):    
        m,n = len(maze),len(maze[0])
        distance = [[sys.maxint for _ in xrange(n)] for _ in xrange(m)]          
        distance[ball[0]][ball[1]] = 0
        dirs=((-1,0), (1,0), (0,-1), (0,1))
        def dfs(maze, start, dest, distance):
            for direct in dirs:
                count = 0
                x=start[0]+direct[0]
                y=start[1]+direct[1]
                while x >= 0 and y >= 0 and x < m and y < n and maze[x][y] == 0:
                    x += direct[0]
                    y += direct[1]
                    count +=1
                print x, y, count, direct[0], direct[1]
                if distance[start[0]][start[1]]+count < distance[x-direct[0]][y-direct[1]]:
                    distance[x-direct[0]][y-direct[1]] = distance[start[0]][start[1]]+count
                    dfs(maze, (x-direct[0],y-direct[1]), dest, distance)
                
        dfs(maze, ball, hole, distance)
        if distance[hole[0]][hole[1]] == sys.maxint:
            return -1
        else:
            return distance[hole[0]][hole[1]]            
        
          
   
if __name__=="__main__":
    maze=[ [0, 0, 1, 0, 0],
           [1, 1, 0, 0, 1],
           [0, 0, 0, 0, 0],
           [0, 1, 0, 0, 1],
           [0, 1, 0, 0, 0],
          ]          
    #print Solution().findShortestWay(maze, (4,3), (0,1))
    print Solution().findShortestWayDFS(maze, (4,3), (0,1))
    #if Solution().hasPath(maze, (0,4), (4,4)):
    #if Solution().hasPath(maze, (0,4), (3,2)):
    #if Solution().hasPathBFS(maze, (0,4), (3,2)):
    