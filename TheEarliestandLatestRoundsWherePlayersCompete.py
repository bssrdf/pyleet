'''
-Hard-
*DP*
*Memoization*
*Bitmask*

There is a tournament where n players are participating. The players are standing in a single row and are numbered from 1 to n based on their initial standing position (player 1 is the first player in the row, player 2 is the second player in the row, etc.).

The tournament consists of multiple rounds (starting from round number 1). In each round, the ith player from the front of the row competes against the ith player from the end of the row, and the winner advances to the next round. When the number of players is odd for the current round, the player in the middle automatically advances to the next round.

For example, if the row consists of players 1, 2, 4, 6, 7
Player 1 competes against player 7.
Player 2 competes against player 6.
Player 4 automatically advances to the next round.
After each round is over, the winners are lined back up in the row based on the original ordering assigned to them initially (ascending order).

The players numbered firstPlayer and secondPlayer are the best in the tournament. They can win against any other player before they compete against each other. If any two other players compete against each other, either of them might win, and thus you may choose the outcome of this round.

Given the integers n, firstPlayer, and secondPlayer, return an integer array containing two values, the earliest possible round number and the latest possible round number in which these two players will compete against each other, respectively.

 

Example 1:

Input: n = 11, firstPlayer = 2, secondPlayer = 4
Output: [3,4]
Explanation:
One possible scenario which leads to the earliest round number:
First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
Second round: 2, 3, 4, 5, 6, 11
Third round: 2, 3, 4
One possible scenario which leads to the latest round number:
First round: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
Second round: 1, 2, 3, 4, 5, 6
Third round: 1, 2, 4
Fourth round: 2, 4
Example 2:

Input: n = 5, firstPlayer = 1, secondPlayer = 5
Output: [1,1]
Explanation: The players numbered 1 and 5 compete in the first round.
There is no way to make them compete in any other round.
 

Constraints:

2 <= n <= 28
1 <= firstPlayer < secondPlayer <= n

'''

from collections import deque
from typing import List
from functools import lru_cache
from itertools import product
class Solution:
    def earliestAndLatest(self, n: int, firstPlayer: int, secondPlayer: int) -> List[int]:
        F, S = firstPlayer-1, secondPlayer-1 # 0-indexed
        
        @lru_cache(None)
        def fn(k, mask): 
            # print('{:011b}'.format(mask))
            """Return earliest and latest rounds."""
            can = deque()
            for i in range(n): 
                if mask & (1 << i): can.append(i)
                    
            cand = [] # eliminated player
            while len(can) > 1: 
                p1, p2 = can.popleft(), can.pop()
                if p1 == F and p2 == S or p1 == S and p2 == F: 
                    return [k, k] # game of interest 
                if p1 in (F, S): cand.append([p2]) # p2 eliminated 
                elif p2 in (F, S): cand.append([p1]) # p1 eliminated 
                else: cand.append([p1, p2]) # both could be elimited 
            
            minn, maxx = float('inf'), -float('inf')
            for x in product(*cand): 
                mask0 = mask
                for i in x: mask0 ^= 1 << i
                mn, mx = fn(k+1, mask0)
                minn = min(minn, mn)
                maxx = max(maxx, mx)
            return minn, maxx
        
        return fn(1, (1<<n)-1)
    

if __name__ == "__main__":
    print(Solution().earliestAndLatest(n = 11, firstPlayer = 2, secondPlayer = 4))