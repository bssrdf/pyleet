'''
-Hard-

*DP*

You are given an n x n grid representing a field of cherries, each cell is 
one of three possible integers.

0 means the cell is empty, so you can pass through,
1 means the cell contains a cherry that you can pick up and pass through, 
or
-1 means the cell contains a thorn that blocks your way.
Return the maximum number of cherries you can collect by following the 
rules below:

Starting at the position (0, 0) and reaching (n - 1, n - 1) by moving right 
or down through valid path cells (cells with value 0 or 1).
After reaching (n - 1, n - 1), returning to (0, 0) by moving left or up through 
valid path cells.
When passing through a path cell containing a cherry, you pick it up, and the 
cell becomes an empty cell 0.
If there is no valid path between (0, 0) and (n - 1, n - 1), then no cherries 
can be collected.

Input: grid = [[0,1,-1],[1,0,-1],[1,1,1]]
Output: 5
Explanation: The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.
Example 2:

Input: grid = [[1,1,-1],[1,-1,1],[-1,1,1]]
Output: 0
 

Constraints:

n == grid.length
n == grid[i].length
1 <= n <= 50
grid[i][j] is -1, 0, or 1.
grid[0][0] != -1
grid[n - 1][n - 1] != -1

'''

import sys

class Solution(object):

    def cherryPickupMemo(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        """
        top-down dp (memoization)
        detailed explanation see
        https://leetcode.com/problems/cherry-pickup/discuss/329945/Very-easy-to-follow-%3A-step-by-step-recursive-backtracking-with-memoization-N4.

        Runtime: 776 ms, faster than 60.68% of Python online submissions for Cherry Pickup.
        Memory Usage: 22.2 MB, less than 29.06% of Python online submissions for Cherry Pickup.
        """
        n = len(grid)
        dp = [[[0 for _ in range(n)] for _ in range(n)] for _ in range(n)]
        '''
        Instead of going once from 0,0 to n-1,n-1 and then back, we simply go twice 
        from 0,0 to n-1,n-1 because every path from n-1,n-1 to 0,0 can be interpreted 
        as a path from 0,0 to n-1,n-1
        Note that the one person can never cross the past path of the other person 
        (they can only meet at the same position) so we don't need to worry about 
        one person picking up an already picked up cherry from the past
        What does a state represent? dp[r1][c1][c2] represents the max number of 
        cherries that can be collected by 2 people going from r1,c1 and r2,c2 to 
        n-1,n-1
        Transitions between states? we collect cherries on current positions of the 
        two people (r1,c1 and r2,c2), then we go through all possible next states 
        and choose the best one (max number of cherries) as the next state (we do 
        this by adding the number of cherries of the best next state to the number 
        of cherries we picked up on the current two positions of the people). 
        In the end, the state dp[0][0][0] will contain the max number of cherries 
        that can be picked up by going from 0,0 to n-1,n-1 and back.
        '''
        def helper(r1, c1, c2):

         # we can deduce r2 because r1 + c1 == r2 + c2, since with each move 
         # either r or c of a person gets incremented by exactly one (Manhattan 
         # distance to origin stays equal)
         # this way we reduce the 4D dp problem to a 3D one (we save space by 
         # reducing the number of things we store in a state)
            r2 = r1 + c1 - c2

           # check if current state is out of bounds or on thorns
            if (r1 >= n or c1 >= n or r2 >= n or c2 >= n or 
               grid[r1][c1] == -1 or grid[r2][c2] == -1):
               return -sys.maxsize  # current state should not be included 
                                    # in the solution

            # check if we have already computed a solution for this state
            if dp[r1][c1][c2] != 0: return dp[r1][c1][c2]

            # check if we reached the end state (note that if r1,c1 reached the end, 
            # this implies that r2,c2 also reached the end)
            if r1 == n - 1 and c1 == n - 1:
                return grid[r1][c1]

            # compute and return answer for current state
            result = grid[r1][c1]

            # in case the second person is on the same position, don't pick up the 
            # same cherry twice. Note that r1 == r2 <--> c1 == c2 (eg. they can't 
            # be on the same row without also being on the same column) 
            if r1 != r2:
                result += grid[r2][c2]

            # pick best possible next state
            bestNextState = max(helper(r1 + 1, c1, c2),   # down, down 
                                helper(r1, c1 + 1, c2 + 1))  # right, right    
            bestNextState = max(bestNextState, helper(r1 + 1, c1, c2 + 1))  # down, right
            bestNextState = max(bestNextState, helper(r1, c1 + 1, c2))   # right, down

            result += bestNextState
            dp[r1][c1][c2] = result   # store current state such that it can be 
                                      # re-used

            return result

        return max(0, helper(0, 0, 0)) # return 0 if there is no path from 0,0 
                                       # to n-1,n-1
       

    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        """
        bottom-up dp
        detailed explanation see
        https://www.cnblogs.com/grandyang/p/8215787.html
        """
        n = len(grid)
        m = 2*n-1
        dp = [[-1 for _ in range(n)] for _ in range(n)]
        dp[0][0] = grid[0][0]
        for k in range(1, m):
            for i in range(n-1, -1, -1):
                for p in range(n-1, -1, -1):
                    j, q = k - i, k - p
                    if (j < 0 or j >= n or q < 0 or q >= n or 
                        grid[i][j] < 0 or grid[p][q] < 0):
                        dp[i][p] = -1
                        continue                    
                    if i > 0: dp[i][p] = max(dp[i][p], dp[i - 1][p])
                    if p > 0: dp[i][p] = max(dp[i][p], dp[i][p - 1])
                    if i > 0 and p > 0: dp[i][p] = max(dp[i][p], dp[i - 1][p - 1])
                    if dp[i][p] >= 0: dp[i][p] += grid[i][j] + (grid[p][q] if i != p else 0)
        return max(dp[n - 1][n - 1], 0)

if __name__ == "__main__":
    print(Solution().cherryPickup([[0,1,-1],[1,0,-1],[1,1,1]]))
    print(Solution().cherryPickupMemo([[0,1,-1],[1,0,-1],[1,1,1]]))