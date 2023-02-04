
"""
-Medium-
*Dijkstra*

There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by 
rolling up, down, left or right, but it won't stop rolling until hitting a wall. When the ball stops, 
it could choose the next direction.

Given the ball's start position, the destination and the maze, find the shortest distance for the 
ball to stop at the destination. The distance is defined by the number of empty spaces traveled 
by the ball from the start position (excluded) to the destination (included). If the ball cannot 
stop at the destination, return -1.

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. 
You may assume that the borders of the maze are all walls. The start and destination coordinates 
are represented by row and column indexes.

 

Example 1:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: 12

Explanation: One shortest way is : left -> down -> left -> down -> right -> down -> right.
             The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

Example 2:

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: -1

Explanation: There is no way for the ball to stop at the destination.

 

Note:

There is only one ball and one destination in the maze.
Both the ball and the destination exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and both the width and height of the maze won't exceed 100.

"""
#from queue import Queue
from collections import deque
from collections import defaultdict
import heapq
import sys

class Solution(object):         

    def findShortestWay(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type ball: List[int]
        :type hole: List[int]
        :rtype: str
        """      
        start, destination = tuple(start), tuple(destination)
        row,col = len(maze),len(maze[0])
        def neighbors(maze, node):
            temp = []
            used = set()
            used.add(node)
            for dx, dy in [(-1, 0), (0, 1), (0, -1), (1, 0)]:
                (x,y), dist = node, 0
                while 0 <= x+dx < row and 0 <= y+dy < col and maze[x+dx][y+dy] == 0:
                    x += dx
                    y += dy
                    dist += 1
                if (x,y) not in used:
                    temp.append((dist, (x,y)))
            return temp

        heap = [(0, start)]
        visited = set()
        while heap:
            dist, node = heapq.heappop(heap)
            if node in visited: continue
            if node == destination:
                return dist
            visited.add(node)
            for neighbor_dist, neighbor in neighbors(maze, node):
                heapq.heappush(heap, (dist+neighbor_dist, neighbor))
        return -1
            

        
    def findShortestWayTLE(self, maze, ball, hole):    
        m,n = len(maze),len(maze[0])
        distance = [[sys.maxint for _ in range(n)] for _ in range(m)]          
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
                #print x, y, count, direct[0], direct[1]
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
    print(Solution().findShortestWay(maze, (4,3), (0,1)))
    maze = [[0,0,0,0,0],
            [1,1,0,0,1],
            [0,0,0,0,0],
            [0,1,0,0,1],
            [0,1,0,0,0]]
    print(Solution().findShortestWay(maze, (4,3), (0,1)))
    #if Solution().hasPath(maze, (0,4), (3,2)):
    #if Solution().hasPathBFS(maze, (0,4), (3,2)):
    
