'''

-Hard-
*BFS*
*DFS*

There is a 1 million by 1 million grid on an XY-plane, and the coordinates of each grid square are (x, y).

We start at the source = [sx, sy] square and want to reach the target = [tx, ty] square. There is also an array of blocked squares, where each blocked[i] = [xi, yi] represents a blocked square with coordinates (xi, yi).

Each move, we can walk one square north, east, south, or west if the square is not in the array of blocked squares. We are also not allowed to walk outside of the grid.

Return true if and only if it is possible to reach the target square from the source square through a sequence of valid moves.

 

Example 1:

Input: blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]
Output: false
Explanation: The target square is inaccessible starting from the source square because we cannot move.
We cannot move north or east because those squares are blocked.
We cannot move south or west because we cannot go outside of the grid.
Example 2:

Input: blocked = [], source = [0,0], target = [999999,999999]
Output: true
Explanation: Because there are no blocked cells, it is possible to reach the target square.
 

Constraints:

0 <= blocked.length <= 200
blocked[i].length == 2
0 <= xi, yi < 106
source.length == target.length == 2
0 <= sx, sy, tx, ty < 106
source != target
It is guaranteed that source and target are not blocked.



'''

from typing import List
from collections import deque

class Solution:
    def isEscapePossible(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked = set(map(tuple, blocked))

        def dfs(x, y, target, seen):
            if not (0 <= x < 10**6 and 0 <= y < 10**6) or (x, y) in blocked or (x, y) in seen: return False
            seen.add((x, y))
            if len(seen) > 20000 or [x, y] == target: return True
            return dfs(x + 1, y, target, seen) or \
                dfs(x - 1, y, target, seen) or \
                dfs(x, y + 1, target, seen) or \
                dfs(x, y - 1, target, seen)
        return dfs(source[0], source[1], target, set()) and dfs(target[0], target[1], source, set())

    def isEscapePossible3(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked = {tuple(p) for p in blocked}

        def bfs(source, target):
            bfs, seen = [source], {tuple(source)}
            for x0, y0 in bfs:
                for i, j in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    x, y = x0 + i, y0 + j
                    if 0 <= x < 10**6 and 0 <= y < 10**6 and (x, y) not in seen and (x, y) not in blocked:
                        if [x, y] == target: return True
                        bfs.append([x, y])
                        seen.add((x, y))
                if len(bfs) == 20000: return True
            return False
        return bfs(source, target) and bfs(target, source)

    def isEscapePossible2(self, blocked: List[List[int]], source: List[int], target: List[int]) -> bool:
        blocked = {tuple(p) for p in blocked}
        def bfs(source, target):
            que, seen = deque([source]), {tuple(source)}
            while que:
                x0, y0 = que.popleft()
                for i, j in [[0, 1], [1, 0], [-1, 0], [0, -1]]:
                    x, y = x0 + i, y0 + j
                    if 0 <= x < 10**6 and 0 <= y < 10**6 and (x, y) not in seen and (x, y) not in blocked:
                        if [x, y] == target: 
                            return True
                        que.append([x, y])
                        seen.add((x, y))
                if len(seen) == 20000: 
                    return True            
            return False

        return bfs(source, target) and bfs(target, source)




if __name__ == "__main__":
    print(Solution().isEscapePossible(blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]))
    print(Solution().isEscapePossible2(blocked = [[0,1],[1,0]], source = [0,0], target = [0,2]))