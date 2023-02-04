'''
-Hard-
You are given an integer array nums. In one operation, you can replace any element 
in nums with any integer.

nums is considered continuous if both of the following conditions are fulfilled:

All elements in nums are unique.
The difference between the maximum element and the minimum element in nums equals nums.length - 1.
For example, nums = [4, 2, 5, 3] is continuous, but nums = [1, 2, 3, 5, 6] is not continuous.

Return the minimum number of operations to make nums continuous.

 

Example 1:

Input: nums = [4,2,5,3]
Output: 0
Explanation: nums is already continuous.
Example 2:

Input: nums = [1,2,3,5,6]
Output: 1
Explanation: One possible solution is to change the last element to 4.
The resulting array is [1,2,3,5,4], which is continuous.
Example 3:

Input: nums = [1,10,100,1000]
Output: 3
Explanation: One possible solution is to:
- Change the second element to 2.
- Change the third element to 3.
- Change the fourth element to 4.
The resulting array is [1,2,3,4], which is continuous.
 

Constraints:

1 <= nums.length <= 10^5
1 <= nums[i] <= 10^9



'''
from typing import List
import bisect

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Store the original length, n = len(nums).
        # Firstly, make elements in nums unique and sort nums array.
        # Try elements in nums as the start of the continuous array, let say start.
        # Elements in the continuous array must in range [start, end], where end = start + n - 1.
        # Binary search to find the index of the right insert position of end in nums, let say idx.
        # Then we can calculate the number of unique numbers in range [start, end] by 
        # uniqueLen = n - idx.
        # The cost to make coninuous array is cost = n - uniqueLen.
        # We update the best answer so far, ans = min(ans, cost)
        # Then return the best ans we have.
        n = len(nums)
        nums = sorted(set(nums))  # Make `nums` as unique numbers and sort `nums`.

        ans = n
        for i, start in enumerate(nums):
            end = start + n - 1  # We expect elements of continuous array must in range [start..end]
            idx = bisect.bisect_right(nums, end)  # Find right insert position
            uniqueLen = idx - i
            ans = min(ans, n - uniqueLen)
            print(end, idx, i, uniqueLen, n-uniqueLen)
        return ans

if __name__ == "__main__":
    #print(Solution().minOperations([4,2,5,3]))
    print(Solution().minOperations([1,10,100,1000]))
        