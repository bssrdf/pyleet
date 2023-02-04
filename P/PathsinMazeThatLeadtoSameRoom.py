'''

-Medium-

$$$


A maze consists of n rooms numbered from 1 to n, and some rooms are connected by corridors. You are given a 2D integer array corridors where corridors[i] = [room1i, room2i] indicates that there is a corridor connecting room1i and room2i, allowing a person in the maze to go from room1i to room2i and vice versa.

The designer of the maze wants to know how confusing the maze is. The confusion score of the maze is the number of different cycles of length 3.

For example, 1 → 2 → 3 → 1 is a cycle of length 3, but 1 → 2 → 3 → 4 and 1 → 2 → 3 → 2 → 1 are not.
Two cycles are considered to be different if one or more of the rooms visited in the first cycle is not in the second cycle.

Return the confusion score of the maze.

 

Example 1:



Input: n = 5, corridors = [[1,2],[5,2],[4,1],[2,4],[3,1],[3,4]]
Output: 2
Explanation:
One cycle of length 3 is 4 → 1 → 3 → 4, denoted in red.
Note that this is the same cycle as 3 → 4 → 1 → 3 or 1 → 3 → 4 → 1 because the rooms are the same.
Another cycle of length 3 is 1 → 2 → 4 → 1, denoted in blue.
Thus, there are two different cycles of length 3.
Example 2:



Input: n = 4, corridors = [[1,2],[3,4]]
Output: 0
Explanation:
There are no cycles of length 3.
 

Constraints:

2 <= n <= 1000
1 <= corridors.length <= 5 * 104
corridors[i].length == 2
1 <= room1i, room2i <= n
room1i != room2i
There are no duplicate corridors.




'''

from typing import List
from collections import defaultdict
from itertools import combinations

class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        #方法一：哈希表

        # 长度为 3 的环，由三个顶点、三条边组成。我们假设三个顶点分别为 a, b, c。

        # 那么一定存在 c <=> a，c <=> b 以及 a <=> b，即环中的每个点都与其他两点直接相连。
        # 我们可以用哈希表来存放每个点的相邻点。

        # 由于环的长度为 3，每个相同的环会被重复统计 3 次，因此答案需除以 3。

        # 时间复杂度 O(N^2)，空间复杂度 O(N)。
        g = defaultdict(set)
        for a, b in corridors:
            g[a].add(b)
            g[b].add(a)
        ans = 0
        for i in range(1, n + 1):
            for j, k in combinations(g[i], 2): # j, k both connected to i
                if j in g[k]: # if j also connected to k
                    ans += 1
        return ans // 3


if __name__ == "__main__":
    print(Solution().numberOfPaths(n = 5, corridors = [[1,2],[5,2],[4,1],[2,4],[3,1],[3,4]]))