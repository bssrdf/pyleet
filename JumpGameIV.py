'''
-Hard-

Given an array of integers arr, you are initially positioned at the first index 
of the array.

In one step you can jump from index i to index:

i + 1 where: i + 1 < arr.length.
i - 1 where: i - 1 >= 0.
j where: arr[i] == arr[j] and i != j.
Return the minimum number of steps to reach the last index of the array.

Notice that you can not jump outside of the array at any time.

 

Example 1:

Input: arr = [100,-23,-23,404,100,23,23,23,3,404]
Output: 3
Explanation: You need three jumps from index 0 --> 4 --> 3 --> 9. Note that 
index 9 is the last index of the array.

Example 2:

Input: arr = [7]
Output: 0
Explanation: Start index is the last index. You don't need to jump.
Example 3:

Input: arr = [7,6,9,6,9,6,9,7]
Output: 1
Explanation: You can jump directly from index 0 to index 7 which is last index 
of the array.
Example 4:

Input: arr = [6,1,9]
Output: 2
Example 5:

Input: arr = [11,22,7,7,7,7,7,7,7,22,13]
Output: 3
 

Constraints:

1 <= arr.length <= 5 * 10^4
-10^8 <= arr[i] <= 10^8


'''

from collections import defaultdict
from collections import deque
class Solution(object):
    def minJumps(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        n = len(arr)
        pos = defaultdict(list)
        for i,v in enumerate(arr):
            pos[v].append(i)
        visited = [False]*n        
        q = deque([(0, 0)])
        visited[0] = True
        while q:
            cur, steps = q.popleft()
            if cur == n-1: return steps 
            for nxt in (cur+1, cur-1):
                if 0 <= nxt < n and not visited[nxt]:
                    visited[nxt] = True
                    q.append((nxt, steps+1))              
            if pos[arr[cur]]:
                for nxt in pos[arr[cur]]:
                    if 0 <= nxt < n and not visited[nxt]:
                        visited[nxt] = True
                        q.append((nxt,steps+1)) 
                # for cases like [7,7,7,..........7,11] where the same
                # number occurs many times, once their positions are put
                # into the queue, all occurrings can be eliminated; this 
                # prevents the algorithm from going to O(n^2)  
                pos[arr[cur]] = []
        return -1
                
if __name__ == "__main__":
    print(Solution().minJumps([100,-23,-23,404,100,23,23,23,3,404]))
    print(Solution().minJumps([7]))
    print(Solution().minJumps([7,6,9,6,9,6,9,7]))
    print(Solution().minJumps([6,1,9]))
    print(Solution().minJumps([11,22,7,7,7,7,7,7,7,22,13]))
    arr = [7]*4999+[11]
    print(Solution().minJumps(arr))