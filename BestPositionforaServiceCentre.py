'''
-Hard-
*Gradient Decent*

A delivery company wants to build a new service centre in a new city. The company knows the positions of all the customers in this city on a 2D-Map and wants to build the new centre in a position such that the sum of the euclidean distances to all customers is minimum.

Given an array positions where positions[i] = [xi, yi] is the position of the ith customer on the map, return the minimum sum of the euclidean distances to all customers.

In other words, you need to choose the position of the service centre [xcentre, ycentre] such that the following formula is minimized:


Answers within 10^-5 of the actual value will be accepted.

 

Example 1:


Input: positions = [[0,1],[1,0],[1,2],[2,1]]
Output: 4.00000
Explanation: As shown, you can see that choosing [xcentre, ycentre] = [1, 1] will make the distance to each customer = 1, the sum of all distances is 4 which is the minimum possible we can achieve.
Example 2:


Input: positions = [[1,1],[3,3]]
Output: 2.82843
Explanation: The minimum possible sum of distances = sqrt(2) + sqrt(2) = 2.82843
Example 3:

Input: positions = [[1,1]]
Output: 0.00000
Example 4:

Input: positions = [[1,1],[0,0],[2,0]]
Output: 2.73205
Explanation: At the first glance, you may think that locating the centre at [1, 0] will achieve the minimum sum, but locating it at [1, 0] will make the sum of distances = 3.
Try to locate the centre at [1.0, 0.5773502711] you will see that the sum of distances is 2.73205.
Be careful with the precision!
Example 5:

Input: positions = [[0,1],[3,2],[4,5],[7,6],[8,9],[11,1],[2,12]]
Output: 32.94036
Explanation: You can use [4.3460852395, 4.9813795505] as the position of the centre.
 

Constraints:

1 <= positions.length <= 50
positions[i].length == 2
0 <= positions[i][0], positions[i][1] <= 100

'''
import math

class Solution(object):
    def getMinDistSum(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: float
        """
        EPSILON = 1.0
        ALPHA = 0.5
        BETA = 0.8
        N = len(positions)
        def calcgradient(x, y):
            ans = [0, 0]
            for i in range(N):
                denom = math.sqrt(pow(positions[i][0]-x, 2) + pow(positions[i][1] - y, 2))
                
                ans[0] += (x - positions[i][0])/denom
                ans[1] += (y - positions[i][1])/denom
            return ans
        
        def object(x, y):
            res = 0.0
            for i in range(N):
                res += math.sqrt(pow(positions[i][0]-x, 2) + pow(positions[i][1] - y, 2)) 
            # print("x:", x, " obj:", res)
            return res
        
        def armijo(x, y, epsilon):
            grad = calcgradient(x, y)
            left = object(x - epsilon * grad[0], y - epsilon * grad[1]) - object(x, y)
            right =  -1 * ALPHA * epsilon *  (grad[0] * grad[0] + grad[1] * grad[1])
            res = left <= right
            # print(left, right)
            return res
        def backtrack(x, y):
            eps = EPSILON
            while armijo(x, y, eps) is False:
                eps = BETA * eps
            return eps
        x = 0.1
        y = 0.1
        res = object(x, y)
        flag = True
        while flag:
            # print(i)
            stepsize = backtrack(x, y)
            grad = calcgradient(x, y)
            x -= stepsize * grad[0]
            y -= stepsize * grad[1]
            nres = object(x, y)
            # print(x, y, nres)
            if nres < res - 0.00000001:
                flag = True
            else:
                flag = False
            res = nres
        return  res
    
    def getMinDistSum2(self, positions):
        from math import sqrt
        
        def dist_all(x, y):  # calculate the sum of distances from (x, y) to all points
            return sum(sqrt((x2-x)**2 + (y2-y)**2) for x2, y2 in P)
        P = positions  
        l = len(P)
        x, y = sum(x for x, y in P) / l, sum(y for x, y in P) / l  # use centroid as the start point
        d = dist_all(x, y)  # sum of distances for initial point
        
        # step: inital searching step. choosing 10 since all point coordinates are in range [0, 100]
        # eps: since the problem demands an accuracy of 10^-5. I choose a smaller one, no reason
        # these two numbers are kind of arbitrarily choosen
        step, eps = 10, 0.000001
        while step > eps:
            flag = False  # Do we find a  better point in this round?
            for dx, dy in ((0,1),(0,-1),(1,0),(-1,0)):
                x2, y2 = x + step * dx, y + step * dy
                t = dist_all(x2, y2)
                if t < d:  # do find a better solution point
                    x, y, d = x2, y2, t
                    flag = True
                    break
            if not flag: step /= 2  # if no better point is found, shrink ths step for a closer search
        return d


if __name__ == "__main__":
    pos = [[0,1],[1,0],[1,2],[2,1]]
    print(Solution().getMinDistSum(pos))