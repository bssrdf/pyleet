'''
-Hard-

Given N axis-aligned rectangles where N > 0, determine if they all together 
form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point. 
For example, a unit square is represented as [1,1,2,2]. (coordinate of 
bottom-left point is (1, 1) and top-right point is (2, 2)).


Example 1:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]

Return true. All 5 rectangles together form an exact cover of a rectangular region.
 

 

Example 2:

rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
]

Return false. Because there is a gap between the two rectangular regions.
 

 

Example 3:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
]

Return false. Because there is a gap in the top center.
 

 

Example 4:

rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]

Return false. Because two of the rectangles overlap with each other.

'''

class Solution(object):
    def isRectangleCover(self, rectangles):
        """
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        X1, Y1, X2, Y2 = float('inf'), float('inf'), -float('inf'), -float('inf')
        allarea = 0
        vertices = set()
        for x1,y1,x2,y2 in rectangles:
            X1 = min(x1, X1)
            Y1 = min(y1, Y1)
            X2 = max(x2, X2)
            Y2 = max(y2, Y2)
            allarea += (y2-y1)*(x2-x1)
            for (x,y) in [(x1,y1), (x2,y1), (x1,y2), (x2,y2)]:
                if (x, y) in vertices:
                    vertices.remove((x,y))
                else:
                    vertices.add((x,y))
        area = (Y2-Y1)*(X2-X1)
        if area != allarea: return False
        if len(vertices) != 4: return False
        if (X1,Y1) not in vertices: return False
        if (X1,Y2) not in vertices: return False
        if (X2,Y1) not in vertices: return False
        if (X2,Y2) not in vertices: return False
        return True


if __name__ == "__main__":
    rect =  [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
  ]
    print(Solution().isRectangleCover(rect)) 
    rect = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
]
    print(Solution().isRectangleCover(rect)) 
