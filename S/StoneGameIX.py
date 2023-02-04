'''
-Medium-

Alice and Bob continue their games with stones. There is a row of n stones, and each stone has an associated value. You are given an integer array stones, where stones[i] is the value of the ith stone.

Alice and Bob take turns, with Alice starting first. On each turn, the player may remove any stone from stones. The player who removes a stone loses if the sum of the values of all removed stones is divisible by 3. Bob will win automatically if there are no remaining stones (even if it is Alice's turn).

Assuming both players play optimally, return true if Alice wins and false if Bob wins.

 

Example 1:

Input: stones = [2,1]
Output: true
Explanation: The game will be played as follows:
- Turn 1: Alice can remove either stone.
- Turn 2: Bob removes the remaining stone. 
The sum of the removed stones is 1 + 2 = 3 and is divisible by 3. Therefore, Bob loses and Alice wins the game.
Example 2:

Input: stones = [2]
Output: false
Explanation: Alice will remove the only stone, and the sum of the values on the removed stones is 2. 
Since all the stones are removed and the sum of values is not divisible by 3, Bob wins the game.
Example 3:

Input: stones = [5,1,2,4,3]
Output: false
Explanation: Bob will always win. One possible way for Bob to win is shown below:
- Turn 1: Alice can remove the second stone with value 1. Sum of removed stones = 1.
- Turn 2: Bob removes the fifth stone with value 3. Sum of removed stones = 1 + 3 = 4.
- Turn 3: Alices removes the fourth stone with value 4. Sum of removed stones = 1 + 3 + 4 = 8.
- Turn 4: Bob removes the third stone with value 2. Sum of removed stones = 1 + 3 + 4 + 2 = 10.
- Turn 5: Alice removes the first stone with value 5. Sum of removed stones = 1 + 3 + 4 + 2 + 5 = 15.
Alice loses the game because the sum of the removed stones (15) is divisible by 3. Bob wins the game.
 

Constraints:

1 <= stones.length <= 105
1 <= stones[i] <= 104

'''
from typing import List
from collections import Counter

class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        # Important observation here is when turn came for alex or bob, 
        # she/he can either choose one out of {"1" or "2"} and "0". Now, 
        # at anyone turn, he/she have to take decision whether he/she will 
        # choose {"1" or "2"} or {"0"}, and both case will yield right result. 
        # Think about it, if alex is allowed to choose "1" (as sum formed after
        # choose 1 is not divisible by 3) but instead she choose "0" this will 
        # result in reverse answer(as alex sort of skipped her turn). which is 
        # in-fact same as alex would have choosen "1" and at then end when 
        # snothing left out and forced to choose "0".
        n = len(stones)
        def get(k):
            cnt = Counter(a % 3 for a in stones)            
            if cnt[k] < 1 : return False
            cnt[k] -= 1
            sums = k
            for i in range(1, n):
                if cnt[1] and (sums+1) % 3 != 0:
                    cnt[1] -= 1
                    sums += 1
                elif cnt[2] and (sums+2) % 3 != 0:
                    cnt[2] -= 1
                    sums += 2 
                elif cnt[0] and sums % 3 != 0:
                    cnt[0] -= 1
                else:
                    return True if i % 2 else False
            return False        
        return get(2) or get(1)


if __name__ == "__main__":
    print(Solution().stoneGameIX(stones = [5,1,2,4,3]))        
    print(Solution().stoneGameIX(stones = [2,1]))        

    