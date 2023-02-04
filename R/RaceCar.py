'''

-Hard-

*DP*

*BFS*


Your car starts at position 0 and speed +1 on an infinite number line. Your car can go into negative positions. Your car drives automatically according to a sequence of instructions 'A' (accelerate) and 'R' (reverse):

When you get an instruction 'A', your car does the following:
position += speed
speed *= 2
When you get an instruction 'R', your car does the following:
If your speed is positive then speed = -1
otherwise speed = 1
Your position stays the same.
For example, after commands "AAR", your car goes to positions 0 --> 1 --> 3 --> 3, and your speed goes to 1 --> 2 --> 4 --> -1.

Given a target position target, return the length of the shortest sequence of instructions to get there.

 

Example 1:

Input: target = 3
Output: 2
Explanation: 
The shortest instruction sequence is "AA".
Your position goes from 0 --> 1 --> 3.
Example 2:

Input: target = 6
Output: 5
Explanation: 
The shortest instruction sequence is "AAARA".
Your position goes from 0 --> 1 --> 3 --> 7 --> 7 --> 6.
 

Constraints:

1 <= target <= 104


'''
import math
import collections

class Solution:
    dp = [0]*10001
    def racecar(self, target: int) -> int:
        # let T(i) be the length of the shortest instructions to move the car from 
        # position 0 to position i, with initail speed of 1 and its direction pointing 
        # towards position i. Then our original problem will be T(target), and the 
        # base case is T(0) = 0. Next we need to figure out the recurrence relations for T(i).

        # Note that to apply the definition of T(i) to subproblems, the car has to start 
        # with speed of 1, which implies we can only apply T(i) right after the reverse 
        # instruction. Also we need to make sure the direction of the initial speed when 
        # applying T(i) is pointing towards the final target position.

        # 试想一下，到达target的路径可能会有哪几种模式。需要特别注意的是，最后达到终点的时候可能
        # 是正向的，也可能是反向的。所以需要分成这么两大类：

        # 到达target时是正向的。这包括： 
        # a. 最幸运的是，直接加速一路恰好到达。（ # 这种情况可以提前处理） 
        # 
        # b. 先正向加速一段，然后停止（为了减速到零），然后继续到达终点。 
        # 
        # c. 先正向加速一段，然后反向走一段，然后再正向，最后继续到达终点。 
        # 其中b和c两种情况其实可以归并为一类，只是反向走的路程的长短不一样而已。

        # 到达target时是反向的。于是这需要先正向加速一段冲过target，然后反向，继续到达终点。

        # 在第一大类和第二大类的情况中，正向加速分别到什么时候为止呢？直觉告诉我们：
        # 加速到恰好不超过target的时候，即为分界线。也就是当n=log2(target+1)时，
        # 2^(n)-1表示正向加速不超过target的最远距离；相应的2^(n+1)-1就是恰好超过target的最近距离。

        # 第一大类中，确定了n，那么可以遍历反向的步数k，再用递归求解总的步数。
        # 也就是说：前向走n步，反向，反向走ｋ步，再反向，剩下的递归．

        # for k = 0,1,2,...,n-1
        # dp[target] = min(n+1+k+1+racecar(target-(2^n-1) + (2^k-1)))
        # 第二大类中，确定了n，可以直接用递归求解剩余的步数

        # dp[target] = n+1+1+(2^(n+1)-1-target)
        # 最后dp[target]取上述几种讨论的最小值．

        if Solution.dp[target] != 0: return Solution.dp[target]
        n = int(math.log2(target+1))
        if pow(2,n)-1 == target:
            Solution.dp[target] = n
            return n
        Solution.dp[target] = (n+1)+1+self.racecar(pow(2,n+1)-1-target)
        for k in range(n):
            temp = (n+1)+(k+1)+self.racecar(target-(pow(2,n)-1)+(pow(2,k)-1))
            Solution.dp[target] = min(Solution.dp[target], temp)
        return Solution.dp[target]
    

    def racecar2(self, target: int) -> int:
        #1. Initialize double ended queue as 0 moves, 0 position, +1 velocity
        queue = collections.deque([(0, 0, 1)])
        while queue:
            
            # (moves) moves, (pos) position, (vel) velocity)
            moves, pos, vel = queue.popleft()

            if pos == target:
                return moves
            
            #2. Always consider moving the car in the direction it is already going
            queue.append((moves + 1, pos + vel, 2 * vel))
            
            #3. Only consider changing the direction of the car if one of the following conditions is true
            #   i.  The car is driving away from the target.
            #   ii. The car will pass the target in the next move.  
            if (pos + vel > target and vel > 0) or (pos + vel < target and vel < 0):
                queue.append((moves + 1, pos, -vel / abs(vel)))



        

if __name__ == "__main__":
    print(Solution().racecar(6))