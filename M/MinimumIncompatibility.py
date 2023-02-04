'''
-Hard-

You are given an integer array nums​​​ and an integer k. You are asked to distribute 
this array into k subsets of equal size such that there are no two equal elements 
in the same subset.

A subset's incompatibility is the difference between the maximum and minimum 
elements in that array.

Return the minimum possible sum of incompatibilities of the k subsets after 
distributing the array optimally, or return -1 if it is not possible.

A subset is a group integers that appear in the array with no particular order.

 

Example 1:

Input: nums = [1,2,1,4], k = 2
Output: 4
Explanation: The optimal distribution of subsets is [1,2] and [1,4].
The incompatibility is (2-1) + (4-1) = 4.
Note that [1,1] and [2,4] would result in a smaller sum, but the first subset contains 2 equal elements.
Example 2:

Input: nums = [6,3,8,1,3,1,2,2], k = 4
Output: 6
Explanation: The optimal distribution of subsets is [1,2], [2,3], [6,8], and [1,3].
The incompatibility is (2-1) + (3-2) + (8-6) + (3-1) = 6.
Example 3:

Input: nums = [5,3,3,6,3,3], k = 3
Output: -1
Explanation: It is impossible to distribute nums into 3 subsets where no two elements are equal in the same subset.
 

Constraints:

1 <= k <= nums.length <= 16
nums.length is divisible by k
1 <= nums[i] <= nums.length

'''

from typing import List
from collections import Counter
from functools import lru_cache
from itertools import combinations

class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:        
        d=len(nums)//k # the length of each partition
        
        @lru_cache(None)
        def helper(nums):
            if not nums:
                return 0
            ret=10**15
            for a in combinations(nums,d): # choose a as a partition
                if len(set(a))<d: # check for duplicates
                    continue
                left=list(nums) # numbers left after removing partition a
                for v in a:
                    left.remove(v)
                ret=min(ret,max(a)-min(a)+helper(tuple(left)))
            return ret
        
        ans=helper(tuple(nums)) # turn the input into a tuple so the function can be cached
        return ans if ans!=10**15 else -1

    def minimumIncompatibility1(self, nums: List[int], k: int) -> int:
        groupSize = len(nums) // k
        @lru_cache(None)
        def helper(bitmask): # return minimal sum of incompatibilities achievable with unselected indices.
            if bitmask == 0:
                return 0
            else:
                optimal = float('inf')
                remaining = [i for i in range(len(nums)) if bitmask & (1 << i)]
                comb = combinations(remaining,groupSize) 
                for combo in list(comb): 
                    comboElems = [nums[-elem-1] for elem in combo]
                    if len(set(comboElems)) != groupSize:
                        continue
                    else:
                        newBitmask = bitmask
                        for idx in combo:
                            newBitmask ^= 1 << idx
                        incompat = max(comboElems)-min(comboElems)
                        optimal = min(optimal,incompat+helper(newBitmask))
                    
                return optimal
            
        result = helper(2**len(nums)-1)
        if result == float('inf'):
            return -1
        else:
            return result

       

    def minimumIncompatibility2(self, nums: List[int], k: int) -> int:        
        n = len(nums)
        m = n // k
        count = Counter(nums)
        for i in count:
            if count[i] > k: return -1
        if m == 1: return 0
        if k == 1: return max(nums) - min(nums)
        def count(mask):            
            return bin(mask).count('1')
        def icom(mask):
            mi, mx = -1, -1
            for i in range(n):
                if mask & (1<<i) > 0:
                    if mi == -1: mi = i
                    elif mx == -1: mx = i
            #print('icom:', mx-mi, mx, mi, bin(mask))
            return mx - mi
        @lru_cache(None)
        def dp(g, mask, gmask):
            if g == k: 
                #rint('x')
                return 0
            ans = float('inf')
            if count(gmask) == m:
                ans = min(ans, icom(gmask)+dp(g+1, mask, 0))
                #print('d', bin(mask), g, ans)
                return ans
            else:
                for i in range(n):
                    if mask & (1 << i) == 0 and gmask & (1<<(nums[i]-1)) == 0:
                        ans = min(ans, dp(g, mask|(1 << i), gmask|(1<<(nums[i]-1))))    
                 #   if g == 0 and mask == 0 and gmask == 0:
                 #       print('a', i, ans)
                return ans 
        return dp(0, 0, 0)     

    def minimumIncompatibility3(self, nums: List[int], k: int) -> int:        
        n = len(nums)
        m = n // k
        count = Counter(nums)
        for i in count:
            if count[i] > k: return -1
        if m == 1: return 0
        if k == 1: return max(nums) - min(nums)
        def count(mask):            
            return bin(mask).count('1')
        def icom(c,mask):
            mi, mx = -1, -1
            for i in range(n):
                if mask & (1<<i) > 0:
                    if mi == -1: mi = i
                    elif mx == -1: mx = i
            print('icom:', c, mx-mi, mx, mi, bin(mask))
            return mx - mi
        @lru_cache(None)
        def dp(mask, gmask):
            if mask == (1<<n)-1:
               # print('x', bin(mask))
                if count(gmask) == m: 
                   return icom('x', gmask)
                return float('inf')
            ans = float('inf')
            ic = 0
            if count(gmask) == m:
                #ans = min(ans, icom(gmask)+dp(mask, 0))
                ic = icom('a',gmask)
                gmask = 0
                # print('d', bin(mask), ans)
                # return ans
            #else:
            for i in range(n):
                if mask & (1 << i) == 0 and gmask & (1<<(nums[i]-1)) == 0:
                    ans = min(ans, dp(mask|(1 << i), gmask|(1<<(nums[i]-1))))    
                #   if g == 0 and mask == 0 and gmask == 0:
                #       print('a', i, ans)
            return ans + ic
        return dp(0, 0)     
         
        

if __name__ == "__main__":
    # print(Solution().minimumIncompatibility2(nums = [1,2,1,4], k = 2))
    # print(Solution().minimumIncompatibility3(nums = [1,2,1,4], k = 2))
    # print(Solution().minimumIncompatibility2(nums = [6,3,8,1,3,1,2,2], k = 4))
    # print(Solution().minimumIncompatibility3(nums = [6,3,8,1,3,1,2,2], k = 4))
    # print(Solution().minimumIncompatibility2(nums = [5,3,3,6,3,3], k = 3))
    # print(Solution().minimumIncompatibility3(nums = [5,3,3,6,3,3], k = 3))
    # print(Solution().minimumIncompatibility2(nums = [1,1], k = 1))    
    #print(Solution().minimumIncompatibility2(nums = [1,2], k = 2))
    #print(Solution().minimumIncompatibility2(nums = [1,2], k = 2))
    # print(Solution().minimumIncompatibility2(nums = [10,4,4,2,11,10,8,9,1,2,2,10], k=4))
    print(Solution().minimumIncompatibility3(nums = [10,4,4,2,11,10,8,9,1,2,2,10], k=4))

