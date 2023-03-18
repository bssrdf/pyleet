'''

-Medium-
*Binary Search*
*torting*


You are given a 0-indexed integer array nums. You are allowed to permute nums into a new array perm of your choosing.

We define the greatness of nums be the number of indices 0 <= i < nums.length for which perm[i] > nums[i].

Return the maximum possible greatness you can achieve after permuting nums.

 

Example 1:

Input: nums = [1,3,5,2,1,3,1]
Output: 4
Explanation: One of the optimal rearrangements is perm = [2,5,1,3,3,1,1].
At indices = 0, 1, 3, and 4, perm[i] > nums[i]. Hence, we return 4.
Example 2:

Input: nums = [1,2,3,4]
Output: 3
Explanation: We can prove the optimal perm is [2,3,4,1].
At indices = 0, 1, and 2, perm[i] > nums[i]. Hence, we return 3.
 

Constraints:

1 <= nums.length <= 105
0 <= nums[i] <= 109




'''

from typing import List
from collections import defaultdict

class Solution:
    def maximizeGreatness(self, nums: List[int]) -> int:
        n = len(nums)
        A = sorted(nums)
        l, r = 0, n 
        def possible(m):
            a = A[:m]
            b = A[-m:]
            for x,y in zip(a,b):
                if x >= y: return False 
            return True
        while l < r:
            mid = l + (r-l)//2
            if possible(mid):
                l = mid+1
            else:
                r = mid 
        return l-1



if __name__ == '__main__':
    print(Solution().maximizeGreatness(nums = [1,3,5,2,1,3,1]))
    print(Solution().maximizeGreatness(nums = [1,2,3,4]))
        