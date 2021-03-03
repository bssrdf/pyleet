'''
-Medium-
*Auxillary Array*

Given an array nums of n integers where n > 1,  return an array output such 
that output[i] is equal to the product of all the elements of nums except 
nums[i].

Example:

Input:  [1,2,3,4]
Output: [24,12,8,6]
Constraint: It's guaranteed that the product of the elements of any 
prefix or suffix of the array (including the whole array) fits in a 
32 bit integer.

Note: Please solve it without division and in O(n).

Follow up:
Could you solve it with constant space complexity? (The output array 
does not count as extra space for the purpose of space complexity 
analysis.)

'''

class Solution(object):

    def productExceptSelfO1Space(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)        
        ans = [1] * N
        for i in range(1, N):
            ans[i] = nums[i-1] * ans[i-1]
        right = 1
        for i in range(N-1, -1, -1):
            ans[i] *= right 
            right = right * nums[i]
        return ans

    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        L = [1] * N
        R = [1] * N
        ans = [1] * N
        for i in range(1, N):
            L[i] = nums[i-1] * L[i-1]
        for i in range(N-2, -1, -1):
            R[i] = nums[i+1] * R[i+1]
        for i in range(N):
            ans[i] = L[i] * R[i]
        return ans


if __name__ == '__main__':
    print(Solution().productExceptSelf([1,2,3,4]))
    print(Solution().productExceptSelfO1Space([1,2,3,4]))