'''
-Hard-
*DP*
*Memoization* 
*Memoization with tuple*
*Memoization with bitmask*


You are given four integers, m, n, introvertsCount, and extrovertsCount. You have an m x n grid, and 
there are two types of people: introverts and extroverts. There are introvertsCount introverts and 
extrovertsCount extroverts.

You should decide how many people you want to live in the grid and assign each of them one grid cell. 
Note that you do not have to have all the people living in the grid.

The happiness of each person is calculated as follows:

Introverts start with 120 happiness and lose 30 happiness for each neighbor (introvert or extrovert).
Extroverts start with 40 happiness and gain 20 happiness for each neighbor (introvert or extrovert).
Neighbors live in the directly adjacent cells north, east, south, and west of a person's cell.

The grid happiness is the sum of each person's happiness. Return the maximum possible grid happiness.

 

Example 1:


Input: m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2
Output: 240
Explanation: Assume the grid is 1-indexed with coordinates (row, column).
We can put the introvert in cell (1,1) and put the extroverts in cells (1,3) and (2,3).
- Introvert at (1,1) happiness: 120 (starting happiness) - (0 * 30) (0 neighbors) = 120
- Extrovert at (1,3) happiness: 40 (starting happiness) + (1 * 20) (1 neighbor) = 60
- Extrovert at (2,3) happiness: 40 (starting happiness) + (1 * 20) (1 neighbor) = 60
The grid happiness is 120 + 60 + 60 = 240.
The above figure shows the grid in this example with each person's happiness. The introvert stays in the light green cell while the extroverts live on the light purple cells.
Example 2:

Input: m = 3, n = 1, introvertsCount = 2, extrovertsCount = 1
Output: 260
Explanation: Place the two introverts in (1,1) and (3,1) and the extrovert at (2,1).
- Introvert at (1,1) happiness: 120 (starting happiness) - (1 * 30) (1 neighbor) = 90
- Extrovert at (2,1) happiness: 40 (starting happiness) + (2 * 20) (2 neighbors) = 80
- Introvert at (3,1) happiness: 120 (starting happiness) - (1 * 30) (1 neighbor) = 90
The grid happiness is 90 + 80 + 90 = 260.
Example 3:

Input: m = 2, n = 2, introvertsCount = 4, extrovertsCount = 0
Output: 240
 

Constraints:

1 <= m, n <= 5
0 <= introvertsCount, extrovertsCount <= min(m * n, 6)

'''
from functools import lru_cache

class Solution(object):
    def getMaxGridHappiness(self, m, n, introvertsCount, extrovertsCount):
        """
        :type m: int
        :type n: int
        :type introvertsCount: int
        :type extrovertsCount: int
        :rtype: int
        """
        def calc_cost(r, c, in_mask, ex_mask, d):
            ans, up = 0, (1 << (n - 1))
            if c > 0 and (in_mask & 1):
                ans += d - 30;
            if r > 0 and (in_mask & up):
                ans += d - 30;
            if c > 0 and (ex_mask & 1):
                ans += d + 20;
            if r > 0 and (ex_mask & up):
                ans += d + 20;
            return ans;
        
        @lru_cache(None)
        def dp(idx, in_mask, ex_mask, in_cnt, ex_cnt):
            r, c = divmod(idx, n)
            if r >= m:
                return 0
            
            n_in_mask = (in_mask << 1) & ((1 << n) - 1)
            n_ex_mask = (ex_mask << 1) & ((1 << n) - 1)
            #if r == 0 and c == 1 and ex_cnt == 1 and in_cnt == 1:
            #    print('{:04b}'.format(ex_mask), 
            #          '{:04b}'.format(ex_mask<<1),
            #          '{:04b}'.format(n_ex_mask))
            ans = dp(idx + 1, n_in_mask, n_ex_mask, in_cnt, ex_cnt)
            if in_cnt > 0:
                cur = 120 + calc_cost(r, c, in_mask, ex_mask, -30)
                ans = max(ans, cur + dp(idx + 1, n_in_mask + 1, n_ex_mask, in_cnt - 1, ex_cnt))
            if ex_cnt > 0:
                cur = 40 + calc_cost(r, c, in_mask, ex_mask, 20)
                ans = max(ans, cur + dp(idx + 1, n_in_mask, n_ex_mask + 1, in_cnt, ex_cnt - 1))
            return ans
       
        return dp(0, 0, 0, introvertsCount, extrovertsCount)     

    def getMaxGridHappinessFast(self, m, n, introvertsCount, extrovertsCount):
        """
        :type m: int
        :type n: int
        :type introvertsCount: int
        :type extrovertsCount: int
        :rtype: int
        """
        @lru_cache(None)
        def helper(i, memory, intros, extros):

            if intros == extros == 0 or i == N:
                return 0

            #      1    up     n
            #      |     |     | 
            #      # # # * * * *     
            #      * * * X <--current pos
            #          ^ 
            #          |
            #         left 
            #  memory holds state information (0, 1, 2) for all '*' positions   
            #  its length is n (num of columns)
            up, left = memory[0], memory[-1]

            # leave room empty
            best = helper(i+1, memory[1:] + tuple([0]), intros, extros)

            # add an introvert
            j = i % C
            if intros:
                score = 120 + score_map[(up, 1)] + bool(j) * score_map[(left, 1)]
                best = max(best, score + helper(i+1, memory[1:] + tuple([1]), intros - 1, extros))

            # add an extrovert
            if extros:
                score = 40 + score_map[(up, 2)] + bool(j) * score_map[(left, 2)]
                best = max(best, score + helper(i+1, memory[1:] + tuple([2]), intros, extros - 1))

            return best

        score_map ={(0, 1): 0,         # empty neighbor (0) add introvert (1) to current cell
                    (0, 2): 0,         # empty neighbor (0) add extrovert (2) to current cell
                    (1, 1): -30 - 30,  # introvert neighbor (1) add introvert (1) to current cell
                    (2, 1): 20 - 30,   # extrovert neighbor (2) add introvert (1) to current cell
                    (1, 2): -30 + 20,  # introvert neighbor (1) add extrovert (2) to current cell
                    (2, 2): 20 + 20}   # extrovert neighbor (2) add extrovert (2) to current cell

        N = m * n
        C, R = sorted((m, n))
        memory = tuple([0 for _ in range(C)])
        return helper(0, memory, introvertsCount, extrovertsCount)


if __name__ == "__main__":
    print(Solution().getMaxGridHappiness(m = 2, n = 3, introvertsCount = 1, extrovertsCount = 2))