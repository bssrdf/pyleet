'''

-Hard-

*DP*
*Bitmask*

You are given an array of n integers, nums, where there are at most 50 unique 
values in the array. You are also given an array of m customer order 
quantities, quantity, where quantity[i] is the amount of integers the ith 
customer ordered. Determine if it is possible to distribute nums such that:

The ith customer gets exactly quantity[i] integers,
The integers the ith customer gets are all equal, and
Every customer is satisfied.
Return true if it is possible to distribute nums according to the above conditions.

 

Example 1:

Input: nums = [1,2,3,4], quantity = [2]
Output: false
Explanation: The 0th customer cannot be given two different integers.
Example 2:

Input: nums = [1,2,3,3], quantity = [2]
Output: true
Explanation: The 0th customer is given [3,3]. The integers [1,2] are not used.
Example 3:

Input: nums = [1,1,2,2], quantity = [2,2]
Output: true
Explanation: The 0th customer is given [1,1], and the 1st customer is given [2,2].
 

Constraints:

n == nums.length
1 <= n <= 105
1 <= nums[i] <= 1000
m == quantity.length
1 <= m <= 10
1 <= quantity[i] <= 105
There are at most 50 unique values in nums.


'''

from typing import List
from collections import Counter
from functools import lru_cache

from numpy import True_
class Solution:
    def canDistribute(self, nums: List[int], quantity: List[int]) -> bool:
        q = sorted(quantity, reverse=True)
        freq = list(Counter(nums).values())
        freq.sort(reverse=True)
        n, m = len(freq), len(q)
       # print(freq, q)
        subsetSum = [0]*(1<<m)
        @lru_cache(None)
        def dp(i, avail):
            if avail == 0: return True
            if i == n: return False
            mask = avail
            while mask:
                sm = subsetSum[mask]
                if sm == 0:
                    j = 0
                    while 1<<j <= mask:
                        if mask & (1<<j) > 0:
                            sm += q[j]
                        j += 1
                    subsetSum[mask] = sm
                if sm <= freq[i] and dp(i+1, avail ^ mask):
                    return True
                mask = (mask-1) & avail
            return False
        return dp(0, (1<<m)-1)



if __name__ == "__main__":
    print(Solution().canDistribute(nums = [1,2,3,4], quantity = [2]))
    print(Solution().canDistribute(nums = [1,2,3,3], quantity = [2]))