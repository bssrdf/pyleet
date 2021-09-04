'''
-Hard-
*Geometry*

You are given a 2D integer array trees where trees[i] = [x_i, y_i] represents the location of 
the i-th tree in the garden.

You are asked to fence the entire garden using the minimum length of rope possible. The garden is 
well-fenced only if all the trees are enclosed and the rope used forms a perfect circle. A tree is 
considered enclosed if it is inside or on the border of the circle.

More formally, you must form a circle using the rope with a center (x, y) and radius r where all trees 
lie inside or on the circle and r is minimum.

Return the center and radius of the circle as a length 3 array [x, y, r]. Answers within 10-5 of the 
actual answer will be accepted.

Example 1:

Image text

Input: trees = [[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]

Output: [2.00000,2.00000,2.00000]

Explanation: The fence will have center = (2, 2) and radius = 2

Example 2:

Image text

Input: trees = [[1,2],[2,2],[4,2]]

Output: [2.50000,2.00000,1.50000]

Explanation: The fence will have center = (2.5, 2) and radius = 1.5

Constraints:

1 <= trees.length <= 3000
trees[i].length == 2
0 <= x_i, y_i <= 3000


'''

import random

class Solution(object):
    def smallestCircle(self, trees):
        """
        :type trees: List[List[int]]
        :rtype: List[float]
        """
        def dist(a, b):
            return ((a[0]-b[0])**2 + (a[1]-b[1])**2)**0.5

        def inside(c, p):
            return dist(c[0], p) < c[1]+EPS

        def circle_center(bx, by, cx, cy):
            B = bx*bx + by*by
            C = cx*cx + cy*cy
            D = bx*cy - by*cx
            return [float(cy*B - by*C)/(2*D),
                    float(bx*C - cx*B)/(2*D)]

        def circle_from_2_points(A, B):
            C = [(A[0]+B[0])/2.0, (A[1]+B[1])/2.0]
            return [C, dist(A, B)/2.0]

        def circle_from_3_points(A, B, C):
            I = circle_center(B[0]-A[0], B[1]-A[1],
                              C[0]-A[0], C[1]-A[1])
            I[0] += A[0]
            I[1] += A[1]
            return [I, dist(I, A)]

        def trivial(boundaries):  # circumscribed circle
            if not boundaries:
                return None
            if len(boundaries) == 1:
                return [boundaries[0], 0.0]
            if len(boundaries) == 2:
                return circle_from_2_points(boundaries[0], boundaries[1])
            return circle_from_3_points(boundaries[0], boundaries[1], boundaries[2])

        def Welzl(points, boundaries, curr):
            if curr == len(points) or len(boundaries) == 3:
                return trivial(boundaries)
            result = Welzl(points, boundaries, curr+1)
            if result is not None and inside(result, points[curr]):
                return result
            boundaries.append(points[curr])
            result = Welzl(points, boundaries, curr+1)
            boundaries.pop()
            return result

        EPS = 1e-5
        random.seed(0)
        random.shuffle(trees)
        result = Welzl(trees, [], 0)
        return result[0][0], result[0][1], result[1]

if __name__=="__main__":
    print(Solution().smallestCircle([[1,1],[2,2],[2,0],[2,4],[3,3],[4,2]]))