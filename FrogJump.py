'''
-Hard-
*DP*
*DFS*
*Memoization*

A frog is crossing a river. The river is divided into some number of units, and at 
each unit, there may or may not exist a stone. The frog can jump on a stone, but it 
must not jump into the water.

Given a list of stones' positions (in units) in sorted ascending order, determine 
if the frog can cross the river by landing on the last stone. Initially, the frog 
is on the first stone and assumes the first jump must be 1 unit.

If the frog's last jump was k units, its next jump must be either k - 1, k, or k + 1 
units. The frog can only jump in the forward direction.

 

Example 1:

Input: stones = [0,1,3,5,6,8,12,17]
Output: true
Explanation: The frog can jump to the last stone by jumping 1 unit to the 2nd stone, 
then 2 units to the 3rd stone, then 2 units to the 4th stone, then 3 units to the 
6th stone, 4 units to the 7th stone, and 5 units to the 8th stone.
Example 2:

Input: stones = [0,1,2,3,4,8,9,11]
Output: false
Explanation: There is no way to jump to the last stone as the gap between the 5th 
and 6th stone is too large.
 

Constraints:

2 <= stones.length <= 2000
0 <= stones[i] <= 2^31 - 1
stones[0] == 0


'''

class Solution(object):
    def canCross(self, stones):
        """
        :type stones: List[int]
        :rtype: bool
        """
        self.positionAndCanJump = {}
        stonePositions = set(stones)
        # curStep initized to 0 so the first stone can be handled in a general way
        return self.DFS(stonePositions, stones[-1], stones[0], 0)
    
    def DFS(self, stonePositions, lastPosition, curPosition, curStep):
    
        if (curPosition == lastPosition):
            return True

        key = (curPosition, curStep)
        if key in self.positionAndCanJump:
            return self.positionAndCanJump[key]
 
        for count in [1,0,-1]:
            nextStep = curStep + count
            if nextStep <= 0: continue
            nextPosition = curPosition + nextStep
            if nextPosition in stonePositions:
                if self.DFS(stonePositions, lastPosition, nextPosition, nextStep):
                    return True
        self.positionAndCanJump[key] = False
 
        return self.positionAndCanJump[key]


if __name__ == "__main__":
    print(Solution().canCross([0,1,3,5,6,8,12,17]))
    print(Solution().canCross([0,1,2,3,4,8,9,11]))