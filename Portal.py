'''
-Medium-
*BFS*
*Bidirectional BFS*

Chell is the protagonist of the Portal Video game series developed by Valve Corporation.
One day, She fell into a maze. The maze can be thought of as an array of 2D characters of 
size n x m. It has 4 kinds of rooms. 'S' represents where Chell started(Only one starting point). 
'E' represents the exit of the maze(When chell arrives, she will leave the maze, this question 
may have multiple exits). '*' represents the room that Chell can pass. '#' represents a wall, 
Chell can not pass the wall.
She can spend a minute moving up,down,left and right to reach a room, but she can not reach the wall.
Now, can you tell me how much time she needs at least to leave the maze?
If she can not leave, return -1.

We guarantee that the size of the maze is n x m, and 1<=n<=200,1<=m<=200.
There is only one 'S', and one or more 'E'.
样例
Example1

Input: 
[
    ['S','E','*'],
    ['*','*','*'],
    ['*','*','*']
]
Output: 1
Explanation:
Chell spent one minute walking from (0,0) to (0,1).
Example2

Input: 
[
    ['S','#','#'], 
    ['#','*','#'], 
    ['#','*','*'], 
    ['#','*','E']
]
Output: -1
Explanation:
Chell can not leave the maze.


'''

from collections import deque
class Solution:
    """
    @param Maze: 
    @return: nothing
    """
    def Portal(self, Maze):
        # 
        A = Maze
        m, n = len(Maze), len(Maze[0])
        qs, qt = deque(), deque()
        vs, vt = set(), set()
        dirs = [ (-1,0), (1,0), (0,-1), (0,1)]
        for i in range(m):
            for j in range(n):
                if A[i][j] == 'S':
                    qs.append((i,j))
                    vs.add((i,j))
                if A[i][j] == 'E':
                    qt.append((i,j))
                    vt.add((i,j))
        sk, tk = 0, 0 
        while qs and qt:
            nxt = deque()
            for _ in range(len(qs)):
                si,sj = qs.popleft()
                if (si, sj) in vt:
                    return sk+tk
                for dx,dy in dirs:
                    x, y = si+dx, sj+dy
                    if x >= 0 and x < m and y >= 0 and y < n and (x,y) not in vs and A[x][y]!='#':
                        vs.add((x,y))
                        nxt.append((x,y))                        
            sk += 1
            qs = nxt
            nxt = deque()
            for _ in range(len(qt)):
                si,sj = qt.popleft()
                if (si, sj) in vs:
                    return sk+tk
                for dx,dy in dirs:
                    x, y = si+dx, sj+dy
                    if x >= 0 and x < m and y >= 0 and y < n and (x,y) not in vt and A[x][y]!='#':
                        vt.add((x,y))
                        nxt.append((x,y))                        
            tk += 1
            qt = nxt
        return -1

if __name__ == "__main__":
    maze = [
            ['S','E','*'],
            ['*','*','*'],
            ['*','*','*']
            ]
    print(Solution().Portal(maze))
    maze = [
    ['S','#','#'], 
    ['#','*','#'], 
    ['#','*','*'], 
    ['#','*','E']
]
    print(Solution().Portal(maze))
    maze = ["S*E",
            "***",
            "#**",
            "##E"]
    print(Solution().Portal(maze))



                

        


