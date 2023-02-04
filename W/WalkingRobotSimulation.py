'''
-Easy-

*Greedy*

A robot on an infinite grid starts at point (0, 0) and faces north. The 
robot can receive one of three possible types of commands:

-2: turn left 90 degrees,
-1: turn right 90 degrees, or
1 <= x <= 9: move forward x units
Some of the grid squares are obstacles. The ith obstacle is at grid 
point obstacles[i] = (xi, yi).

If the robot would try to move onto them, the robot stays on the previous 
grid square instead (but still continues following the rest of the route.)

Return the square of the maximum Euclidean distance that the robot will 
be from the origin.

 

Example 1:

Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: robot will go to (3, 4)
Example 2:

Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: robot will be stuck at (1, 4) before turning left and 
going to (1, 8)
 

Constraints:

1 <= commands.length <= 10^4
commands[i] is in the list [-2,-1,1,2,3,4,5,6,7,8,9].
0 <= obstacles.length <= 10^4
-3 * 10^4 <= xi, yi <= 3 * 10^4
The answer is guaranteed to be less than 2^31.

'''

class Solution(object):
    def robotSim(self, commands, obstacles):
        """
        :type commands: List[int]
        :type obstacles: List[List[int]]
        :rtype: int
        """        
        dx = [0, 1, 0, -1]
        dy = [1, 0, -1, 0]
        x = y = di = 0
        obstacleSet = set(map(tuple, obstacles))
        ans = 0
        for c in commands:
            if c == -2:
                di = (di-1)%4
            elif c == -1:
                di = (di+1)%4
            else:
                for _ in range(c):
                    xi = x + dx[di]
                    yi = y + dy[di]
                    if (xi,yi) not in obstacleSet:
                        x, y = xi, yi
                        ans = max(ans, x*x+y*y)
                    else:
                        break
        return ans


if __name__ == "__main__":
    print(Solution().robotSim([4,-1,4,-2,4], [[2,4]]))