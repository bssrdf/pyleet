'''

-Medium-

There are n friends that are playing a game. The friends are sitting in a circle and are numbered 
from 1 to n in clockwise order. More formally, moving clockwise from the ith friend brings you to 
the (i+1)th friend for 1 <= i < n, and moving clockwise from the nth friend brings you to the 1st friend.

The rules of the game are as follows:

Start at the 1st friend.
Count the next k friends in the clockwise direction including the friend you started at. The counting 
wraps around the circle and may count some friends more than once.
The last friend you counted leaves the circle and loses the game.
If there is still more than one friend in the circle, go back to step 2 starting from the friend 
immediately clockwise of the friend who just lost and repeat.
Else, the last friend in the circle wins the game.
Given the number of friends, n, and an integer k, return the winner of the game.

 

Example 1:


Input: n = 5, k = 2
Output: 3
Explanation: Here are the steps of the game:
1) Start at friend 1.
2) Count 2 friends clockwise, which are friends 1 and 2.
3) Friend 2 leaves the circle. Next start is friend 3.
4) Count 2 friends clockwise, which are friends 3 and 4.
5) Friend 4 leaves the circle. Next start is friend 5.
6) Count 2 friends clockwise, which are friends 5 and 1.
7) Friend 1 leaves the circle. Next start is friend 3.
8) Count 2 friends clockwise, which are friends 3 and 5.
9) Friend 5 leaves the circle. Only friend 3 is left, so they are the winner.
Example 2:

Input: n = 6, k = 5
Output: 1
Explanation: The friends leave in this order: 5, 4, 6, 2, 3. The winner is friend 1.

'''
from collections import deque

class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        que = deque([i for i in range(1,n+1)])
        while len(que) != 1:
            x = k  % len(que)
            if x == 0: x = k
            while x > 1:
                r = que[0] 
                que.popleft()
                que.append(r)
                x -= 1
            que.popleft()
        return que[0]    
    
    def findTheWinnerMath(self, n: int, k: int) -> int:
       # bottom-up DP
       # For the same k, suppose you know the index of the winner is f(i-1) starting at index 0 where n=i-1.
       # Now imagine the scenario where n=i and we remove the first kth index person.
       # Then now we have an i-1 person game, starting at index k.
       # But we know that the winner of an i-1 person game is f(i-1) if starting at index 0.
       # So the index of the winner of this new game is f(i-1)+k and we add a %i to wrap around.
       # f(i) = (f(i-1)+k)%i
        res = 0
        for i in range(1, n + 1):
            res = (res + k) % i
        return res + 1
                
if __name__ == "__main__":
    print(Solution().findTheWinner(5,2))            
    print(Solution().findTheWinner(6,5))            