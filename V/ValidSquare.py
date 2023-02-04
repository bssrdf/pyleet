'''
-Medium-

Given the coordinates of four points in 2D space, return whether the four 
points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two 
integers.

Example:

Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
Output: True
 

Note:

All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal 
angles (90-degree angles).
Input points have no order.
'''
class Solution(object):
    def validSquareSimple(self, p1, p2, p3, p4):
        def orthogonal(p1, p2, p3):
            if not (p3[0]-p1[0]==0 and p3[1]-p1[1]==0) and \
               not (p2[0]-p1[0]==0 and p2[1]-p1[1]==0) and \
            (p3[0]-p1[0])*(p2[0]-p1[0])+(p3[1]-p1[1])*(p2[1]-p1[1]) == 0:
                return True
            else:
                return False
        print(orthogonal(p1, p2, p3))
        print(orthogonal(p2, p1, p4))
        print(orthogonal(p3, p1, p4))
        if orthogonal(p1, p2, p3) and orthogonal(p2, p1, p4) and \
           orthogonal(p3, p1, p4): 
            return True
        if orthogonal(p1, p2, p3) and orthogonal(p3, p1, p2) and \
           orthogonal(p4, p1, p2): 
            return True    
        else:
            return False

           
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        d2 = (p1[0]-p2[0])**2+(p1[1]-p2[1])**2
        d3 = (p1[0]-p3[0])**2+(p1[1]-p3[1])**2
        d4 = (p1[0]-p4[0])**2+(p1[1]-p4[1])**2        
        if d2 == 0 or d3 == 0 or d4 == 0: return False
        if d2 == d3 and d2+d3 == d4 and \
           (p2[0]-p1[0])*(p3[0]-p1[0])+(p2[1]-p1[1])*(p3[1]-p1[1]) == 0 and \
           (p2[0]-p4[0])*(p3[0]-p4[0])+(p2[1]-p4[1])*(p3[1]-p4[1]) == 0:
            return True
        if d2 == d4 and d2+d4 == d3 and \
           (p2[0]-p1[0])*(p4[0]-p1[0])+(p2[1]-p1[1])*(p4[1]-p1[1]) == 0 and \
           (p2[0]-p3[0])*(p4[0]-p3[0])+(p2[1]-p3[1])*(p4[1]-p3[1]) == 0:
            return True
        if d3 == d4 and d3+d4 == d2 and \
           (p3[0]-p1[0])*(p4[0]-p1[0])+(p3[1]-p1[1])*(p4[1]-p1[1]) == 0 and \
           (p3[0]-p2[0])*(p4[0]-p2[0])+(p3[1]-p2[1])*(p4[1]-p2[1]) == 0:
            return True
        return False

if __name__ == "__main__":
    print(Solution().validSquare([0,0], [1,1], [1,0], [0,1]))
    print(Solution().validSquare([0,1], [1,2], [0,2], [0,0]))
    print(Solution().validSquare([1,1], [0,1], [1,2], [0,0]))
    #print(Solution().validSquareSimple([0,0], [1,1], [1,0], [0,1]))
    #print(Solution().validSquareSimple([0,1], [1,2], [0,2], [0,0]))
    #print(Solution().validSquareSimple([1,1], [0,1], [1,2], [0,0]))
