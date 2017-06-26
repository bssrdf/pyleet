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
#from queue import Queue
from collections import deque
from collections import defaultdict
import sys

class Solution(object):               
            

    def findShortestWay(self, maze, ball, hole):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str
        """
        ball, hole = tuple(ball), tuple(hole)
        dmap = defaultdict(lambda: defaultdict(int))
        w, h = len(maze), len(maze[0])
        for dir in 'dlru': dmap[hole][dir] = hole
        for x in range(w):
            for y in range(h):
                if maze[x][y] or (x, y) == hole: continue
                dmap[(x, y)]['u'] = dmap[(x - 1, y)]['u'] if x > 0 and dmap[(x - 1, y)]['u'] else (x, y)
                dmap[(x, y)]['l'] = dmap[(x, y - 1)]['l'] if y > 0 and dmap[(x, y - 1)]['l'] else (x, y)
        print dmap[ball]['l'],dmap[ball]['u'] 
        for x in range(w - 1, -1, -1):
            for y in range(h - 1, -1, -1):
                if maze[x][y] or (x, y) == hole: continue
                dmap[(x, y)]['d'] = dmap[(x + 1, y)]['d'] if x < w - 1 and dmap[(x + 1, y)]['d'] else (x, y)
                dmap[(x, y)]['r'] = dmap[(x, y + 1)]['r'] if y < h - 1 and dmap[(x, y + 1)]['r'] else (x, y)
        print dmap[ball]['r'],dmap[ball]['d'] 
        bmap = {ball : (0, '')}
        distance = lambda pa, pb: abs(pa[0] - pb[0]) + abs(pa[1] - pb[1])
        queue = deque([(ball, 0, '')])
        while queue:
            front, dist, path = queue.popleft()
            for dir in 'dlru':
                if dir not in dmap[front]: continue
                np = dmap[front][dir]
                ndist = dist + distance(front, np)
                npath = path + dir
                if np not in bmap or (ndist, npath) < bmap[np]:
                    bmap[np] = (ndist, npath)
                    queue.append((np, ndist, npath))
        return bmap[hole][1] if hole in bmap else 'impossible'    
        
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
    print Solution().findShortestWay(maze, (4,3), (0,1))
    #print Solution().findShortestWayDFS(maze, (4,3), (0,1))
    #if Solution().hasPath(maze, (0,4), (4,4)):
    #if Solution().hasPath(maze, (0,4), (3,2)):
    #if Solution().hasPathBFS(maze, (0,4), (3,2)):
    
