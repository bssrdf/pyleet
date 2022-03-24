'''

-Hard-

We have n buildings numbered from 0 to n - 1. Each building has a number 
of employees. It's transfer season, and some employees want to change 
the building they reside in.

You are given an array requests where requests[i] = [fromi, toi] 
represents an employee's request to transfer from building fromi to 
building toi.

All buildings are full, so a list of requests is achievable only if 
for each building, the net change in employee transfers is zero. 
This means the number of employees leaving is equal to the number 
of employees moving in. For example if n = 3 and two employees are 
leaving building 0, one is leaving building 1, and one is leaving 
building 2, there should be two employees moving to building 0, 
one employee moving to building 1, and one employee moving to building 2.

Return the maximum number of achievable requests.

 

Example 1:


Input: n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]
Output: 5
Explantion: Let's see the requests:
From building 0 we have employees x and y and both want to move to building 1.
From building 1 we have employees a and b and they want to move to buildings 2 and 0 respectively.
From building 2 we have employee z and they want to move to building 0.
From building 3 we have employee c and they want to move to building 4.
From building 4 we don't have any requests.
We can achieve the requests of users x and b by swapping their places.
We can achieve the requests of users y, a and z by swapping the places in the 3 buildings.
Example 2:


Input: n = 3, requests = [[0,0],[1,2],[2,1]]
Output: 3
Explantion: Let's see the requests:
From building 0 we have employee x and they want to stay in the same building 0.
From building 1 we have employee y and they want to move to building 2.
From building 2 we have employee z and they want to move to building 1.
We can achieve all the requests. 
Example 3:

Input: n = 4, requests = [[0,3],[3,1],[1,2],[2,0]]
Output: 4
 

Constraints:

1 <= n <= 20
1 <= requests.length <= 16
requests[i].length == 2
0 <= fromi, toi < n

'''

from collections import defaultdict

from typing import List


class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        m, r = len(requests), requests
        ans = 0
        for mask in range(1<<m):
            arr = [0]*n
            for i in range(m):
                if mask & (1 << i) > 0:
                   # bits += 1
                    arr[r[i][0]] -= 1
                    arr[r[i][1]] += 1
             #   if bin(mask).count('1') == 6:
             #       print(arr)    
            #if bin(mask).count('1') == 6:
            #    print(arr, bin(mask))
            if any(arr): continue       
            ans = max(ans, bin(mask).count('1') )
        return ans

    def maximumRequests2(self, n: int, requests: List[List[int]]) -> int:
        m, r = len(requests), requests
        ans = 0
        for mask in range(1<<m):
            ind = [0]*n
            outd = [0]*n
            for i in range(m):
                if mask & (1 << i) > 0:
                    ind[r[i][0]] += 1
                    outd[r[i][1]] += 1
            ans = max(ans, sum(outd) if ind == outd else 0)
        return ans

if __name__ == "__main__":
    print(Solution().maximumRequests(n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]))
    print(Solution().maximumRequests(n = 3, requests = [[0,0],[1,2],[2,1]]))
    print(Solution().maximumRequests(n = 4, requests = [[0,3],[3,1],[1,2],[2,0]]))
    print(Solution().maximumRequests2(n = 5, requests = [[0,1],[1,0],[0,1],[1,2],[2,0],[3,4]]))
    print(Solution().maximumRequests2(n = 3, requests = [[0,0],[1,2],[2,1]]))
    print(Solution().maximumRequests2(n = 4, requests = [[0,3],[3,1],[1,2],[2,0]]))
    n = 20
    requests = [[0,0],[3,7],[4,4],[4,4],[4,14],[6,4],[7,11],[7,18],[8,3],[9,3],[10,6],[11,7],[12,4],[14,12],[18,6],[18,8]]
    print(Solution().maximumRequests(n, requests))
    print(Solution().maximumRequests2(n, requests))
