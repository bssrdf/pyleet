'''
$$$
-Medium-

*BFS*
*DFS*

In an infinite chess board with coordinates from -infinity to +infinity, 
you have a knight at square [0, 0].

A knight has 8 possible moves it can make, as illustrated below. 

Each move is two squares in a cardinal direction, then one square in an 
orthogonal direction.



Return the minimum number of steps needed to move the knight to the square 
[x, y].  It is guaranteed the answer exists.

 

Example 1:

Input: x = 2, y = 1
Output: 1
Explanation: [0, 0] → [2, 1]
Example 2:

Input: x = 5, y = 5
Output: 4
Explanation: [0, 0] → [2, 1] → [4, 2] → [3, 4] → [5, 5]
 

Constraints:

|x| + |y| <= 300

'''

from collections import deque

class Solution(object):

    def minKnightMoves(self, x: int, y: int) -> int:
        x, y = sorted(map(abs, (x, y)))
        memo_s = {(0,0):0}
        memo_t = {(x,y):0}
        queue_s = deque([(0,0)])
        queue_t = deque([(x,y)])
        
        def get_next(loc, memo):
            xx, yy = loc
            for dx, dy in [(-1,-2),(-1,2),(1,-2),(1,2),
                           (-2,-1),(-2,1),(2,-1),(2,1)]:
                nx, ny = xx + dx, yy + dy
                if (nx, ny) in memo: continue
                if nx < -2 or ny < -2 or nx > x + 2 or ny > y + 2: continue
                if nx - ny > 2: continue
                yield (nx, ny)
        
        step = 0
        while True:
            step += 1
            # bfs from source
            for _ in range(len(queue_s)):
                loc = queue_s.popleft()
                if loc in memo_t: return memo_s[loc] + memo_t[loc]
                for next_loc in get_next(loc, memo_s):
                    memo_s[next_loc] = step
                    queue_s.append(next_loc)
            # bfs from target
            for _ in range(len(queue_t)):
                loc = queue_t.popleft()
                if loc in memo_s: return memo_s[loc] + memo_t[loc]
                for next_loc in get_next(loc, memo_t):
                    memo_t[next_loc] = step
                    queue_t.append(next_loc)



    def minimumMoves(self, x, y):
        '''
        :type x: int
        :type y: int
        :rtype: int

        '''
        q = deque([((0,0),0)])
        visited = set([(0,0)])
        dirs = [(-2, 1), (-1, 2), (1, 2), (2, 1),
                (-2, -1), (-1, -2), (1, -2), (2, -1)]
        while q:
            (i, j), steps = q.popleft()
            if i == x and j == y: return steps
            for di, dj in dirs:
                ni, nj = i+di, j+dj
                if 0 <= ni <= 300 and 0 <= nj <= 300 and (ni, nj) not in visited:
                    visited.add((di, dj))
                    q.append(((ni,nj), steps+1))
        return -1


if __name__ == "__main__":
    print(Solution().minimumMoves(5,5))
    print(Solution().minimumMoves(2,1))
    #print(Solution().minimumMoves(145, 70))