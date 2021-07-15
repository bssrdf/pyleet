'''
-Medium-

Given an array of n integers nums and a target, find the number of index triplets i, j, k 
with 0 <= i < j < k < n that satisfy the condition nums[i] + nums[j] + nums[k] < target.

Example:

Input: nums = [-2,0,1,3], and target = 2
Output: 2 
Explanation: Because there are two triplets which sums are less than 2:
             [-2,0,1]
             [-2,0,3]
Follow up: Could you solve it in O(n2) runtime?


'''

class Solution:
    """
    @param nums:  an array of n integers
    @param target: a target
    @return: the number of index triplets satisfy the condition nums[i] + nums[j] + nums[k] < target
    """
    def threeSumSmaller(self, nums, target):
        # Write your code here
        n = len(nums)
        if n < 3: return 0
        res = 0
        nums.sort()
        for i in range(n-2):
            left, right = i+1, n-1
            while left < right:
                if nums[left] + nums[right] + nums[i] < target:
                    res += right - left
                    left += 1
                else:
                    right -= 1
        return res

if __name__ == "__main__":
    print(Solution().threeSumSmaller([-2,0,1,3], 2))