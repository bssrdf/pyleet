'''

-Medium-
*DP*
*Bitmask*

Alice and Bob are opponents in an archery competition. The competition has set the 
following rules:

Alice first shoots numArrows arrows and then Bob shoots numArrows arrows.
The points are then calculated as follows:
The target has integer scoring sections ranging from 0 to 11 inclusive.
For each section of the target with score k (in between 0 to 11), say Alice and Bob 
have shot ak and bk arrows on that section respectively. If ak >= bk, then Alice 
takes k points. If ak < bk, then Bob takes k points.

However, if ak == bk == 0, then nobody takes k points.
For example, if Alice and Bob both shot 2 arrows on the section with score 11, then Alice takes 11 points. On the other hand, if Alice shot 0 arrows on the section with score 11 and Bob shot 2 arrows on that same section, then Bob takes 11 points.

You are given the integer numArrows and an integer array aliceArrows of size 12, which represents the number of arrows Alice shot on each scoring section from 0 to 11. Now, Bob wants to maximize the total number of points he can obtain.

Return the array bobArrows which represents the number of arrows Bob shot on each scoring section from 0 to 11. The sum of the values in bobArrows should equal numArrows.

If there are multiple ways for Bob to earn the maximum total points, return any one of them.

 

Example 1:


Input: numArrows = 9, aliceArrows = [1,1,0,1,0,0,2,1,0,1,2,0]
Output: [0,0,0,0,1,1,0,0,1,2,3,1]
Explanation: The table above shows how the competition is scored. 
Bob earns a total point of 4 + 5 + 8 + 9 + 10 + 11 = 47.
It can be shown that Bob cannot obtain a score higher than 47 points.
Example 2:


Input: numArrows = 3, aliceArrows = [0,0,1,0,0,0,0,0,0,0,0,2]
Output: [0,0,0,0,0,0,0,0,1,1,1,0]
Explanation: The table above shows how the competition is scored.
Bob earns a total point of 8 + 9 + 10 = 27.
It can be shown that Bob cannot obtain a score higher than 27 points.
 

Constraints:

1 <= numArrows <= 105
aliceArrows.length == bobArrows.length == 12
0 <= aliceArrows[i], bobArrows[i] <= numArrows
sum(aliceArrows[i]) == numArrows




'''

from typing import List
from functools import lru_cache

class Solution:
    def maximumBobPoints(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        def test(mask, remainArrows):
            score = 0
            bobArrows = [0] * 12
            for k in range(12):
                if (mask >> k) & 1:
                    arrowsNeeded = aliceArrows[k] + 1
                    if remainArrows < arrowsNeeded: return 0, []
                    score += k
                    bobArrows[k] = arrowsNeeded
                    remainArrows -= arrowsNeeded
                    
			# In case of having remain arrows then it means in all sections Bob always win 
			# then we can distribute the remain to any section, here we simple choose first section.
            bobArrows[0] += remainArrows
            return score, bobArrows
        
        bestScore = 0
        bestBobArrows = None
        for mask in range(1 << 12):
            score, bobArrows = test(mask, numArrows)
            if score > bestScore:
                bestScore = score
                bestBobArrows = bobArrows
        return bestBobArrows
    
    def maximumBobPoints2(self, numArrows: int, aliceArrows: List[int]) -> List[int]:
        @lru_cache(None)
        def dp(k, numArrows):
            if k == 12 or numArrows <= 0:
                return 0
            
            maxScore = dp(k+1, numArrows)  # Bob Lose
            if numArrows > aliceArrows[k]:
                maxScore = max(maxScore, dp(k+1, numArrows-aliceArrows[k]-1) + k)  # Bob Win
            return maxScore
        
        # backtracking
        ans = [0] * 12
        remainBobArrows = numArrows
        for k in range(12):
            if dp(k, numArrows) != dp(k+1, numArrows): # If Bob win
                ans[k] = aliceArrows[k] + 1
                numArrows -= ans[k]
                remainBobArrows -= ans[k]
                
        ans[0] += remainBobArrows  # In case of having remain arrows then it means in all sections Bob always win 
        # then we can distribute the remain to any section, here we simple choose first section.
        return ans
        

if __name__ == "__main__":
    print(Solution().maximumBobPoints(numArrows = 9, aliceArrows = [1,1,0,1,0,0,2,1,0,1,2,0]))


