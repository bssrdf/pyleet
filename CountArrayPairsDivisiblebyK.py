'''
-Hard-
*GCD*
*Hash Table*

Given a 0-indexed integer array nums of length n and an integer k, return the number of pairs (i, j) such that:

0 <= i < j <= n - 1 and
nums[i] * nums[j] is divisible by k.
 

Example 1:

Input: nums = [1,2,3,4,5], k = 2
Output: 7
Explanation: 
The 7 pairs of indices whose corresponding products are divisible by 2 are
(0, 1), (0, 3), (1, 2), (1, 3), (1, 4), (2, 3), and (3, 4).
Their products are 2, 4, 6, 8, 10, 12, and 20 respectively.
Other pairs such as (0, 2) and (2, 4) have products 3 and 15 respectively, which are not divisible by 2.    
Example 2:

Input: nums = [1,2,3,4], k = 5
Output: 0
Explanation: There does not exist any pair of indices whose corresponding product is divisible by 5.
 

Constraints:

1 <= nums.length <= 105
1 <= nums[i], k <= 105

'''
import math
from typing import List
from collections import Counter
class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        # Wrong
        ans, m, n = 0, 0, len(nums)
        for i, a in enumerate(nums):
            if a % k == 0:
                ans += n - i - 1 + m
            else:
                m += 1
        return ans
    
    def countPairs2(self, nums: List[int], k: int) -> int:
        ans, gcds = 0, {}
        for a in nums:
            gcd_i = math.gcd(a, k)
            for gcd_j, cnt in gcds.items():
                if gcd_i*gcd_j % k == 0:
                    ans += cnt
            gcds[gcd_i] = gcds.get(gcd_i, 0) + 1
        return ans    
        


        
        

if __name__ == "__main__":
    print(Solution().countPairs(nums = [1,2,3,4,5], k = 2))
    print(Solution().countPairs(nums = [1,2,3,4], k = 5))
    print(Solution().countPairs2(nums = [8,10,2,5,9,6,3,8,2], k = 6))