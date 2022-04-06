'''
-Hard-


You are given a 0-indexed 2D integer array tires where tires[i] = [fi, ri] indicates 
that the ith tire can finish its xth successive lap in fi * ri(x-1) seconds.

For example, if fi = 3 and ri = 2, then the tire would finish its 1st lap in 3 seconds, 
its 2nd lap in 3 * 2 = 6 seconds, its 3rd lap in 3 * 2^2 = 12 seconds, etc.
You are also given an integer changeTime and an integer numLaps.

The race consists of numLaps laps and you may start the race with any tire. You have 
an unlimited supply of each tire and after every lap, you may change to any given 
tire (including the current tire type) if you wait changeTime seconds.

Return the minimum time to finish the race.

 

Example 1:

Input: tires = [[2,3],[3,4]], changeTime = 5, numLaps = 4
Output: 21
Explanation: 
Lap 1: Start with tire 0 and finish the lap in 2 seconds.
Lap 2: Continue with tire 0 and finish the lap in 2 * 3 = 6 seconds.
Lap 3: Change tires to a new tire 0 for 5 seconds and then finish the lap in another 2 seconds.
Lap 4: Continue with tire 0 and finish the lap in 2 * 3 = 6 seconds.
Total time = 2 + 6 + 5 + 2 + 6 = 21 seconds.
The minimum time to complete the race is 21 seconds.
Example 2:

Input: tires = [[1,10],[2,2],[3,4]], changeTime = 6, numLaps = 5
Output: 25
Explanation: 
Lap 1: Start with tire 1 and finish the lap in 2 seconds.
Lap 2: Continue with tire 1 and finish the lap in 2 * 2 = 4 seconds.
Lap 3: Change tires to a new tire 1 for 6 seconds and then finish the lap in another 2 seconds.
Lap 4: Continue with tire 1 and finish the lap in 2 * 2 = 4 seconds.
Lap 5: Change tires to tire 0 for 6 seconds then finish the lap in another 1 second.
Total time = 2 + 4 + 6 + 2 + 4 + 6 + 1 = 25 seconds.
The minimum time to complete the race is 25 seconds. 
 

Constraints:

1 <= tires.length <= 105
tires[i].length == 2
1 <= fi, changeTime <= 105
2 <= ri <= 105
1 <= numLaps <= 1000


'''
from typing import List

class Solution:
    def minimumFinishTime(self, tires: List[List[int]], changeTime: int, numLaps: int) -> int:
        tires.sort()
        new_tires = []
        for t in tires:
            if not new_tires or new_tires[-1][1] > t[1]:
                new_tires.append(t)
        tires = new_tires
        n, BIG = len(tires), 2*10**9
        # to handle the cases where numLaps is small
		# without_change[i][j]: the total time to run j laps consecutively with tire i
        without_change = [[BIG]*20 for _ in range(n)]
        for i in range(n):
            without_change[i][1] = tires[i][0]
            for j in range(2, 20):
                if without_change[i][j-1] * tires[i][1] >= BIG:
                    break
                without_change[i][j] = without_change[i][j-1] * tires[i][1]
            # since we define it as the total time, rather than just the time for the j-th lap
			# we have to make it prefix sum
            for j in range(2, 20):
                if without_change[i][j-1] + without_change[i][j] >= BIG:
                    break
                without_change[i][j] += without_change[i][j-1]
        
		# dp[x]: the minimum time to finish x laps
        dp = [BIG]*(numLaps+1)
        for i in range(n):
            dp[1] = min(dp[1], tires[i][0])
        for x in range(2, numLaps+1):
            if x < 20:
				# x is small enough, so an optimal solution might never changes tires!
                for i in range(n):
                    dp[x] = min(dp[x], without_change[i][x])
            j = x-1
            while j > 0 and j >= x-18:
                dp[x] = min(dp[x], dp[j] + changeTime + dp[x-j])
                j -= 1
        return dp[numLaps]

if __name__ == "__main__":
    print(Solution().minimumFinishTime(tires = [[1,10],[2,2],[3,4]], changeTime = 6, numLaps = 5))

        