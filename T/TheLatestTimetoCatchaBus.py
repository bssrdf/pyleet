'''

-Medium-

You are given a 0-indexed integer array buses of length n, where buses[i] represents the departure time of the ith bus. You are also given a 0-indexed integer array passengers of length m, where passengers[j] represents the arrival time of the jth passenger. All bus departure times are unique. All passenger arrival times are unique.

You are given an integer capacity, which represents the maximum number of passengers that can get on each bus.

The passengers will get on the next available bus. You can get on a bus that will depart at x minutes if you arrive at y minutes where y <= x, and the bus is not full. Passengers with the earliest arrival times get on the bus first.

Return the latest time you may arrive at the bus station to catch a bus. You cannot arrive at the same time as another passenger.

Note: The arrays buses and passengers are not necessarily sorted.

 

Example 1:

Input: buses = [10,20], passengers = [2,17,18,19], capacity = 2
Output: 16
Explanation: 
The 1st bus departs with the 1st passenger. 
The 2nd bus departs with you and the 2nd passenger.
Note that you must not arrive at the same time as the passengers, which is why you must arrive before the 2nd passenger to catch the bus.
Example 2:

Input: buses = [20,30,10], passengers = [19,13,26,4,25,11,21], capacity = 2
Output: 20
Explanation: 
The 1st bus departs with the 4th passenger. 
The 2nd bus departs with the 6th and 2nd passengers.
The 3rd bus departs with the 1st passenger and you.
 

Constraints:

n == buses.length
m == passengers.length
1 <= n, m, capacity <= 105
2 <= buses[i], passengers[i] <= 109
Each element in buses is unique.
Each element in passengers is unique.

'''

from typing import List

class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        B, P, C = buses, passengers, capacity
        B.sort()
        P.sort()
        n, m = len(B), len(P)
        i = j = 0
        k = 0
        while i < n and j < m:
            while j < m and P[j] <= B[i] and k < C:
                j += 1
                k += 1
            #if k == C:
            i += 1
            print(i, j, k)
        if j == m:
            return B[n-1]
        else:
            return P[j]-1    
            
    def latestTimeCatchTheBus2(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        B, P, C = buses, passengers, capacity
        B.sort()
        P.sort()
        n, m = len(B), len(P)
        i = j = 0
        while i < n:
            c = 0
            while j < m and P[j] <= B[i] and c < C:
                j += 1
                c += 1                
            if i == n-1:
                if c < C:
                    k = j-1
                    t = B[i]
                    while k >= 0 and P[k] == t:
                        k -= 1
                        t -= 1
                    return t
                else:
                    t = P[j-1]-1
                    k = j-2
                    while k >= 0 and P[k] == t:
                        k -= 1
                        t -= 1
                    return t
            i += 1
        return -1



if __name__ == "__main__":
    print(Solution().latestTimeCatchTheBus(buses = [20,30,10], passengers = [19,13,26,4,25,11,21], capacity = 2))
    print(Solution().latestTimeCatchTheBus2(buses = [20,30,10], passengers = [19,13,26,4,25,11,21], capacity = 2))
        