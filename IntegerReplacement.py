'''
-Medium-

*BFS*

Given a positive integer n, you can apply one of the following operations:

If n is even, replace n with n / 2.
If n is odd, replace n with either n + 1 or n - 1.
Return the minimum number of operations needed for n to become 1.

 

Example 1:

Input: n = 8
Output: 3
Explanation: 8 -> 4 -> 2 -> 1
Example 2:

Input: n = 7
Output: 4
Explanation: 7 -> 8 -> 4 -> 2 -> 1
or 7 -> 6 -> 3 -> 2 -> 1
Example 3:

Input: n = 4
Output: 2
 

Constraints:

1 <= n <= 2^31 - 1



'''
from collections import deque

class Solution:
    def integerReplacement(self, n: int) -> int:
        que = deque([(0, n)])
        while que:
            t, x = que.popleft() 
            if x == 1: return t
            if x % 2 == 0:
                que.append((t+1, x//2))                
            else:
                que.append((t+1, x+1))
                que.append((t+1, x-1))
        return -1