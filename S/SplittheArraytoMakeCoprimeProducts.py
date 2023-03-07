'''

-Hard-

You are given a 0-indexed integer array nums of length n.

A split at an index i where 0 <= i <= n - 2 is called valid if the product of the first i + 1 elements and the product of the remaining elements are coprime.

For example, if nums = [2, 3, 3], then a split at the index i = 0 is valid because 2 and 9 are coprime, while a split at the index i = 1 is not valid because 6 and 3 are not coprime. A split at the index i = 2 is not valid because i == n - 1.
Return the smallest index i at which the array can be split validly or -1 if there is no such split.

Two values val1 and val2 are coprime if gcd(val1, val2) == 1 where gcd(val1, val2) is the greatest common divisor of val1 and val2.

 

Example 1:


Input: nums = [4,7,8,15,3,5]
Output: 2
Explanation: The table above shows the values of the product of the first i + 1 elements, the remaining elements, and their gcd at each index i.
The only valid split is at index 2.
Example 2:


Input: nums = [4,7,15,8,3,5]
Output: -1
Explanation: The table above shows the values of the product of the first i + 1 elements, the remaining elements, and their gcd at each index i.
There is no valid split.
 

Constraints:

n == nums.length
1 <= n <= 104
1 <= nums[i] <= 106


'''

from typing import List
from collections import Counter
import math

def primes_set(m):
    if m == 1: return set()
    for i in range(2, int(math.sqrt(m))+1):
        if m % i == 0:
            return primes_set(m//i) | set([i])
    return set([m])

def sieve(n):
    A = [i for i in range(n+1)]
    A[1] = 0
    for p in range(2, math.floor(math.sqrt(n))+1):
        if A[p]:
            j = p*p
            while j <= n:
                A[j] = 0
                j += p
    L = []
    for p in range(2, n+1):
        if A[p]:
            L.append(A[p])
    return L

class Solution:
    def findValidSplit(self, nums: List[int]) -> int:
        n = len(nums)        
        dp = Counter()
        for i in range(n-1, 0, -1):
            for p in primes_set(nums[i]):
                dp[p] += 1
        pm = primes_set(nums[0])
        cop = True
        pm2 = set()
        # print(pm, dp)
        for p in pm:
            if p in dp:
                cop = False
                pm2.add(p)
        if cop: return 0
        pm = pm2
        for i in range(1, n-1):
            for p in primes_set(nums[i]):
                dp[p] -= 1
                if dp[p] == 0:
                    dp.pop(p)
                else:
                    pm.add(p)    
            # print(pm, dp)
            cop = True        
            for p in pm:
                if p in dp:
                    cop = False
                    break
            if cop: return i
        return -1
        
            


if __name__ == '__main__':
    print(Solution().findValidSplit(nums = [4,7,8,15,3,5]))
    print(Solution().findValidSplit(nums = [1,1,89]))

