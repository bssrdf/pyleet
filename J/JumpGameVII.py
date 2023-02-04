'''
-Medium-
*BFS*
*DP*

You are given a 0-indexed binary string s and two integers minJump and maxJump. 
In the beginning, you are standing at index 0, which is equal to '0'. You can 
move from index i to index j if the following conditions are fulfilled:

i + minJump <= j <= min(i + maxJump, s.length - 1), and
s[j] == '0'.
Return true if you can reach index s.length - 1 in s, or false otherwise.

 

Example 1:

Input: s = "011010", minJump = 2, maxJump = 3
Output: true
Explanation:
In the first step, move from index 0 to index 3. 
In the second step, move from index 3 to index 5.
Example 2:

Input: s = "01101110", minJump = 2, maxJump = 3
Output: false
 

Constraints:

2 <= s.length <= 105
s[i] is either '0' or '1'.
s[0] == '0'
1 <= minJump <= maxJump < s.length


'''
from collections import deque
import heapq
class Solution(object):
    def canReachTLE(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        n = len(s)
        if s[-1] == '1': return False
        queue = deque([0])
        visited = {0}
        while queue:
            i = queue.popleft()
            if i == n-1: return True
            for j in range(i+minJump, min(i+maxJump+1,n)):
                if s[j] == '0' and j not in visited:
                    queue.append(j)
                    visited.add(j)
        return False

    def canReach(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """
        n = len(s)
        if s[-1] == '1': return False
        queue = deque([0])
        mx = 0
        while queue:
            i = queue.popleft()
            for j in range(max(i+minJump, mx+1), min(i+maxJump+1,n)):
                if s[j] == '0':
                    if j == n-1: return True
                    queue.append(j)
            mx = i + maxJump        
        return False

    def canReachDP(self, s, minJump, maxJump):
        """
        :type s: str
        :type minJump: int
        :type maxJump: int
        :rtype: bool
        """    
        """
        1. It's a bottom-up DP implementation. The boolean value represents 
        whether this position is reachable from start. So the first step is to 
        generate the table. Here the table was pre-labeled True or False, 
        thus '1's are already labeled False.

        2. To determine the state of dp[i], one need to check the states in 
        window dp[i-maxJ : i-minJ], because any one of them can reach i if 
        it's labeled True.

        3. Then you need to check if there is a True in this window. Notice 
        that this is a sliding window problem, so you don't need to calculate 
        it everytime. You only need to remove the effect from dp[i-maxJ-1] and 
        add the dp[i-minJ]. This is done by these two lines of code 
        pre += dp[i - minJ] and pre -= dp[i - maxJ - 1]
        
        4. The if statements if i >= minJ: and if i > maxJ: are dealing with 
        the initial boundary.

        The brilliance of this algorithm is combining the sliding window to DP, 
        hope you enjoy it.
        """
        dp = [c == '0' for c in s]
        pre = 0
        for i in range(1, len(s)):
            if i >= minJump: pre += dp[i - minJump]
            if i > maxJump: pre -= dp[i - maxJump - 1]
            dp[i] &= pre > 0 # if previously dp[i] = False (s[i]='1'), it stays False
                             # if previously dp[i] = True (s[i]='0'):
                             #   it stays True if pre > 0 (can reach from a '0' to the left) 
                             #   it changes to False if pre == 0 (can not reach from a '0' to the left)
        return dp[-1]
        

if __name__ == "__main__":    
    print(Solution().canReach(s = "011010", minJump = 2, maxJump = 3))
    print(Solution().canReach(s = "01101110", minJump = 2, maxJump = 3))
    s = "0"*100000
    print(Solution().canReach(s, minJump = 5, maxJump = 99998))
    s = "0"*50001+"1"*49999
    print(s.count('0'), s.count('1'), len(s))
    print(Solution().canReach(s, minJump = 1, maxJump = 49999))