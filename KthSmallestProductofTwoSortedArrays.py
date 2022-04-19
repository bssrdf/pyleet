'''

-Hard-
*Binary Search*


Given two sorted 0-indexed integer arrays nums1 and nums2 as well as an integer k, 
return the kth (1-based) smallest product of nums1[i] * nums2[j] 
where 0 <= i < nums1.length and 0 <= j < nums2.length.
 

Example 1:

Input: nums1 = [2,5], nums2 = [3,4], k = 2
Output: 8
Explanation: The 2 smallest products are:
- nums1[0] * nums2[0] = 2 * 3 = 6
- nums1[0] * nums2[1] = 2 * 4 = 8
The 2nd smallest product is 8.
Example 2:

Input: nums1 = [-4,-2,0,3], nums2 = [2,4], k = 6
Output: 0
Explanation: The 6 smallest products are:
- nums1[0] * nums2[1] = (-4) * 4 = -16
- nums1[0] * nums2[0] = (-4) * 2 = -8
- nums1[1] * nums2[1] = (-2) * 4 = -8
- nums1[1] * nums2[0] = (-2) * 2 = -4
- nums1[2] * nums2[0] = 0 * 2 = 0
- nums1[2] * nums2[1] = 0 * 4 = 0
The 6th smallest product is 0.
Example 3:

Input: nums1 = [-2,-1,0,1,2], nums2 = [-3,-1,2,4,5], k = 3
Output: -6
Explanation: The 3 smallest products are:
- nums1[0] * nums2[4] = (-2) * 5 = -10
- nums1[0] * nums2[3] = (-2) * 4 = -8
- nums1[4] * nums2[0] = 2 * (-3) = -6
The 3rd smallest product is -6.
 

Constraints:

1 <= nums1.length, nums2.length <= 5 * 104
-105 <= nums1[i], nums2[j] <= 105
1 <= k <= nums1.length * nums2.length
nums1 and nums2 are sorted.


'''

from typing import List

from bisect import bisect_right, bisect_left
from math import ceil

class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        # The idea of this problem is to use binary search: let check(x) be the answer 
        # to the question: how many products are less or equal than x. Then we use binary 
        # search and find the first moment where we have exactly k such numbers.
        def check(x):
            total = 0
            for n1 in nums1:
                # If n1 is positive, then values in nums2 * n1 go in increasing order, so we 
                # use bisect to find number of values which are <= x//n1.
                if n1 > 0: total += bisect_right(nums2, x//n1)
                # If n1 is negative, then values in nums2 * n1 going in decreasing order, so we 
                # need to take the right part.
                if n1 < 0: total += len(nums2) - bisect_left(nums2, ceil(x/n1))
                # If n1 equal to 0, than all values in nums2 * n1 are equal to 0. So, we update 
                # total only if x >= 0.
                if n1 == 0 and x >= 0: total += len(nums2)

            return total

        left, right = -10**10 - 1, 10**10 + 1
        
        while left < right:
            mid = left + (right - left)//2
            if check(mid) >= k:
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    print(Solution().kthSmallestProduct(nums1 = [2,5], nums2 = [3,4], k = 2))
    print(Solution().kthSmallestProduct(nums1 = [-4,-2,0,3], nums2 = [2,4], k = 6))
    print(Solution().kthSmallestProduct(nums1 = [-2,-1,0,1,2], nums2 = [-3,-1,2,4,5], k = 3))

        