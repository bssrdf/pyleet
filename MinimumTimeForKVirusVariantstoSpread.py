'''
-Hard-
$$$
*Sweep Line*
*Scan Line*
*Segment Tree*




There are n unique virus variants in an infinite 2D grid. You are given a 2D array points, 
where points[i] = [xi, yi] represents a virus originating at (xi, yi) on day 0. Note 
that it is possible for multiple virus variants to originate at the same point.

Every day, each cell infected with a virus variant will spread the virus to all 
neighboring points in the four cardinal directions (i.e. up, down, left, and right). 
If a cell has multiple variants, all the variants will spread without interfering 
with each other.

Given an integer k, return the minimum integer number of days for any point to 
contain at least k of the unique virus variants.

 

Example 1:



Input: points = [[1,1],[6,1]], k = 2
Output: 3
Explanation: On day 3, points (3,1) and (4,1) will contain both virus variants. Note that these are not the only points that will contain both virus variants.
Example 2:



Input: points = [[3,3],[1,2],[9,2]], k = 2
Output: 2
Explanation: On day 2, points (1,3), (2,3), (2,2), and (3,2) will contain the first two viruses. Note that these are not the only points that will contain both virus variants.
Example 3:



Input: points = [[3,3],[1,2],[9,2]], k = 3
Output: 4
Explanation: On day 4, the point (5,2) will contain all 3 viruses. Note that this is not the only point that will contain all 3 virus variants.
 

Constraints:

n == points.length
2 <= n <= 50
points[i].length == 2
1 <= xi, yi <= 100
2 <= k <= n
Solutions


'''

from collections import defaultdict


class Solution(object):
    def minDayskVariants(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: int
        """
        n = len(points)
        xmin, xmax = min(x[0] for x in points), max(x[0] for x in points) 
        ymin, ymax = min(x[1] for x in points), max(x[1] for x in points) 
        l, r = 0, 101 
        def reachable(d):
            xevents, yevents = [], []
            for i,(x,y) in enumerate(points):
                xevents.append((x-d, -1, i )) 
                xevents.append((x+d, 1, i)) 
                yevents.append((y-d, -1, i)) 
                yevents.append((y+d, 1, i)) 
            xevents.sort()
            yevents.sort()
            xr, yr = [], []
            r = set()
            for x, t, i in xevents:
                if t == -1: r.add(i)
                else: r.remove(i) 
                if len(r) >= k:
                    xr.append(set(r))
            r = set()
            for y, t, i in yevents:
                if t == -1: r.add(i)
                else: r.remove(i) 
                if len(r) >= k:
                    yr.append(set(r))
            if d == 1:
                print(xr, yr)
            for i in range(len(xr)):
                for j in range(len(yr)):
                    if len(xr[i] & yr[j]) >= k:
                        return True
            return False
        while l < r:
            mid = l + (r-l)//2
            if reachable(mid):
                r = mid
            else:
                l = mid + 1
            print(l, r, mid)
        return l-1
    
    def minDayskVariants2(self, points, k):
        # The points (region) infected by a virus after some days form
        # a square rotated counterclockwise by 45 degrees on the x-y plane.          
        # so the first step is to do a transform of co-ordinates of all points,
        # all computations later are based on these transformed(rotated) co-ordinates
        points = [[v[0]+v[1], v[0]-v[1]] for v in points] # rotate counterclockwise by 45 degrees
        min_x = min(points, key=lambda x:x[0])[0]
        max_x = max(points, key=lambda x:x[0])[0]
        min_y = min(points, key=lambda x:x[1])[1]
        max_y = max(points, key=lambda x:x[1])[1]
        # print(min_x, min_y, max_x, max_y)
        def check(l): # Time O(n^2), Space: O(n)
            mint = lambda : defaultdict(int)
            intervals = defaultdict(mint)
            y_set = set()
            for p in points:
                x0, y0, x1, y1 = p[0]-l, p[1]-l, p[0]+l, p[1]+l
                # print(x0, y0, x1, y1)
                # 2D Sweep Line Algorithm; aka, difference array 
                # all points in range (x0, y0) - (x1, y1) inclusive are 
                # infected by virus at p after l days 
                intervals[x0][y0] += 1
                intervals[x0][y1+1] -= 1
                intervals[x1+1][y0] -= 1
                intervals[x1+1][y1+1] += 1
                y_set.add(y0)
                y_set.add(y1+1)
            sorted_x = []
            for x in intervals:
                sorted_x.append(x)
            sorted_x.sort()
            sorted_y = list(y_set)
            sorted_y.sort()
            count = defaultdict(int)
            for x in sorted_x: # for each sweep line (at a particular x)
                for y,c in intervals[x].items():
                    # print(y,c)
                    count[y] += c # add or substract contribution from all viruses that cover this x,y  
                cnt = 0
                for y in sorted_y: # check each x,y 
                    cnt += count[y] # sum up the total contribution
                    if cnt >= k: 
                        return True
            return False  

        left, right = 0, (max_x-min_x+max_y-min_y+1)//2
        while left <= right:
            mid = left + (right-left)//2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left        





if __name__ == "__main__":   
    points = [[1,1],[6,1]]; k = 2
    print(Solution().minDayskVariants2(points, k))
    points = [[3,3],[1,2],[9,2]]; k = 2
    # print(Solution().minDayskVariants(points, k))
    print(Solution().minDayskVariants2(points, k))
    points = [[3,3],[1,2],[9,2]]; k = 3
    print(Solution().minDayskVariants2(points, k))