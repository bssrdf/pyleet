'''

-Hard-

$$$

There are n persons numbered from 0 to n - 1 and a door. Each person can enter or exit through the door once, taking one second.

You are given a non-decreasing integer array arrival of size n, where arrival[i] is the arrival time of the ith person at the door. You are also given an array state of size n, where state[i] is 0 if person i wants to enter through the door or 1 if they want to exit through the door.

If two or more persons want to use the door at the same time, they follow the following rules:

If the door was not used in the previous second, then the person who wants to exit goes first.
If the door was used in the previous second for entering, the person who wants to enter goes first.
If the door was used in the previous second for exiting, the person who wants to exit goes first.
If multiple persons want to go in the same direction, the person with the smallest index goes first.
Return an array answer of size n where answer[i] is the second at which the ith person crosses the door.

Note that:

Only one person can cross the door at each second.
A person may arrive at the door and wait without entering or exiting to follow the mentioned rules.
 

Example 1:

Input: arrival = [0,1,1,2,4], state = [0,1,0,0,1]
Output: [0,3,1,2,4]
Explanation: At each second we have the following:
- At t = 0: Person 0 is the only one who wants to enter, so they just enter through the door.
- At t = 1: Person 1 wants to exit, and person 2 wants to enter. Since the door was used the previous second for entering, person 2 enters.
- At t = 2: Person 1 still wants to exit, and person 3 wants to enter. Since the door was used the previous second for entering, person 3 enters.
- At t = 3: Person 1 is the only one who wants to exit, so they just exit through the door.
- At t = 4: Person 4 is the only one who wants to exit, so they just exit through the door.
Example 2:

Input: arrival = [0,0,0], state = [1,0,1]
Output: [0,2,1]
Explanation: At each second we have the following:
- At t = 0: Person 1 wants to enter while persons 0 and 2 want to exit. Since the door was not used in the previous second, the persons who want to exit get to go first. Since person 0 has a smaller index, they exit first.
- At t = 1: Person 1 wants to enter, and person 2 wants to exit. Since the door was used in the previous second for exiting, person 2 exits.
- At t = 2: Person 1 is the only one who wants to enter, so they just enter through the door.
 

Constraints:

n == arrival.length == state.length
1 <= n <= 105
0 <= arrival[i] <= n
arrival is sorted in non-decreasing order.
state[i] is either 0 or 1.

'''

from typing import List
from collections import deque
import heapq

from math import inf
class Solution:
    def timeToCross(self, arrival: List[int], state: List[int]) -> List[int]:
        enterq = []
        exitq = []
        ans = [-1]*len(arrival)
        for i, (a,s) in enumerate(zip(arrival, state)):
            if s == 0:
                heapq.heappush(enterq, (a, i))
            else:
                heapq.heappush(exitq, (a, i))
        cur, prev = -1, 0
        while enterq or exitq:
            t1, _ = exitq[0] if exitq else (inf,-1)
            t2, _ = enterq[0] if enterq else (inf,-1)
            if t1 < t2:
                t, i = heapq.heappop(exitq)                
                cur, prev = max(cur, t), 1
            elif t1 > t2:
                t, i = heapq.heappop(enterq)                
                cur, prev = max(cur, t), -1
            else:
                if t1-1 == cur:
                    if prev >= 0:
                        t, i = heapq.heappop(exitq)                
                        cur, prev = max(cur, t), 1                        
                    elif prev < 0:
                        t, i = heapq.heappop(enterq)                
                        cur, prev = max(cur, t), -1                        
                else:
                    t, i = heapq.heappop(exitq)                
                    cur, prev = max(cur, t), 1
            ans[i] = cur
            print(cur, exitq, enterq, ans)
        return ans

    def timeToCross2(self, arrival: List[int], state: List[int]) -> List[int]:
        A, S = arrival, state
        n = len(A)
        enterq, exitq = deque(), deque()
        ans = [-1]*len(arrival)
        ops = [0]*(n+1)
        cur, i = 0, 0
        while i < n:
            while i < n and A[i] <= cur:
                if S[i] > 0:
                    exitq.append(i)
                else:
                    enterq.append(i)
                i += 1
            # print(i, enterq, exitq)
            j = -1
            if cur > 0:
                if ops[cur - 1] >= 0:
                    if exitq:
                        j = exitq.popleft()
                        ops[cur] = 1
                    else:
                        j = enterq.popleft()
                        ops[cur] = -1                
                elif ops[cur - 1] == -1:
                    if enterq:
                        j  =  enterq.popleft() 
                        ops[cur] = -1
                    else : 
                        j = exitq.popleft()
                        ops[cur] = 1            
            else:
                if exitq:
                    j = exitq.popleft()
                    ops[cur] = 1
                elif enterq:
                    j = enterq.popleft()
                    ops[cur] = -1
            if j >= 0:
                ans[j] = cur
            cur += 1
            # print(j, cur, enterq, exitq)
        while exitq or enterq:
            if ops[cur - 1] >= 0:
                if exitq:
                    j = exitq.popleft()
                    ops[cur] = 1
                else:
                    j = enterq.popleft()
                    ops[cur] = -1                
            elif ops[cur - 1] == -1:
                if enterq:
                    j  =  enterq.popleft() 
                    ops[cur] = -1
                else : 
                    j = exitq.popleft()
                    ops[cur] = 1
            ans[j] = cur
            cur += 1         
        return ans
    
    def timeToCross3(self, arrival: List[int], state: List[int]) -> List[int]:
        A, S = arrival, state
        n = len(A)
        ans = [0]*n
        qs = [deque(), deque()]
        d, time = 1, 0
        def popQueues(time, d, arrivalTime):
            while arrivalTime > time and (qs[0] or qs[1]):
                if not qs[d]:
                    d ^= 1
                ans[qs[d][0]] = time
                qs[d].popleft()
                time += 1
            return time,d    

        for i in range(n):
            time, d = popQueues(time, d, A[i])
            # If the door was not used in the previous second, then the person who
            #  wants to exit goes first.
            if A[i] > time:
                time = arrival[i]  # Forward the `time` to now.
                d = 1
            qs[S[i]].append(i)

        popQueues(time, d, 200000)
        return ans







        



if __name__=="__main__":        
    # print(Solution().timeToCross(arrival = [0,1,1,2,4], state = [0,1,0,0,1]))
    print(Solution().timeToCross2(arrival = [0,1,1,2,4], state = [0,1,0,0,1]))
    print(Solution().timeToCross3(arrival = [0,1,1,2,4], state = [0,1,0,0,1]))
    print(Solution().timeToCross2(arrival = [0,0,0], state = [1,0,1]))
    print(Solution().timeToCross3(arrival = [0,0,0], state = [1,0,1]))


