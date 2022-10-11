'''

-Medium-

*Hash Table*

You are given n points in the plane that are all distinct, where points[i] = [xi, yi]. A boomerang is a tuple of points (i, j, k) such that the distance between i and j equals the distance between i and k (the order of the tuple matters).

Return the number of boomerangs.

 

Example 1:

Input: points = [[0,0],[1,0],[2,0]]
Output: 2
Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].
Example 2:

Input: points = [[1,1],[2,2],[3,3]]
Output: 2
Example 3:

Input: points = [[1,1]]
Output: 0
 

Constraints:

n == points.length
1 <= n <= 500
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.



'''

from typing import List
from collections import Counter
from math import factorial, comb
class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        n = len(points)
        P = points
        ans = 0
        for i in range(n):
            dist = Counter()
            for j in range(n):
                if i != j:
                    dist[(P[i][0]-P[j][0])**2 + (P[i][1]-P[j][1])**2] += 1
            for c in dist.values():
            #    if c > 1:
            #        ans += comb(c,2) * 2
                ans += c*(c-1) 
        return ans
            



if __name__ == "__main__":
    # print(Solution().numberOfBoomerangs(points = [[0,0],[1,0],[2,0]]))
    # print(Solution().numberOfBoomerangs(points = [[1,1],[2,2],[3,3]]))
    # print(Solution().numberOfBoomerangs(points = [[1,1]]))
    print(Solution().numberOfBoomerangs(points = [[0,0],[1,0],[-1,0],[0,1],[0,-1]]))
        


