'''
-Medium-
*Hash Table*

You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

Return the minimum area of a rectangle formed from these points, with sides parallel to the X and Y axes. If there is not any such rectangle, return 0.

 

Example 1:


Input: points = [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4
Example 2:


Input: points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
 

Constraints:

1 <= points.length <= 500
points[i].length == 2
0 <= xi, yi <= 4 * 104
All the given points are unique.


'''


from typing import List
from collections import defaultdict
class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        linesMap = defaultdict(set)
        for (x,y) in points:
            linesMap[x].add(y)
        ans = float('inf')
        xPos = sorted(linesMap.keys())
        for i in range(len(xPos)-1):
            p1 = linesMap[xPos[i]]
            if len(p1) < 2: continue
            for j in range(i+1, len(xPos)):
                p2 = linesMap[xPos[j]]
                if len(p2) < 2: continue
                for y1 in p1:
                    for y2 in p1:
                        if y2 != y1 and y1 in p2 and y2 in p2:
                            ans = min(ans, abs(y1-y2)*(xPos[j]-xPos[i]))

        return 0 if ans == float('inf') else ans

            





if __name__ == "__main__":
    print(Solution().minAreaRect(points = [[1,1],[1,3],[3,1],[3,3],[2,2]]))
    print(Solution().minAreaRect(points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]))
        