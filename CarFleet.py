'''
-Medium-

There are n cars going to the same destination along a one-lane road. The destination is target 
miles away.

You are given two integer array position and speed, both of length n, where position[i] is 
the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to 
bumper at the same speed.

The distance between these two cars is ignored (i.e., they are assumed to have the same position).

A car fleet is some non-empty set of cars driving at the same position and same speed. Note 
that a single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered 
as one car fleet.

Return the number of car fleets that will arrive at the destination.

 

Example 1:

Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
Output: 3
Explanation: 
The cars starting at 10 and 8 become a fleet, meeting each other at 12.
The car starting at 0 doesn't catch up to any other car, so it is a fleet by itself.
The cars starting at 5 and 3 become a fleet, meeting each other at 6.
Note that no other cars meet these fleets before the destination, so the answer is 3.
Example 2:

Input: target = 10, position = [3], speed = [3]
Output: 1
 

Constraints:

n == position.length == speed.length
1 <= n <= 10^5
0 < target <= 10^6
0 <= position[i] < target
All the values of position are unique.
0 < speed[i] <= 10^6

'''
import math
class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        n = len(position)
        pi = [(v,i) for i,v in enumerate(position)]
        pi.sort(reverse=True)
        ans = 1
        t = (target-pi[0][0])/speed[pi[0][1]]
        for p,i in pi[1:]:
            t1 = (target-p)/speed[i]
            if t1 > t:
                ans += 1
                t = t1
        return ans




if __name__ == "__main__": 
    print(Solution().carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))
    print(Solution().carFleet(target = 10, position = [3], speed = [3]))
    print(Solution().carFleet(target = 10, position = [6,8], speed = [3,2]))
    print(Solution().carFleet(10, [8,3,7,4,6,5], [4,4,4,4,4,4]))