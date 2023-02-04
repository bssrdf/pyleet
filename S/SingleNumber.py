'''
-Easy-

Given a non-empty array of integers nums, every element appears twice except for one. 
Find that single one.

Follow up: Could you implement a solution with a linear runtime complexity and without 
using extra memory?

 

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 10^4
-3 * 10^4 <= nums[i] <= 3 * 10^4
Each element in the array appears twice except for one element which appears only once.


'''

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        for i in nums:
            ans ^= i
        return ans

if __name__ == "__main__":
    print(Solution().singleNumber([4,1,2,1,2]))