'''
-Medium-
$$$
*DP*



You are given an integer array nums.

Splitting of an integer array nums into subarrays is valid if:

the greatest common divisor of the first and last elements of each subarray is greater than 1, and
each element of nums belongs to exactly one subarray.
Return the minimum number of subarrays in valid subarray splitting of nums.

Note that:

The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
A subarray is a contiguous part of an array.
 

Example 1:

Input: nums = [2,6,3,4,3]
Output: 2
Explanation: We can create a valid split in the following way: [2,6] | [3,4,3].
- The starting element of the 1st subarray is 2 and the ending is 6. Their greatest common divisor is 2, which is greater than 1.
- The starting element of the 2nd subarray is 3 and the ending is 3. Their greatest common divisor is 3, which is greater than 1.
It can be proved that 2 is the minimum number of subarrays that we can obtain in a valid split.
Example 2:

Input: nums = [3,5]
Output: 2
Explanation: We can create a valid split in the following way: [3] | [5].
- The starting element of the 1st subarray is 3 and the ending is 3. Their greatest common divisor is 3, which is greater than 1.
- The starting element of the 2nd subarray is 5 and the ending is 5. Their greatest common divisor is 5, which is greater than 1.
It can be proved that 2 is the minimum number of subarrays that we can obtain in a valid split.
Example 3:

Input: nums = [1,2,1]
Output: -1
Explanation: It is impossible to create valid split.
 

Constraints:

1 <= nums.length <= 1000
1 <= nums[i] <= 105


'''

from typing import List
import math
from math import gcd
from functools import lru_cache
import sys
sys.setrecursionlimit(5000)

class Solution:
    def validSubarraySplit(self, nums: List[int]) -> int:
        n = len(nums)
        inf = float('inf')
        @lru_cache(None)
        def dp(i):
            if i == n: return 0 
            ret = inf
            for j in range(i, n):
                if gcd(nums[i], nums[j]) > 1:
                    ret = min(ret, dp(j+1)+1)
            return ret 
        ans = dp(0)
        return ans if ans != inf else -1 
    
    
    
    def validSubarraySplit2(self, nums: List[int]) -> int:
        @lru_cache(None)
        def dfs(i):
            if i >= n:
                return 0
            ans = math.inf
            for j in range(i, n):
                if gcd(nums[i], nums[j]) > 1:
                    ans = min(ans, 1 + dfs(j + 1))
            return ans

        n = len(nums)
        ans = dfs(0)
        dfs.cache_clear()
        return ans if ans < math.inf else -1
                    


from random import randint

if __name__ == "__main__":   
    print(Solution().validSubarraySplit(nums = [2,6,3,4,3]))
    print(Solution().validSubarraySplit(nums = [3,5]))
    print(Solution().validSubarraySplit(nums = [1,2,1]))
    N = 10**5
    n = 800
    nums = [randint(1,N) for _ in range(n)]
    print(nums)
    print(Solution().validSubarraySplit(nums = nums))
    print(Solution().validSubarraySplit2(nums = nums))

