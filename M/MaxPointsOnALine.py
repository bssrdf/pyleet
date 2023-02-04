'''
Given n points on a 2D plane, find the maximum number of points that lie on 
the same straight line.

Example 1:

Input: [[1,1],[2,2],[3,3]]
Output: 3
Explanation:
^
|
|        o
|     o
|  o  
+------------->
0  1  2  3  4
Example 2:

Input: [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
Explanation:
^
|
|  o
|     o        o
|        o
|  o        o
+------------------->
0  1  2  3  4  5  6
NOTE: input types have been changed on April 15, 2019. Please reset to 
default code definition to get new method signature.

'''
from collections import defaultdict

class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        n = len(points)
        if n <= 1:
            return n        
        res = 0
        def gcd(a,b):
            if(b==0):
               return a
            else:
               return gcd(b,a%b)
        for i in range(n):
            samePoints = 0
            m = defaultdict(int)        
            for j in range(i+1,n):            
                if points[j][0] == points[i][0] and \
                   points[j][1] == points[i][1]:
                   samePoints += 1
                   continue
                if points[j][0] == points[i][0]:
                    m['inf'] += 1
                else:
                    num = (points[j][1] - points[i][1])
                    dem = (points[j][0] - points[i][0])
                    g = gcd(num, dem)
                    slope = (num // g, dem // g)
                    m[slope] += 1                           
            res = max(res, max(m.values() or [0])+samePoints)
        return res+1

if __name__ == "__main__":
    print(Solution().maxPoints([[0,0],[-1,-1],[2,2]]))
    print(Solution().maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]))