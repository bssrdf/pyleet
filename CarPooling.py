'''
-Medium-

You are driving a vehicle that has capacity empty seats initially available 
for passengers.  The vehicle only drives east (ie. it cannot turn around 
and drive west.)

Given a list of trips, trip[i] = [num_passengers, start_location, end_location] 
contains information about the i-th trip: the number of passengers that must 
be picked up, and the locations to pick them up and drop them off.  The locations 
are given as the number of kilometers due east from your vehicle's initial 
location.

Return true if and only if it is possible to pick up and drop off all passengers 
for all the given trips. 
 

Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
Example 3:

Input: trips = [[2,1,5],[3,5,7]], capacity = 3
Output: true
Example 4:

Input: trips = [[3,2,7],[3,7,9],[8,3,9]], capacity = 11
Output: true
 
 

Constraints:

trips.length <= 1000
trips[i].length == 3
1 <= trips[i][0] <= 100
0 <= trips[i][1] < trips[i][2] <= 1000
1 <= capacity <= 100000

'''
from collections import defaultdict

class Solution(object):

    def carPoolingDiffArray(self, trips, capacity):
        N  =  1001
        df = [0]*(N+1)
        for np, sp, ep in trips:
            df[sp] += np
            df[ep] -= np #这个地方不能加1，考虑同一站既有上车又有下车（题目说了先下后上）
        sm = 0        
        for i in range(N+1):            
            sm += df[i]
            if sm > capacity: return False
        return True
             
    
    def carPooling(self, trips, capacity):
        """
        :type trips: List[List[int]]
        :type capacity: int
        :rtype: bool
        """
        seat_left = capacity
        n = len(trips)        
        sPos = []
        ePos = []
        for t in trips:
            np, sp, ep = t            
            sPos.append((sp, np))
            ePos.append((ep, np))
        sPos.sort()
        ePos.sort()        

        i = j = 0
        while i < n and j < n:            
            if sPos[i][0] < ePos[j][0]:                
                seat_left -= sPos[i][1]
                i += 1                
            elif sPos[i][0] > ePos[j][0]:                
                seat_left += ePos[j][1]
                j += 1
            else:   
                seat_left += ePos[j][1]             
                while j+1 < n and ePos[j+1][0] == ePos[j][0]:                    
                    j += 1               
                    seat_left += ePos[j][1]             
                seat_left -= sPos[i][1]    
                while i+1 < n and sPos[i+1][0] == sPos[i][0]:
                    i += 1              
                    seat_left -= sPos[i][1]                    
                i += 1
                j += 1            
            
            if seat_left < 0:
                return False
            if i == n:
                break
            
        
        return True        


if __name__ == "__main__":
    print(Solution().carPooling([[2,1,5],[3,3,7]], 4))
    print(Solution().carPooling([[2,1,5],[3,3,7]], 5))
    print(Solution().carPooling([[2,1,5],[3,5,7]], 3))
    print(Solution().carPooling([[3,2,7],[3,7,9],[8,3,9]], 11))
    print(Solution().carPooling([[5,4,7],[7,4,8],[4,1,8]], 17))   
    print(Solution().carPooling([[9,3,4],[9,1,7],[4,2,4],[7,4,5]], 23))
    print(Solution().carPooling([[3,5,9],[4,2,5],[3,4,6],[9,1,4],[5,6,8],[5,4,6]], 14))
    print("------------------------")
    print(Solution().carPoolingDiffArray([[2,1,5],[3,3,7]], 4))
    print(Solution().carPoolingDiffArray([[2,1,5],[3,3,7]], 5))
    print(Solution().carPoolingDiffArray([[2,1,5],[3,5,7]], 3))
    print(Solution().carPoolingDiffArray([[3,2,7],[3,7,9],[8,3,9]], 11))
    print(Solution().carPoolingDiffArray([[5,4,7],[7,4,8],[4,1,8]], 17))   
    print(Solution().carPoolingDiffArray([[9,3,4],[9,1,7],[4,2,4],[7,4,5]], 23))
    print(Solution().carPoolingDiffArray([[3,5,9],[4,2,5],[3,4,6],[9,1,4],
                                   [5,6,8],[5,4,6]], 14))
