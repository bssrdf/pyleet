'''

-Medium-
*Math*
*Hash Table*

You are given an array of points in the X-Y plane points where points[i] = [xi, yi].

Return the minimum area of any rectangle formed from these points, with sides not necessarily parallel to the X and Y axes. If there is not any such rectangle, return 0.

Answers within 10-5 of the actual answer will be accepted.

 

Example 1:


Input: points = [[1,2],[2,1],[1,0],[0,1]]
Output: 2.00000
Explanation: The minimum area rectangle occurs at [1,2],[2,1],[1,0],[0,1], with an area of 2.
Example 2:


Input: points = [[0,1],[2,1],[1,1],[1,0],[2,0]]
Output: 1.00000
Explanation: The minimum area rectangle occurs at [1,0],[1,1],[2,1],[2,0], with an area of 1.
Example 3:


Input: points = [[0,3],[1,2],[3,1],[1,3],[2,1]]
Output: 0
Explanation: There is no possible rectangle to form from these points.
 

Constraints:

1 <= points.length <= 50
points[i].length == 2
0 <= xi, yi <= 4 * 104
All the given points are unique.


'''

from typing import List
from math import sqrt
from collections import defaultdict

class Solution:
    def minAreaFreeRect(self, points: List[List[int]]) -> float:
        """
        to form up a rectangle, 
        1) two diagonal bisect eachother
        2) two diagonal has same length

        => find two line 
        1) has same length, 
        2) middle position are same,

        lines = {(len,(x,y)) => [((x1,y1), (x2,y2))]}

        p2 x1'y1'    x2y2

        p1 x1y1      p3 x2'y2'

        e1 = sqrt((x1-x1')^2 + (y1-y1')^2)
        e2 = sqrt((x1-x2')^2 + (y1-y2')^2)

        """
        def distSquare(x1,y1,x2,y2):
            return (x1-x2)**2 + (y1-y2)**2
        def dist(x1,y1,x2,y2):
            return sqrt((x1-x2)**2 + (y1-y2)**2)
        def midPos(x1,y1,x2,y2):
            return ((x1+x2)/2,(y1+y2)/2)
        
        linesMap = defaultdict(list) # (len, mid of p1 and p2) => [(p1,p2)]
        N = len(points)
        for i in range(N):
            for j in range(i + 1, N):
                l = distSquare(*points[i], *points[j])
                m = midPos(*points[i], *points[j])
                linesMap[(l, m)].append((i,j))
        
        minArea = float("inf")
        for lines in linesMap.values():
            if len(lines) < 2: continue
            # try all pairs of lines
            M = len(lines)
            for i in range(M):
                for j in range(i + 1, M):
                    p1, p2, p3 = points[lines[i][0]], points[lines[j][0]], points[lines[j][1]] 
                    d1, d2 = dist(*p1, *p2), dist(*p1, *p3)
                    minArea = min(minArea, d1 * d2)
                    print(p1, points[lines[i][1]],  p2, p3, minArea)
        return minArea if minArea != float("inf") else 0

    

if __name__ == "__main__":
    print(Solution().minAreaFreeRect(points = [[1,2],[2,1],[1,0],[0,1]]))