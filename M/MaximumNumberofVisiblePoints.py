'''
-Hard-

*Sliding Window*

You are given an array points, an integer angle, and your location, where 
location = [posx, posy] and points[i] = [xi, yi] both denote integral coordinates 
on the X-Y plane.

Initially, you are facing directly east from your position. You cannot move from your 
position, but you can rotate. In other words, posx and posy cannot be changed. Your 
field of view in degrees is represented by angle, determining how wide you can see 
from any given view direction. Let d be the amount in degrees that you rotate counterclockwise. 
Then, your field of view is the inclusive range of angles [d - angle/2, d + angle/2].


You can see some set of points if, for each point, the angle formed by the point, 
your position, and the immediate east direction from your position is in your field of view.

There can be multiple points at one coordinate. There may be points at your location, 
and you can always see these points regardless of your rotation. Points do not obstruct 
your vision to other points.

Return the maximum number of points you can see.

 

Example 1:


Input: points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]
Output: 3
Explanation: The shaded region represents your field of view. All points can be made visible in your field of view, including [3,3] even though [2,2] is in front and in the same line of sight.
Example 2:

Input: points = [[2,1],[2,2],[3,4],[1,1]], angle = 90, location = [1,1]
Output: 4
Explanation: All points can be made visible in your field of view, including the one at your location.
Example 3:


Input: points = [[1,0],[2,1]], angle = 13, location = [1,1]
Output: 1
Explanation: You can only see one of the two points, as shown above.
 

Constraints:

1 <= points.length <= 10^5
points[i].length == 2
location.length == 2
0 <= angle < 360
0 <= posx, posy, xi, yi <= 100


'''

import math
import bisect
class Solution(object):
    def visiblePoints(self, points, angle, location):
        """
        :type points: List[List[int]]
        :type angle: int
        :type location: List[int]
        :rtype: int
        """
        # 68.18% 
        res = 0
        angles = []
        for p in points: 
            dx, dy = p[0] - location[0], p[1] - location[1] 
            if dx == 0 and dy == 0: 
                res += 1
                continue
            angles.append(math.atan2(dy,dx))
        angles = [a*180.0/math.pi for a in angles]
        angles.sort()
        angles2 = [a+360.0 for a in angles]
        angles = angles + angles2          
        ans =   0
        #print(angles)
        #lmin, rmax = 0, len(angles)
        lmin, rmax = bisect.bisect_left(angles, -angle/2.0), bisect.bisect_right(angles, 360.0+angle/2.0), 
        l = lmin
        for r in range(lmin, rmax):
            while angles[r] - angles[l] > angle:
                l += 1
            ans = max(ans, r - l + 1)
        return ans + res

    def visiblePointsAC(self, points, angle, location):
        
        arr, extra = [], 0
        xx, yy = location
        
        for x, y in points:
            if x == xx and y == yy:
                extra += 1
                continue
            arr.append(math.atan2(y - yy, x - xx))
        
        arr.sort()
        arr = arr + [x + 2.0 * math.pi for x in arr]
        angle = math.pi * angle / 180
        a = [x*180.0/math.pi for x in arr]
        #print(a)
        l = ans = 0
        for r in range(len(arr)):
            while arr[r] - arr[l] > angle:
                l += 1
            ans = max(ans, r - l + 1)
            
        return ans + extra
        

if __name__ == "__main__":
    print(Solution().visiblePoints(points = [[2,1],[2,2],[3,3]], angle = 90, location = [1,1]))
    points = [[41,7],[22,94],[90,53],[94,54],[58,50],[51,96],[87,88],[55,98],[65,62],[36,47],[91,61],[15,41],[31,94],[82,80],[42,73],[79,6],[45,4]]
    print(Solution().visiblePoints(points, 17, [6,84]))
    print(Solution().visiblePointsAC(points, 17, [6,84]))
    points = [[79,44],[85,96],[53,20],[63,50],[54,10],[21,78],[65,32],[30,42],[18,9],[98,20],[17,68],[37,9],[60,19],[93,13],[27,93],[80,99],[73,20],[49,61],[66,74],[58,97],[13,20],[27,53],[99,91],[5,24],[62,66],[77,40],[77,63],[80,77],[51,92],[49,33],[66,96],[77,42],[18,25],[35,8],[49,14],[20,96],[81,93],[3,32],[39,74],[42,39],[11,85],[8,95],[96,50],[49,32],[92,78],[68,23],[34,2],[69,55],[13,11],[24,89],[45,67],[92,9],[23,63],[8,55],[9,53],[16,34],[88,0],[11,45],[80,28],[96,55],[88,10],[91,98],[1,47],[15,14],[85,47],[90,7],[30,39],[30,60],[94,68],[54,19],[22,41],[10,45],[57,83],[6,54],[1,68],[14,89],[11,2],[48,25],[50,21],[74,85],[86,78],[91,4],[3,96],[85,12],[69,94],[66,45],[80,36],[81,19],[83,5],[41,81],[4,50],[37,55],[81,88],[20,64],[78,81],[61,38],[42,14],[85,67],[74,99],[52,47],[87,18],[5,38],[43,37],[34,58],[41,18],[26,72],[48,39],[63,65],[91,27],[7,78],[17,29],[85,29],[49,26],[100,98],[60,18],[11,22],[58,18],[43,94],[11,6],[42,18],[79,75],[51,23],[69,43],[7,61],[28,82],[61,93],[77,36],[32,34],[58,27],[46,14],[95,54],[47,9],[52,58],[29,2],[75,80],[14,97],[75,16],[37,69],[71,30],[26,4],[18,67],[33,12],[24,77],[27,22],[28,39],[92,87],[5,81],[88,66],[25,36],[33,18],[28,82],[62,15],[74,84],[23,59],[99,49],[72,11],[10,34],[8,3],[8,84],[96,49],[34,99],[18,5],[44,19],[54,35],[56,98],[97,95],[20,52],[54,16],[8,94],[85,18],[23,22],[99,64],[7,10],[57,83],[81,75],[1,4],[42,78],[35,71],[96,89]]
    print(Solution().visiblePoints(points, 248, [7,12]))
    print(Solution().visiblePointsAC(points, 248, [7,12]))