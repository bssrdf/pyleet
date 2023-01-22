'''

-Hard-
*Greedy*
*GCD*

There exists an infinitely large grid. You are currently at point (1, 1), and you need to reach the point (targetX, targetY) using a finite number of steps.

In one step, you can move from point (x, y) to any one of the following points:

(x, y - x)
(x - y, y)
(2 * x, y)
(x, 2 * y)
Given two integers targetX and targetY representing the X-coordinate and Y-coordinate of your final position, return true if you can reach the point from (1, 1) using some number of steps, and false otherwise.

 

Example 1:

Input: targetX = 6, targetY = 9
Output: false
Explanation: It is impossible to reach (6,9) from (1,1) using any sequence of moves, so false is returned.
Example 2:

Input: targetX = 4, targetY = 7
Output: true
Explanation: You can follow the path (1,1) -> (1,2) -> (1,4) -> (1,8) -> (1,7) -> (2,7) -> (4,7).
 

Constraints:

1 <= targetX, targetY <= 109



'''

from math import gcd
from collections import Counter

class Solution:
    def isReachable(self, targetX: int, targetY: int) -> bool:
        g = gcd(targetX, targetY)
        return Counter(bin(g))['1'] == 1

    def isReachable2(self, targetX: int, targetY: int) -> bool:
        return (True if targetX == 1 and targetY == 1 else 
                self.isReachable2(targetX//2, targetY) if targetX % 2 == 0 else 
                self.isReachable2(targetX, targetY//2) if targetY % 2 == 0 else 
                self.isReachable2(targetX-targetY, targetY) if targetX > targetY  else 
                self.isReachable2(targetX, targetY-targetX) if targetY > targetX  else False
                ) 
    
    def isReachable3(self, targetX: int, targetY: int) -> bool:
        if targetX == 1 and targetY == 1:
            return True   
        elif targetX % 2 == 0:
            return self.isReachable3(targetX//2, targetY)
        elif targetY % 2 == 0:
            return self.isReachable3(targetX, targetY//2)
        elif targetX > targetY:
            return self.isReachable3(targetX-targetY, targetY)
        elif targetY > targetX:
            return self.isReachable3(targetX, targetY-targetX) 
        else:
            return False


if __name__ == '__main__':
    print(Solution().isReachable(targetX = 4, targetY = 7))
    print(Solution().isReachable2(targetX = 4, targetY = 7))
    print(Solution().isReachable3(targetX = 4, targetY = 7))