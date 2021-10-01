'''

-Hard-

Given an integer array nums and an integer k, return the number of good subarrays of nums.

A good array is an array where the number of different integers in that array is exactly k.

For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [1,2,1,2,3], k = 2
Output: 7
Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]
Example 2:

Input: nums = [1,2,1,3,4], k = 3
Output: 3
Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
 

Constraints:

1 <= nums.length <= 2 * 10^4
1 <= nums[i], k <= nums.length


'''

from typing import List
from collections import defaultdict

class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        n = len(nums)
        def helper(m): # number of subarrays with at most m distinct numbers
            left, right, ans = 0, 0, 0
            htbl = defaultdict(int)
            while right < n:              
                htbl[nums[right]] += 1
                right += 1
                while len(htbl) > m:
                    htbl[nums[left]] -= 1
                    if htbl[nums[left]] == 0:
                        htbl.pop(nums[left])
                    left += 1
                ans += right - left
            return ans
        # the answer is 
        # number of subarrays with at most k   distinct numbers    
        #                 -
        # number of subarrays with at most (k-1) distinct numbers       
        return helper(k) - helper(k-1) 

        

if __name__ == "__main__":
    print(Solution().subarraysWithKDistinct(nums = [1,2,1,2,3], k = 2))
    print(Solution().subarraysWithKDistinct([1,2,1,3,4], k = 3))