'''
-Medium-


You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching if the cards have the same value.

Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked cards. If it is impossible to have matching cards, return -1.

 

Example 1:

Input: cards = [3,4,2,3,4,7]
Output: 4
Explanation: We can pick up the cards [3,4,2,3] which contain a matching pair of cards with value 3. Note that picking up the cards [4,2,3,4] is also optimal.
Example 2:

Input: cards = [1,0,5,3]
Output: -1
Explanation: There is no way to pick up a set of consecutive cards that contain a pair of matching cards.
 

Constraints:

1 <= cards.length <= 105
0 <= cards[i] <= 106



'''
from typing import List

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        n = len(cards)        
        ans = n+1
        st = {}
        for r in range(n):
            if cards[r] in st:                
                ans = min(ans, r - st[cards[r]]+1)
            st[cards[r]] = r 
        return -1 if ans == n+1 else ans 



if __name__ == "__main__":
    print(Solution().minimumCardPickup(cards = [3,4,2,3,4,7]))
    print(Solution().minimumCardPickup(cards = [1,0,5,3]))
    print(Solution().minimumCardPickup(cards = [3,1,0,5,3]))
    cards = [95,11,8,65,5,86,30,27,30,73,15,91,30,7,37,26,55,76,60,43,36,85,47,96,6]
    print(Solution().minimumCardPickup(cards))
    cards = [746,464,175,787,105,164,370,110,642,413,353,410,200,141,915,170,928,326,123,528,8,11,474,168,992,43,901,133,579,152,135,893,950,102,863,119,835,795,783,728,35,916,770,698,832,324,391,338,102,770,183,739,804,468,591,174,929,992,406,349,472,260,586,938,677,331,629,769,148,566,501,628,845,197,48,369,754,542,608,632,639,815,758,206,400,105,298,993,187,133,950,430,92,225,609,507,753,873,732,353,894,63,867,814,736,109,440,288,846,152,164,42,96,134,170,649,832,385,265,178,447,678,415,32,428,524,118,775,593,221,247,887,119,159,391,661,220,175,693,184,534,281,569,306,383,330,355,408,30,200,391,136,721,925]
    print(Solution().minimumCardPickup(cards))
