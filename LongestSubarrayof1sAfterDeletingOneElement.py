'''
-Medium-

Given a binary array nums, you should delete one element from it.

Return the size of the longest non-empty subarray containing only 1's 
in the resulting array. Return 0 if there is no such subarray.

 

Example 1:

Input: nums = [1,1,0,1]
Output: 3
Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
Example 2:

Input: nums = [0,1,1,1,0,1,1,0,1]
Output: 5
Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
Example 3:

Input: nums = [1,1,1]
Output: 2
Explanation: You must delete one element.
Example 4:

Input: nums = [1,1,0,0,1,1,1,0,1]
Output: 4
Example 5:

Input: nums = [0,0,0]
Output: 0
 

Constraints:

1 <= nums.length <= 10^5
nums[i] is either 0 or 1.

'''

from typing import List

class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        n = len(nums)
        left, right = 0, 0
        zeros, res = 0, 0
        while right < n:
            if nums[right] == 0: zeros += 1
            right += 1
            while zeros > 1:
                if nums[left] == 0: zeros -= 1
                left += 1
            res = max(res, right-left-1)
        return res
            

        
if __name__ == "__main__":
    print(Solution().longestSubarray([0,1,1,1,0,1,1,0,1]))
    print(Solution().longestSubarray([0,0,0]))

