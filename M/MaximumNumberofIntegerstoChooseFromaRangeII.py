'''
-Medium-
$$$
*Greedy*
*Sorting*
*Binary Search*

You are given an integer array banned and two integers n and maxSum. You are choosing some number of integers following the below rules:

The chosen integers have to be in the range [1, n].
Each integer can be chosen at most once.
The chosen integers should not be in the array banned.
The sum of the chosen integers should not exceed maxSum.
Return the maximum number of integers you can choose following the mentioned rules.

 
Example 1:

Input: banned = [1,4,6], n = 6, maxSum = 4
Output: 1
Explanation: You can choose the integer 2 and 3.
2 and 3 are are in the range [1, 6], both do not appear in banned, and their sum is 5, which does not exceed maxSum.
Example 2:

Input: banned = [4,3,5,6], n = 7, maxSum = 18
Output: 3
Explanation: You can choose the integers 1, 2, 3 and 7.
All these integers are in the range [1, 7], all do not appear in banned, and their sum is 13, which does not exceed maxSum.
 

 

Constraints:

1 <= banned.length <= 10^5
1 <= banned[i] <= n <= 10^9
1 <= maxSum <= 10^15


'''

from typing import List
from itertools import pairwise
class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        # TLE
        A = sorted(banned) + [n+1]
        t, ans = 0, 0
        s = 1
        for i in range(len(A)):
            e = A[i]-1
            if s <= e:
                x = (s+e)*(e-s+1)//2
                if t + x <= maxSum: 
                    t += x
                    ans += e-s+1  
                else:
                    l = s
                    while l <= e and t + l <= maxSum:
                        t += l
                        l += 1
                        ans += 1
            s = A[i]+1
        return ans    
    
    def maxCount3(self, banned: List[int], n: int, maxSum: int) -> int:
        A = sorted(set(banned)) + [n+1]
        t, ans = 0, 0
        s = 1
        for i in range(len(A)):
            e = A[i]-1
            if s <= e:
                x = (s+e)*(e-s+1)//2
                if t + x <= maxSum: 
                    t += x
                    ans += e-s+1  
                else:
                    l, r = s, e+1
                    while l < r:
                        mid = l + (r-l)//2
                        if t + (mid+s)*(mid-s+1)//2 <= maxSum:
                            l = mid + 1 
                        else:
                            r = mid
                    ans += l - s # the number one can choose is from s to l-1 hence l-1-s+1 = l-s
                    t += (l-1+s)*(l-s)//2
            s = A[i]+1
        return ans    

    
    def maxCount2(self, banned: List[int], n: int, maxSum: int) -> int:
        banned.extend([0, n + 1])
        ban = sorted(set(banned))
        ans = 0
        for i, j in pairwise(ban):
            left, right = 0, j - i - 1
            while left < right:
                mid = (left + right + 1) >> 1
                if (i + 1 + i + mid) * mid // 2 <= maxSum:
                    left = mid
                else:
                    right = mid - 1
            ans += left
            maxSum -= (i + 1 + i + left) * left // 2
            if maxSum <= 0:
                break
        return ans

from random import randint
import time
if __name__ == '__main__':
    print(Solution().maxCount(banned = [1,4,6], n = 6, maxSum = 4))
    print(Solution().maxCount(banned = [4,3,5,6], n = 7, maxSum = 18))
    print(Solution().maxCount3(banned = [4,3,5,6], n = 7, maxSum = 18))
    # print(Solution().maxCount(banned = [4,10**8,5,6], n = 10**9, maxSum = 10**13))
    print(Solution().maxCount3(banned = [4,10**8,5,6], n = 10**9, maxSum = 10**13))
    print(Solution().maxCount2(banned = [4,10**8,5,6], n = 10**9, maxSum = 10**13))
    for _ in range(1000):
        N, n = 10**5, 10**8
        maxSum = randint(1, 10**15)
        banned = [randint(1, n) for _ in range(N)]
        starttime = time.time()        
        sol1 = Solution().maxCount3(banned = banned, n = n, maxSum = maxSum)
        endtime = time.time()
        t1 =  endtime-starttime
        starttime = time.time()        
        sol2 = Solution().maxCount2(banned = banned, n = n, maxSum = maxSum)
        endtime = time.time()
        t2 =  endtime-starttime
        if sol1 != sol2:
            print('Error')
            break
        print('Elapsed ', t1, t2, sol1, sol2)


