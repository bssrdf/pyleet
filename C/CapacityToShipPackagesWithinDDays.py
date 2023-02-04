'''

-Medium-

*Binary Search*

A conveyor belt has packages that must be shipped from one port to another 
within D days.

The i-th package on the conveyor belt has a weight of weights[i].  Each day, 
we load the ship with packages on the conveyor belt (in the order given 
by weights). We may not load more weight than the maximum weight capacity 
of the ship.

Return the least weight capacity of the ship that will result in all the 
packages on the conveyor belt being shipped within D days.

 

Example 1:

Input: weights = [1,2,3,4,5,6,7,8,9,10], D = 5
Output: 15
Explanation: 
A ship capacity of 15 is the minimum to ship all the packages in 5 days like this:
1st day: 1, 2, 3, 4, 5
2nd day: 6, 7
3rd day: 8
4th day: 9
5th day: 10

Note that the cargo must be shipped in the order given, so using a ship of 
capacity 14 and splitting the packages into parts like (2, 3, 4, 5), 
(1, 6, 7), (8), (9), (10) is not allowed. 

Example 2:

Input: weights = [3,2,2,4,1,4], D = 3
Output: 6
Explanation: 
A ship capacity of 6 is the minimum to ship all the packages in 3 days like this:
1st day: 3, 2
2nd day: 2, 4
3rd day: 1, 4
Example 3:

Input: weights = [1,2,3,1,1], D = 4
Output: 3
Explanation: 
1st day: 1
2nd day: 2
3rd day: 3
4th day: 1, 1
 

Constraints:

1 <= D <= weights.length <= 50000
1 <= weights[i] <= 500

'''
import sys

class Solution(object):


    def shipWithinDaysAC(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        def canShip(m):
            t, days = 0, 0
            for w in weights:
                if t + w > m:
                    days += 1
                    t = w
                else:
                    t += w
            return days+1 <= D
        l, r = max(weights), sum(weights)
        while l < r:
            mid = l + (r-l)//2
            if canShip(mid):
                r = mid
            else:
                l = mid + 1
        return l

    def shipWithinDays(self, weights, D):
        """
        :type weights: List[int]
        :type D: int
        :rtype: int
        """
        def canShip(m, target):
            sm = 0
            cnt = 0
            for n in weights:
                if sm + n > target:
                   sm = n
                   cnt += 1
                else: 
                   sm += n
            cnt += 1
            return cnt <= m
        l = 1
        r = 0
        for i in weights:
            l = max(l, i)
            r += i
        while l+1 < r:
            mid = l + (r-l)//2
            if canShip(D, mid):
                r = mid 
            else:
                l = mid+1
        if canShip(D, l): return l
        else: return r

if __name__ == "__main__":
    print(Solution().shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5))
    print(Solution().shipWithinDays([3,2,2,4,1,4], 3))
    print(Solution().shipWithinDays([1,2,3,1,1], 4))
    print(Solution().shipWithinDaysAC([1,2,3,4,5,6,7,8,9,10], 5))
    print(Solution().shipWithinDaysAC([3,2,2,4,1,4], 3))
    print(Solution().shipWithinDaysAC([1,2,3,1,1], 4))