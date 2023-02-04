'''

-Medium-
*Geometry*

Given a list of points that form a polygon when joined sequentially, it is found that 
the polygon is convex (Convex polygon definition).

There are at least 3 and at most 10,000 points.
Coordinates are in the range -10,000 to 10,000.
You may assume the polygon formed by given points is always a simple polygon (Simple polygon definition). 
In other words, we ensure that exactly two edges intersect at each vertex, and that edges 
otherwise don't intersect each other.
样例
Example 1:
	Input: points = [[0, 0], [0, 1], [1, 1], [1, 0]]
	Output:  true
	
	Explanation:


Example 2:
	Input:  points = [[0, 0], [0, 10], [10, 10], [10, 0], [5, 5]]
	Output:  false
	
	Explanation:

'''

class Solution:
    """
    @param point: a list of two-tuples
    @return: a boolean, denote whether the polygon is convex
    """
    def isConvex(self, point):
        # write your code here
        n, cur, pre = len(point), 0, 0

        def cross(o, a, b):
            return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
        for i in range(n):
            cur = cross(point[i], point[(i+1)%n], point[(i+2)%n])
            if cur != 0:
                if (cur * pre < 0): return False
                else: pre = cur
        return True

if __name__=="__main__":
    print(Solution().isConvex([[0, 0], [0, 1], [1, 1], [1, 0]]))
    print(Solution().isConvex([[0, 0], [0, 10], [10, 10], [10, 0], [5, 5]]))