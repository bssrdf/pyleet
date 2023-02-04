'''
-Medium-

*Geometry*

You are given a circle represented as (radius, xCenter, yCenter) and an axis-aligned rectangle represented as (x1, y1, x2, y2), where (x1, y1) are the coordinates of the bottom-left corner, and (x2, y2) are the coordinates of the top-right corner of the rectangle.

Return true if the circle and rectangle are overlapped otherwise return false. In other words, check if there is any point (xi, yi) that belongs to the circle and the rectangle at the same time.

 

Example 1:


Input: radius = 1, xCenter = 0, yCenter = 0, x1 = 1, y1 = -1, x2 = 3, y2 = 1
Output: true
Explanation: Circle and rectangle share the point (1,0).
Example 2:

Input: radius = 1, xCenter = 1, yCenter = 1, x1 = 1, y1 = -3, x2 = 2, y2 = -1
Output: false
Example 3:


Input: radius = 1, xCenter = 0, yCenter = 0, x1 = -1, y1 = 0, x2 = 0, y2 = 1
Output: true
 

Constraints:

1 <= radius <= 2000
-104 <= xCenter, yCenter <= 104
-104 <= x1 < x2 <= 104
-104 <= y1 < y2 <= 104



'''

class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        # TLE
        if xCenter+radius < x1 or xCenter-radius > x2: return False
        if yCenter+radius < y1 or yCenter-radius > y2: return False
        r2 = radius ** 2
        for x in range(xCenter-radius, xCenter+radius+1):
            for y in range(yCenter-radius, yCenter+radius+1):
                if (x-xCenter)*(x-xCenter) + (y-yCenter)*(y-yCenter) <= r2 and \
                   x1 <= x <= x2 and y1 <= y <= y2:
                   return True
        return False  
    
    def checkOverlap2(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        x1 -= xCenter; x2 -= xCenter
        y1 -= yCenter; y2 -= yCenter
        minX = min(x1*x1, x2*x2) if x1 * x2 > 0 else 0
        minY = min(y1*y1, y2*y2) if y1 * y2 > 0 else 0
        return minY + minX <= radius * radius
    
    def checkOverlap3(self, radius: int, xCenter: int, yCenter: int, x1: int, y1: int, x2: int, y2: int) -> bool:
        edgeX = x1 if xCenter < x1 else (x2 if xCenter > x2 else xCenter)
        edgeY = y1 if yCenter < y1 else (y2 if yCenter > y2 else yCenter)
        distX = xCenter - edgeX
        distY = yCenter - edgeY
        return distX * distX + distY * distY <= radius * radius







if __name__ == "__main__":
    print(Solution().checkOverlap(radius = 1939, xCenter = 623, yCenter = -964,
                x1 = -497,  y1 = -380, x2 = -407, y2 = -47)) 
    print(Solution().checkOverlap2(radius = 1939, xCenter = 623, yCenter = -964,
                x1 = -497,  y1 = -380, x2 = -407, y2 = -47)) 
