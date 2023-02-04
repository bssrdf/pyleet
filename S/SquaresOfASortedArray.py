'''
-Easy-

Given an integer array nums sorted in non-decreasing order, return an array of 
the squares of each number sorted in non-decreasing order.

 

Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
 

Constraints:

1 <= nums.length <= 10^4
-10^4 <= nums[i] <= 10^4
nums is sorted in non-decreasing order.

'''

class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        l, r, p = 0, n-1, n-1
        res = [0] * n 
        while l <= r:
            if abs(nums[r]) <= abs(nums[l]):
                res[p] = nums[l]**2
                l += 1
            else:
                res[p] = (nums[r]**2)
                r -= 1
            p -= 1
        return res




if __name__ == "__main__":
    print(Solution().sortedSquares([-4,-1,0,3,10]))
    print(Solution().sortedSquares([-7,-3,2,3,11]))