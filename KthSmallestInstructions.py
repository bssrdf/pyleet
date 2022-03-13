'''
-Hard-

Bob is standing at cell (0, 0), and he wants to reach destination: (row, column). He can 
only travel right and down. You are going to help Bob by providing instructions for him 
to reach destination.

The instructions are represented as a string, where each character is either:

'H', meaning move horizontally (go right), or
'V', meaning move vertically (go down).
Multiple instructions will lead Bob to destination. For example, if destination is (2, 3), 
both "HHHVV" and "HVHVH" are valid instructions.

However, Bob is very picky. Bob has a lucky number k, and he wants the kth lexicographically 
smallest instructions that will lead him to destination. k is 1-indexed.

Given an integer array destination and an integer k, return the kth lexicographically smallest 
instructions that will take Bob to destination.

 

Example 1:



Input: destination = [2,3], k = 1
Output: "HHHVV"
Explanation: All the instructions that reach (2, 3) in lexicographic order are as follows:
["HHHVV", "HHVHV", "HHVVH", "HVHHV", "HVHVH", "HVVHH", "VHHHV", "VHHVH", "VHVHH", "VVHHH"].
Example 2:



Input: destination = [2,3], k = 2
Output: "HHVHV"
Example 3:



Input: destination = [2,3], k = 3
Output: "HHVVH"
 

Constraints:

destination.length == 2
1 <= row, column <= 15
1 <= k <= nCr(row + column, row), where nCr(a, b) denotes a choose b​​​​​.


'''

from typing import List
from collections import deque
import heapq 
class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        # BFS + min heap solution, TLE for large test case (15,15, 155117520)
        m, n = destination[0]+1, destination[1]+1
        que = deque([(0,0,'')])
        pq = []
        while que:
            x,y,ins = que.popleft()
            if x == destination[0] and y == destination[1]:
                heapq.heappush(pq, ins)
            for dx, dy, c in [(1,0,'V'),(0,1,'H')]:
                i, j = x + dx, y + dy
                if i < m and j < n:
                    que.append((i,j,ins+c)) 
            #if len(pq) == k:
            #    break
        ans = ''
        for _ in range(k):
            ans = heapq.heappop(pq)
        return ans   

    def kthSmallestPath2(self, destination: List[int], k: int) -> str:
        # DP
        ti, tj = destination[0], destination[1]
        m, n = ti + 1, tj + 1
        dp = [[0]*n for _ in range(m)] 
        for i in range (ti, -1, -1):
            for j in range (tj, -1, -1):            
                if i == ti and j == tj: dp[i][j] = 1
                elif i == ti: dp[i][j] = dp[i][j+1]
                elif j == tj: dp[i][j] = dp[i+1][j]
                else:  dp[i][j] = dp[i+1][j] + dp[i][j+1]
         
        # in each (i, j), we have dp[i][j] kind of instructions, which equal to dp[i][j+1] + dp[i+1][j]
        # all dp[i][j+1] kinds of instructions are lexicographically smaller than the left dp[i+1][j] kinds of instructions.
        # we can just compare k with dp[i][j+1] to determin how to choose next step.
        
        ans = []        
        def helper(i, j, k, sb):        
            if i == len(dp) - 1:
                # if we came to most down position then we can only go right
                j += 1
                while j < len(dp[0]): 
                    sb.append("H")
                    j += 1
                return
            if j == len(dp[0]) - 1:
                #if we came to most right position then we can only go down
                i += 1
                while i < len(dp):
                    sb.append("V")
                    i += 1
                return
            if dp[i][j+1] >= k:
                # if k is smaller than the first dp[i][j+1] solutions, then we should go right
                sb.append("H")
                helper(i, j+1, k, sb)
            else:
                # else we go donw, and we should also minus the first dp[i][j+1] solutions from k
                sb.append("V")
                helper(i+1, j, k-dp[i][j+1], sb)
        helper(0, 0, k, ans)
        return ''.join(ans)

        

if __name__ == "__main__":
    print(Solution().kthSmallestPath(destination = [2,3], k = 3))
    print(Solution().kthSmallestPath2(destination = [2,3], k = 3))
    print(Solution().kthSmallestPath2(destination = [15,15], k = 155117520))