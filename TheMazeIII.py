'''
-Hard-

*Dijkstra*
*BFS*

There is a ball in a maze with empty spaces and walls. The ball can go through empty spaces by 
rolling up (u), down (d), left (l) or right (r), but it won't stop rolling until hitting a wall. 
When the ball stops, it could choose the next direction. There is also a hole in this maze. 
The ball will drop into the hole if it rolls on to the hole.

Given the ball position, the hole position and the maze, find out how the ball could drop into the 
hole by moving the shortest distance. The distance is defined by the number of empty spaces traveled 
by the ball from the start position (excluded) to the hole (included). Output the moving directions 
by using 'u', 'd', 'l' and 'r'. Since there could be several different shortest ways, you should 
output the lexicographically smallest way. If the ball cannot reach the hole, output "impossible".

The maze is represented by a binary 2D array. 1 means the wall and 0 means the empty space. 
You may assume that the borders of the maze are all walls. The ball and the hole coordinates 
are represented by row and column indexes.

 

Example 1:

Input 1: a maze represented by a 2D array

0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
0 1 0 0 1
0 1 0 0 0

Input 2: ball coordinate (rowBall, colBall) = (4, 3)
Input 3: hole coordinate (rowHole, colHole) = (0, 1)

Output: "lul"

Explanation: There are two shortest ways for the ball to drop into the hole.
The first way is left -> up -> left, represented by "lul".
The second way is up -> left, represented by 'ul'.
Both ways have shortest distance 6, but the first way is lexicographically smaller because 'l' < 'u'. 
So the output is "lul".

Example 2:

Input 1: a maze represented by a 2D array

0 0 0 0 0
1 1 0 0 1
0 0 0 0 0
0 1 0 0 1
0 1 0 0 0

Input 2: ball coordinate (rowBall, colBall) = (4, 3)
Input 3: hole coordinate (rowHole, colHole) = (3, 0)

Output: "impossible"

Explanation: The ball cannot reach the hole.

 

Note:

There is only one ball and one hole in the maze.
Both the ball and hole exist on an empty space, and they will not be at the same position initially.
The given maze does not contain border (like the red rectangle in the example pictures), but you could assume the border of the maze are all walls.
The maze contains at least 2 empty spaces, and the width and the height of the maze won't exceed 30.


'''
from collections import deque
from collections import defaultdict
import heapq
class Solution:
    """
    @param maze: the maze
    @param ball: the ball position
    @param hole: the hole position
    @return: the lexicographically smallest way
    """
    def findShortestWayBFS(self, maze, ball, hole):
        # write your code here
        ball, hole = tuple(ball), tuple(hole)
        dmap = defaultdict(lambda: defaultdict(int))
        w, h = len(maze), len(maze[0])
        for dir in 'dlru': dmap[hole][dir] = hole
        for x in range(w):
            for y in range(h):
                if maze[x][y] or (x, y) == hole: continue
                dmap[(x, y)]['u'] = dmap[(x - 1, y)]['u'] if x > 0 and dmap[(x - 1, y)]['u'] else (x, y)
                dmap[(x, y)]['l'] = dmap[(x, y - 1)]['l'] if y > 0 and dmap[(x, y - 1)]['l'] else (x, y)
        #print dmap[ball]['l'],dmap[ball]['u'] 
        for x in range(w - 1, -1, -1):
            for y in range(h - 1, -1, -1):
                if maze[x][y] or (x, y) == hole: continue
                dmap[(x, y)]['d'] = dmap[(x + 1, y)]['d'] if x < w - 1 and dmap[(x + 1, y)]['d'] else (x, y)
                dmap[(x, y)]['r'] = dmap[(x, y + 1)]['r'] if y < h - 1 and dmap[(x, y + 1)]['r'] else (x, y)
        #print dmap[ball]['r'],dmap[ball]['d'] 
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
    

    def findShortestWay(self, maze, ball, hole):
        # write your code here
        start, destination = tuple(ball), tuple(hole)
        row,col = len(maze),len(maze[0])
        def neighbors(maze, node):
            #temp = []
            #used = set()
            #used.add(node)
            for (dx, dy), dir in zip([(-1, 0), (0, 1), (0, -1), (1, 0)], 'urld'):
                (x,y), dist = node, 0
                while 0 <= x+dx < row and 0 <= y+dy < col and maze[x+dx][y+dy] == 0:
                    x += dx
                    y += dy
                    dist += 1
                    if (x,y) == destination: break
             #   if (x,y) not in used:
              #      temp.append((dist, dir, (x,y)))
                yield (dist, dir, (x,y))
            #return temp

        heap = [(0, '', start)]
        visited = set()
        while heap:
            dist, path, node = heapq.heappop(heap)
            #print(dist, path, node)
            if node == destination:  return path
            if node in visited: continue            
            visited.add(node)
            for neighbor_dist, npath, neighbor in neighbors(maze, node):
                heapq.heappush(heap, (dist+neighbor_dist, path+npath, neighbor))
        return 'impossible'
            

if __name__=="__main__":
    '''
    maze=[ [0, 0, 1, 0, 0],
           [1, 1, 0, 0, 1],
           [0, 0, 0, 0, 0],
           [0, 1, 0, 0, 1],
           [0, 1, 0, 0, 0],
          ]          
    print(Solution().findShortestWayBFS(maze, (4,3), (0,4)))
    print(Solution().findShortestWay(maze, (4,3), (0,4)))
    '''
    maze = [[0,0,0,0,0],
            [1,1,0,0,1],
            [0,0,0,0,0],
            [0,1,0,0,1],
            [0,1,0,0,0]]
    #print(Solution().findShortestWay(maze, (4,3), (3,0)))    
    print(Solution().findShortestWay(maze, (4,3), (0,1)))

