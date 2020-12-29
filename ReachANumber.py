'''
-Medium-
*Math*

You are standing at position 0 on an infinite number line. There is a 
goal at position target.

On each move, you can either go left or right. During the n-th move 
(starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:
Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.
Example 2:
Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.
Note:
target will be a non-zero integer in the range [-10^9, 10^9].


'''

from collections import deque

class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        
        """
        target = abs(target) # due to symmetry, just consider target > 0
        step, sums = 0, 0
        # greedily move 'step' towards target until sum(1...step) >= target
        # the goal is to get rid of the difference sum-target to reach target. 
        # For ith move, if we switch the right move to the left, the change in 
        # summation will be 2*i less. Now the difference between sum and target 
        # has to be an even number in order for the math to check out.
        # if sum-target is odd, continue moving until sum-target is even
        # return step
        while sums < target or (sums-target) % 2 != 0:
            step += 1
            sums += step
        return step        

if __name__ == "__main__":
    print(Solution().reachNumber(2))