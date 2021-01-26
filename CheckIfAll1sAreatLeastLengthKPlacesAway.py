'''

-Easy-

Given an array nums of 0s and 1s and an integer k, return True if all 1's are at 
least k places away from each other, otherwise return False.

 

Example 1:



Input: nums = [1,0,0,0,1,0,0,1], k = 2
Output: true
Explanation: Each of the 1s are at least 2 places away from each other.
Example 2:



Input: nums = [1,0,0,1,0,1], k = 2
Output: false
Explanation: The second 1 and third 1 are only one apart from each other.
Example 3:

Input: nums = [1,1,1,1,1], k = 0
Output: true
Example 4:

Input: nums = [0,1,0,1], k = 1
Output: true
 

Constraints:

1 <= nums.length <= 10^5
0 <= k <= nums.length
nums[i] is 0 or 1
'''

class Solution(object):
    def kLengthApart(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        lastPos = -1
        for i, v in enumerate(nums):
            if v == 1:
                if lastPos != -1 and i - lastPos <= k:
                    return False
                lastPos = i
        return True            
                 
        
if __name__ == "__main__":
    print(Solution().kLengthApart([1,0,0,0,1,0,0,1], 2))
    print(Solution().kLengthApart([1,0,0,1,0,1],  2))