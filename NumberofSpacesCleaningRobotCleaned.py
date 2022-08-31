'''
-Medium-

$$$

A room is represented by a 0-indexed 2D binary matrix room where a 0 represents an empty space and a 1 represents a space with an object. The top left corner of the room will be empty in all test cases.

A cleaning robot starts at the top left corner of the room and is facing right. The robot will continue heading straight until it reaches the edge of the room or it hits an object, after which it will turn 90 degrees clockwise and repeat this process. The starting space and all spaces that the robot visits are cleaned by it.

Return the number of clean spaces in the room if the robot runs indefinetely.

 

Example 1:


Input: room = [[0,0,0],[1,1,0],[0,0,0]]
Output: 7
Explanation:
The robot cleans the spaces at (0, 0), (0, 1), and (0, 2).
The robot is at the edge of the room, so it turns 90 degrees clockwise and now faces down.
The robot cleans the spaces at (1, 2), and (2, 2).
The robot is at the edge of the room, so it turns 90 degrees clockwise and now faces left.
The robot cleans the spaces at (2, 1), and (2, 0).
The robot has cleaned all 7 empty spaces, so return 7.
Example 2:


Input: room = [[0,1,0],[1,0,0],[0,0,0]]
Output: 1
Explanation:
The robot cleans the space at (0, 0).
The robot hits an object, so it turns 90 degrees clockwise and now faces down.
The robot hits an object, so it turns 90 degrees clockwise and now faces left.
The robot is at the edge of the room, so it turns 90 degrees clockwise and now faces up.
The robot is at the edge of the room, so it turns 90 degrees clockwise and now faces right.
The robot is back at its starting position.
The robot has cleaned 1 space, so return 1.
 

Constraints:

m == room.length
n == room[r].length
1 <= m, n <= 300
room[r][c] is either 0 or 1.
room[0][0] == 0



'''



from typing import List

class Solution:
    def numberOfCleanRooms(self, room: List[List[int]]) -> int:
        # wrong
        m, n = len(room), len(room[0])
        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans, k = 1, 0
        r, c = 0, 0
        room[r][c] = 2
        vis = {(r, c, k%4)}
        while True:
            dir = dirs[k % 4]            
            r1, c1 = r + dir[0], c + dir[1]  
            if (r1, c1, k%4) in vis: break
            if 0 <= r1 < m and 0 <= c1 < n: 
                if room[r1][c1] == 0:
                    ans += 1
                    r, c = r1, c1
                    # print(ans, r1, c1)
                    room[r1][c1] = 2
                    vis.add((r1, c1, k%4))
                elif room[r1][c1] == 1:
                    vis.add((r1, c1, k%4))
                    k += 1   
                else:
                    r, c = r1, c1
                    vis.add((r1, c1, k%4))                
            else:
                k += 1
        return ans
    
    def numberOfCleanRooms2(self, room: List[List[int]]) -> int:
        m = len(room)
        n = len(room[0])
        dirs = [0, 1, 0, -1, 0]
        ans = 1
        i = 0
        j = 0
        state = 0  # 0 := right, 1 := down, 2 := left, 3 := up
        seen = {(i, j, state)}
        room[i][j] = 2  # 2 := cleaned

        while True:
            x = i + dirs[state]
            y = j + dirs[state + 1]
            if x < 0 or x == m or y < 0 or y == n or room[x][y] == 1:
                # turns 90 degrees clockwise
                state = (state + 1) % 4
            else:
                # walk to (x, y)
                if room[x][y] == 0:
                    ans += 1
                    room[x][y] = 2
                i = x
                j = y
            if (x, y, state) in seen:
                return ans
            seen.add((x, y, state))

from random import randint, random

if __name__ == "__main__":
    # print(Solution().numberOfCleanRooms(room = [[0,0,0],[1,1,0],[0,0,0]]))
    # print(Solution().numberOfCleanRooms(room = [[0,1,0],[1,0,0],[0,0,0]]))
    # room = [[0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0],
    #         [1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    #         [1, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0],
    #         [0, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1, 1],
    #         [1, 1, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1]]
    room = [[0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 1],
            [1, 0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0],
            [1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 1, 0, 0, 0]]
    sol = Solution().numberOfCleanRooms(room = room )
    print(sol)
    # sol = Solution().numberOfCleanRooms2(room = room )
    # print(sol)
    m, n = 30, 20
    room = []
    for r in range(m):
        tmp = []
        for j in range(n):
            tmp.append(0 if random() > 0.1 else 1)
        room.append(tmp)
    room[0][0] = 0
    roomc = [[c for c in row] for row in room] 
    room2 = [[c for c in row] for row in room] 
    sol2 = Solution().numberOfCleanRooms2(room = room2)
    print('correct sol', sol2)
    for r in roomc:
        print(r)
    sol1 = Solution().numberOfCleanRooms(room = room )    
    
    print('sol:', sol1, sol2)
    # if sol1 != sol2:
    #     for r in roomc:
    #         print(r)




