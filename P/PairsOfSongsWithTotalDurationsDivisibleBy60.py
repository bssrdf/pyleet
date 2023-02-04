'''
-Medium-

You are given a list of songs where the ith song has a duration of time[i] seconds.

Return the number of pairs of songs for which their total duration in seconds is 
divisible by 60. Formally, we want the number of indices i, j such that i < j 
with (time[i] + time[j]) % 60 == 0.

 

Example 1:

Input: time = [30,20,150,100,40]
Output: 3
Explanation: Three pairs have a total duration divisible by 60:
(time[0] = 30, time[2] = 150): total duration 180
(time[1] = 20, time[3] = 100): total duration 120
(time[1] = 20, time[4] = 40): total duration 60
Example 2:

Input: time = [60,60,60]
Output: 3
Explanation: All three pairs have a total duration of 120, which is divisible 
by 60.
 

Constraints:

1 <= time.length <= 6 * 10^4
1 <= time[i] <= 500

'''

from collections import defaultdict

class Solution(object):
    def numPairsDivisibleBy60(self, time):
        """
        :type time: List[int]
        :rtype: int
        if (a+b)%K = 0, let c = a%K, d = b%K
        there must be c+d = K or c = 0 and d = 0
        so this problem is a variation of 2SUM: find 2 numbers in time
        that time[i]%60 + time[j]%60 = 60  
        """
        m = defaultdict(int)
        n = len(time)        
        ans = 0       
        m[time[0]%60]+=1
        for t in time[1:]:
            l = t%60
            n = 0 if l == 0 else 60-l
            if n in m:
                ans += m[n]
            m[l] += 1            
        return ans



if __name__ == "__main__":       
    print(Solution().numPairsDivisibleBy60([30,20,150,100,40]))
    print(Solution().numPairsDivisibleBy60([60,60,60]))

    