'''
-Medium-

You are given a 0-indexed array nums of distinct integers. You want to 
rearrange the elements in the array such that every element in the 
rearranged array is not equal to the average of its neighbors.

More formally, the rearranged array should have the property such that 
for every i in the range 1 <= i < nums.length - 1, 
(nums[i-1] + nums[i+1]) / 2 is not equal to nums[i].

Return any rearrangement of nums that meets the requirements.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: [1,2,4,5,3]
Explanation:
When i=1, nums[i] = 2, and the average of its neighbors is (1+4) / 2 = 2.5.
When i=2, nums[i] = 4, and the average of its neighbors is (2+5) / 2 = 3.5.
When i=3, nums[i] = 5, and the average of its neighbors is (4+3) / 2 = 3.5.
Example 2:

Input: nums = [6,2,0,9,7]
Output: [9,7,6,2,0]
Explanation:
When i=1, nums[i] = 7, and the average of its neighbors is (9+6) / 2 = 7.5.
When i=2, nums[i] = 6, and the average of its neighbors is (7+2) / 2 = 4.5.
When i=3, nums[i] = 2, and the average of its neighbors is (6+0) / 2 = 3.
 

Constraints:

3 <= nums.length <= 105
0 <= nums[i] <= 105

'''

from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        # print(len(nums))
        # print(nums)
        for i in range(1, len(nums)-1):
            if nums[i]*2 == nums[i-1] + nums[i+1]:
               nums[i-1], nums[i], nums[i+1] = nums[i+1], nums[i-1], nums[i]
        return nums

    def rearrangeArray2(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        med = nums[n//2] if n%2 == 1 else (nums[n//2-1]+nums[n//2])/2
        ans = [-1]*n
        i, j = 0, 1
        # print(med)
        # print(nums)
        for a in nums:
            # print(i,j,a,ans)
            if a >= med:
                ans[i] = a
                i += 2
            else:
                ans[j] = a
                j += 2 
        return ans

if __name__ == "__main__":
    print(Solution().rearrangeArray([1,2,3,4,5]))
    print(Solution().rearrangeArray([6,2,0,9,7]))
    print(Solution().rearrangeArray([3,1,12,10,7,6,17,14,4,13]))
    print(Solution().rearrangeArray([15,7,13,6,3,11,14,1,20]))
    print(Solution().rearrangeArray2([1,2,3,4,5]))
    print(Solution().rearrangeArray2([6,2,0,9,7]))
    print(Solution().rearrangeArray2([3,1,12,10,7,6,17,14,4,13]))
    print(Solution().rearrangeArray2([15,7,13,6,3,11,14,1,20]))
