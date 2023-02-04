'''
-Hard-

Given a rectangle of size n x m, find the minimum number of integer-sided squares that 
tile the rectangle.

 

Example 1:



Input: n = 2, m = 3
Output: 3
Explanation: 3 squares are necessary to cover the rectangle.
2 (squares of 1x1)
1 (square of 2x2)
Example 2:



Input: n = 5, m = 8
Output: 5
Example 3:



Input: n = 11, m = 13
Output: 6
 

Constraints:

1 <= n <= 13
1 <= m <= 13

'''

class Solution(object):
    def tilingRectangle(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        # use area_left as a heuristic function to eliminate unworthy search branches
        # remove the memo used to cache best usedCount obtained for each skyline state,
        # it seems that the collision is quite scarse compared to all the states we had to store.

        # The main idea is that, if there exists a solution,
        # we can always fill in the squares from bottom up.
        # That means any state during this "filling" process can
        # be encoded as a skyline (array of heights at each position)
        # NOTE
        # y = skyline[x] contributes a line at y, from x to x + 1. This eliminates
        # ambiguity at the edge, where there may be edges of 2 square at 1 x position.
        # e.g.
        # placing a 1x1 square at bottom left of 2x1 rectangle, 
        # the skyline is [1, 0]

        # heuristic: given area left to be filled,
        # calculate the least number of squares that can sum up to it.
        # this will be the absolute lower bound for that area.
        # store the result for faster access
        width, height = n, m
        total_area = width * height
        dp = [-1 for i in range(total_area +1)]
        dp[0] = 0
        for i in range(1, total_area + 1):
            # try each possible k
            dp[i] = 1 + min(dp[i - k**2] for k in range(1, int(i ** 0.5) + 1))
        self.res = total_area


        def dfs(skyline, usedCount, area_left):
            # [List Int], Int, Int -> Void
            # - given state as skyline, 
            # - the number of squares already used, 
            # - area left to be filled
            # try to find the min square tiling
            # continuing from this point.

            # no need to search further if the best we can do with this path
            # is no better than the best result so far
            if usedCount + dp[area_left] >= self.res:
                return

            # solution found iff skyline overlaps with the ceiling
            filled = True
            # the algorithm places squares at left first, so we consider heights only on right edge
            # minimum height and the position.
            min_pos = 0
            min_height = skyline[0]
            for pos in range(width):
                # not filled if any skyline doesn't touch the ceiling
                if (skyline[pos] < height):
                    filled = False
                # update lowest spot
                if (skyline[pos] < min_height):
                    min_pos = pos
                    min_height = skyline[pos]

            # already filled, another solution found.
            if filled:
                self.res = min(usedCount, self.res)
                return
            
            # try to fill the leftmost lowest void, find the maximum size of square
            # we can put there. end represents the x-coordinate of right edge
            # NOTE x = end is where the right edge of this newly placed square will be
            end = min_pos + 1
            # in order to increment end:
            # - right edge stays in the rectangle 
            # - bottom edge must have same height
            # - top edge stays in the rectangle
            while (end < width and \
                   skyline[end] == min_height and \
                   (end - min_pos + 1 + min_height) <= height):  
                end += 1

            # try fill with larger square first, to exhaust more void
            # and potentially yield better search.
            for right_pos in range(end, min_pos, -1):
                # calcualte size of the square to be used
                sqr_height = right_pos - min_pos 

                new_skyline = list(skyline)
                # increase the skyline at relavent positions
                for i in range(min_pos, right_pos):
                    new_skyline[i] += sqr_height
                # continue dfs from here.
                dfs(new_skyline, usedCount + 1, area_left - sqr_height * sqr_height)
        
        skyline = [0 for i in range(width)]
        dfs(skyline, 0, total_area)

        return self.res

    def tilingRectangleBackTracking(self, n: int, m: int) -> int:
        self.best = m * n
        total_area = self.best

        # heuristic: given area left to be filled,
        # calculate the least number of squares that can sum up to it.
        # this will be the absolute lower bound for that area.
        # store the result for faster access
        # this compuations itself is a medium problem: perfect squares
        dp = [-1 for i in range(total_area +1)]
        dp[0] = 0
        for i in range(1, total_area + 1):
            # try each possible k
            dp[i] = 1 + min(dp[i - k**2] for k in range(1, int(i ** 0.5) + 1))        

        def dfs(height, moves, area_left):

            if all(h == n for h in height): # skyline gets to the ceiling
                self.best = min(self.best, moves) # filling done, update counts
                return
            
            # no need to search further if the best we can do with this path
            # is no better than the best result so far
            if moves+dp[area_left] >= self.best:
                return

            min_height = min(height) # lowest height
            idx = height.index(min_height) # its position
            ridx = idx + 1
            # find the rightmost edge where this lowest height extends to
            while ridx < m and height[ridx] == min_height:
                ridx += 1
            # try each possible square of size 'i' from biggest to smallest(1)
            # i is bounded by the distance to the ceiling and the horizontal extent      
            for i in range(min(ridx - idx, n - min_height), 0, -1):
                new_height = height[:] # save the current skyline
                for j in range(i):
                    new_height[idx + j] += i # update teh skyline by filling the square i
                dfs(new_height, moves + 1, area_left - i*i) # dfs to next skyline
        # initially, heights at all positions are 0 
        dfs([0] * m, 0, total_area)
        return self.best

if __name__ == '__main__':
    print(Solution().tilingRectangle(5, 8))
    print(Solution().tilingRectangleBackTracking(5, 8))