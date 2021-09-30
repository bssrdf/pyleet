'''
-Medium-

The product sum of two equal-length arrays a and b is equal to the sum of a[i] * b[i] 
for all 0 <= i < a.length (0-indexed).

For example, if a = [1,2,3,4] and b = [5,2,3,1], the product sum would be 1*5 + 2*2 + 3*3 + 4*1 = 22.
Given two arrays nums1 and nums2 of length n, return the minimum product sum if you are 
allowed to rearrange the order of the elements in nums1.

Example 1:

Input: nums1 = [5,3,4,2], nums2 = [4,2,2,5]

Output: 40

Explanation: We can rearrange nums1 to become [3,5,4,2]. The product sum of [3,5,4,2] and [4,2,2,5] is 34 + 52 + 42 + 25 = 40.

Example 2:

Input: nums1 = [2,1,4,5,7], nums2 = [3,2,4,8,6]

Output: 65

Explanation: We can rearrange nums1 to become [5,7,4,1,2]. The product sum of [5,7,4,1,2] and [3,2,4,8,6] is 53 + 72 + 44 + 18 + 2*6 = 65.

Constraints:

n == nums1.length == nums2.length
1 <= n <= 10^5
1 <= nums1[i], nums2[i] <= 100

'''

from typing import List

class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort(reverse = True)
        nums2.sort()
        return sum(a*b for a,b in zip(nums1, nums2))



if __name__ == "__main__":
    print(Solution().minProductSum(nums1 = [5,3,4,2], nums2 = [4,2,2,5]))
    print(Solution().minProductSum(nums1 = [2,1,4,5,7], nums2 = [3,2,4,8,6]))