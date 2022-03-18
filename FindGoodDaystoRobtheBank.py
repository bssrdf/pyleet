'''
-Medium-

You and a gang of thieves are planning on robbing a bank. You are given a 0-indexed 
integer array security, where security[i] is the number of guards on duty on 
the ith day. The days are numbered starting from 0. You are also given an integer time.

The ith day is a good day to rob the bank if:

There are at least time days before and after the ith day,
The number of guards at the bank for the time days before i are non-increasing, and
The number of guards at the bank for the time days after i are non-decreasing.
More formally, this means day i is a good day to rob the bank if and only if 
security[i - time] >= security[i - time + 1] >= ... >= security[i] <= ... <= security[i + time - 1] <= security[i + time].

Return a list of all days (0-indexed) that are good days to rob the bank. The 
order that the days are returned in does not matter.

 

Example 1:

Input: security = [5,3,3,3,5,6,2], time = 2
Output: [2,3]
Explanation:
On day 2, we have security[0] >= security[1] >= security[2] <= security[3] <= security[4].
On day 3, we have security[1] >= security[2] >= security[3] <= security[4] <= security[5].
No other days satisfy this condition, so days 2 and 3 are the only good days to rob the bank.
Example 2:

Input: security = [1,1,1,1,1], time = 0
Output: [0,1,2,3,4]
Explanation:
Since time equals 0, every day is a good day to rob the bank, so return every day.
Example 3:

Input: security = [1,2,3,4,5,6], time = 2
Output: []
Explanation:
No day has 2 days before it that have a non-increasing number of guards.
Thus, no day is a good day to rob the bank, so return an empty list.
 

Constraints:

1 <= security.length <= 10^5
0 <= security[i], time <= 10^5


'''
from typing import List

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n, mx = len(security), 10**5+1
        inc, dec = [0]*(n+1), [0]*(n+1)
        arr = [0] + security + [mx]
        for i in range(1, n+2):            
            if arr[i] >= arr[i-1]:
                inc[i-1] = 1
        arr = [mx] + security + [0]
        for i in range(1, n+2):            
            if arr[i] <= arr[i-1]:
                dec[i-1] = 1
        #print(inc)
        #print(dec)
        preSumI, preSumD = [0]*(n+2), [0]*(n+2)
        for i in range(1, n+2):
            preSumI[i] = preSumI[i-1]+inc[i-1]
            preSumD[i] = preSumD[i-1]+dec[i-1]
        ans = []
        #print(preSumI)
        #print(preSumD)
        for i in range(n):
            if i-time >= 0 and i+time <= n-1:
         #       if i == 4:
         #           print(preSumI[i+time+1]-preSumI[i+1])
         #           print(preSumD[i+1]-preSumD[i-time+1])
                if preSumI[i+time+1]-preSumI[i+1] == preSumD[i+1]-preSumD[i-time+1] == time:
                    ans.append(i)
        
        return ans

    def goodDaysToRobBank2(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        arr = security
        preSumI, preSumD = [0]*(n), [0]*(n)
        for i in range(1, n):            
            if arr[i] >= arr[i-1]:
                preSumI[i] = preSumI[i-1]+1
            if arr[i] <= arr[i-1]:
                preSumD[i] = preSumD[i-1]+1
        ans = []
        for i in range(n):
            if i-time >= 0 and i+time <= n-1:
                if preSumI[i+time]-preSumI[i] == preSumD[i]-preSumD[i-time] == time:
                    ans.append(i)
        
        return ans
    
    def goodDaysToRobBank3(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        arr = security
        preSumI, preSumD = [0]*(n), [0]*(n)
        for i in range(1, n):     
            if arr[i] >= arr[i-1]:
                preSumI[i] = preSumI[i-1]+1                  
            
        ans = [0] if time == 0 else []
        for i in range(1, n):
            if arr[i] <= arr[i-1]:
                preSumD[i] = preSumD[i-1]+1            
            if i-time >= 0 and i+time <= n-1:
                if preSumI[i+time]-preSumI[i] == preSumD[i]-preSumD[i-time] == time:
                    ans.append(i)
        
        return ans
        
        
             

        

if __name__ == "__main__":
    print(Solution().goodDaysToRobBank(security = [5,3,3,3,5,6,2], time = 2))
    print(Solution().goodDaysToRobBank2(security = [5,3,3,3,5,6,2], time = 2))
    print(Solution().goodDaysToRobBank(security = [1,2,3,4,5,6], time = 2))
    print(Solution().goodDaysToRobBank2(security = [1,2,3,4,5,6], time = 2))