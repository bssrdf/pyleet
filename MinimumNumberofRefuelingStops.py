'''
-Hard-
*Priority Quque*
*Greedy*
*DP*

A car travels from a starting position to a destination which is target 
miles east of the starting position.

Along the way, there are gas stations.  Each station[i] represents a gas 
station that is station[i][0] miles east of the starting position, and 
has station[i][1] liters of gas.

The car starts with an infinite tank of gas, which initially has startFuel 
liters of fuel in it.  It uses 1 liter of gas per 1 mile that it drives.

When the car reaches a gas station, it may stop and refuel, transferring 
all the gas from the station into the car.

What is the least number of refueling stops the car must make in order to 
reach its destination?  If it cannot reach the destination, return -1.

Note that if the car reaches a gas station with 0 fuel left, the car can 
still refuel there.  If the car reaches the destination with 0 fuel left, 
it is still considered to have arrived.

 

Example 1:

Input: target = 1, startFuel = 1, stations = []
Output: 0
Explanation: We can reach the target without refueling.
Example 2:

Input: target = 100, startFuel = 1, stations = [[10,100]]
Output: -1
Explanation: We can't reach the target (or even the first gas station).
Example 3:

Input: target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
Output: 2
Explanation: 
We start with 10 liters of fuel.
We drive to position 10, expending 10 liters of fuel.  We refuel from 0 
liters to 60 liters of gas.
Then, we drive from position 10 to position 60 (expending 50 liters of fuel),
and refuel from 10 liters to 50 liters of gas.  We then drive to and reach
the target.
We made 2 refueling stops along the way, so we return 2.
 

Note:

1 <= target, startFuel, stations[i][1] <= 10^9
0 <= stations.length <= 500
0 < stations[0][0] < stations[1][0] < ... < stations[stations.length-1][0] < target

'''

import heapq

class Solution(object):
    def minRefuelStopsDP(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int        
        """
        n = len(stations)
        # the recursive function F[i], the farthest location we can get to 
        # using i refueling stops. This is motivated by the fact that we 
        # want the smallest i for which F[i] >= target.
        F = [0] * (n+1)
        F[0] = startFuel
        for i, (loc, cap) in enumerate(stations):
            # once arriving at a station, update all prior F[i]'s which
            # could reach the current station location. this means some
            # prior F[i]'s could skip all the way to the current one, hence
            # reducing the # of refuelings 
            for t in range(i, -1, -1):
                if F[t] >= loc:
                    F[t+1] = max(F[t+1], F[t] + cap) 
        for i,d in enumerate(F):
            if d >= target:
                return i
        return -1

    def minRefuelStops(self, target, startFuel, stations):
        """
        :type target: int
        :type startFuel: int
        :type stations: List[List[int]]
        :rtype: int        
        """
        i = res = 0
        pq = []
        cur = startFuel
        while cur < target:
            while i < len(stations) and stations[i][0] <= cur:
                heapq.heappush(pq, -stations[i][1])
                i += 1
            if not pq: return -1
            cur += -1*heapq.heappop(pq)
            res += 1
        return res




if __name__ == "__main__":
    print(Solution().minRefuelStops(100, 100, [[10,60],[20,30],[30,30],[60,40]]))
    print(Solution().minRefuelStops(100, 10, [[10,60],[20,30],[30,30],[60,40]]))
    print(Solution().minRefuelStops(100, 50, [[25,25],[50,50]]))
    
    
            
        