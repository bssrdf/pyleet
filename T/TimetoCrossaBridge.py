'''
-Hard-
*Priority Queue*
*Simulation*


There are k workers who want to move n boxes from an old warehouse to a new one. You are given the two integers n and k, and a 2D integer array time of size k x 4 where time[i] = [leftToRighti, pickOldi, rightToLefti, putNewi].

The warehouses are separated by a river and connected by a bridge. The old warehouse is on the right bank of the river, and the new warehouse is on the left bank of the river. Initially, all k workers are waiting on the left side of the bridge. To move the boxes, the ith worker (0-indexed) can :

Cross the bridge from the left bank (new warehouse) to the right bank (old warehouse) in leftToRighti minutes.
Pick a box from the old warehouse and return to the bridge in pickOldi minutes. Different workers can pick up their boxes simultaneously.
Cross the bridge from the right bank (old warehouse) to the left bank (new warehouse) in rightToLefti minutes.
Put the box in the new warehouse and return to the bridge in putNewi minutes. Different workers can put their boxes simultaneously.
A worker i is less efficient than a worker j if either condition is met:

leftToRighti + rightToLefti > leftToRightj + rightToLeftj
leftToRighti + rightToLefti == leftToRightj + rightToLeftj and i > j
The following rules regulate the movement of the workers through the bridge :

If a worker x reaches the bridge while another worker y is crossing the bridge, x waits at their side of the bridge.
If the bridge is free, the worker waiting on the right side of the bridge gets to cross the bridge. If more than one worker is waiting on the right side, the one with the lowest efficiency crosses first.
If the bridge is free and no worker is waiting on the right side, and at least one box remains at the old warehouse, the worker on the left side of the river gets to cross the bridge. If more than one worker is waiting on the left side, the one with the lowest efficiency crosses first.
Return the instance of time at which the last worker reaches the left bank of the river after all n boxes have been put in the new warehouse.

 

Example 1:

Input: n = 1, k = 3, time = [[1,1,2,1],[1,1,3,1],[1,1,4,1]]
Output: 6
Explanation: 
From 0 to 1: worker 2 crosses the bridge from the left bank to the right bank.
From 1 to 2: worker 2 picks up a box from the old warehouse.
From 2 to 6: worker 2 crosses the bridge from the right bank to the left bank.
From 6 to 7: worker 2 puts a box at the new warehouse.
The whole process ends after 7 minutes. We return 6 because the problem asks for the instance of time at which the last worker reaches the left bank.
Example 2:

Input: n = 3, k = 2, time = [[1,9,1,8],[10,10,10,10]]
Output: 50
Explanation: 
From 0  to 10: worker 1 crosses the bridge from the left bank to the right bank.
From 10 to 20: worker 1 picks up a box from the old warehouse.
From 10 to 11: worker 0 crosses the bridge from the left bank to the right bank.
From 11 to 20: worker 0 picks up a box from the old warehouse.
From 20 to 30: worker 1 crosses the bridge from the right bank to the left bank.
From 30 to 40: worker 1 puts a box at the new warehouse.
From 30 to 31: worker 0 crosses the bridge from the right bank to the left bank.
From 31 to 39: worker 0 puts a box at the new warehouse.
From 39 to 40: worker 0 crosses the bridge from the left bank to the right bank.
From 40 to 49: worker 0 picks up a box from the old warehouse.
From 49 to 50: worker 0 crosses the bridge from the right bank to the left bank.
From 50 to 58: worker 0 puts a box at the new warehouse.
The whole process ends after 58 minutes. We return 50 because the problem asks for the instance of time at which the last worker reaches the left bank.
 

Constraints:

1 <= n, k <= 104
time.length == k
time[i].length == 4
1 <= leftToRighti, pickOldi, rightToLefti, putNewi <= 1000


'''

from typing import List
import heapq
from heapq import heappop, heappush
from math import inf

class Solution:
    def findCrossingTime(self, n: int, k: int, time: List[List[int]]) -> int:
        T, pq = time, []
        for i,(lr, po, rl, pn) in enumerate(time):
            heapq.heappush(pq, (0, 1, -(lr+rl), -i, 0))
        mp = {2:0, 0:1, 1:-1, 3:-1}    
        bfree = 0
        while pq:
            curT, lr, e, j, cur = heapq.heappop(pq)
            # oldT = curT
            # oldc = cur
            l = cur % 4            
            # if l == 3 and n > 0: n -= 1
            # if l == 3 and -j == 5:
            #     print('xxxx')
            if l == 0 and n > 0 or l > 0:                 
                if l % 2 == 0 and curT < bfree:
                    curT = bfree
                    nxt = cur
                    heapq.heappush(pq, (curT, lr, e, j, nxt))
                else: 
                    curT += T[-j][l]
                    nxt = cur + 1
                    nxtd = nxt % 4
                    nxd = mp[nxtd]
                    if nxtd == 1: n -= 1                    
                    heapq.heappush(pq, (curT, nxd, e, j, nxt))
                    if l % 2 == 0: bfree = curT
            # print(oldT,oldc, curT, lr, nxd, l, cur, nxt, -j, bfree, n)
        # print(curT, -j)
        return curT - T[-j][-1] 
    
    def findCrossingTime4(self, n: int, k: int, time: List[List[int]]) -> int:
        T, pq = time, []
        for i,(lr, po, rl, pn) in enumerate(time):
            heapq.heappush(pq, (0, 1, -(lr+rl), -i, 0))
        mp = {2:0, 0:1, 1:-1, 3:-1}    
        bfree = 0
        while pq:
            curT, lr, e, j, cur = heapq.heappop(pq)
            # oldT = curT
            # oldc = cur
            l = cur % 4            
            # if l == 3 and n > 0: n -= 1
            # if l == 3 and -j == 5:
            #     print('xxxx')
            if l == 0 and n > 0 or l > 0:                 
                if l % 2 == 0 and curT < bfree:
                    curT = bfree
                    nxt = cur
                    heapq.heappush(pq, (curT, lr, e, j, nxt))
                else: 
                    curT += T[-j][l]
                    nxt = cur + 1
                    nxtd = nxt % 4
                    nxd = mp[nxtd]
                    if nxtd == 1: n -= 1                    
                    if nxtd == 1 or nxtd == 3:
                        nxd = mp[(nxtd+1)%4]
                        nxt += 1
                        heapq.heappush(pq, (curT+T[-j][nxtd], nxd, e, j, nxt))                        
                    else:
                        heapq.heappush(pq, (curT, nxd, e, j, nxt))
                    if l % 2 == 0: bfree = curT
            # print(oldT,oldc, curT, lr, nxd, l, cur, nxt, -j, bfree, n)
        # print(curT, -j)
        return curT - T[-j][-1] 


    
    def findCrossingTime3(self, n: int, k: int, time: List[List[int]]) -> int:
        b_t = 0                 # the earliest time when the bridge is empty for use
        m = len(time)
        stack = []
        for i in range(m):
            heapq.heappush(stack, (0, 1, -(time[i][0]+time[i][2]), -i))   # (time, bank, -1 * trips to/from the new house)
        task = [None for _ in range(m)]      # bank= 0,1 for the old, new side. Smaller (time, bank, -trip) is selected first
        for i in range(m):
            task[i] = [[time[i][2], time[i][3]], [time[i][0], time[i][1]]]           
        print('start', stack)
        while n:     
            t,bank,trip,j=heapq.heappop(stack)
            n -= 1-bank               # box decreases by 1 if one crosses from the old side,
            t = b_t = max(t, b_t) + task[-j][bank][0]            
            if n == 0:
                return t 
            t += task[-j][bank][1]     # cross from the new (old) side, need t1+t2 (t3+t4) back to the bridge. 
            
            print(n, bank, -j, stack)
            heapq.heappush(stack, (t,1-bank,trip,j))
            print(stack)

    
    def findCrossingTime2(self, n: int, k: int, time: List[List[int]]) -> int:
        # l: (-(leftToRight + rightToLeft), -i), waiting on the left side, sort by efficiency
        # r: (-(leftToRight + rightToLeft), -i), waiting on the right side, sort by efficiency
        # ll: (time, i), on what time can move to l from new warehouse
        # rr: (time, i), on what time can move to r from old warehouse

        ll, l, r, rr = [],[],[],[]
        for i,(l2r, po, r2l, pn) in enumerate(time):
            heappush(l, (-l2r-r2l, -i))
        
        t = 0
        while n:
            # Waiting to cross.
            # ll and rr are the workers that are already picked up and droped off the packages.
            # The earliest time for them to cross has been pre computed, and they are waiting for that time to come.
            while ll and ll[0][0] <= t:
                _, i = heappop(ll)
                heappush(l, (-time[i][0]-time[i][2],-i))
            while rr and rr[0][0] <= t:
                _, i = heappop(rr)
                heappush(r, (-time[i][0]-time[i][2],-i))
            
            # Crossing
            # The bridge is free, worker in r already waited until their pre-computed time to come, and now is the time.
            # time for each worker in r must <= t.
            if r:
                _,i = heappop(r)
                # Increase the time, this worker is crossing.
                t += time[-i][2]
                # Precompute the time when this worker can cross on the other side.
                heappush(ll, (t+time[-i][3], -i))
                # One box arrived to new.
                n -= 1
                # print('at right', -i, n, t)
            
            # The bridge is free, worker in l already waited until their pre-computed time to come, and now is the time.
            # Time for each worker in l must <= t.
            # Also there are still boxes left in the warehouse.
            elif l and n > len(r) + len(rr):
                _,i = heappop(l)
                # Increase the time, this worker is crossing.
                t += time[-i][0]
                # Precompute the time when this worker can cross on the other side.
                heappush(rr, (t+time[-i][1], -i))
                # print('at left', -i, n, t)
            
            # The cases left are: 
            # (1) r is empty, we don't need to move rr to r, because that is not about crossing. 
            # (2) l is not empty, but no more boxes in the old warehouse. 
            # (3) l is empty, and there is still boxes left in old whare house.
            # we just need to update t at this point, so that release the workers waiting to cross to the crossing queue in the next iteration.
            else:
                x = ll[0][0] if ll and n > len(r) + len(rr) else inf
                y = rr[0][0] if rr else inf
                t = min(x,y)
                # print('update t:', n, t)
        return t






print(Solution().findCrossingTime(n = 1, k = 3, time = [[1,1,2,1],[1,1,3,1],[1,1,4,1]]))
print(Solution().findCrossingTime(n = 3, k = 2, time = [[1,9,1,8],[10,10,10,10]]))
# print(Solution().findCrossingTime3(n = 3, k = 2, time = [[1,9,1,8],[10,10,10,10]]))
print(Solution().findCrossingTime(n = 10, k = 6, time = [[2,10,5,8],[3,5,2,2],[5,8,10,10],[7,8,8,5],[5,6,6,10],[6,10,6,2]]))
print(Solution().findCrossingTime2(n = 10, k = 6, time = [[2,10,5,8],[3,5,2,2],[5,8,10,10],[7,8,8,5],[5,6,6,10],[6,10,6,2]]))
print(Solution().findCrossingTime4(n = 10, k = 6, time = [[2,10,5,8],[3,5,2,2],[5,8,10,10],[7,8,8,5],[5,6,6,10],[6,10,6,2]]))
time = [[991,991,992,990],[990,994,998,999],[1000,992,996,993],[996,995,995,999],[994,994,990,992],[994,993,990,998],[992,999,994,993],[994,998,992,994],[998,995,995,998],[1000,991,993,990],[993,999,1000,993],[997,990,998,993],[996,994,991,995],[1000,990,995,997],[993,992,998,998],[996,999,997,995],[999,997,999,991],[995,993,998,993],[993,991,1000,993],[999,995,993,994],[994,994,990,1000],[1000,990,999,997],[997,998,992,995],[995,996,994,995],[993,998,994,992],[992,993,996,991],[996,999,1000,993],[1000,996,991,996],[994,997,999,999],[1000,999,998,995],[991,991,993,990],[990,990,995,991],[992,991,1000,992],[998,1000,994,990],[996,994,990,990],[1000,1000,995,997],[996,992,998,991],[993,993,992,999],[995,994,1000,997],[1000,997,1000,993],[991,996,998,992],[991,994,993,998],[995,992,993,995],[990,992,997,991],[999,995,994,994],[997,992,1000,1000],[994,999,995,999],[997,996,1000,990],[991,995,994,996],[990,998,993,999],[991,997,992,993],[997,995,998,997],[990,996,991,995],[1000,997,992,995],[990,995,997,994],[990,1000,991,997],[995,999,995,993],[992,999,995,995],[994,991,1000,999],[997,993,992,999],[999,998,999,994],[994,998,1000,1000],[990,993,999,996],[999,993,1000,992],[995,990,998,997],[992,994,993,996],[993,993,992,994],[993,993,993,990],[998,996,991,998],[994,993,1000,998],[993,999,992,993],[994,996,999,993],[997,996,1000,1000],[995,990,992,999],[992,996,997,994],[993,991,997,990],[995,1000,997,995],[997,990,996,990],[1000,993,995,993],[999,999,998,990],[994,990,999,994],[991,995,995,992],[992,992,996,992],[992,990,991,990],[990,994,991,991],[994,999,999,996],[998,998,1000,1000],[994,994,994,994],[999,996,991,994],[990,994,992,993],[994,990,992,994],[1000,998,994,996],[1000,994,990,999],[995,993,992,997],[993,997,999,996],[997,999,991,996],[993,997,996,990],[1000,995,997,990],[995,990,990,990],[998,1000,995,998],[990,999,998,1000],[1000,992,997,995],[998,995,995,997],[995,992,996,991],[991,1000,999,999],[996,996,997,995],[994,995,999,991],[997,999,993,992],[992,992,998,999],[991,999,995,1000],[994,995,993,992],[993,997,996,990],[990,993,1000,990],[996,997,997,998]]
print(Solution().findCrossingTime(n = 10000, k = 114, time = time))
print(Solution().findCrossingTime4(n = 10000, k = 114, time = time))
# print(Solution().findCrossingTime2(n = 10000, k = 114, time = time))

        