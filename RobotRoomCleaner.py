'''
-Hard-
*DFS*

You are controlling a robot that is located somewhere in a room. The room is modeled as an m x n binary grid where 0 represents a wall and 1 represents an empty slot.

The robot starts at an unknown location in the room that is guaranteed to be empty, and you do not have access to the grid, but you can move the robot using the given API Robot.

You are tasked to use the robot to clean the entire room (i.e., clean every empty cell in the room). The robot with the four given APIs can move forward, turn left, or turn right. Each turn is 90 degrees.

When the robot tries to move into a wall cell, its bumper sensor detects the obstacle, and it stays on the current cell.

Design an algorithm to clean the entire room using the following APIs:

interface Robot {
  // returns true if next cell is open and robot moves into the cell.
  // returns false if next cell is obstacle and robot stays on the current cell.
  boolean move();

  // Robot will stay on the same cell after calling turnLeft/turnRight.
  // Each turn will be 90 degrees.
  void turnLeft();
  void turnRight();

  // Clean the current cell.
  void clean();
}
Note that the initial direction of the robot will be facing up. You can 
assume all four edges of the grid are all surrounded by a wall.

 

Custom testing:

The input is only given to initialize the room and the robot's position internally. 
You must solve this problem "blindfolded". In other words, you must control the robot using only the four mentioned APIs without knowing the room layout and the initial robot's position.



'''

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """

class Solution:
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """

        # 我们设定机器人起始位置 (0, 0)，朝向 d = 0。

        # 将起始位置进行清扫，并进行标记（即清扫过的格子也算作障碍）；然后依次选择四个朝向 up，right，down 和 left 进行深度优先搜索，相邻的两个朝向仅差一次向右旋转的操作；

        # 对于选择的朝向，检查下一个格子是否有障碍，如果没有，则向对应朝向移动一格，并开始新的搜索；
        # 如果有，则向右旋转。
        # 如果四个朝向都搜索完毕，则回溯到上一次搜索。
        def back():
            # go back to the previous cell
            robot.turnRight()
            robot.turnRight()
            robot.move()
            robot.turnRight()
            robot.turnRight()

        def dfs(i, j, d):
            # here (i,j) is not the absolute position robot currently is on
            # because its start pos is not known. we simply use (i,j) in a 
            # relative sense
            vis.add((i, j))
            robot.clean()
            # explore clockwise: 0: ^, 1: >, 2: v, 3: <
            # the order is important since the idea is always turn right
            for k in range(4):
                nd = (d + k) % 4
                x, y = i + dirs[nd][0], j + dirs[nd][1]
                if (x, y) not in vis and robot.move():
                    dfs(x, y, nd)
                    back()
                robot.turnRight() # always turn the robot clockwise

        vis = set()
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        dfs(0, 0, 0)

    


if __name__ == "__main__":
    room = [[1,1,1,1,1,0,1,1],
            [1,1,1,1,1,0,1,1],
            [1,0,1,1,1,1,1,1],
            [0,0,0,1,0,0,0,0],
            [1,1,1,1,1,1,1,1]]
    
