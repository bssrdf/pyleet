'''

-Hard-
*DP*
*Bitmask*


You are given an integer array nums. We call a subset of nums good if its product 
can be represented as a product of one or more distinct prime numbers.

For example, if nums = [1, 2, 3, 4]:
[2, 3], [1, 2, 3], and [1, 3] are good subsets with products 6 = 2*3, 6 = 2*3, 
and 3 = 3 respectively.
[1, 4] and [4] are not good subsets with products 4 = 2*2 and 4 = 2*2 respectively.
Return the number of different good subsets in nums modulo 109 + 7.

A subset of nums is any array that can be obtained by deleting some (possibly none or all) 
elements from nums. Two subsets are different if and only if the chosen indices 
to delete are different.

 

Example 1:

Input: nums = [1,2,3,4]
Output: 6
Explanation: The good subsets are:
- [1,2]: product is 2, which is the product of distinct prime 2.
- [1,2,3]: product is 6, which is the product of distinct primes 2 and 3.
- [1,3]: product is 3, which is the product of distinct prime 3.
- [2]: product is 2, which is the product of distinct prime 2.
- [2,3]: product is 6, which is the product of distinct primes 2 and 3.
- [3]: product is 3, which is the product of distinct prime 3.
Example 2:

Input: nums = [4,2,3,15]
Output: 5
Explanation: The good subsets are:
- [2]: product is 2, which is the product of distinct prime 2.
- [2,3]: product is 6, which is the product of distinct primes 2 and 3.
- [2,15]: product is 30, which is the product of distinct primes 2, 3, and 5.
- [3]: product is 3, which is the product of distinct prime 3.
- [15]: product is 15, which is the product of distinct primes 3 and 5.
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 30

'''

from typing import List
from collections import Counter
from functools import lru_cache
import math

class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        arr, ones, mod  = [], 0, 10**9+7
        for i in nums:
            if i == 1: ones += 1
            else: arr.append(i)
        nums = arr 
        n = len(nums)        
        def primes_list(m):
            for i in range(2, int(math.sqrt(m))+1):
                if m % i == 0:
                    return primes_list(m//i) + [i]
            return [m]
        primes, num2prime = set(), [None for _ in range(31)]              
        for i in range(2, 31):
            ps = primes_list(i)
            num2prime[i] = ps
            primes |= set(ps)
        index = {v:i for i,v in enumerate(sorted(list(primes)))}
        m = len(primes)
        allmask = (1 << m) - 1 
        #print(m, primes, num2prime) 
        @lru_cache(None) 
        def dp(i, mask):
            if mask == allmask: return 1
            if i == n: return 0            
            ans = dp(i+1, mask) # not picking number i
            present = False
            newmask = mask
            for p in num2prime[nums[i]]:
                if newmask & (1 << index[p]) > 0: 
                    present = True
                    break                
                newmask |= 1 << index[p]
            if not present:
                ans += 1 + dp(i+1, newmask)
                ans %= mod
            return ans
        ans = dp(0, 0)
        #print(ans, ones)
        return (ones + 1)*ans
    
    def numberOfGoodSubsets2(self, nums: List[int]) -> int:
        M = 10**9 + 7
        P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        cnt = Counter(nums)
        bm = [sum(1<<i for i, p in enumerate(P) if x % p == 0) for x in range(31)]
        bad = set([4, 8, 9, 12, 16, 18, 20, 24, 25, 27, 28])
        M = 10**9 + 7
        
        @lru_cache(None)
        def dp(mask, num):
            if num == 1: return 1
            ans = dp(mask, num - 1)
            if num not in bad and mask | bm[num] == mask:
                ans += dp(mask ^ bm[num], num - 1) * cnt[num]
            return ans % M
        # - 1 is for  subtracting count of empty subset 1
        return ((dp(1023, 30) - 1) * pow(2, cnt[1], M)) % M

    def numberOfGoodSubsets3(self, nums: List[int]) -> int:
        M = 10**9 + 7
        P = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
        cnt = Counter(nums)
        bm = [sum(1<<i for i, p in enumerate(P) if x % p == 0) for x in range(31)]
        bad = set([4, 8, 9, 12, 16, 18, 20, 24, 25, 27, 28])
        M = 10**9 + 7
        
        @lru_cache(None)
        def dp(mask, num):
            if num == 1: return 1
            if mask == 1023: return 1
            ans = dp(mask, num - 1)
            if num not in bad and mask & bm[num] == 0:
                ans += dp(mask | bm[num], num - 1) * cnt[num]
            return ans % M

        return ((dp(0, 30) - 1) * pow(2, cnt[1], M)) % M
        

        
if __name__ == "__main__":
    print(Solution().numberOfGoodSubsets([1,2,3,4]))
    #print(Solution().numberOfGoodSubsets([2,3,4]))
    #print(Solution().numberOfGoodSubsets([4,2,3,15]))
    print(Solution().numberOfGoodSubsets([5,10,1,26,24,21,24,23,11,12,27,4,17,16,2,6,1,1,6,8,13,30,24,20,2,19]))
    print(Solution().numberOfGoodSubsets2([5,10,1,26,24,21,24,23,11,12,27,4,17,16,2,6,1,1,6,8,13,30,24,20,2,19]))
    print(Solution().numberOfGoodSubsets3([5,10,1,26,24,21,24,23,11,12,27,4,17,16,2,6,1,1,6,8,13,30,24,20,2,19]))