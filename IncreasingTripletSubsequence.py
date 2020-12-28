'''
-Medium-

Given an integer array nums, return true if there exists a triple of indices 
(i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such 
indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because 
nums[3] == 0 < nums[4] == 4 < nums[5] == 6.
 

Constraints:

1 <= nums.length <= 10^5
-2^31 <= nums[i] <= 2^31 - 1

Follow up: Could you implement a solution that runs in O(n) time 
complexity and O(1) space complexity?

'''
import sys
class Solution(object):
    def increasingTriplet(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        m1, m2 = sys.maxsize, sys.maxsize
        for i in nums:
            if m1 >= i: m1 = i
            elif m2 >= i: m2 = i
            else: return True
        return False
    def increasingTripletO1Space(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        if n < 3: return False
        f = [nums[0]]*n
        b = [nums[-1]]*n
        for i in range(1, n):
            # f[i] min in [0, i]
            f[i] = min(f[i-1], nums[i])
        for i in range(n-2, -1, -1):
            # b[i] max in [i, n-1]
            b[i] = max(b[i+1], nums[i])
        for i in range(n):
            if nums[i] > f[i] and nums[i] < b[i]: # triplet exists
                return True
        return False       

if __name__ == "__main__":
    print(Solution().increasingTriplet([1,2,3,4,5]))