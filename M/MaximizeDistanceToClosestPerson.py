'''
-Medium-
*DP*
*2Pass*

You are given an array representing a row of seats where seats[i] = 1 
represents a person sitting in the ith seat, and seats[i] = 0 represents 
that the ith seat is empty (0-indexed).

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and 
the closest person to him is maximized. 

Return that maximum distance to the closest person.

 

Example 1:


Input: seats = [1,0,0,0,1,0,1]
Output: 2
Explanation: 
If Alex sits in the second open seat (i.e. seats[2]), then the closest 
person has distance 2.

If Alex sits in any other open seat, the closest person has distance 1.
Thus, the maximum distance to the closest person is 2.
Example 2:

Input: seats = [1,0,0,0]
Output: 3
Explanation: 
If Alex sits in the last seat (i.e. seats[3]), the closest person is 3 
seats away.
This is the maximum distance possible, so the answer is 3.
Example 3:

Input: seats = [0,1]
Output: 1
 

Constraints:

2 <= seats.length <= 2 * 10^4
seats[i] is 0 or 1.
At least one seat is empty.
At least one seat is occupied.

'''

class Solution(object):

    def maxDistToClosest1Pass(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        n = len(seats)
        start, res = 0, 0
        for i in range(n):
            if not seats[i]:
                continue
            if start == 0:
                res = max(res, i-start)
            else:
                res = max(res, (i-start+1)//2)
            start = i+1       
        res = max(res, n-start) 
        return res


    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        n = len(seats)
        dist1 = [n+1]*(n+1)
        dist2 = [n+1]*(n+1)
        for i in range(1,n+1):
            if not seats[i-1]:
                dist1[i] = dist1[i-1]+1
            else:
                dist1[i] = 0
            if not seats[n-i]:
                dist2[n-i] = dist2[n-i+1]+1
            else:
                dist2[n-i] = 0        
        res = 1        
        for d1, d2 in zip(dist1[1:], dist2[:-1]):        
            res = max(res, min(d1, d2))   
        #print(dist1)
        #print(dist2)
        return res
    
if __name__ == "__main__":
    print(Solution().maxDistToClosest([1,0,0,0,1,0,1]))
    print(Solution().maxDistToClosest([1,0,0,0]))
    print(Solution().maxDistToClosest([0,1]))
    print(Solution().maxDistToClosest1Pass([1,0,0,0,1,0,1]))
    print(Solution().maxDistToClosest1Pass([1,0,0,0]))
    print(Solution().maxDistToClosest1Pass([0,1]))

