'''
-Medium-
*Greedy*
*Priority Queue*

There is a special kind of apple tree that grows apples every day for n days. 
On the ith day, the tree grows apples[i] apples that will rot after days[i] days, 
that is on day i + days[i] the apples will be rotten and cannot be eaten. 
On some days, the apple tree does not grow any apples, which are denoted 
by apples[i] == 0 and days[i] == 0.

You decided to eat at most one apple a day (to keep the doctors away). 
Note that you can keep eating after the first n days.

Given two integer arrays days and apples of length n, return the 
maximum number of apples you can eat.

 

Example 1:

Input: apples = [1,2,3,5,2], days = [3,2,1,4,2]
Output: 7
Explanation: You can eat 7 apples:
- On the first day, you eat an apple that grew on the first day.
- On the second day, you eat an apple that grew on the second day.
- On the third day, you eat an apple that grew on the second day. After this day, the apples that grew on the third day rot.
- On the fourth to the seventh days, you eat apples that grew on the fourth day.
Example 2:

Input: apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2]
Output: 5
Explanation: You can eat 5 apples:
- On the first to the third day you eat apples that grew on the first day.
- Do nothing on the fouth and fifth days.
- On the sixth and seventh days you eat apples that grew on the sixth day.
 

Constraints:

n == apples.length == days.length
1 <= n <= 2 * 104
0 <= apples[i], days[i] <= 2 * 104
days[i] = 0 if and only if apples[i] = 0.


'''

from typing import List
import heapq

class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        pq, ans = [], 0
        for i,(a,d) in enumerate(zip(apples, days)):
            while pq and pq[0][0] <= i:
                heapq.heappop(pq)
            if a > 0:
                heapq.heappush(pq, (i+d, a))
            if pq and pq[0][1] > 0:
                ans += 1 
                day, j = heapq.heappop(pq)
                if j - 1 > 0:
                    heapq.heappush(pq, (day, j-1))
        i = len(apples)
        while pq:
            while pq and pq[0][0] <= i:
                heapq.heappop(pq)
            if pq and pq[0][1] > 0:
                ans += 1
                day, j = heapq.heappop(pq)
                if j - 1 > 0:
                    heapq.heappush(pq, (day, j-1))
            i += 1
        return ans  

    def eatenApples2(self, apples: List[int], days: List[int]) -> int:
        pq, ans = [], 0
        i, n = 0, len(apples) 
        while i < n or pq:
            while pq and pq[0][0] <= i:
                heapq.heappop(pq)
            if i < len(apples) and apples[i] > 0:    
                heapq.heappush(pq, (i+days[i], apples[i]))
            if pq and pq[0][1] > 0:
                ans += 1 
                day, j = heapq.heappop(pq)
                if j - 1 > 0:
                    heapq.heappush(pq, (day, j-1))
            i += 1
        return ans    


            


if __name__ == "__main__":
    print(Solution().eatenApples(apples = [1,2,3,5,2], days = [3,2,1,4,2]))
    print(Solution().eatenApples(apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2]))
    print(Solution().eatenApples(apples = [3,0,0,1,2], days = [6,0,0,3,2]))
    print(Solution().eatenApples(apples = [2,1,10], days = [2,10,1]))

    print(Solution().eatenApples2(apples = [1,2,3,5,2], days = [3,2,1,4,2]))
    print(Solution().eatenApples2(apples = [3,0,0,0,0,2], days = [3,0,0,0,0,2]))
    print(Solution().eatenApples2(apples = [3,0,0,1,2], days = [6,0,0,3,2]))
    print(Solution().eatenApples2(apples = [2,1,10], days = [2,10,1]))
        