'''
-Medium-
*BFS*

*DP*

A certain bug's home is on the x-axis at position x. Help them get there 
from position 0.

The bug jumps according to the following rules:

It can jump exactly a positions forward (to the right).
It can jump exactly b positions backward (to the left).
It cannot jump backward twice in a row.
It cannot jump to any forbidden positions.

The bug may jump forward beyond its home, but it cannot jump to positions 
numbered with negative integers.

Given an array of integers forbidden, where forbidden[i] means that the 
bug cannot jump to the position forbidden[i], and integers a, b, and x, 
return the minimum number of jumps needed for the bug to reach its home. 
If there is no possible sequence of jumps that lands the bug on position x, 
return -1.

 

Example 1:

Input: forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9
Output: 3
Explanation: 3 jumps forward (0 -> 3 -> 6 -> 9) will get the bug home.
Example 2:

Input: forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11
Output: -1
Example 3:

Input: forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7
Output: 2
Explanation: One jump forward (0 -> 16) then one jump backward (16 -> 7) will get the bug home.
 

Constraints:

1 <= forbidden.length <= 1000
1 <= a, b, forbidden[i] <= 2000
0 <= x <= 2000
All the elements in forbidden are distinct.
Position x is not forbidden.

'''
from typing import List
from collections import deque
import math
class Solution:
    def minimumJumps2(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        que = deque([(0, False, 0)])
        max_val = max([x]+forbidden) + a + b
        # why do we need a 2D visited array, instead of the usual 1D?

        # 1) for index i, if it first gets visited by a backward jump, 
        # then we can't visit i - b for next jump. Assume then a forward 
        # jump comes to i, it should be able to visit i - b, but if we simply 
        # use 1D visited array, i has already been marked as visited by previous 
        # backward jump, so i - b can never get visited, thus the wrong answer.

        # 2) the problem says that you cannot jump backward twice , but there 
        # can be a valid case where we can reach a particular point from both 
        # forward and backward jump(only once), but by keeping a visited array 
        # we will be reject one of them , so that leads to wrong answer , 
        # therefore we need to maintain direction as well .
        visited = [[0]*(max_val+1) for _ in range(2)]
        visited[0][0] = 1
        visited[1][0] = 1
        forb = set(forbidden)
        while que:
            pos, dir, steps = que.popleft()
            #print(pos, dir, steps)
            if pos == x: return steps
            y = pos + a
            if y <= max_val and visited[0][y] == 0 and y not in forb:
                visited[0][y] = 1
                que.append((y, False, steps+1))
            y = pos - b
            if y > 0 and visited[1][y] == 0 and y not in forb and not dir:
                visited[1][y] = 1
                que.append((y, True, steps+1))
        return -1

    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        
        max_val=max([x]+forbidden) + a + b
        
        jumps = [0]+[math.inf] * max_val
        for pos in forbidden: jumps[pos]=-1
        queue = deque([0])
        
        while queue:
            pos = queue.popleft()
            if pos+a <= max_val and jumps[pos+a] > jumps[pos]+1:
                queue.append(pos+a)
                jumps[pos+a] = jumps[pos]+1
            if pos-b > 0 and jumps[pos-b] > jumps[pos]+1:
                jumps[pos-b] = jumps[pos]+1
                if pos-b+a <= max_val and jumps[pos-b+a] > jumps[pos]+2:
                    queue.append(pos-b+a)
                    jumps[pos-b+a] = jumps[pos]+2
      
        return jumps[x] if jumps[x] < math.inf else -1



if __name__ == "__main__":
    print(Solution().minimumJumps(forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9))
    print(Solution().minimumJumps(forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11))
    print(Solution().minimumJumps(forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7))
    forbidden = [162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98]
    print(Solution().minimumJumps(forbidden, 29, 98, 80))
    print(Solution().minimumJumps2(forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9))
    print(Solution().minimumJumps2(forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11))
    print(Solution().minimumJumps2(forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7))
    forbidden = [162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98]
    print(Solution().minimumJumps2(forbidden, 29, 98, 80))