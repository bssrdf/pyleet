'''
-Medium-
*Binary Search*

You are given a sorted array consisting of only integers where every 
element appears exactly twice, except for one element which appears exactly once.

Return the single element that appears only once.

Your solution must run in O(log n) time and O(1) space.

 

Example 1:

Input: nums = [1,1,2,3,3,4,4,8,8]
Output: 2
Example 2:

Input: nums = [3,3,7,7,10,11,11]
Output: 10
 

Constraints:

1 <= nums.length <= 10^5
0 <= nums[i] <= 10^5


'''
from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] == nums[mid+1]:
                if (n-1-mid)%2 == 1: r = mid
                else: l = mid + 1
            else:
                if mid == 0 or nums[mid] != nums[mid-1]:
                    return nums[mid]
                if (n-1-mid)%2 == 0: r = mid
                else: l = mid + 1
        return nums[l]

    def singleNonDuplicate2(self, nums: List[int]) -> int:
        n = len(nums)
        l, r = 0, n-1
        while l < r:
            mid = l + (r-l)//2
            if nums[mid] == nums[mid^1]:                
                l = mid + 1
            else:
                r = mid
        return nums[l]
            

if __name__ == "__main__":
    print(Solution().singleNonDuplicate(nums = [1,1,2,3,3,4,4,8,8]))
    print(Solution().singleNonDuplicate(nums = [3,3,7,7,10,11,11]))
    print(Solution().singleNonDuplicate2(nums = [1,1,2,3,3,4,4,8,8]))
    print(Solution().singleNonDuplicate2(nums = [3,3,7,7,10,11,11]))
        