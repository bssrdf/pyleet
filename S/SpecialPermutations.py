'''
-Medium-
*Bitmask*
*DP*
*Memoization*

You are given a 0-indexed integer array nums containing n distinct positive integers. A permutation of nums is called special if:

For all indexes 0 <= i < n - 1, either nums[i] % nums[i+1] == 0 or nums[i+1] % nums[i] == 0.
Return the total number of special permutations. As the answer could be large, return it modulo 109 + 7.

 

Example 1:

Input: nums = [2,3,6]
Output: 2
Explanation: [3,6,2] and [2,6,3] are the two special permutations of nums.
Example 2:

Input: nums = [1,4,3]
Output: 2
Explanation: [3,1,4] and [4,1,3] are the two special permutations of nums.
 

Constraints:

2 <= nums.length <= 14
1 <= nums[i] <= 109


'''
from typing import List
from functools import lru_cache
class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        @lru_cache(None)
        def dfs(i, j, mask):
            if i == n: return 1            
            ret = 0
            for k in range(n):
                if mask & (1 << k) == 0:
                    if j == -1 or (nums[k] % nums[j] == 0 or nums[j] % nums[k] == 0):
                        ret = (ret + dfs(i+1, k, mask | (1 << k)) ) % MOD 
            return ret 
        return dfs(0, -1, 0)           
    
    def specialPerm2(self, nums: List[int]) -> int:
        n = len(nums)
        MOD = 10**9 + 7
        all1 = (1 << n) - 1
        @lru_cache(None)
        def dfs(j, mask):
            if mask == all1: return 1            
            ret = 0
            for k in range(n):
                if mask & (1 << k) == 0:
                    if j == -1 or (nums[k] % nums[j] == 0 or nums[j] % nums[k] == 0):
                        ret = (ret + dfs(k, mask | (1 << k)) ) % MOD 
            return ret 
        return dfs(-1, 0)           


if __name__ == "__main__":
    print(Solution().specialPerm(nums = [2,3,6]))        
    print(Solution().specialPerm(nums = [1,4,3]))        
    print(Solution().specialPerm2(nums = [2,3,6]))        
    print(Solution().specialPerm2(nums = [1,4,3]))        