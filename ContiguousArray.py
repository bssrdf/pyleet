'''
-Medium-

Given a binary array nums, return the maximum length of a contiguous subarray 
with an equal number of 0 and 1.

 

Example 1:

Input: nums = [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
Example 2:

Input: nums = [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
 

Constraints:

1 <= nums.length <= 10^5
nums[i] is either 0 or 1.

'''

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        res, sm = 0, 0
        m = {0:-1}
        for i in range(n):
            sm += nums[i] if nums[i] == 1 else -1
            if sm in m:
                res = max(res, i-m[sm])
            else:
                m[sm] = i
        return res

if __name__ == "__main__":
    print(Solution().findMaxLength([0,1,0]))
    print(Solution().findMaxLength([0,1,0,1]))
    print(Solution().findMaxLength([0,1]))


